"""Self-assessment routine tests (hermetic: no API key, no real wiki)."""
import json
import sys
import sys as _sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from rsis.config import RSISConfig, SelfAssessConfig


def test_self_assess_config_defaults():
    cfg = SelfAssessConfig()
    assert cfg.window_days == 7
    assert cfg.assessments_dir == "wiki/assessments"
    assert cfg.reflections_dir == "wiki/reflections"
    assert cfg.backlog_dir == "wiki/backlog"
    assert cfg.daemon_timeout_s == 60
    assert cfg.llm_enabled is True
    assert RSISConfig().self_assess == cfg


from rsis.self_assess import HealthReport, scan_wiki_health


def make_wiki(root: Path):
    """Minimal wiki: one deep page, one stub page, one broken link."""
    wiki = root / "wiki"
    (wiki / "concepts").mkdir(parents=True)
    deep = "word " * 350
    (wiki / "concepts" / "deep.md").write_text(
        f"---\ntype: concept\ntitle: Deep\ntags: [a]\n---\n\n{deep}[[missing-target]]\n",
        encoding="utf-8")
    (wiki / "concepts" / "shallow.md").write_text(
        "---\ntype: concept\ntitle: Shallow\nstatus: stub\n---\n\nshort body\n",
        encoding="utf-8")
    (root / "stub-index.json").write_text(
        json.dumps({"total": 1, "stubs": [{"path": "wiki/concepts/shallow.md"}]}),
        encoding="utf-8")


FAKE_LINTER = [_sys.executable, "-c",
               "import json; print(json.dumps({'summary': "
               "{'broken_links': 1, 'orphan_notes': 1}}))"]


def test_scan_wiki_health_counts(tmp_path):
    make_wiki(tmp_path)
    report = scan_wiki_health(tmp_path, linter_cmd=FAKE_LINTER)
    assert report.total_pages == 2
    assert report.stubs == 1
    assert report.broken_links == 1
    assert report.orphans == 1
    assert report.below_floor == 1
    assert report.body_words >= 350
    assert report.links_scanned is True


def test_health_score_weights():
    report = HealthReport(total_pages=10, total_links=10, broken_links=0,
                          orphans=0, stubs=0, body_words=3200)
    assert report.score() == 1.0
    broken = HealthReport(total_pages=10, total_links=10, broken_links=10,
                          orphans=0, stubs=0, body_words=3200)
    assert broken.score() == 0.75  # link weight 0.25 zeroed


def test_health_scan_missing_wiki_is_soft(tmp_path):
    report = scan_wiki_health(tmp_path, linter_cmd=FAKE_LINTER)
    assert report.total_pages == 0
    assert report.score() == 1.0
    assert report.notes


def test_scan_wiki_health_bad_stub_index_is_soft(tmp_path):
    make_wiki(tmp_path)
    (tmp_path / "stub-index.json").write_text("[]", encoding="utf-8")
    report = scan_wiki_health(tmp_path, linter_cmd=FAKE_LINTER)
    assert report.stubs == 0
    assert any("stub-index.json unreadable" in n for n in report.notes)


def test_scan_wiki_health_skips_hidden_segments(tmp_path):
    make_wiki(tmp_path)
    hidden = tmp_path / "wiki" / ".obsidian"
    hidden.mkdir()
    (hidden / "workspace.md").write_text("hidden note\n", encoding="utf-8")
    report = scan_wiki_health(tmp_path, linter_cmd=FAKE_LINTER)
    assert report.total_pages == 2


def test_scan_wiki_health_linter_unavailable_is_fail_closed(tmp_path):
    make_wiki(tmp_path)
    report = scan_wiki_health(tmp_path, linter_cmd=["python3", "-c",
                                                    "print('not json')"])
    assert report.links_scanned is False
    assert report.score() < 1.0
    assert any("kb_linter unavailable" in n for n in report.notes)


from rsis.self_assess import GapItem, analyze_gaps, build_coverage_index


def test_coverage_index_maps_tokens_to_pages(tmp_path):
    wiki = tmp_path / "wiki"
    wiki.mkdir()
    (wiki / "page.md").write_text("quantum decoherence notes\n",
                                  encoding="utf-8")
    index = build_coverage_index(wiki)
    assert "quantum" in index
    assert "decoherence" in index
    assert index["quantum"] == {"page.md"}


def test_analyze_gaps_covered_and_uncovered(tmp_path):
    wiki = tmp_path / "wiki"
    wiki.mkdir()
    (wiki / "page.md").write_text("quantum decoherence entanglement\n",
                                  encoding="utf-8")
    index = build_coverage_index(wiki)
    syntheses = [
        {"title": "Quantum Decoherence Patterns",
         "description": "entanglement collapse behavior"},
        {"title": "Zebra Migration Routes",
         "description": "seasonal savanna movement"},
    ]
    gaps = analyze_gaps(syntheses, index)
    assert len(gaps) == 1
    assert gaps[0].topic == "Zebra Migration Routes"
    assert gaps[0].priority == "high"
    assert gaps[0].slug == "zebra-migration-routes"


