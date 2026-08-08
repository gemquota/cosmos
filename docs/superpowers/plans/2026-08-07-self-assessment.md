# Self-Assessment Routine Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add `python -m rsis self-assess` — a deterministic-first routine that scans KB health, finds coverage gaps, detects trends from telemetry/git/logs, writes `assessments/` + `reflections/` notes, files `backlog/` items, and optionally enriches with a fail-closed LLM pass.

**Architecture:** A single phase-based module `rsis/self_assess.py` composes six pure-function phases (health scan, gap analysis, trend detection, artifacts, backlog, LLM enrichment) behind a `SelfAssessment` orchestrator. It reuses `MyKBGateway` for syntheses and the daemon's `kb_linter.py --json` for link/orphan metrics (read-only subprocess); writes are create-only OKF notes in new `wiki/assessments/`, `wiki/reflections/`, `wiki/backlog/` areas. CLI wiring, config, batch hook, version, changelog, and docs follow the repo's existing loop conventions.

**Tech Stack:** Python 3.13 stdlib only (subprocess, ast-free regex/JSON), pytest, existing RSIS3 config/telemetry/mykb_gateway modules, bash (run-batch hook).

---

## File Structure

| File | Responsibility |
|------|----------------|
| `components/rsis3/rsis/self_assess.py` (create) | All phases + `SelfAssessment` orchestrator (health, gaps, trends, artifacts, backlog, LLM) |
| `components/rsis3/tests/test_self_assess.py` (create) | Unit + end-to-end tests, hermetic (no API key) |
| `components/rsis3/rsis/config.py` (modify) | `SelfAssessConfig` dataclass + wire into `RSISConfig` |
| `components/rsis3/rsis/main.py` (modify) | `cmd_self_assess` + `self-assess` subparser |
| `components/rsis3/rsis/__init__.py` (modify) | version `0.4.4` |
| `components/rsis3/CHANGELOG.md` (modify) | `[0.4.4]` entry |
| `infra/loops/run-batch.sh` (modify) | `self-assess` step + new wiki areas in the pre-snapshot `git add` |
| `components/rsis3/docs/usage-practices.md` (modify) | document the command |

Reference interfaces (already in repo — do not reimplement):
- `MyKBGateway(root).read_syntheses(limit)` → list of `{title, description, tags, ...}`; `MyKBGateway(mykb_root=...)` resolves root explicitly.
- `TelemetryCollector.record(TelemetryEvent(event_type=..., metadata={...}))`.
- `CONFIG.self_assess` (added in Task 1) and `CONFIG.workspace_dir`.
- daemon `kb_linter.py --json` prints `{"summary": {"broken_links": N, "orphan_notes": N, ...}}`.
- daemon `build_stub_index.py` writes `components/mykb/stub-index.json` with `{"total": N, "stubs": [...]}` (tracked snapshot; read it, never regenerate).

All test commands run from the repo root unless stated. Expected output lines are shown after each command.

---

## Task 1: `SelfAssessConfig` + wiring

**Files:**
- Modify: `components/rsis3/rsis/config.py` (add dataclass near `EvaluatorConfig`; add field to `RSISConfig`)
- Test: `components/rsis3/tests/test_self_assess.py` (create)

- [ ] **Step 1: Write the failing test**

Create `components/rsis3/tests/test_self_assess.py`:

```python
"""Self-assessment routine tests (hermetic: no API key, no real wiki)."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from rsis.config import CONFIG


def test_self_assess_config_defaults():
    assert CONFIG.self_assess.window_days == 7
    assert CONFIG.self_assess.assessments_dir == "wiki/assessments"
    assert CONFIG.self_assess.backlog_dir == "wiki/backlog"
    assert CONFIG.self_assess.daemon_timeout_s == 60
    assert CONFIG.self_assess.llm_enabled is True
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python3 -m pytest components/rsis3/tests/test_self_assess.py -q`
Expected: FAIL with `AttributeError: ... 'RSISConfig' object has no attribute 'self_assess'`

- [ ] **Step 3: Implement the config**

In `components/rsis3/rsis/config.py`, after the `EvaluatorConfig` dataclass, add:

```python
@dataclass
class SelfAssessConfig:
    """Self-assessment routine (pass 14)."""
    window_days: int = 7
    assessments_dir: str = "wiki/assessments"
    reflections_dir: str = "wiki/reflections"
    backlog_dir: str = "wiki/backlog"
    daemon_timeout_s: int = 60
    llm_enabled: bool = True
```

In `RSISConfig`, after the `tools: ToolConfig` field, add:

```python
    self_assess: SelfAssessConfig = field(default_factory=SelfAssessConfig)
```

- [ ] **Step 4: Run test to verify it passes**

Run: `python3 -m pytest components/rsis3/tests/test_self_assess.py -q`
Expected: PASS (1 passed)

- [ ] **Step 5: Commit**

```bash
git add components/rsis3/rsis/config.py components/rsis3/tests/test_self_assess.py
git commit -m "rsis: self-assess config (pass 14 scaffolding)"
```

---

## Task 2: P1 health scan + scoring

**Files:**
- Create: `components/rsis3/rsis/self_assess.py` (module skeleton + `HealthReport` + `scan_wiki_health`)
- Test: `components/rsis3/tests/test_self_assess.py`

- [ ] **Step 1: Write the failing tests**

Append to `components/rsis3/tests/test_self_assess.py`:

```python
import json
import sys as _sys

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
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `python3 -m pytest components/rsis3/tests/test_self_assess.py -q`
Expected: FAIL with `ModuleNotFoundError: No module named 'rsis.self_assess'`

- [ ] **Step 3: Implement the module skeleton + health scan**

Create `components/rsis3/rsis/self_assess.py`:

```python
"""Self-assessment routine — KB health, gaps, trends, artifacts, backlog.

Deterministic-first (stdlib-only) with optional fail-closed LLM
enrichment, matching the immutable evaluator gate philosophy (pass 13).
Design: docs/superpowers/specs/2026-08-07-self-assessment-design.md

Usage:
    python -m rsis self-assess [--days 7] [--no-backlog] [--json]
"""

