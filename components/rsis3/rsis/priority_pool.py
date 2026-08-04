"""Priority-aware worker pools (ported from Agent OS, sync-first).

Concepts from AO's ``priority_worker_pool`` / ``advanced_priority_pool`` /
``checkpoint_worker``, adapted to RSIS3's thread-based executor model:

  * **Priority ordering** — ready tasks dispatch in priority order; the queue
    order key mirrors AO's ``(-priority, created, task_id)`` tuple.
  * **Priority aging** — effective priority grows with queue wait time
    (``priority + aging_rate * waited_sec``, monotonic clock) so low-priority
    work cannot starve; recomputed at every dispatch pass (no background
    loop needed in the sync model).
  * **Cooperative preemption** — threads cannot be force-cancelled, so
    ``request_preemption()`` (or the dispatch-pass heuristic) flags a RUNNING
    task and the executor wrapper / :class:`CheckpointRunner` raises
    ``TaskPreemptedError`` at the next step boundary; the task is reset to
    PENDING with a +1.0 priority boost and re-queued.  Plain executors that
    never check the flag run to completion — preemption is a yield, not a kill.
  * **Step checkpoints** — completed steps are saved onto the task so a
    preempted or retried task resumes instead of restarting.

Retry semantics mirror :class:`rsis.pipeline.DAGWorkerPool` (Phase D1):
per-task budgets, fatal failures fail fast, category-based exponential
backoff with jitter (RATE_LIMIT grows 2x, else 1.5x), failed dependencies
fail their dependents, and a deadlock guard aborts unresolvable graphs.

Events publish to an optional :class:`rsis.event_bus.EventBus` under AO's
vocabulary (``worker.task.*``, ``worker.priority_tick``) so dashboards and
telemetry can subscribe with wildcards; an ``on_event`` hook is also
supported for backward compatibility.
"""

from __future__ import annotations

import concurrent.futures
import logging
import random
import time
from dataclasses import dataclass, field
from typing import Any, Callable, Optional

from rsis.error_classifier import ErrorCategory, classify_error, is_retryable
from rsis.event_bus import EventBus
from rsis.pipeline import TaskStatus

logger = logging.getLogger(__name__)

__all__ = [
    "TaskCheckpoint", "PriorityTaskNode", "TaskPreemptedError",
    "PriorityWorkerPool", "AdvancedPriorityWorkerPool",
    "CheckpointRunner", "CheckpointWorkerPool",
]


class TaskPreemptedError(Exception):
    """Raised when a RUNNING task yields to a higher-priority task."""


@dataclass
class TaskCheckpoint:
    """Saved progress for a multi-step task (resume point)."""

    step_index: int = 0
    checkpoint_time: float = field(default_factory=time.time)
    state_data: Any = None


@dataclass
class PriorityTaskNode:
    """One node of a priority-scheduled execution graph."""

    task_id: str
    role: str
    payload: dict[str, Any]
    depends_on: list[str] = field(default_factory=list)
    status: TaskStatus = TaskStatus.PENDING
    result: Any = None
    error: Optional[str] = None
    attempts: int = 0                # completed executions of this node
    priority: float = 5.0            # default = 5; high = 10+, low = 1
    max_retries: int = 3
    last_error_category: Optional[str] = None
    checkpoint: Optional[TaskCheckpoint] = None
    completed_steps: list[str] = field(default_factory=list)
    created_at: float = field(default_factory=time.time)
    _created_mono: float = field(default_factory=time.monotonic, repr=False)
    retry_at: float = 0.0            # earliest wall-clock time for a retry
    started_at: float = 0.0
    finished_at: float = 0.0
    preempt_requested: bool = False

    @property
    def latency_s(self) -> float:
        return (self.finished_at - self.started_at) if self.finished_at else 0.0

    def save_step_checkpoint(self, step_name: str, step_index: int,
                             state_data: dict[str, Any]) -> None:
        """Save current progress so execution can resume after preemption."""
        self.completed_steps.append(step_name)
        self.checkpoint = TaskCheckpoint(
            step_index=step_index,
            checkpoint_time=time.time(),
            state_data=state_data,
        )

    def effective_priority(self, aging_rate: float = 0.0) -> float:
        """Current priority including wait-time aging (monotonic clock)."""
        waited_sec = time.monotonic() - self._created_mono
        return self.priority + (aging_rate * waited_sec)