def test_gap_slug_fallback():
    gap = GapItem(topic="!!!", priority="high", reason="x")
    assert gap.slug == "gap"


def test_build_coverage_index_skips_hidden_segments(tmp_path):
    wiki = tmp_path / "wiki"
    (wiki / ".obsidian").mkdir(parents=True)
    (wiki / "page.md").write_text("quantum decoherence\n", encoding="utf-8")
    (wiki / ".obsidian" / "workspace.md").write_text("quantum notes\n",
                                                    encoding="utf-8")
    index = build_coverage_index(wiki)
    assert index["quantum"] == {"page.md"}


def test_build_coverage_index_missing_dir_is_empty(tmp_path):
    assert build_coverage_index(tmp_path / "nope") == {}


def test_analyze_gaps_max_gaps_and_covered(tmp_path):
    wiki = tmp_path / "wiki"
    wiki.mkdir()
    (wiki / "page.md").write_text("quantum decoherence entanglement\n",
                                  encoding="utf-8")
    index = build_coverage_index(wiki)
    syntheses = [
        {"title": "Quantum Decoherence Patterns",
         "description": "entanglement collapse behavior"},
        {"title": "Zebra Migration Routes",
         "description": "seasonal savanna movement"},
        {"title": "Orchid Pollination Cycles",
         "description": "tropical insect mutualism"},
    ]
    gaps = analyze_gaps(syntheses, index, max_gaps=1)
    assert len(gaps) == 1
    assert gaps[0].topic == "Zebra Migration Routes"


def test_analyze_gaps_zero_max_returns_empty(tmp_path):
    wiki = tmp_path / "wiki"
    wiki.mkdir()
    (wiki / "page.md").write_text("quantum notes\n", encoding="utf-8")
    index = build_coverage_index(wiki)
    syntheses = [{"title": "Zebra Migration Routes",
                  "description": "seasonal savanna movement"}]
    assert analyze_gaps(syntheses, index, max_gaps=0) == []
    assert analyze_gaps(syntheses, index, max_gaps=-1) == []


def test_analyze_gaps_no_missing_keywords_fallback(tmp_path):
    wiki = tmp_path / "wiki"
    wiki.mkdir()
    for i, word in enumerate(["quantum", "decoherence", "patterns",
                              "entanglement", "collapse", "behavior"]):
        (wiki / f"p{i}.md").write_text(f"{word} filler\n",
                                       encoding="utf-8")
    index = build_coverage_index(wiki)
    syntheses = [{"title": "Quantum Decoherence Patterns",
                  "description": "entanglement collapse behavior"}]
    gaps = analyze_gaps(syntheses, index)
    assert len(gaps) == 1
    assert "no page contains two keywords together" in gaps[0].reason


from datetime import datetime, timedelta, timezone

from rsis.self_assess import detect_trends


def make_telemetry(tele_dir: Path, now: datetime):
    tele_dir.mkdir(parents=True, exist_ok=True)
    rows = []
    for i in range(1, 4):
        rows.append({"type": f"l{i}_start",
                     "timestamp": (now - timedelta(days=1)).isoformat()})
        rows.append({"type": f"l{i}_complete",
                     "timestamp": (now - timedelta(days=1)).isoformat()})
    for _ in range(3):
        rows.append({"type": "l2_evaluation", "decision": "FAIL",
                     "timestamp": now.isoformat()})
    (tele_dir / "events.jsonl").write_text(
        "\n".join(json.dumps(r) for r in rows) + "\n", encoding="utf-8")


def test_detect_trends_from_telemetry(tmp_path):
    now = datetime(2026, 8, 7, 12, 0, tzinfo=timezone.utc)
    make_telemetry(tmp_path, now)
    trends = detect_trends(tmp_path, window_days=7, now=now)
    names = {t.name for t in trends}
    assert "loop-completion" in names
    evaluator = next(t for t in trends if t.name == "evaluator-fail-rate")
    assert evaluator.direction == "up"
    assert evaluator.magnitude == 1.0


def test_detect_trends_requires_data_points(tmp_path):
    now = datetime(2026, 8, 7, 12, 0, tzinfo=timezone.utc)
    (tmp_path / "events.jsonl").write_text(
        json.dumps({"type": "l1_start", "timestamp": now.isoformat()}) + "\n",
        encoding="utf-8")
    assert detect_trends(tmp_path, window_days=7, now=now) == []


def test_detect_trends_git_cadence():
    commits = [{"subject": "fix: broken link"}, {"subject": "docs: x"},
               {"subject": "feat: y"}]
    trends = detect_trends(Path("/nonexistent"), window_days=7,
                           git_log=lambda: commits)
    cadence = next(t for t in trends if t.name == "commit-cadence")
    assert cadence.magnitude == 3.0
    assert "fix" in cadence.evidence


def test_detect_trends_ignores_malformed_events(tmp_path):
    now = datetime(2026, 8, 7, 12, 0, tzinfo=timezone.utc)
    (tmp_path / "events.jsonl").write_text(
        json.dumps({"type": None, "timestamp": now.isoformat()}) + "\n"
        + "[1, 2, 3]\n"
        + json.dumps({"type": 42, "timestamp": now.isoformat()}) + "\n",
        encoding="utf-8")
    assert detect_trends(tmp_path, window_days=7, now=now) == []