from __future__ import annotations

import json
import logging
import os
import re
import subprocess
import sys
from dataclasses import dataclass, field
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Callable, Optional

from rsis.config import CONFIG
from rsis.mykb_gateway import MyKBGateway
from rsis.telemetry import TelemetryCollector, TelemetryEvent

logger = logging.getLogger(__name__)

STUB_FLOOR = 320  # matches .wiki-daemon/build_stub_index.py
FM_RE = re.compile(r"^---\s*\n(.*?)\n---", re.S)
KEY_RE = re.compile(r"^(\w+):\s*(.*)$", re.M)
WIKILINK_RE = re.compile(r"\[\[([^\]|]+)(?:\|[^\]]+)?\]\]")
TOKEN_RE = re.compile(r"[a-z0-9]+")
STOPWORDS = frozenset({
    "the", "and", "for", "with", "from", "that", "this", "into", "what",
    "when", "where", "which", "about", "than", "then", "have", "were",
})


@dataclass
class HealthReport:
    """P1 — deterministic KB health metrics (spec §7)."""
    total_pages: int = 0
    total_links: int = 0
    broken_links: int = 0
    orphans: int = 0
    stubs: int = 0
    body_words: int = 0
    below_floor: int = 0
    notes: list[str] = field(default_factory=list)

    def score(self) -> float:
        """Weighted 0.0–1.0 health score (link .25 / orphan .15 / stub .30 / depth .30)."""
        def ratio(good: int, total: int) -> float:
            return 1.0 if total == 0 else max(0.0, good / total)

        link_h = ratio(self.total_links - self.broken_links, self.total_links)
        orphan_h = ratio(self.total_pages - self.orphans, self.total_pages)
        stub_h = ratio(self.total_pages - self.stubs, self.total_pages)
        depth = 1.0 if self.total_pages == 0 else min(
            1.0, (self.body_words / max(1, self.total_pages)) / STUB_FLOOR)
        return round(0.25 * link_h + 0.15 * orphan_h
                     + 0.30 * stub_h + 0.30 * depth, 3)


def _frontmatter(text: str) -> dict:
    fm: dict = {}
    m = FM_RE.match(text or "")
    if not m:
        return fm
    for k, v in KEY_RE.findall(m.group(1)):
        fm[k] = v.strip().strip('"').strip("'")
    return fm


def _body_words(text: str) -> int:
    body = re.sub(r"^---\s*\n.*?\n---", "", text or "", count=1, flags=re.S)
    body = re.sub(r"```.*?```", " ", body, flags=re.S)
    return len(TOKEN_RE.findall(body.lower()))


def _run_json(cmd: list[str], timeout_s: int) -> Optional[dict]:
    """Run a daemon tool that prints JSON; None on any failure."""
    try:
        r = subprocess.run(cmd, capture_output=True, text=True,
                           timeout=timeout_s)
        return json.loads(r.stdout)
    except (subprocess.SubprocessError, json.JSONDecodeError, OSError):
        return None


def scan_wiki_health(mykb_root: Path,
                     linter_cmd: Optional[list[str]] = None,
                     timeout_s: int = 60) -> HealthReport:
    """P1 — read-only KB health scan (spec §5/§7)."""
    report = HealthReport()
    wiki = mykb_root / "wiki"
    if not wiki.is_dir():
        report.notes.append("wiki root missing")
        return report
    for rel in sorted(wiki.rglob("*.md")):
        if any(seg.startswith(".") for seg in rel.relative_to(wiki).parts):
            continue
        text = rel.read_text(encoding="utf-8", errors="ignore")
        words = _body_words(text)
        report.total_pages += 1
        report.body_words += words
        report.total_links += len(WIKILINK_RE.findall(text))
        if words < STUB_FLOOR:
            report.below_floor += 1

    stub_index = mykb_root / "stub-index.json"
    if stub_index.is_file():
        try:
            report.stubs = int(json.loads(
                stub_index.read_text(encoding="utf-8")).get("total", 0))
        except (json.JSONDecodeError, OSError, TypeError):
            report.notes.append("stub-index.json unreadable")

    cmd = linter_cmd or [sys.executable,
                         str(mykb_root / ".wiki-daemon" / "kb_linter.py"),
                         "--json"]
    data = _run_json(cmd, timeout_s)
    if data and isinstance(data.get("summary"), dict):
        summary = data["summary"]
        report.broken_links = int(summary.get("broken_links", 0))
        report.orphans = int(summary.get("orphan_notes", 0))
    else:
        report.notes.append("kb_linter unavailable — link/orphan metrics "
                            "not scanned")
    return report
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `python3 -m pytest components/rsis3/tests/test_self_assess.py -q`
Expected: PASS (4 passed)

- [ ] **Step 5: Commit**

```bash
git add components/rsis3/rsis/self_assess.py components/rsis3/tests/test_self_assess.py
git commit -m "rsis: self-assess P1 — KB health scan + weighted score"
```

---

## Task 3: P2 coverage index + gap analysis

**Files:**
- Modify: `components/rsis3/rsis/self_assess.py` (append `GapItem`, `build_coverage_index`, `analyze_gaps`)
- Test: `components/rsis3/tests/test_self_assess.py`

- [ ] **Step 1: Write the failing tests**

Append to the test file:

```python
from rsis.self_assess import GapItem, analyze_gaps, build_coverage_index


def test_coverage_index_maps_tokens_to_pages(tmp_path):
    wiki = tmp_path / "wiki"
    wiki.mkdir()
    (wiki / "page.md").write_text("quantum decoherence notes\n", encoding="utf-8")
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
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `python3 -m pytest components/rsis3/tests/test_self_assess.py -q`
Expected: FAIL with `ImportError` for `build_coverage_index`

- [ ] **Step 3: Implement**

Append to `components/rsis3/rsis/self_assess.py`:

```python
@dataclass
class GapItem:
    """P2 — a topic the wiki does not cover (spec §6.3)."""
    topic: str
    priority: str
    reason: str
    slug: str = ""

    def __post_init__(self) -> None:
        if not self.slug:
            slug = re.sub(r"[^a-z0-9]+", "-", self.topic.lower()).strip("-")
            self.slug = slug or "gap"


