"""Agent scheduler with recursion guards (ported from Agent OS).

Priority-queue scheduling for multi-agent L2 pipelines:

  * Priority queue — CRITICAL interrupts (security alerts, user
    interrupts) preempt background work; equal-priority tasks stay
    strictly FIFO via a monotonic sequence tie-breaker.
  * Recursion guards — a hard depth cap (REJECTED results, not silent
    drops) plus directed-edge cycle detection: if the same (role,
    description) hand-off repeats more than `cycle_limit` times (e.g.
    Coder <-> Reviewer ping-pong), the branch is aborted.
  * Process table — `register_agent` / `list_agents`; one failing agent
    never kills the loop (FAILED results are recorded and the queue
    drains).

Synchronous and stdlib-only, mirroring the Agent OS Module 4 reference
(`kernel/scheduler.py`). The DAG pipeline (`rsis/pipeline.py`) uses these
guards when L2 runs parallel candidates.
"""

from __future__ import annotations

import itertools
import logging
from dataclasses import dataclass, field
from enum import IntEnum
from queue import PriorityQueue
from typing import Any, Callable, Optional

logger = logging.getLogger(__name__)

_seqs = itertools.count()   # global monotonic counter for FIFO tie-breaking


class Priority(IntEnum):
    """Scheduling priorities — lower numbers run first."""

    CRITICAL = 1   # security alerts, user interrupts
    HIGH = 2
    MEDIUM = 3     # default
    LOW = 4        # background routines


@dataclass(order=True)
class Task:
    """One schedulable unit of work."""

    priority: int
    task_id: str = field(compare=False)
    target_role: str = field(compare=False)
    description: str = field(compare=False)
    payload: dict = field(default_factory=dict, compare=False)
    parent_task_id: Optional[str] = field(default=None, compare=False)
    depth: int = field(default=0, compare=False)
    # FIFO tie-breaker: the only other compared field (order = priority, seq)
    seq: int = field(default_factory=lambda: next(_seqs), compare=True)


