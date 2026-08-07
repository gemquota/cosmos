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
MIN_SIGNIFICANT_TOKEN_LEN = 4  # shared by coverage index and gap analysis
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
    links_scanned: bool = True
    notes: list[str] = field(default_factory=list)

    def score(self) -> float:
        """Weighted 0.0–1.0 health score (link .25 / orphan .15 / stub .30 / depth .30).

        When the linter did not run (``links_scanned`` False), the link and
        orphan components are unknown and are excluded with renormalization
        instead of being counted as perfect.
        """
        def ratio(good: int, total: int) -> float:
            return 1.0 if total == 0 else max(0.0, good / total)

        components = []
        if self.links_scanned:
            components.append(
                (0.25, ratio(self.total_links - self.broken_links,
                             self.total_links)))
            components.append(
                (0.15, ratio(self.total_pages - self.orphans,
                             self.total_pages)))
        components.append(
            (0.30, ratio(self.total_pages - self.stubs, self.total_pages)))
        depth = 1.0 if self.total_pages == 0 else min(
            1.0, (self.body_words / max(1, self.total_pages)) / STUB_FLOOR)
        components.append((0.30, depth))
        total_weight = sum(w for w, _ in components)
        if total_weight == 0:
            return 1.0
        return round(sum(w * v for w, v in components) / total_weight, 3)


def _frontmatter(text: str) -> dict:
    fm: dict = {}
    m = FM_RE.match(text or "")
    if not m:
        return fm
    for k, v in KEY_RE.findall(m.group(1)):
        fm[k] = v.strip().strip('"').strip("'")
    return fm


def _body_words(text: str) -> int:
    body = FM_RE.sub("", text or "", count=1)
    body = re.sub(r"```.*?```", " ", body, flags=re.S)
    return len(TOKEN_RE.findall(body.lower()))


def _safe_int(value, default: int = 0) -> int:
    """Coerce JSON numbers/strings to int; default on garbage."""
    try:
        return int(value)
    except (TypeError, ValueError):
        return default


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
            parsed = json.loads(stub_index.read_text(encoding="utf-8"))
            if not isinstance(parsed, dict):
                raise ValueError("stub-index.json is not an object")
            report.stubs = _safe_int(parsed.get("total"))
        except (json.JSONDecodeError, OSError, ValueError, AttributeError):
            report.notes.append("stub-index.json unreadable")

    cmd = linter_cmd or [sys.executable,
                         str(mykb_root / ".wiki-daemon" / "kb_linter.py"),
                         "--json"]
    data = _run_json(cmd, timeout_s)
    if isinstance(data, dict) and isinstance(data.get("summary"), dict):
        summary = data["summary"]
        report.broken_links = _safe_int(summary.get("broken_links"))
        report.orphans = _safe_int(summary.get("orphan_notes"))
    else:
        report.links_scanned = False
        report.notes.append("kb_linter unavailable — link/orphan metrics "
                            "not scanned")
    return report


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
        hidden = any(seg.startswith(".")
                     for seg in rel.relative_to(wiki_root).parts)
        if hidden:
            continue
        text = rel.read_text(encoding="utf-8", errors="ignore")
        body = FM_RE.sub("", text, count=1)
        page_id = str(rel.relative_to(wiki_root))
        for tok in set(TOKEN_RE.findall(body.lower())):
            if (tok not in STOPWORDS
                    and len(tok) >= MIN_SIGNIFICANT_TOKEN_LEN):
                index.setdefault(tok, set()).add(page_id)
    return index