class PriorityWorkerPool:
    """Bounded-concurrency executor dispatching ready tasks by priority.

    Tasks are registered with ``add_task()`` before ``run()`` (the graph is
    static during execution).  Retry/backoff semantics match the Phase D1
    ``DAGWorkerPool``; priority ordering is the only scheduling change.
    """

    def __init__(self, num_workers: int = 4,
                 event_bus: Optional[EventBus] = None,
                 on_event: Optional[Callable[[dict], None]] = None,
                 base_backoff_sec: float = 0.5,
                 max_backoff_sec: float = 30.0):
        self.num_workers = max(1, num_workers)
        self.event_bus = event_bus
        self.on_event = on_event
        self.base_backoff_sec = max(0.0, base_backoff_sec)
        self.max_backoff_sec = max(self.base_backoff_sec, max_backoff_sec)
        self.tasks: dict[str, PriorityTaskNode] = {}
        self._executor: Optional[concurrent.futures.ThreadPoolExecutor] = None
        self._running_futures: dict[str, concurrent.futures.Future] = {}

    # -- queue ordering ------------------------------------------------- #

    def _order_key(self, task: PriorityTaskNode):
        """Sort key: highest priority first, FIFO within a priority."""
        return (-task.effective_priority(0.0), task._created_mono, task.task_id)

    def _is_ready(self, task: PriorityTaskNode) -> bool:
        """True when every prerequisite task is COMPLETED."""
        for dep_id in task.depends_on:
            dep = self.tasks.get(dep_id)
            if not dep or dep.status != TaskStatus.COMPLETED:
                return False
        return True

    # -- public API ----------------------------------------------------- #

    def add_task(self, task_id: str, role: str, payload: dict[str, Any],
                 priority: float = 5.0,
                 depends_on: Optional[list[str]] = None,
                 max_retries: int = 3) -> PriorityTaskNode:
        """Register one task node into the priority graph."""
        task = PriorityTaskNode(
            task_id=task_id, role=role, payload=payload,
            depends_on=depends_on or [],
            priority=priority, max_retries=max_retries,
        )
        self.tasks[task_id] = task
        self._emit("created", task)
        return task

    def cancel_task(self, task_id: str) -> bool:
        """Cancel a PENDING task; request cooperative yield on a RUNNING one."""
        task = self.tasks.get(task_id)
        if not task:
            return False
        if task.status == TaskStatus.RUNNING:
            task.preempt_requested = True
            self._emit("cancel_requested", task,
                       {"reason": "cooperative (thread pool)"})
            return True
        if task.status == TaskStatus.PENDING:
            task.status = TaskStatus.CANCELLED
            self._emit("cancelled", task,
                       {"reason": "cancelled before execution"})
            return True
        return False

    # -- execution ------------------------------------------------------ #

    def run(self, executor: Callable[[PriorityTaskNode], Any]
            ) -> dict[str, PriorityTaskNode]:
        """Dispatch the graph until every task settles.

        Raises RuntimeError on an unresolvable dependency cycle.  Returns
        ``self.tasks`` for fan-in aggregation.
        """
        remaining = set(self.tasks.keys())
        queued: dict[str, concurrent.futures.Future] = {}

        with concurrent.futures.ThreadPoolExecutor(
                max_workers=self.num_workers,
                thread_name_prefix="rsis-prio") as pool:
            self._executor = pool
            while remaining:
                dispatch_made, waiting_backoff = self._dispatch_pass(
                    executor, pool, remaining, queued)
                settled = self._collect_pass(remaining, queued)

                if not remaining:
                    break
                if settled:
                    continue
                if not dispatch_made and not queued and not waiting_backoff:
                    stuck = sorted(t for t in remaining)
                    raise RuntimeError(
                        f"priority pool deadlock — unresolvable "
                        f"dependencies: {stuck}")
                self._tick_if_due()
                time.sleep(0.02)   # poll tick

        self._executor = None
        summary = {
            "total": len(self.tasks),
            "completed": sum(1 for t in self.tasks.values()
                             if t.status == TaskStatus.COMPLETED),
            "failed": sum(1 for t in self.tasks.values()
                          if t.status == TaskStatus.FAILED),
            "retries": sum(t.attempts for t in self.tasks.values()),
        }
        if self.event_bus is not None:
            self.event_bus.publish("worker.pool.complete", dict(summary))
        if self.on_event is not None:
            self.on_event({"kind": "worker.pool.complete", **summary})
        return self.tasks

    def _dispatch_pass(self, executor, pool, remaining, queued):
        """Fan-out: dispatch every ready task in priority order."""
        dispatch_made = False
        waiting_backoff = False
        ready: list[PriorityTaskNode] = []

        for tid in list(remaining):
            task = self.tasks[tid]
            if tid in queued:
                continue
            if task.status == TaskStatus.CANCELLED:
                remaining.discard(tid)
                continue
            # Failed dependencies fail the dependent outright.  This must run
            # before readiness so dependents settle instead of deadlocking.
            failed_dep = next(
                (d for d in task.depends_on
                 if self.tasks.get(d)
                 and self.tasks[d].status == TaskStatus.FAILED), None)
            if failed_dep:
                task.status = TaskStatus.FAILED
                task.error = f"dependency failed: {failed_dep}"
                task.finished_at = time.time()
                self._emit("failed", task, {"reason": "DEPENDENCY_FAILED"})
                remaining.discard(tid)
                continue
            if not self._is_ready(task):
                continue
            if task.retry_at > time.time():
                waiting_backoff = True
                continue
            ready.append(task)

        # Highest effective priority first; free a slot for the top task if
        # every worker is saturated and the margin clears the threshold.
        ready.sort(key=self._order_key)
        if ready and len(queued) >= self.num_workers:
            self._preempt_lowest_for(ready[0])

        for task in ready:
            task.status = TaskStatus.RUNNING
            task.started_at = time.time()
            task.retry_at = 0.0
            task.preempt_requested = False
            self._emit("started", task)
            future = pool.submit(self._run_one, executor, task)
            queued[task.task_id] = future
            self._running_futures[task.task_id] = future
            dispatch_made = True
        return dispatch_made, waiting_backoff

    def _collect_pass(self, remaining, queued) -> bool:
        """Collect settled futures; apply retry/preempt/fail transitions."""
        settled = False
        for tid, future in list(queued.items()):
            if not future.done():
                continue
            settled = True
            task = self.tasks[tid]
            task.finished_at = time.time()
            try:
                task.result = future.result()
                task.status = TaskStatus.COMPLETED
                remaining.discard(tid)
                self._emit("completed", task, {
                    "duration_sec": round(task.latency_s, 3),
                })
            except TaskPreemptedError:
                self._handle_preempted(task)
            except Exception as exc:
                if self._handle_failure(task, exc):
                    remaining.discard(tid)
            del queued[tid]
            self._running_futures.pop(tid, None)
        return settled

    # -- transitions ---------------------------------------------------- #

    def _handle_preempted(self, task: PriorityTaskNode) -> None:
        """Reset a preempted task to PENDING with a boost and re-queue it."""
        task.status = TaskStatus.PENDING
        task.preempt_requested = False
        task.priority += 1.0
        task.started_at = 0.0
        task.finished_at = 0.0
        self._emit("requeued", task,
                   {"reason": "preempted_by_higher_priority"})

    def _handle_failure(self, task: PriorityTaskNode, exc: Exception) -> bool:
        """Apply retry/backoff or fail the task.  Returns True when settled."""
        category = classify_error(exc)
        task.last_error_category = category.value
        task.error = str(exc)
        if task.attempts < task.max_retries and is_retryable(exc):
            task.attempts += 1
            delay = self._backoff(category, task.attempts)
            task.status = TaskStatus.PENDING
            task.retry_at = time.time() + delay
            logger.warning("Priority task %s (%s) failed (%d/%d); "
                           "retrying in %.2fs: %s", task.task_id,
                           task.role, task.attempts, task.max_retries,
                           delay, exc)
            self._emit("retrying", task, {
                "error": str(exc),
                "error_category": category.value,
                "next_retry_delay_sec": round(delay, 2),
            })
            return False
        task.status = TaskStatus.FAILED
        reason = ("FATAL_ERROR" if not is_retryable(exc)
                  else "BUDGET_EXHAUSTED")
        logger.warning("Priority task %s (%s) failed: %s",
                       task.task_id, task.role, exc)
        self._emit("failed", task, {
            "error": str(exc),
            "error_category": category.value,
            "reason": reason,
        })
        return True

    def _backoff(self, category: ErrorCategory, attempt: int) -> float:
        """Exponential backoff with full jitter, category-scaled, capped."""
        multiplier = 2.0 if category == ErrorCategory.RATE_LIMIT else 1.5
        calc = self.base_backoff_sec * (multiplier ** attempt)
        return min(self.max_backoff_sec, calc + random.uniform(0.0, 0.5 * calc))

    # -- helpers -------------------------------------------------------- #

    def _run_one(self, executor, task: PriorityTaskNode):
        """Executor wrapper: honor a preemption request made before start."""
        if task.preempt_requested:
            raise TaskPreemptedError()
        return executor(task)

    def completed_results(self) -> dict[str, Any]:
        """Fan-in helper: task_id -> result for every COMPLETED task."""
        return {tid: t.result for tid, t in self.tasks.items()
                if t.status == TaskStatus.COMPLETED}

    def failed_tasks(self) -> dict[str, str]:
        """Fan-in helper: task_id -> error for every FAILED task."""
        return {tid: (t.error or "unknown error") for tid, t in self.tasks.items()
                if t.status == TaskStatus.FAILED}

    # -- telemetry ------------------------------------------------------ #

    def _emit(self, action: str, task: Optional[PriorityTaskNode],
              extra: Optional[dict] = None) -> None:
        """Publish one event to the bus (and/or the on_event hook)."""
        payload = dict(extra or {})
        if task is not None:
            payload = {
                "task_id": task.task_id,
                "role": task.role,
                "status": task.status.value,
                "priority": round(task.priority, 2),
                "attempts": task.attempts,
                "max_retries": task.max_retries,
                "depends_on": task.depends_on,
                **payload,
            }
        if self.event_bus is not None:
            self.event_bus.publish(f"worker.task.{action}", payload)
        if self.on_event is not None:
            self.on_event({"kind": f"worker.task.{action}", **payload})

    def _tick_if_due(self) -> None:
        """Hook for subclass aging telemetry (cadence-limited)."""