class AgentScheduler:
    """Priority-queue scheduler with depth + cycle guards."""

    def __init__(self, max_depth: int = 5, cycle_limit: int = 3):
        self.task_queue: PriorityQueue[Task] = PriorityQueue()
        self.agent_registry: dict[str, Callable[[Task], str]] = {}
        self.max_depth = max_depth
        self.cycle_limit = cycle_limit
        self.task_history: list[str] = []
        self.execution_results: list[dict[str, Any]] = []
        self._cycle_counts: dict[tuple, int] = {}

    # ------------------------------------------------------------------ #
    def register_agent(self, role: str,
                       handler: Callable[[Task], str]) -> None:
        """Registers an agent handler function to a specific role."""
        self.agent_registry[role] = handler

    def list_agents(self) -> list[str]:
        """Names of all registered roles (process table, read-only)."""
        return sorted(self.agent_registry)

    # ------------------------------------------------------------------ #
    def submit_task(
        self,
        task_id: str,
        target_role: str,
        description: str,
        priority: Priority = Priority.MEDIUM,
        payload: dict[str, Any] | None = None,
        parent_task_id: Optional[str] = None,
        depth: int = 0,
    ) -> bool:
        """Enqueues a task into the priority queue with depth checks.

        Returns True when queued, False when the branch was rejected by a
        recursion guard.
        """
        # --- guard 1: hard depth cap ---------------------------------- #
        if depth > self.max_depth:
            logger.error("[scheduler] task '%s' exceeded maximum recursion "
                         "depth (%d). Aborting branch.", task_id, self.max_depth)
            self._record("REJECTED", task_id, target_role, depth=depth,
                         error=f"max depth {self.max_depth} exceeded")
            return False

        # --- guard 2: cycle detection --------------------------------- #
        signature = (target_role, description)
        self._cycle_counts[signature] = self._cycle_counts.get(signature, 0) + 1
        if self._cycle_counts[signature] > self.cycle_limit:
            logger.error("[scheduler] task '%s' repeats %s more than %d "
                         "times — cycle suspected. Aborting branch.",
                         task_id, signature, self.cycle_limit)
            self._record("REJECTED", task_id, target_role, depth=depth,
                         error=f"cycle limit {self.cycle_limit} exceeded "
                               f"on {signature!r}")
            return False

        self.task_queue.put(Task(
            priority=int(priority),
            task_id=task_id,
            target_role=target_role,
            description=description,
            payload=payload or {},
            parent_task_id=parent_task_id,
            depth=depth,
        ))
        return True

    # ------------------------------------------------------------------ #
    def run_event_loop(self) -> list[dict[str, Any]]:
        """Processes enqueued tasks in priority order until the queue drains."""
        while not self.task_queue.empty():
            current: Task = self.task_queue.get()
            role = current.target_role
            handler = self.agent_registry.get(role)

            if handler is None:
                logger.warning("[scheduler] no agent registered for role "
                               "'%s'. Skipping task '%s'.", role,
                               current.task_id)
                self._record("SKIPPED", current.task_id, role,
                             depth=current.depth, parent=current.parent_task_id,
                             error=f"no agent registered for role '{role}'")
                continue

            logger.info("[scheduler] dispatching '%s' to [%s] "
                        "(priority=%s, depth=%d)",
                        current.task_id, role,
                        Priority(current.priority).name, current.depth)

            try:
                output = handler(current)
                self._record("SUCCESS", current.task_id, role,
                             output=output, depth=current.depth,
                             parent=current.parent_task_id)
                self.task_history.append(current.task_id)
            except Exception as exc:   # one bad agent must not kill the loop
                logger.exception("[scheduler] agent '%s' failed on task '%s'",
                                 role, current.task_id)
                self._record("FAILED", current.task_id, role,
                             error=str(exc), depth=current.depth,
                             parent=current.parent_task_id)

        return self.execution_results

    # ------------------------------------------------------------------ #
    def _record(self, status: str, task_id: str, role: str,
                error: str | None = None, output: str | None = None,
                depth: int | None = None,
                parent: str | None = None) -> None:
        """Append one execution result (success/failure/rejection)."""
        entry: dict[str, Any] = {"task_id": task_id, "role": role,
                                 "status": status}
        if depth is not None:
            entry["depth"] = depth
        if output is not None:
            entry["output"] = output
        if error is not None:
            entry["error"] = error
        if parent is not None:
            entry["parent_task_id"] = parent
        self.execution_results.append(entry)


# ── Demo (python -m rsis scheduler) ──────────────────────────────────────

def run_demo() -> int:
    """Smoke demo: priority preemption, FIFO tie-breaks, guards."""
    sched = AgentScheduler(max_depth=3, cycle_limit=2)
    sched.register_agent("planner", lambda t: f"planned {t.description}")
    sched.register_agent("coder", lambda t: f"coded {t.description}")
    sched.register_agent("reviewer", lambda t: f"reviewed {t.description}")

    sched.submit_task("t1", "planner", "decompose", Priority.MEDIUM)
    sched.submit_task("t2", "coder", "implement", Priority.HIGH)
    sched.submit_task("t3", "reviewer", "review", Priority.LOW)
    sched.submit_task("t4", "coder", "interrupt", Priority.CRITICAL)
    # FIFO: same priority, submitted in order -> t5 before t6
    sched.submit_task("t5", "coder", "fifo-a", Priority.MEDIUM)
    sched.submit_task("t6", "coder", "fifo-b", Priority.MEDIUM)
    # Guards: depth exceeded + cycle repetition
    sched.submit_task("deep", "coder", "too deep", Priority.MEDIUM, depth=4)
    for i in range(4):
        sched.submit_task(f"cyc-{i}", "reviewer", "ping-pong", Priority.MEDIUM)

    results = sched.run_event_loop()
    order = [r["task_id"] for r in results if r["status"] == "SUCCESS"]
    print("  dispatch order:", order)
    print("  cycle repeats rejected:",
          sum(1 for r in results if r["status"] == "REJECTED"))
    for r in results:
        if r["status"] == "REJECTED":
            print(f"    {r['task_id']} ({r['role']}): {r['error']}")
    return 0
