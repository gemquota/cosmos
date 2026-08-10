"""Batch launcher — run the full L1–L9 loop batch from one entry point.

Mirrors ``infra/loops/run-batch.sh`` in Python so the standing rhythm
(run → evolve → optimize → strategies → identity → metacog → metameta →
mmm) can be driven programmatically and tested. One cycle may source its
L2 goal from a SPACE spec artifact (``goal_space_cycle``), leaving the
traceable spec link the pass-9 verification chain relies on.

Usage:
    python -m rsis launch --cycles 5 --goal-space-cycle 1 --dry-run
"""

from __future__ import annotations

import logging
import os
import subprocess
import sys
from pathlib import Path
from typing import Callable, Optional

logger = logging.getLogger(__name__)

LOOP_ORDER = ("run", "evolve", "optimize", "strategies",
              "identity", "metacog", "metameta", "mmm")
DEFAULT_GOAL = "self-improve the codebase"
FROM_SPACE_GOAL = "from-space"

# ``(loop, goal) -> exit code``; used to make batches testable without
# spawning subprocesses.
Executor = Callable[[str, str, str], int]


def package_root() -> Path:
    """Return the directory that contains the ``rsis`` package."""
    return Path(__file__).resolve().parent.parent


def plan_batch(cycles: int, goal_space_cycle: int = 1,
               goal: Optional[str] = None) -> list[tuple[str, str]]:
    """Return the ``(loop, goal)`` plan for a full L1–L9 batch.

    Every cycle's ``run`` sources its L2 goal from a SPACE spec artifact
    (``from-space``), so a batch covers the whole 326-probe framework via
    series rotation (1..7). ``goal_space_cycle`` is kept for backward
    compatibility but every cycle is now space-sourced. ``goal`` (Phase 11:
    a project profile goal) overrides the run-loop goal for every cycle.
    """
    cycles = max(1, int(cycles))
    max(1, int(goal_space_cycle))  # kept for CLI/API compatibility
    run_goal = goal or FROM_SPACE_GOAL
    plan: list[tuple[str, str]] = []
    for c in range(1, cycles + 1):
        for loop in LOOP_ORDER:
            if loop == "run":
                plan.append((loop, run_goal))
            else:
                plan.append((loop, DEFAULT_GOAL))
    return plan


def _default_executor(cwd: Path) -> Executor:
    """Run ``python -m rsis <loop> --goal <goal>`` in the package root."""

    def execute(loop: str, goal: str, disk_pct: str) -> int:
        env = dict(os.environ)
        if disk_pct:
            env["RSIS_DISK_USAGE_PCT"] = disk_pct
        cmd = [sys.executable, "-m", "rsis", loop]
        if loop == "run":
            cmd += ["--goal", goal]
        logger.info("launch: executing %s (cwd=%s)", " ".join(cmd), cwd)
        proc = subprocess.run(cmd, cwd=str(cwd), env=env)
        return proc.returncode

    return execute


def run_batch(cycles: int, goal_space_cycle: int = 1,
              disk_pct: Optional[int] = None,
              executor: Optional[Executor] = None,
              cwd: Optional[Path] = None,
              goal: Optional[str] = None) -> dict:
    """Execute a batch and return a results summary.

    ``executor`` defaults to spawning ``python -m rsis`` subprocesses in
    the package root. The summary carries the full plan, per-loop failure
    counts, and a single ``exit_code`` (0 when every execution succeeded).
    """
    plan = plan_batch(cycles, goal_space_cycle, goal=goal)
    root = cwd or package_root()
    disk = str(disk_pct) if disk_pct is not None else os.environ.get(
        "RSIS_DISK_USAGE_PCT", "100")
    run = executor or _default_executor(root)

    per_loop: dict[str, int] = {}
    failed: list[tuple[str, str]] = []
    space_runs = 0
    for loop, goal in plan:
        if loop == "run" and goal == FROM_SPACE_GOAL:
            space_runs += 1
            # Rotate goal sourcing across SPACE series 1..7 so a batch
            # covers the whole 326-probe framework, not just series 1.
            os.environ["RSIS_SPACE_SERIES"] = str((space_runs - 1) % 7 + 1)
        code = run(loop, goal, disk)
        per_loop[loop] = per_loop.get(loop, 0) + (0 if code == 0 else 1)
        if code != 0:
            failed.append((loop, goal))

    exit_code = 0 if not failed else 1
    return {
        "cycles": max(1, int(cycles)),
        "executions": len(plan),
        "goal_space_cycle": max(1, int(goal_space_cycle)),
        "disk_pct": disk,
        "goal": goal,
        "plan": [{"loop": l, "goal": g} for l, g in plan],
        "per_loop_failures": per_loop,
        "failed": [{"loop": l, "goal": g} for l, g in failed],
        "exit_code": exit_code,
        "report": _report(plan, failed, per_loop, disk),
    }


def _report(plan: list[tuple[str, str]], failed: list[tuple[str, str]],
            per_loop: dict[str, int], disk_pct: str) -> str:
    lines = [
        f"🌌 batch: {len(plan)} executions, {len(failed)} failed "
        f"(disk override RSIS_DISK_USAGE_PCT={disk_pct})",
    ]
    if failed:
        for loop, goal in failed:
            lines.append(f"  ✗ {loop} (goal: {goal})")
    else:
        for loop, count in sorted(per_loop.items()):
            lines.append(f"  ✓ {loop}: {count} ok")
    return "\n".join(lines)