def build_coverage_index(wiki_root: Path) -> dict[str, set[str]]:
    """Token → set of page ids containing it (read-only, spec §6.2a)."""
    index: dict[str, set[str]] = {}
    if not wiki_root.is_dir():
        return index
    for rel in sorted(wiki_root.rglob("*.md")):
        text = rel.read_text(encoding="utf-8", errors="ignore")
        body = re.sub(r"^---\s*\n.*?\n---", "", text, count=1, flags=re.S)
        page_id = str(rel.relative_to(wiki_root))
        for tok in set(TOKEN_RE.findall(body.lower())):
            if tok not in STOPWORDS and len(tok) >= 4:
                index.setdefault(tok, set()).add(page_id)
    return index


def analyze_gaps(syntheses: list[dict], index: dict[str, set[str]],
                 max_gaps: int = 10) -> list[GapItem]:
    """P2 — topics under-covered by the wiki (spec §6.2a).

    A synthesis topic is covered when at least two of its significant
    tokens co-occur in some wiki page; otherwise it becomes a gap.
    """
    gaps: list[GapItem] = []
    for syn in syntheses:
        text = f"{syn.get('title', '')} {syn.get('description', '')}".lower()
        tokens = sorted({t for t in TOKEN_RE.findall(text)
                         if t not in STOPWORDS and len(t) >= 5})
        if len(tokens) < 2:
            continue
        pairs = [(t1, t2)
                 for i, t1 in enumerate(tokens) for t2 in tokens[i + 1:]]
        covered = any(bool(index.get(t1, set()) & index.get(t2, set()))
                      for t1, t2 in pairs)
        if covered:
            continue
        missing = [t for t in tokens if not index.get(t)][:3]
        gaps.append(GapItem(
            topic=syn.get("title", "untitled synthesis"),
            priority="high",
            reason=f"under-covered topic; missing keywords: {', '.join(missing)}",
        ))
        if len(gaps) >= max_gaps:
            break
    return gaps
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `python3 -m pytest components/rsis3/tests/test_self_assess.py -q`
Expected: PASS (7 passed)

- [ ] **Step 5: Commit**

```bash
git add components/rsis3/rsis/self_assess.py components/rsis3/tests/test_self_assess.py
git commit -m "rsis: self-assess P2 — coverage index + gap analysis"
```

---

## Task 4: P3 trend detection

**Files:**
- Modify: `components/rsis3/rsis/self_assess.py` (append `Trend`, `detect_trends`)
- Test: `components/rsis3/tests/test_self_assess.py`

- [ ] **Step 1: Write the failing tests**

Append:

```python
from datetime import datetime, timedelta, timezone

from rsis.self_assess import detect_trends


def make_telemetry(tele_dir: Path, now: datetime):
    tele_dir.mkdir(parents=True)
    rows = []
    for i in range(1, 4):
        rows.append({"type": f"l{i}_start",
                     "timestamp": (now - timedelta(days=1)).isoformat()})
        rows.append({"type": f"l{i}_complete",
                     "timestamp": (now - timedelta(days=1)).isoformat()})
    rows.append({"type": "l2_evaluation", "decision": "FAIL",
                 "timestamp": now.isoformat()})
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
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `python3 -m pytest components/rsis3/tests/test_self_assess.py -q`
Expected: FAIL with `ImportError` for `detect_trends`

- [ ] **Step 3: Implement**

Append to `components/rsis3/rsis/self_assess.py`:

```python
@dataclass
class Trend:
    """P3 — a detected pattern with direction and evidence (spec §8)."""
    name: str
    direction: str
    magnitude: float
    evidence: str


def _as_utc(dt: datetime) -> datetime:
    if dt.tzinfo is None:
        return dt.replace(tzinfo=timezone.utc)
    return dt.astimezone(timezone.utc)


def detect_trends(telemetry_dir: Path, window_days: int = 7,
                  git_log: Optional[Callable[[], list[dict]]] = None,
                  now: Optional[datetime] = None) -> list[Trend]:
    """P3 — trends from telemetry + git (spec §8; ≥3 data points each)."""
    now = _as_utc(now or datetime.now(timezone.utc))
    cutoff = now - timedelta(days=window_days)
    counts: dict[str, int] = {}
    passes = fails = 0
    for f in sorted(Path(telemetry_dir).glob("*.jsonl")):
        for line in f.read_text(encoding="utf-8", errors="ignore").splitlines():
            try:
                ev = json.loads(line)
            except json.JSONDecodeError:
                continue
            try:
                ts = _as_utc(datetime.fromisoformat(ev.get("timestamp", "")))
            except (TypeError, ValueError):
                continue
            if ts < cutoff:
                continue
            etype = ev.get("type", "")
            counts[etype] = counts.get(etype, 0) + 1
            if etype.endswith("_evaluation"):
                if ev.get("decision") == "PASS":
                    passes += 1
                else:
                    fails += 1
    trends: list[Trend] = []
    starts = sum(counts.get(f"l{i}_start", 0) for i in range(1, 10))
    completes = sum(counts.get(f"l{i}_complete", 0) for i in range(1, 10))
    if starts >= 3:
        ratio = completes / starts
        trends.append(Trend(
            "loop-completion", "down" if ratio < 0.9 else "flat",
            round(ratio, 3), f"{completes}/{starts} loop completions"))
    total_evals = passes + fails
    if total_evals >= 3:
        fail_rate = fails / total_evals
        trends.append(Trend(
            "evaluator-fail-rate",
            "up" if fail_rate > 0.2 else "flat",
            round(fail_rate, 3), f"{fails}/{total_evals} evaluator FAILs"))
    if git_log is not None:
        commits = git_log() or []
        if len(commits) >= 3:
            fixish = sum(1 for c in commits
                         if re.search(r"\b(revert|fix|hotfix)\b",
                                      c.get("subject", "").lower()))
            trends.append(Trend(
                "commit-cadence", "flat", round(len(commits), 3),
                f"{len(commits)} commits in window, {fixish} fix/revert"))
    return trends
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `python3 -m pytest components/rsis3/tests/test_self_assess.py -q`
Expected: PASS (10 passed)

