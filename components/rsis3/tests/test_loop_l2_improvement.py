"""L2 — real candidate generation and safe application."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from rsis.config import CONFIG
from rsis.evaluator import EvalResult
from rsis.loop_l2 import L2ImprovementLoop
from rsis.telemetry import TelemetryCollector


class RecordTelemetry:
    def __init__(self):
        self.events = []

    def record(self, event):
        self.events.append(event)


class PassEvaluator:
    def evaluate(self, candidate):
        return EvalResult(
            decision="PASS",
            scores={"correctness": 1.0, "safety": 1.0},
            rationale="stub evaluator passes",
        )


def make_loop(workspace: Path, monkeypatch) -> L2ImprovementLoop:
    monkeypatch.setattr(CONFIG, "workspace_dir", str(workspace))
    return L2ImprovementLoop(
        telemetry=RecordTelemetry(),
        evaluator=PassEvaluator(),
        checkpoint_mgr=type("CP", (), {"checkpoint": lambda self, *a, **k: None})(),
    )


def test_goal_target_parses_path(tmp_path, monkeypatch):
    loop = make_loop(tmp_path, monkeypatch)
    (tmp_path / "rsis").mkdir()
    target = loop._resolve_target(
        "Implement BatchRunner in rsis/batch.py - replace stub with production code")
    assert target == ("rsis/batch.py", "BatchRunner")


def test_goal_target_skips_existing_files(tmp_path, monkeypatch):
    loop = make_loop(tmp_path, monkeypatch)
    (tmp_path / "rsis").mkdir()
    (tmp_path / "rsis" / "existing.py").write_text("x = 1\n")
    target = loop._resolve_target("Implement X in rsis/existing.py")
    assert target is None


def test_generates_compilable_scaffold(tmp_path, monkeypatch):
    loop = make_loop(tmp_path, monkeypatch)
    (tmp_path / "rsis").mkdir()
    candidate = loop._generate_candidate(
        "Implement TimeoutGuard in rsis/guard.py - replace stub", 1, [])
    assert candidate is not None
    assert candidate.target_files == ["rsis/guard.py"]
    compile(candidate.diff_or_code, "rsis/guard.py", "exec")


def test_apply_writes_only_missing_files(tmp_path, monkeypatch):
    loop = make_loop(tmp_path, monkeypatch)
    (tmp_path / "rsis").mkdir()
    (tmp_path / "rsis" / "keep.py").write_text("KEEP = True\n")
    candidate = loop._generate_candidate(
        "Implement Runner in rsis/new_mod.py", 1, [])
    assert candidate is not None
    loop._apply_improvement(candidate)
    assert (tmp_path / "rsis" / "new_mod.py").exists()
    assert (tmp_path / "rsis" / "keep.py").read_text() == "KEEP = True\n"


def test_run_session_applies_real_improvement(tmp_path, monkeypatch):
    loop = make_loop(tmp_path, monkeypatch)
    (tmp_path / "rsis").mkdir()
    goal = "Implement Watcher in rsis/watcher.py - replace stub with production code"
    result = loop.run_session(goal)
    assert result.success
    assert result.applied is not None
    assert (tmp_path / "rsis" / "watcher.py").exists()
    assert "applied_files" in result.applied.metadata
