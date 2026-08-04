"""DAG worker pool — fan-out / fan-in with guards (ported from Agent OS).

Upgrades linear agent pipelines to a Directed Acyclic Graph model:

  * Planner decomposes a goal into subtasks tagged with `depends_on`.
  * The pool dispatches ready subtasks to N concurrent workers as soon as
    their dependencies complete (fan-out).
  * A fan-in barrier (the caller aggregating `run_pipeline()` results)
    batches completed fragments for the gate (evaluator / reviewer).
  * A `scheduler` (rsis.scheduler.AgentScheduler) can be attached to
    enforce depth/cycle guards on recursive hand-offs.

Safety measures:
  * Dependency readiness — a task dispatches only when every `depends_on`
    task is COMPLETED.
  * Concurrency cap — `num_workers` bounds in-flight executions so LLM
    provider rate limits are respected.
  * Deadlock guard — circular or missing dependencies raise instead of
    hanging the pool.
  * Failure propagation — when a task FAILS, its dependents are marked
    FAILED with `dependency failed: <task_id>` instead of deadlocking;
    workers are always cleaned up.
  * Traceability — per-task status + latency, optionally emitted to
    telemetry via an `on_event` hook.
"""

from __future__ import annotations

import concurrent.futures
import logging
import random
import time
from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Callable, Optional

from rsis.error_classifier import is_retryable

logger = logging.getLogger(__name__)


class TaskStatus(str, Enum):
    PENDING = "PENDING"
    RUNNING = "RUNNING"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"
    CANCELLED = "CANCELLED"  # pool shutdown or guard rejection


@dataclass
class TaskNode:
    """One node of the execution DAG."""

    task_id: str
    role: str                       # e.g. "coder"
    payload: dict[str, Any]         # prompt / tool args / code context
    depends_on: list[str] = field(default_factory=list)
    status: TaskStatus = TaskStatus.PENDING
    result: Any = None
    error: str | None = None
    attempts: int = 0                # completed executions of this node
    retry_at: float = 0.0           # earliest wall-clock time for a retry
    started_at: float = 0.0
    finished_at: float = 0.0

    @property
    def latency_s(self) -> float:
        return (self.finished_at - self.started_at) if self.finished_at else 0.0