- [ ] **Step 5: Commit**

```bash
git add components/rsis3/rsis/self_assess.py components/rsis3/tests/test_self_assess.py
git commit -m "rsis: self-assess P3 — telemetry + git trend detection"
```

---

## Task 5: P4 artifact writers

**Files:**
- Modify: `components/rsis3/rsis/self_assess.py` (append `AssessmentResult`, `_write_note`, `write_assessment`, `write_reflection`)
- Test: `components/rsis3/tests/test_self_assess.py`

- [ ] **Step 1: Write the failing tests**

Append:

```python
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
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `python3 -m pytest components/rsis3/tests/test_self_assess.py -q`
Expected: FAIL with `ImportError` for `write_assessment`

- [ ] **Step 3: Implement**

Append to `components/rsis3/rsis/self_assess.py`:

```python
@dataclass
class AssessmentResult:
    """Output of one self-assessment run."""
    health: HealthReport
    health_score: float
    gaps: list[GapItem]
    trends: list[Trend]
    window_days: int = 7
    prev_score: Optional[float] = None
    assessment_path: Optional[str] = None
    reflection_path: Optional[str] = None
    backlog_paths: list[str] = field(default_factory=list)
    error: Optional[str] = None


def _now_ts() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _write_note(path: Path, fm: dict, body: str) -> Path:
    """Create-only OKF note writer; numeric suffix on same-name collision."""
    path.parent.mkdir(parents=True, exist_ok=True)
    final = path
    n = 2
    while final.exists():
        final = path.with_name(f"{path.stem}-{n}{path.suffix}")
        n += 1
    lines = ["---"]
    for k, v in fm.items():
        if isinstance(v, (list, tuple)):
            lines.append(f"{k}: [{', '.join('\"%s\"' % x for x in v)}]")
        else:
            lines.append(f'{k}: "{v}"')
    lines.append("---")
    final.write_text("\n".join(lines) + "\n\n" + body.strip() + "\n",
                     encoding="utf-8")
    return final


def write_assessment(root: Path, result: AssessmentResult,
                     ts: Optional[str] = None) -> Path:
    """P4 — assessment note (spec §6.1)."""
    ts = ts or _now_ts()
    date = ts[:10]
    prev = (f" (previous: {result.prev_score})"
            if result.prev_score is not None else "")
    body = [
        f"# Self-Assessment {date}",
        "",
        "## Health",
        f"- Health score: **{result.health_score}**{prev}",
        f"- Pages: {result.health.total_pages} · "
        f"Stubs: {result.health.stubs}",
        f"- Broken links: {result.health.broken_links} · "
        f"Orphans: {result.health.orphans}",
        f"- Body words: {result.health.body_words} · "
        f"Below {STUB_FLOOR}-word floor: {result.health.below_floor}",
        "",
        "## Gaps",
    ]
    if result.gaps:
        body += [f"- **[{g.priority}]** {g.topic} — {g.reason} "
                 f"([[backlog/{g.slug}]])" for g in result.gaps]
    else:
        body.append("- No under-covered topics.")
    body += ["", "## Trends"]
    if result.trends:
        body += [f"- {t.name}: {t.direction} (magnitude {t.magnitude}) — "
                 f"{t.evidence}" for t in result.trends]
    else:
        body.append("- No trends in window.")
    for note in result.health.notes:
        body.append(f"- note: {note}")
    return _write_note(root / "assessments" / f"self-assessment-{date}.md", {
        "type": "assessment",
        "title": f"Self-Assessment {date}",
        "description": (f"Health {result.health_score}, "
                        f"{len(result.gaps)} gaps, {len(result.trends)} trends"),
        "tags": ["self-assessment", "health", "gaps", "trends"],
        "timestamp": ts,
        "status": "stable",
        "window_days": result.window_days,
        "health_score": result.health_score,
        "prev_note": "",
    }, "\n".join(body))


def write_reflection(root: Path, result: AssessmentResult,
                     ts: Optional[str] = None) -> Path:
    """P4 — prose reflection note; grows the reflections area (spec §6.2)."""
    ts = ts or _now_ts()
    date = ts[:10]
    top_gap = result.gaps[0].topic if result.gaps else "no open gaps"
    top_trend = result.trends[0].name if result.trends else "none yet"
    body = [
        f"# Reflection {date}",
        "",
        "## Surprises",
        f"- Health came in at {result.health_score} with "
        f"{result.health.stubs} stubs and "
        f"{result.health.broken_links} broken links.",
        "",
        "## Open questions",
        f"- What is driving the top gap: {top_gap}?",
        f"- Which trend should the next pass act on first: {top_trend}?",
        "",
        "## Links",
        f"- Assessment: [[assessments/self-assessment-{date}]]",
    ]
    return _write_note(root / "reflections" / f"reflection-{date}.md", {
        "type": "reflection",
        "title": f"Reflection {date}",
        "description": f"Deterministic reflection for the "
                       f"{date} self-assessment",
        "tags": ["reflection", "self-assessment"],
        "timestamp": ts,
        "status": "growing",
    }, "\n".join(body))
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `python3 -m pytest components/rsis3/tests/test_self_assess.py -q`
Expected: PASS (13 passed)

- [ ] **Step 5: Commit**

```bash
git add components/rsis3/rsis/self_assess.py components/rsis3/tests/test_self_assess.py
git commit -m "rsis: self-assess P4 — assessment + reflection OKF writers"
```

---

## Task 6: P5 backlog filing + guidance mirror

**Files:**
- Modify: `components/rsis3/rsis/self_assess.py` (append `file_backlog`, `mirror_to_guidance_queue`)
- Test: `components/rsis3/tests/test_self_assess.py`

- [ ] **Step 1: Write the failing tests**

Append:

