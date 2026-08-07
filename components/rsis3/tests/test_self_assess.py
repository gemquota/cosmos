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