def analyze_gaps(syntheses: list[dict], index: dict[str, set[str]],
                 max_gaps: int = 10) -> list[GapItem]:
    """P2 — topics under-covered by the wiki (spec §6.2a).

    A synthesis topic is covered when at least two of its significant
    tokens co-occur in some wiki page; otherwise it becomes a gap.
    """
    if max_gaps <= 0:
        return []
    gaps: list[GapItem] = []
    for syn in syntheses:
        text = f"{syn.get('title', '')} {syn.get('description', '')}".lower()
        tokens = sorted({t for t in TOKEN_RE.findall(text)
                         if t not in STOPWORDS
                         and len(t) >= MIN_SIGNIFICANT_TOKEN_LEN})
        if len(tokens) < 2:
            continue
        pairs = [(t1, t2)
                 for i, t1 in enumerate(tokens) for t2 in tokens[i + 1:]]
        covered = any(bool(index.get(t1, set()) & index.get(t2, set()))
                      for t1, t2 in pairs)
        if covered:
            continue
        missing = [t for t in tokens if not index.get(t)]
        if missing:
            detail = f"missing keywords: {', '.join(missing[:3])}"
        else:
            detail = "no page contains two keywords together"
        gaps.append(GapItem(
            topic=syn.get("title", "untitled synthesis"),
            priority="high",
            reason=f"under-covered topic; {detail}",
        ))
        if len(gaps) >= max_gaps:
            break
    return gaps


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
        text = f.read_text(encoding="utf-8", errors="ignore")
        for line in text.splitlines():
            try:
                ev = json.loads(line)
            except json.JSONDecodeError:
                continue
            if not isinstance(ev, dict):
                continue
            try:
                ts = _as_utc(datetime.fromisoformat(ev.get("timestamp", "")))
            except (TypeError, ValueError):
                continue
            if ts < cutoff:
                continue
            etype = ev.get("type", "")
            if not isinstance(etype, str):
                continue
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
    def scalar(value) -> str:
        s = str(value).replace("\\", "\\\\").replace('"', '\\"')
        return f'"{s.replace(chr(10), " ")}"'

    lines = ["---"]
    for k, v in fm.items():
        if isinstance(v, (list, tuple)):
            lines.append(f"{k}: [{', '.join(scalar(x) for x in v)}]")
        else:
            lines.append(f"{k}: {scalar(v)}")
    lines.append("---")
    final.write_text("\n".join(lines) + "\n\n" + body.strip() + "\n",
                     encoding="utf-8")
    return final


def _date_part(ts: str) -> str:
    """Safe YYYY-MM-DD from an OKF timestamp; today on malformed input."""
    m = re.match(r"^(\d{4}-\d{2}-\d{2})", ts or "")
    if m:
        return m.group(1)
    return datetime.now(timezone.utc).strftime("%Y-%m-%d")


def write_assessment(root: Path, result: AssessmentResult,
                     ts: Optional[str] = None) -> Path:
    """P4 — assessment note (spec §6.1)."""
    ts = ts or _now_ts()
    date = _date_part(ts)
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
                        f"{len(result.gaps)} gaps, "
                        f"{len(result.trends)} trends"),
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
    date = _date_part(ts)
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


def file_backlog(root: Path, gaps: list[GapItem],
                 ts: Optional[str] = None) -> list[Path]:
    """P5 — create-only backlog notes; existing slugs are skipped.

    ``root`` is the wiki dir (the one containing ``backlog/``).
    """
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
            "- Source: self-assess",
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
            "assess_ref": f"assessments/self-assessment-{_date_part(ts)}.md",
        }, body))
    return written


def mirror_to_guidance_queue(root: Path, gaps: list[GapItem]) -> int:
    """P5 — mirror open gaps into the guidance-queue buffer (best-effort).

    The buffer is the handoff for drain_guidance.py, which expects the
    daemon shape ``{"items": [...]}``; items use the ``direction`` kind
    with title/note. ``root`` is the mykb dir (the one containing
    ``.wiki-daemon/``). No buffer → no-op.
    """
    buffer = root / ".wiki-daemon" / "buffers" / "guidance-queue.json"
    if not buffer.is_file():
        return 0
    try:
        data = json.loads(buffer.read_text(encoding="utf-8"))
        if not (isinstance(data, dict)
                and isinstance(data.get("items"), list)
                and all(isinstance(item, dict)
                        for item in data["items"])):
            return 0
        items = data["items"]
        existing = {item.get("title") for item in items}
        added = 0
        for gap in gaps:
            if gap.topic in existing:
                continue
            items.append({
                "title": gap.topic,
                "kind": "direction",
                "note": gap.reason,
                "area": "concepts",
                "added": _now_ts(),
            })
            added += 1
        if added:
            buffer.write_text(json.dumps(data, indent=1),
                              encoding="utf-8")
        return added
    except (json.JSONDecodeError, OSError):
        return 0