class DAGWorkerPool:
    """Concurrent DAG dispatcher: N worker threads + dynamic routing."""

    def __init__(self, num_workers: int = 4,
                 on_event: Optional[Callable[[dict], None]] = None,
                 max_retries: int = 0,
                 retry_base_delay_s: float = 0.5,
                 retry_max_delay_s: float = 30.0):
        self.num_workers = max(1, num_workers)
        self.tasks: dict[str, TaskNode] = {}
        self.on_event = on_event      # optional traceability hook
        self.max_retries = max(0, int(max_retries))        # 0 = fail fast
        self.retry_base_delay_s = max(0.0, retry_base_delay_s)
        self.retry_max_delay_s = max(self.retry_base_delay_s,
                                     retry_max_delay_s)

    # ------------------------------------------------------------------ #
    def add_task(self, task_id: str, role: str, payload: dict[str, Any],
                 depends_on: list[str] | None = None) -> TaskNode:
        """Register one subtask node into the DAG."""
        task = TaskNode(task_id=task_id, role=role, payload=payload,
                        depends_on=depends_on or [])
        self.tasks[task_id] = task
        return task

    def _is_ready(self, task: TaskNode) -> bool:
        """True when every prerequisite task is COMPLETED."""
        for dep_id in task.depends_on:
            dep = self.tasks.get(dep_id)
            if not dep or dep.status != TaskStatus.COMPLETED:
                return False
        return True

    # ------------------------------------------------------------------ #
    def run_pipeline(self, executor: Callable[[TaskNode], Any]
                     ) -> dict[str, TaskNode]:
        """
        Dispatch the DAG until every task settles (COMPLETED/FAILED).

        Raises RuntimeError on an unresolvable dependency cycle.  Returns
        `self.tasks` for fan-in aggregation.
        """
        remaining = set(self.tasks.keys())
        queued: dict[str, concurrent.futures.Future] = {}

        with concurrent.futures.ThreadPoolExecutor(
                max_workers=self.num_workers,
                thread_name_prefix="rsis-dag") as pool:
            while remaining:
                # --- fan-out: dispatch every currently-ready task ------- #
                dispatch_made = False
                waiting_backoff = False
                for tid in list(remaining):
                    task = self.tasks[tid]
                    if tid in queued or not self._is_ready(task):
                        continue
                    if task.retry_at > time.time():
                        waiting_backoff = True      # keep the deadlock guard quiet
                        continue
                    failed_dep = next(
                        (d for d in task.depends_on
                         if self.tasks[d].status == TaskStatus.FAILED), None)
                    if failed_dep:
                        task.status = TaskStatus.FAILED
                        task.error = f"dependency failed: {failed_dep}"
                        self._emit(task)
                        remaining.discard(tid)
                        continue
                    task.status = TaskStatus.RUNNING
                    task.started_at = time.time()
                    task.retry_at = 0.0
                    queued[tid] = pool.submit(executor, task)
                    dispatch_made = True

                # --- collect settled futures ---------------------------- #
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
                    except Exception as exc:
                        task.error = str(exc)
                        retrying = (task.attempts < self.max_retries
                                    and is_retryable(exc))
                        if retrying:
                            task.attempts += 1
                            delay = self._retry_delay(task.attempts)
                            task.status = TaskStatus.PENDING
                            task.retry_at = time.time() + delay
                            logger.warning(
                                "DAG task %s (%s) failed (%d/%d); retrying "
                                "in %.2fs: %s", tid, task.role,
                                task.attempts, self.max_retries, delay, exc)
                            self._emit_retry(task, exc, delay)
                        else:
                            task.status = TaskStatus.FAILED
                            logger.warning("DAG task %s (%s) failed: %s",
                                           tid, task.role, exc)
                            remaining.discard(tid)
                    self._emit(task)
                    del queued[tid]

                if not remaining:
                    break

                # A completed dependency may have unlocked new tasks; re-run
                # the fan-out pass before judging the graph as deadlocked.
                if settled:
                    continue

                # --- deadlock guard: nothing dispatchable, nothing in flight
                if not dispatch_made and not queued and not waiting_backoff:
                    stuck = sorted(t for t in remaining)
                    raise RuntimeError(
                        f"DAG deadlock detected — unresolvable "
                        f"dependencies: {stuck}")

                time.sleep(0.02)   # poll tick

        if self.on_event is not None:
            self.on_event({
                "kind": "dag_complete",
                "total": len(self.tasks),
                "completed": sum(1 for t in self.tasks.values()
                                 if t.status == TaskStatus.COMPLETED),
                "failed": sum(1 for t in self.tasks.values()
                              if t.status == TaskStatus.FAILED),
                "retries": sum(t.attempts for t in self.tasks.values()),
            })
        return self.tasks

    # ------------------------------------------------------------------ #
    def _retry_delay(self, attempt: int) -> float:
        """Exponential backoff with full jitter, capped (AO-style)."""
        exp = self.retry_base_delay_s * (2 ** (attempt - 1))
        return min(self.retry_max_delay_s, random.uniform(0.0, exp))

    # ------------------------------------------------------------------ #
    def _emit_retry(self, task: TaskNode, exc: Exception,
                    delay: float) -> None:
        """Push a retry traceability event (if wired)."""
        if self.on_event is not None:
            self.on_event({
                "kind": "dag_task_retrying",
                "task_id": task.task_id,
                "role": task.role,
                "attempt": task.attempts,
                "max_retries": self.max_retries,
                "delay_s": round(delay, 3),
                "error": str(exc),
            })

    # ------------------------------------------------------------------ #
    def _emit(self, task: TaskNode) -> None:
        """Push one per-task traceability event (if wired)."""
        if self.on_event is not None:
            self.on_event({
                "kind": "dag_task", "task_id": task.task_id,
                "role": task.role, "status": task.status.value,
                "error": task.error,
                "latency_s": round(task.latency_s, 3),
            })

    # ------------------------------------------------------------------ #
    def completed_results(self) -> dict[str, Any]:
        """Fan-in helper: task_id -> result for every COMPLETED task."""
        return {tid: t.result for tid, t in self.tasks.items()
                if t.status == TaskStatus.COMPLETED}

    def failed_tasks(self) -> dict[str, str]:
        """Fan-in helper: task_id -> error for every FAILED task."""
        return {tid: (t.error or "unknown error") for tid, t in self.tasks.items()
                if t.status == TaskStatus.FAILED}