```python
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
    buffer.write_text(json.dumps([{"title": "Existing"}]), encoding="utf-8")
    assert mirror_to_guidance_queue(tmp_path, GAPS) == 1
    assert mirror_to_guidance_queue(tmp_path, GAPS) == 0
    data = json.loads(buffer.read_text(encoding="utf-8"))
    assert len(data) == 2
    assert data[1]["kind"] == "direction"


def test_mirror_no_buffer_is_noop(tmp_path):
    assert mirror_to_guidance_queue(tmp_path, GAPS) == 0
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `python3 -m pytest components/rsis3/tests/test_self_assess.py -q`
Expected: FAIL with `ImportError` for `file_backlog`

- [ ] **Step 3: Implement**

Append to `components/rsis3/rsis/self_assess.py`:

```python
def file_backlog(root: Path, gaps: list[GapItem],
                 ts: Optional[str] = None) -> list[Path]:
    """P5 — create-only backlog notes; existing slugs are skipped."""
    ts = ts or _now_ts()
    written: list[Path] = []
    for gap in gaps:
        path = root / "backlog" / f"{gap.slug}.md"
        if path.exists():
            continue
        body = "\n".join([
            f"# {gap.topic}",
            "",
            f"- Priority: {gap.priority}",
            f"- Reason: {gap.reason}",
            f"- Source: self-assess",
        ])
        written.append(_write_note(path, {
            "type": "backlog",
            "title": gap.topic,
            "description": gap.reason,
            "tags": ["backlog", gap.priority],
            "timestamp": ts,
            "status": "open",
            "source": "gap",
            "priority": gap.priority,
            "assess_ref": f"assessments/self-assessment-{ts[:10]}.md",
        }, body))
    return written


def mirror_to_guidance_queue(root: Path, gaps: list[GapItem]) -> int:
    """P5 — mirror open gaps into the guidance-queue buffer (best-effort).

    The buffer is the handoff for drain_guidance.py; items use the
    ``direction`` kind with title/note. No buffer → no-op.
    """
    buffer = root / ".wiki-daemon" / "buffers" / "guidance-queue.json"
    if not buffer.is_file():
        return 0
    try:
        data = json.loads(buffer.read_text(encoding="utf-8"))
        if not isinstance(data, list):
            return 0
    except (json.JSONDecodeError, OSError):
        return 0
    existing = {item.get("title") for item in data}
    added = 0
    for gap in gaps:
        if gap.topic in existing:
            continue
        data.append({
            "title": gap.topic,
            "kind": "direction",
            "note": gap.reason,
            "area": "concepts",
        })
        added += 1
    if added:
        buffer.write_text(json.dumps(data, indent=1), encoding="utf-8")
    return added
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `python3 -m pytest components/rsis3/tests/test_self_assess.py -q`
Expected: PASS (16 passed)

- [ ] **Step 5: Commit**

```bash
git add components/rsis3/rsis/self_assess.py components/rsis3/tests/test_self_assess.py
git commit -m "rsis: self-assess P5 — backlog notes + guidance-queue mirror"
```

---

## Task 7: P6 LLM enrichment (hermetic)

**Files:**
- Modify: `components/rsis3/rsis/self_assess.py` (append `enrich_llm`)
- Test: `components/rsis3/tests/test_self_assess.py`

- [ ] **Step 1: Write the failing tests**

Append:

```python
from rsis.self_assess import enrich_llm


def test_enrich_llm_disabled_without_key(monkeypatch):
    monkeypatch.delenv("RSIS_EVALUATOR_API_KEY", raising=False)
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)
    assert enrich_llm(make_result()) is None
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python3 -m pytest components/rsis3/tests/test_self_assess.py -q`
Expected: FAIL with `ImportError` for `enrich_llm`

- [ ] **Step 3: Implement**

Append to `components/rsis3/rsis/self_assess.py`:

```python
def enrich_llm(result: AssessmentResult) -> Optional[str]:
    """P6 — optional fail-closed narrative; None when not configured."""
    key = os.environ.get("RSIS_EVALUATOR_API_KEY") or \
        os.environ.get("OPENAI_API_KEY")
    if not key:
        return None
    try:
        import openai
    except ImportError:
        return None
    payload = {
        "health_score": result.health_score,
        "gaps": [g.__dict__ for g in result.gaps],
        "trends": [t.__dict__ for t in result.trends],
    }
    try:
        client = openai.OpenAI(api_key=key)
        response = client.chat.completions.create(
            model=os.environ.get("RSIS_EVALUATOR_MODEL", "gpt-4o-mini"),
            temperature=0,
            messages=[{
                "role": "user",
                "content": (
                    "You are the RSIS self-assessment narrator. Given the "
                    "health score, gaps, and trends below, write 2-3 "
                    "sentences interpreting the trends and naming one "
                    "concrete research lead. Be specific.\n"
                    + json.dumps(payload)),
            }],
        )
        text = response.choices[0].message.content
        return text.strip() if isinstance(text, str) and text.strip() else None
    except Exception as e:
        logger.warning("LLM enrichment failed: %s", e)
        return None
```

- [ ] **Step 4: Run test to verify it passes**

Run: `python3 -m pytest components/rsis3/tests/test_self_assess.py -q`
Expected: PASS (17 passed)

- [ ] **Step 5: Commit**

```bash
git add components/rsis3/rsis/self_assess.py components/rsis3/tests/test_self_assess.py
git commit -m "rsis: self-assess P6 — fail-closed LLM enrichment"
```

---

## Task 8: `SelfAssessment` orchestrator

**Files:**
- Modify: `components/rsis3/rsis/self_assess.py` (append `_load_prev_score`, `SelfAssessment`)
- Test: `components/rsis3/tests/test_self_assess.py`

- [ ] **Step 1: Write the failing tests**

Append:

