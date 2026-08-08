"""launch — batch planner and runner."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from rsis.launch import LOOP_ORDER, plan_batch, run_batch


def test_plan_shape():
    plan = plan_batch(2)
    assert len(plan) == 2 * len(LOOP_ORDER)
    assert plan[0] == ("run", "from-space")
    assert plan[1] == ("evolve", "self-improve the codebase")


def test_plan_space_sources_every_cycle():
    plan = plan_batch(3, goal_space_cycle=1)
    runs = [g for loop, g in plan if loop == "run"]
    assert runs == ["from-space", "from-space", "from-space"]


def test_plan_clamps_inputs():
    plan = plan_batch(0, 0)
    assert len(plan) == 1 * len(LOOP_ORDER)


def test_run_batch_with_fake_executor():
    calls = []

    def fake_executor(loop, goal, disk_pct):
        calls.append((loop, goal))
        return 0 if loop != "strategies" else 1

    result = run_batch(1, 1, disk_pct=42, executor=fake_executor)
    assert result["executions"] == len(LOOP_ORDER)
    assert len(calls) == len(LOOP_ORDER)
    assert result["per_loop_failures"]["strategies"] == 1
    assert result["per_loop_failures"]["run"] == 0
    assert len(result["failed"]) == 1
    assert result["exit_code"] == 1
    assert result["disk_pct"] == "42"
    assert "✗ strategies" in result["report"]


def test_run_batch_all_ok():
    result = run_batch(1, 1, disk_pct=100,
                       executor=lambda loop, goal, disk: 0)
    assert result["exit_code"] == 0
    assert all(v == 0 for v in result["per_loop_failures"].values())


def test_run_batch_rotates_space_series(monkeypatch):
    import os
    env_seen = []

    def fake_executor(loop, goal, disk_pct):
        if loop == "run":
            env_seen.append(os.environ.get("RSIS_SPACE_SERIES"))
        return 0

    result = run_batch(8, 1, executor=fake_executor)
    assert result["exit_code"] == 0
    runs = [e for e in env_seen if e is not None]
    assert runs == ["1", "2", "3", "4", "5", "6", "7", "1"]
