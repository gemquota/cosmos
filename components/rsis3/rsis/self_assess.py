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