```python
from rsis.mykb_gateway import MyKBGateway
from rsis.self_assess import SelfAssessment


class RecordTelemetry:
    def __init__(self):
        self.events = []

    def record(self, event):
        self.events.append(event)


def make_mykb(tmp_path: Path) -> MyKBGateway:
    root = tmp_path / "mykb"
    (root / "wiki" / "syntheses").mkdir(parents=True)
    (root / "wiki" / "concepts").mkdir()
    (root / "log.md").write_text("---\ntype: log\ntitle: Bundle Log\n---\n\n# Bundle Log\n",
                                 encoding="utf-8")
    (root / "wiki" / "syntheses" / "s1.md").write_text(
        "---\ntype: synthesis\ntitle: Zebra Migration Routes\n"
        "description: seasonal savanna movement\ntags: [zebra]\n---\n\nbody\n",
        encoding="utf-8")
    (root / "wiki" / "concepts" / "deep.md").write_text(
        "word " * 350 + "\n", encoding="utf-8")
    (root / "stub-index.json").write_text(json.dumps({"total": 0}),
                                          encoding="utf-8")
    return MyKBGateway(mykb_root=str(root))


def test_orchestrator_writes_all_artifacts(tmp_path, monkeypatch):
    mykb = make_mykb(tmp_path)
    telemetry = RecordTelemetry()
    assessor = SelfAssessment(telemetry=telemetry, mykb=mykb,
                              workspace_dir=str(tmp_path),
                              llm=lambda result: None)
    monkeypatch.setattr("rsis.self_assess.scan_wiki_health",
                        lambda root, **kw: HealthReport(
                            total_pages=1, stubs=0, body_words=700))
    result = assessor.run(window_days=7)
    assert result.error is None
    assert result.assessment_path and result.reflection_path
    assert len(result.backlog_paths) == 1  # Zebra gap
    assert (mykb.root / "assessments").is_dir()
    assert (mykb.root / "reflections").is_dir()
    types = {e.type for e in telemetry.events}
    assert {"sa_start", "sa_complete"} <= types


def test_orchestrator_records_error(tmp_path, monkeypatch):
    mykb = make_mykb(tmp_path)
    telemetry = RecordTelemetry()

    def boom(**kw):
        raise RuntimeError("boom")

    monkeypatch.setattr("rsis.self_assess.scan_wiki_health", boom)
    assessor = SelfAssessment(telemetry=telemetry, mykb=mykb,
                              workspace_dir=str(tmp_path),
                              llm=lambda result: None)
    result = assessor.run(window_days=7)
    assert result.error == "boom"
    assert {e.type for e in telemetry.events} == {"sa_start", "sa_error"}
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `python3 -m pytest components/rsis3/tests/test_self_assess.py -q`
Expected: FAIL with `ImportError` for `SelfAssessment`

- [ ] **Step 3: Implement**

Append to `components/rsis3/rsis/self_assess.py`:

```python
def _load_prev_score(root: Path) -> Optional[float]:
    """Read the latest committed assessment's health_score, if any."""
    assessments = root / "assessments"
    if not assessments.is_dir():
        return None
    notes = sorted(assessments.glob("self-assessment-*.md"))
    if not notes:
        return None
    text = notes[-1].read_text(encoding="utf-8", errors="ignore")
    fm = _frontmatter(text)
    try:
        return float(fm.get("health_score", ""))
    except ValueError:
        return None


class SelfAssessment:
    """Runs the deterministic self-assessment phases (spec §3)."""

    def __init__(self, telemetry: Optional[TelemetryCollector] = None,
                 mykb: Optional[MyKBGateway] = None,
                 workspace_dir: Optional[str] = None,
                 llm: Optional[Callable[[AssessmentResult], Optional[str]]] = None):
        self.telemetry = telemetry
        self.mykb = mykb or MyKBGateway()
        self.workspace_dir = Path(workspace_dir or CONFIG.workspace_dir)
        self._llm = llm or enrich_llm

    def run(self, window_days: int = 7,
            file_backlog_items: bool = True) -> AssessmentResult:
        """Run all phases; never raises (errors land in result.error)."""
        self._record("sa_start", {"window_days": window_days})
        try:
            wiki = self.mykb.root / "wiki"
            health = scan_wiki_health(self.mykb.root)
            prev = _load_prev_score(self.mykb.root)
            gaps = analyze_gaps(self.mykb.read_syntheses(limit=20),
                                build_coverage_index(wiki))
            trends = detect_trends(
                self.workspace_dir / ".rsis" / "telemetry",
                window_days=window_days,
                git_log=self._git_log(window_days),
            )
            result = AssessmentResult(
                health=health, health_score=health.score(),
                gaps=gaps, trends=trends, window_days=window_days,
                prev_score=prev,
            )
            ts = _now_ts()
            result.assessment_path = str(
                write_assessment(self.mykb.root, result, ts))
            result.reflection_path = str(
                write_reflection(self.mykb.root, result, ts))
            if file_backlog_items:
                result.backlog_paths = [
                    str(p) for p in file_backlog(self.mykb.root, gaps, ts)]
                mirror_to_guidance_queue(self.mykb.root, gaps)
            narrative = self._llm(result)
            if narrative and result.assessment_path:
                with open(result.assessment_path, "a", encoding="utf-8") as fh:
                    fh.write(f"\n## LLM enrichment\n{narrative}\n")
            self._record("sa_complete", {
                "health_score": result.health_score,
                "gaps": len(result.gaps),
                "trends": len(result.trends),
                "assessment": result.assessment_path or "",
            })
            return result
        except Exception as e:
            logger.exception("self-assessment failed")
            self._record("sa_error", {"error": str(e)})
            return AssessmentResult(
                health=HealthReport(), health_score=0.0,
                gaps=[], trends=[], error=str(e))

    def _git_log(self, window_days: int) -> Callable[[], list[dict]]:
        def load() -> list[dict]:
            try:
                r = subprocess.run(
                    ["git", "-C", str(self.workspace_dir), "log",
                     f"--since={window_days} days ago",
                     "--pretty=format:%s"],
                    capture_output=True, text=True, timeout=30)
                return [{"subject": line}
                        for line in r.stdout.splitlines() if line.strip()]
            except (subprocess.SubprocessError, OSError):
                return []
        return load

    def _record(self, etype: str, metadata: dict) -> None:
        if self.telemetry is not None:
            self.telemetry.record(TelemetryEvent(
                event_type=etype, metadata=metadata))
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `python3 -m pytest components/rsis3/tests/test_self_assess.py -q`
Expected: PASS (19 passed)