class AdvancedPriorityWorkerPool(PriorityWorkerPool):
    """Priority pool with aging ordering + cooperative preemption safeguards.

    Extends :class:`PriorityWorkerPool`:

    - **Aging** — effective priority (``priority + aging_rate * waited_sec``)
      drives dispatch order, so low-priority tasks cannot starve forever.
    - **Preemption** — when all worker slots are saturated and a ready task
      outranks the lowest-priority RUNNING task by ``preemption_threshold``
      or more, the running task is flagged for cooperative yield
      (``TaskPreemptedError`` at its next step boundary), reset to PENDING
      with a +1.0 compensation boost, and re-queued.  The margin prevents
      thrashing.
    """

    def __init__(self, num_workers: int = 4,
                 event_bus: Optional[EventBus] = None,
                 on_event: Optional[Callable[[dict], None]] = None,
                 base_backoff_sec: float = 0.5,
                 max_backoff_sec: float = 30.0,
                 aging_rate: float = 0.2,
                 preemption_threshold: float = 5.0):
        super().__init__(
            num_workers=num_workers, event_bus=event_bus,
            on_event=on_event, base_backoff_sec=base_backoff_sec,
            max_backoff_sec=max_backoff_sec,
        )
        self.aging_rate = aging_rate
        self.preemption_threshold = preemption_threshold

    # -- queue ordering (effective priority) ---------------------------- #

    def _order_key(self, task: PriorityTaskNode):
        return (-task.effective_priority(self.aging_rate),
                task._created_mono, task.task_id)

    # -- preemption ----------------------------------------------------- #

    def request_preemption(self, task_id: str) -> bool:
        """Manually flag a RUNNING task for cooperative preemption."""
        task = self.tasks.get(task_id)
        if not task or task.status != TaskStatus.RUNNING:
            return False
        task.preempt_requested = True
        self._emit("preempted", task, {
            "triggered_by": "external",
            "saved_checkpoint_step": (
                task.checkpoint.step_index if task.checkpoint else 0),
        })
        return True

    def _preempt_lowest_for(self, incoming: PriorityTaskNode) -> None:
        """Flag the lowest-priority running task when the margin is big enough."""
        lowest_id: Optional[str] = None
        lowest_prio = float("inf")
        for tid, future in list(self._running_futures.items()):
            if future.done():
                continue
            node = self.tasks.get(tid)
            if node and node.priority < lowest_prio:
                lowest_prio = node.priority
                lowest_id = tid
        if not lowest_id:
            return
        if incoming.priority >= lowest_prio + self.preemption_threshold:
            lowest = self.tasks[lowest_id]
            lowest.preempt_requested = True
            self._emit("preempted", lowest, {
                "triggered_by": incoming.task_id,
                "saved_checkpoint_step": (
                    lowest.checkpoint.step_index if lowest.checkpoint else 0),
            })

    # -- reprioritization ----------------------------------------------- #

    def update_task_priority(self, task_id: str,
                             new_priority: float) -> bool:
        """Dynamically boost or demote a PENDING task in the queue."""
        task = self.tasks.get(task_id)
        if not task or task.status != TaskStatus.PENDING:
            return False
        task.priority = new_priority
        self._emit("reprioritized", task, {"new_priority": new_priority})
        return True


