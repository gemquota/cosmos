"""Tests for the SPACE spec → L2 goal gateway (spec link, pass 9)."""
import json
import tempfile
from pathlib import Path

from rsis.space_spec import SpaceSpec


def _fixture():
    root = Path(tempfile.mkdtemp(prefix="space-spec-"))
    spec = {
        "meta": {"project_name": "fixture", "completion_pct": 100},
        "answers": {
            "1.1.1": {"open_ended_text": "Experts and researchers"},
        },
        "artifacts": {
            "audience_level": {
                "value": "Experts / researchers",
                "source_question_id": "1.1.1",
                "source_series_id": 1,
                "confidence": 90,
            },
            "domain": {
                "value": "Agentic knowledge systems",
                "source_question_id": "1.2.1",
                "source_series_id": 1,
                "confidence": 80,
            },
        },
    }
    p = root / "spec.json"
    p.write_text(json.dumps(spec))
    return p


def test_load_and_artifacts():
    s = SpaceSpec(str(_fixture()))
    assert s.available
    arts = s.artifacts()
    assert len(arts) == 2
    assert arts[0]["id"] == "audience_level"  # highest confidence first
    assert s.status()["artifacts"] == 2


def test_candidate_goals_reference_artifact():
    s = SpaceSpec(str(_fixture()))
    goals = s.candidate_goals(limit=1)
    assert len(goals) == 1
    assert "spec artifact audience_level" in goals[0]
    assert "question 1.1.1" in goals[0]


def test_search_ranks_by_overlap():
    s = SpaceSpec(str(_fixture()))
    hits = s.search("experts researchers", limit=5)
    assert hits and hits[0]["id"] == "audience_level"


def test_missing_file_not_available():
    s = SpaceSpec("/nonexistent/spec.json")
    assert not s.available
    assert s.candidate_goals() == []


def test_candidate_goals_series_filter():
    p = _fixture()
    d = json.loads(p.read_text())
    d["artifacts"]["deploy_path"] = {
        "value": "Automated CI/CD",
        "source_question_id": "7.1.1",
        "source_series_id": 7,
        "confidence": 100,
    }
    p.write_text(json.dumps(d))
    s = SpaceSpec(str(p))

    series1 = s.candidate_goals(limit=10, series_id=1)
    assert series1 and all("series 1" in g for g in series1)

    series7 = s.candidate_goals(limit=10, series_id=7)
    assert len(series7) == 1
    assert "series 7" in series7[0]
    assert "deploy_path" in series7[0]