- [ ] **Step 5: Commit**

```bash
git add components/rsis3/rsis/self_assess.py components/rsis3/tests/test_self_assess.py
git commit -m "rsis: self-assess orchestrator — phased run + telemetry"
```

---

## Task 9: CLI wiring

**Files:**
- Modify: `components/rsis3/rsis/main.py` (add import, `cmd_self_assess`, subparser)
- Test: `components/rsis3/tests/test_self_assess.py`

- [ ] **Step 1: Write the failing tests**

Append:

```python
import argparse
import subprocess
from unittest import mock

import rsis.main as main_mod
from rsis.self_assess import HealthReport


class FakeSystems:
    def start(self):
        pass

    def stop(self):
        pass


def test_cmd_self_assess_runs(tmp_path, monkeypatch, capsys):
    mykb = make_mykb(tmp_path)
    monkeypatch.setenv("RSIS_MYKB_PATH", str(mykb.root))
    monkeypatch.setattr(main_mod, "_init_subsystems",
                        lambda: (FakeSystems(), FakeSystems(), FakeSystems(),
                                 FakeSystems(), FakeSystems(), FakeSystems()))
    monkeypatch.setattr(main_mod.CONFIG, "workspace_dir", str(tmp_path))
    monkeypatch.setattr("rsis.self_assess.scan_wiki_health",
                        lambda root, **kw: HealthReport(
                            total_pages=1, stubs=0, body_words=700))
    code = main_mod.cmd_self_assess(argparse.Namespace(
        days=1, no_backlog=True, json=True))
    assert code == 0
    out = capsys.readouterr().out
    assert "Self-assessment complete" in out
    assert '"health_score"' in out


def test_self_assess_parser_registered():
    r = subprocess.run(
        [sys.executable, "-m", "rsis", "self-assess", "--help"],
        capture_output=True, text=True, cwd="components/rsis3")
    assert r.returncode == 0
    assert "--no-backlog" in r.stdout
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `python3 -m pytest components/rsis3/tests/test_self_assess.py -q`
Expected: FAIL — `AttributeError: module 'rsis.main' has no attribute 'cmd_self_assess'` (and parser help missing)

- [ ] **Step 3: Implement**

In `components/rsis3/rsis/main.py`:

Add to the imports (after the existing `from rsis.evaluator import EvaluatorClient` line):

```python
from rsis.self_assess import SelfAssessment
```

Add the command function (place it after `cmd_launch`, before `cmd_drive`):

```python
def cmd_self_assess(args: argparse.Namespace) -> int:
    telemetry, checkpoint, memory, evaluator, recovery, enforcer = _init_subsystems()
    enforcer.start()
    telemetry.start()
    try:
        assessor = SelfAssessment(telemetry=telemetry)
        result = assessor.run(window_days=args.days,
                              file_backlog_items=not args.no_backlog)
        if result.error:
            print(f"  \u2717 Self-assessment failed: {result.error}")
            return 1
        print(f"  \u2713 Self-assessment complete (health={result.health_score})")
        print(f"  Gaps: {len(result.gaps)} \u00b7 Trends: {len(result.trends)}")
        print(f"  Assessment: {result.assessment_path}")
        if result.reflection_path:
            print(f"  Reflection: {result.reflection_path}")
        for gap in result.gaps:
            print(f"    gap [{gap.priority}]: {gap.topic}")
        if args.json:
            print(json.dumps({
                "decision": "ok",
                "health_score": result.health_score,
                "gaps": [{"topic": g.topic, "priority": g.priority}
                         for g in result.gaps],
                "trends": [t.__dict__ for t in result.trends],
                "assessment": result.assessment_path,
            }))
        return 0
    finally:
        telemetry.stop()
        enforcer.stop()
```

Add the subparser (place after the `p_launch` block in `main()`):

```python
    p_self = sub.add_parser(
        "self-assess",
        help="Run the self-assessment routine (KB health, gaps, trends)")
    p_self.add_argument("--days", type=int,
                        default=CONFIG.self_assess.window_days,
                        help="Analysis window in days (default: %(default)s)")
    p_self.add_argument("--no-backlog", action="store_true",
                        help="Do not file backlog notes")
    p_self.add_argument("--json", action="store_true",
                        help="Print machine-readable summary")
    p_self.set_defaults(func=cmd_self_assess)
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `python3 -m pytest components/rsis3/tests/test_self_assess.py -q`
Expected: PASS (21 passed)

- [ ] **Step 5: Commit**

```bash
git add components/rsis3/rsis/main.py components/rsis3/tests/test_self_assess.py
git commit -m "rsis: self-assess CLI wiring (cmd_self_assess + subparser)"
```

---

## Task 10: batch hook, version, changelog, docs

**Files:**
- Modify: `infra/loops/run-batch.sh`
- Modify: `components/rsis3/rsis/__init__.py`
- Modify: `components/rsis3/CHANGELOG.md`
- Modify: `components/rsis3/docs/usage-practices.md`

- [ ] **Step 1: Make the edits**

1. `infra/loops/run-batch.sh` — after the cycle loops and before the `── Post-batch gates ──` echo, add a self-assessment step:

```bash
echo ""
echo "── Self-assessment ──────────────────────────────"
cd "$RSIS"
python3 -m rsis self-assess || FAIL=1
```

2. In the same file, the pre-snapshot `git add` must include the new wiki areas so `gen-static-data.py` (git-tracked only) picks them up. Change this line:

```bash
git add components/rsis3/.rsis components/rsis3/dashboard components/rsis3/rack \
        components/mykb/wiki/syntheses components/mykb/log.md components/mykb/log.json \
        components/mykb/guidance.json
```

to:

```bash
git add components/rsis3/.rsis components/rsis3/dashboard components/rsis3/rack \
        components/mykb/wiki/syntheses components/mykb/wiki/assessments \
        components/mykb/wiki/reflections components/mykb/wiki/backlog \
        components/mykb/log.md components/mykb/log.json \
        components/mykb/guidance.json
```