class CheckpointRunner:
    """Step-pipeline helper with auto-checkpointing + cooperative preemption.

    ``run_step()`` skips steps already completed before a preemption (restored
    from the task checkpoint) and raises :class:`TaskPreemptedError` when a
    preemption was requested, giving the pool a clean resume point.
    """

    def __init__(self, task: PriorityTaskNode,
                 event_bus: Optional[EventBus] = None):
        self.task = task
        self.event_bus = event_bus

    def run_step(self, step_index: int, step_name: str,
                 step_fn: Callable[[dict[str, Any]], Any],
                 current_state: dict[str, Any]) -> dict[str, Any]:
        """Execute `step_fn` unless already completed before a preemption."""
        if self.task.preempt_requested:
            raise TaskPreemptedError()
        if self.task.checkpoint and self.task.checkpoint.step_index >= step_index:
            logger.info("Skipping step %d '%s' for %s (restored from "
                        "checkpoint)", step_index, step_name,
                        self.task.task_id)
            return self.task.checkpoint.state_data
        logger.info("Executing step %d '%s' for %s...",
                    step_index, step_name, self.task.task_id)
        new_state = step_fn(current_state)
        self.task.save_step_checkpoint(step_name, step_index, new_state)
        if self.event_bus is not None:
            self.event_bus.publish("worker.task.checkpoint", {
                "task_id": self.task.task_id,
                "step_name": step_name,
                "step_index": step_index,
                "completed_steps": list(self.task.completed_steps),
            })
        return new_state