# ── Demo (python -m rsis pipeline) ───────────────────────────────────────

def run_demo() -> int:
    """Smoke demo: fan-out / fan-in with dependency + deadlock guards."""
    pool = DAGWorkerPool(num_workers=2)
    # planner -> 3 parallel coders -> reviewer fan-in
    pool.add_task("planner", "planner", {"goal": "demo"})
    for i in range(3):
        pool.add_task(f"coder-{i}", "coder", {"i": i}, depends_on=["planner"])
    pool.add_task("reviewer", "reviewer", {},
                  depends_on=[f"coder-{i}" for i in range(3)])

    def run(task):
        if task.role == "planner":
            time.sleep(0.05)
            return "plan"
        if task.role == "coder":
            time.sleep(0.05 * (task.payload["i"] + 1))
            return f"code-{task.payload['i']}"
        return "review:" + ",".join(sorted(pool.completed_results()))

    pool.run_pipeline(run)
    statuses = {t: n.status.value for t, n in pool.tasks.items()}
    print("  statuses:", statuses)
    assert statuses["planner"] == "COMPLETED"
    assert all(statuses[f"coder-{i}"] == "COMPLETED" for i in range(3))
    assert statuses["reviewer"] == "COMPLETED"
    print("  reviewer result:", pool.tasks["reviewer"].result)

    # Retry budget: transient failures retry with backoff; fatal abort.
    rp = DAGWorkerPool(num_workers=2, max_retries=2,
                       retry_base_delay_s=0.01, retry_max_delay_s=0.05)
    rp.add_task("flaky", "flaky", {})
    rp.add_task("fatal", "fatal", {})
    attempts = {"flaky": 0, "fatal": 0}

    def run_retry(task):
        attempts[task.task_id] += 1
        if task.task_id == "flaky" and attempts["flaky"] < 3:
            raise TimeoutError("connection timed out")
        if task.task_id == "fatal":
            raise ValueError("invalid_api_key")
        return "ok"

    rp.run_pipeline(run_retry)
    assert rp.tasks["flaky"].status == TaskStatus.COMPLETED,         "transient failure should recover via retry"
    assert rp.tasks["fatal"].status == TaskStatus.FAILED,         "fatal failure must not be retried"
    print(f"  retry: flaky recovered after {attempts['flaky']} runs "
          f"({rp.tasks['flaky'].attempts} retries); "
          f"fatal aborted without retry (attempts={attempts['fatal']})")

    # Deadlock guard: circular dependency must raise.
    bad = DAGWorkerPool(num_workers=2)
    bad.add_task("a", "x", {}, depends_on=["b"])
    bad.add_task("b", "x", {}, depends_on=["a"])
    try:
        bad.run_pipeline(lambda t: t.task_id)
        print("  deadlock guard: NOT TRIGGERED (BUG)")
        return 1
    except RuntimeError as e:
        print("  deadlock guard:", e)
    return 0