3. `components/rsis3/rsis/__init__.py`: change `__version__ = "0.4.3"` to `__version__ = "0.4.4"`.

4. `components/rsis3/CHANGELOG.md` — insert at the top (before `## [0.4.3]`):

```markdown
## [0.4.4] — 2026-08-07

### Added
- Self-assessment routine: `python -m rsis self-assess` — deterministic
  KB health scan (links, orphans, stubs, content depth with weighted
  score), gap analysis against recent syntheses (backlog items filed
  create-only in `wiki/backlog/`), trend detection from telemetry + git,
  and per-run `wiki/assessments/` + `wiki/reflections/` OKF notes
- Optional fail-closed LLM enrichment (`RSIS_EVALUATOR_API_KEY`) that can
  only add narrative, never alter deterministic findings
- `SelfAssessConfig` (window, artifact dirs, daemon timeout); `sa_start` /
  `sa_complete` / `sa_error` telemetry; `infra/loops/run-batch.sh` runs
  the routine after each scheduled batch

### Verified
- `tests/test_self_assess.py` — 21 cases; full rsis3 suite passes
- `gen-static-data.py --check` OK after first real run
```

5. `components/rsis3/docs/usage-practices.md` — in section 7 (Dashboard & Snapshot Practice), add a bullet:

```markdown
- `python -m rsis self-assess` runs the standing self-assessment (KB
  health, gaps, trends) and writes `wiki/assessments/`,
  `wiki/reflections/`, and `wiki/backlog/` notes; commit them and include
  the new areas when regenerating snapshots.
```

- [ ] **Step 2: Verify syntax and batch script**

Run: `bash -n infra/loops/run-batch.sh && python3 -m py_compile components/rsis3/rsis/main.py components/rsis3/rsis/self_assess.py`
Expected: exit 0, no output

- [ ] **Step 3: Run the full rsis3 suite**

Run: `cd components/rsis3 && python3 -m pytest tests/ -q`
Expected: `141 passed` (120 existing + 21 new)

- [ ] **Step 4: Commit**

```bash
git add infra/loops/run-batch.sh components/rsis3/rsis/__init__.py components/rsis3/CHANGELOG.md components/rsis3/docs/usage-practices.md
git commit -m "rsis: self-assess 0.4.4 — batch hook, changelog, docs"
```

---

## Task 11: first real run + MyKB consolidation + snapshots

**Files:**
- Run artifacts: `components/mykb/wiki/assessments/`, `wiki/reflections/`, `wiki/backlog/`
- Modify: `components/mykb/log.md`, `components/mykb/wiki/syntheses/` (new synthesis)
- Regenerate: `components/mykb/graph.json`, `catalog.json`, `index.json`, `log.json`, `components/rsis3/dashboard/*`

- [ ] **Step 1: Run the routine for real**

Run: `cd components/rsis3 && python3 -m rsis self-assess --json 2>&1 | tail -5`
Expected: prints `✓ Self-assessment complete (health=…)` plus JSON summary; writes one note in each of `components/mykb/wiki/assessments/`, `wiki/reflections/`, and (if gaps) `wiki/backlog/`.

Verify artifacts: `ls components/mykb/wiki/assessments/ components/mykb/wiki/reflections/` — each contains exactly one dated `.md` file.

- [ ] **Step 2: Verify practice checks still pass**

Run: `cd components/rsis3 && python3 -m rsis check-practices`
Expected: `OK — all usage practices satisfied`

- [ ] **Step 3: MyKB consolidation**

1. Append a dated entry to `components/mykb/log.md`:

```markdown
## 2026-08-07 (RSIS3 pass 14 — self-assessment routine)
- Added `python -m rsis self-assess`: deterministic KB health scan,
  gap analysis, telemetry+git trend detection, and per-run
  `wiki/assessments/` + `wiki/reflections/` notes with create-only
  `wiki/backlog/` filing; optional fail-closed LLM enrichment.
- First real run: health X.XXX, N gaps, M trends (fill from Step 1 output);
  version 0.4.4; tests 141 passed.
- Synthesis: `rsis3-pass-14-self-assessment-routine-2026-08-07.md`.
```

2. Write the OKF synthesis `components/mykb/wiki/syntheses/rsis3-pass-14-self-assessment-routine-2026-08-07.md` (frontmatter: `type`, `title`, `description`, `tags`, `timestamp`, `status`; body: Summary / Details / Rules with `[[wikilinks]]` to `[[wiki-self-improvement]]`, `[[guardrails]]`, and the pass-13 synthesis).

- [ ] **Step 4: Regenerate snapshots**

Run:

```bash
cd components/mykb && python3 .wiki-daemon/build_graph.py
cd /data/data/com.termux/files/home/dev/cosmos && python3 gen-static-data.py && python3 gen-static-data.py --check
```

Expected: `catalog: N entries` and final line `check: OK (…, 0 bad, 0 contract FAIL)`.

- [ ] **Step 5: Commit**

```bash
git add -A
git commit -m "rsis: pass 14 — self-assessment routine; mykb: consolidate (synthesis, log, snapshots)"
```

---

## Self-Review

- Spec coverage: P1→Task 2, P2→Task 3, P3→Task 4, P4→Task 5, P5→Task 6, P6→Task 7, orchestrator→Task 8, CLI→Task 9, wiring/version/docs→Task 10, first run + MyKB practice→Task 11. Health weights, artifact frontmatter, backlog dedupe, guidance mirror, telemetry events, and hermetic tests all map to spec sections §3–§12.
- Placeholder scan: no TBD/TODO; every step has complete code and exact commands. The only variable data is the real-run numbers in Task 11 Step 3, marked explicitly.
- Type consistency: `HealthReport.score()`, `GapItem.slug`, `AssessmentResult` fields, `SelfAssessment.run(window_days, file_backlog_items)`, `cmd_self_assess(args.days/no_backlog/json)`, `CONFIG.self_assess.*` are defined once and used consistently across tasks.