from rsis.self_assess import (AssessmentResult, HealthReport, write_assessment,
                              write_reflection)


def make_result():
    return AssessmentResult(
        health=HealthReport(total_pages=2, stubs=1, broken_links=1,
                            body_words=700, below_floor=1),
        health_score=0.7, gaps=[], trends=[], window_days=7, prev_score=0.5)


def test_write_assessment_frontmatter_and_body(tmp_path):
    result = make_result()
    path = write_assessment(tmp_path, result, ts="2026-08-07T10:00:00Z")
    text = path.read_text(encoding="utf-8")
    assert path.name == "self-assessment-2026-08-07.md"
    assert 'type: "assessment"' in text
    assert 'health_score: "0.7"' in text
    assert "Health score: **0.7** (previous: 0.5)" in text
    assert "No under-covered topics." in text


def test_write_note_suffix_on_collision(tmp_path):
    result = make_result()
    first = write_assessment(tmp_path, result, ts="2026-08-07T10:00:00Z")
    second = write_assessment(tmp_path, result, ts="2026-08-07T11:00:00Z")
    assert first.name == "self-assessment-2026-08-07.md"
    assert second.name == "self-assessment-2026-08-07-2.md"


def test_write_reflection_links_assessment(tmp_path):
    result = make_result()
    path = write_reflection(tmp_path, result, ts="2026-08-07T10:00:00Z")
    text = path.read_text(encoding="utf-8")
    assert 'type: "reflection"' in text
    assert "[[assessments/self-assessment-2026-08-07]]" in text


from rsis.self_assess import GapItem, Trend


def test_write_assessment_with_gaps_trends_and_notes(tmp_path):
    result = AssessmentResult(
        health=HealthReport(total_pages=2, stubs=1, broken_links=1,
                            body_words=700, below_floor=1,
                            notes=["wiki root missing"]),
        health_score=0.6,
        gaps=[GapItem(topic="Zebra Migration Routes", priority="high",
                      reason="missing keywords: zebra")],
        trends=[Trend(name="evaluator-fail-rate", direction="up",
                      magnitude=0.5, evidence="2/4 evaluator FAILs")],
        window_days=7, prev_score=0.8)
    path = write_assessment(tmp_path, result, ts="2026-08-07T10:00:00Z")
    text = path.read_text(encoding="utf-8")
    assert "[[backlog/zebra-migration-routes]]" in text
    assert "evaluator-fail-rate: up" in text
    assert "- note: wiki root missing" in text
    reflection = write_reflection(tmp_path, result, ts="2026-08-07T10:00:00Z")
    rtext = reflection.read_text(encoding="utf-8")
    assert "Zebra Migration Routes" in rtext


def test_write_assessment_sanitizes_bad_timestamp(tmp_path):
    result = make_result()
    path = write_assessment(tmp_path, result, ts="../../evil/2026-08-07")
    assert path.parent.name == "assessments"
    assert path.name.startswith("self-assessment-")
    assert ".." not in str(path)


from rsis.self_assess import file_backlog, mirror_to_guidance_queue


GAPS = [GapItem(topic="Zebra Migration Routes", priority="high",
                reason="missing keywords: zebra, migration")]


def test_file_backlog_create_only_and_dedupe(tmp_path):
    first = file_backlog(tmp_path, GAPS, ts="2026-08-07T10:00:00Z")
    second = file_backlog(tmp_path, GAPS, ts="2026-08-07T11:00:00Z")
    assert len(first) == 1
    assert len(second) == 0
    path = tmp_path / "backlog" / "zebra-migration-routes.md"
    assert path.is_file()
    text = path.read_text(encoding="utf-8")
    assert 'type: "backlog"' in text
    assert 'status: "open"' in text
    assert 'source: "gap"' in text


def test_mirror_to_guidance_queue_appends_and_dedupes(tmp_path):
    buffer = tmp_path / ".wiki-daemon" / "buffers" / "guidance-queue.json"
    buffer.parent.mkdir(parents=True)
    buffer.write_text(json.dumps({"queued_at": "2026-08-07",
                                  "items": [{"title": "Existing"}]}),
                      encoding="utf-8")
    assert mirror_to_guidance_queue(tmp_path, GAPS) == 1
    assert mirror_to_guidance_queue(tmp_path, GAPS) == 0
    data = json.loads(buffer.read_text(encoding="utf-8"))
    assert len(data["items"]) == 2
    assert data["items"][1]["kind"] == "direction"


def test_mirror_no_buffer_is_noop(tmp_path):
    assert mirror_to_guidance_queue(tmp_path, GAPS) == 0


def test_mirror_malformed_buffer_is_noop(tmp_path):
    buffer = tmp_path / ".wiki-daemon" / "buffers" / "guidance-queue.json"
    buffer.parent.mkdir(parents=True)
    for payload in ("[]", "{}", '{"items": 42}', '{"items": [1, 2]}'):
        buffer.write_text(payload, encoding="utf-8")
        assert mirror_to_guidance_queue(tmp_path, GAPS) == 0
