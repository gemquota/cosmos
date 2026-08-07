"""Tests for the MyKB gateway (memory link, pass 8)."""
import tempfile
from pathlib import Path
from unittest import mock

from rsis.mykb_gateway import MyKBGateway, _slugify


def _fixture():
    root = Path(tempfile.mkdtemp(prefix="mykb-gw-"))
    syn = root / "wiki" / "syntheses"
    syn.mkdir(parents=True)
    (syn / "first-2026-08-06.md").write_text(
        '---\n'
        'type: "synthesis"\n'
        'title: "First durable synthesis"\n'
        'description: "Improvement guidance from an earlier pass"\n'
        'tags: ["rsis3", "guidance"]\n'
        'timestamp: "2026-08-06T12:00:00Z"\n'
        'status: "growing"\n'
        '---\n\n'
        '# First\n\nBody.\n'
    )
    (root / "log.md").write_text(
        '---\ntype: "log"\ntitle: "Bundle Log"\n---\n\n# Bundle Log\n\n'
        '## 2026-08-06 (earlier)\n- old entry\n'
    )
    return root


def test_read_syntheses_and_search():
    gw = MyKBGateway(str(_fixture()))
    assert gw.available
    hits = gw.search_syntheses("improvement guidance", limit=5)
    assert hits and hits[0]["slug"] == "first-2026-08-06"
    assert hits[0]["title"] == "First durable synthesis"


def test_write_synthesis_okf():
    gw = MyKBGateway(str(_fixture()))
    with mock.patch("rsis.mykb_gateway.datetime") as dt:
        dt.now.return_value.strftime.return_value = "2026-08-06T12:00:00Z"
        dt.now.return_value.strftime.side_effect = lambda f: "2026-08-06" if f == "%Y-%m-%d" else "2026-08-06T12:00:00Z"
        path = gw.write_synthesis(
            title="L3 cycle 1 consolidation",
            description="insights consolidated",
            tags=["rsis3", "l3", "mykb"],
            body="# L3 cycle 1\n\nDurable notes.\n",
        )
    assert path.exists()
    text = path.read_text()
    assert 'type: "synthesis"' in text
    assert 'title: "L3 cycle 1 consolidation"' in text
    assert 'timestamp: "2026-08-06T' in text
    assert 'tags: ["rsis3", "l3", "mykb"]' in text
    # same slug + date gets a numeric suffix (every cycle is durable)
    path2 = gw.write_synthesis(title="L3 cycle 1 consolidation")
    assert path2.name != path.name and path2.exists()


def test_append_log_prepends_after_header():
    gw = MyKBGateway(str(_fixture()))
    with mock.patch("rsis.mykb_gateway.datetime") as dt:
        dt.now.return_value.strftime.return_value = "2026-08-06"
        gw.append_log("RSIS3 L3 cycle 1", ["wrote a synthesis"])
    text = gw.log_path.read_text()
    assert "# Bundle Log\n\n## 2026-08-06 (RSIS3 L3 cycle 1)\n- wrote a synthesis" in text
    assert "- old entry" in text
    assert text.index("L3 cycle 1") < text.index("earlier")


def test_slugify():
    assert _slugify("RSIS3 L3 cycle 1 — memory consolidation") == \
        "rsis3-l3-cycle-1-memory-consolidation"