class CheckpointWorkerPool(AdvancedPriorityWorkerPool):
    """Advanced pool that broadcasts aging telemetry as ``worker.priority_tick``.

    One tick frame per ``aging_interval_s``: payload is the list of pending
    tasks with base / effective priority and aged delta — the data behind the
    dashboard's aging curves.
    """

    def __init__(self, num_workers: int = 4,
                 event_bus: Optional[EventBus] = None,
                 on_event: Optional[Callable[[dict], None]] = None,
                 base_backoff_sec: float = 0.5,
                 max_backoff_sec: float = 30.0,
                 aging_rate: float = 0.2,
                 preemption_threshold: float = 5.0,
                 aging_interval_s: float = 2.0):
        super().__init__(
            num_workers=num_workers, event_bus=event_bus,
            on_event=on_event, base_backoff_sec=base_backoff_sec,
            max_backoff_sec=max_backoff_sec, aging_rate=aging_rate,
            preemption_threshold=preemption_threshold,
        )
        self.aging_interval_s = max(0.1, aging_interval_s)
        self._last_tick_mono = time.monotonic()

    def _tick_if_due(self) -> None:
        """Broadcast one aging frame at most every ``aging_interval_s``."""
        if self.event_bus is None:
            return
        now = time.monotonic()
        if now - self._last_tick_mono < self.aging_interval_s:
            return
        self._last_tick_mono = now
        items = []
        for tid, task in self.tasks.items():
            if task.status != TaskStatus.PENDING:
                continue
            eff = task.effective_priority(self.aging_rate)
            items.append({
                "task_id": tid,
                "base_prio": round(task.priority, 2),
                "effective_prio": round(eff, 2),
                "aged_delta": round(eff - task.priority, 2),
            })
        if items:
            self.event_bus.publish("worker.priority_tick", {"items": items})
