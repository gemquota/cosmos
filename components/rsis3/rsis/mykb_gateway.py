"""MyKB gateway — durable memory link between RSIS3 loops and the MyKB wiki.

Stdlib-only bridge (COSMOS integration arc, pass 8: memory link). Loops use
it to *read* OKF syntheses for context and L3 consolidation uses it to
*write* synthesis notes + `log.md` entries directly, instead of by hand.

Root resolution order:
  1. explicit ``mykb_root`` argument
  2. ``RSIS_MYKB_PATH`` environment override
  3. sibling of the rsis3 workspace: ``<workspace>/../mykb``
"""

from __future__ import annotations

import logging
import os
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

from rsis.config import CONFIG

logger = logging.getLogger(__name__)

FM_RE = re.compile(r"^---\s*\n(.*?)\n---", re.S)
KEY_RE = re.compile(r"^(\w+):\s*(.*)$", re.M)
LIST_RE = re.compile(r"^\[(.*)\]$", re.S)
WIKILINK_RE = re.compile(r"\[\[([^\]|]+)(?:\|[^\]]+)?\]\]")

SYNTHESIS_DIR = "wiki/syntheses"
LOG_FILE = "log.md"


def _parse_frontmatter(text: str) -> dict:
    """Minimal OKF frontmatter parser (mirrors mykb/.wiki-daemon/frontmatter.py)."""
    fm = {}
    m = FM_RE.match(text or "")
    if not m:
        return fm
    for k, v in KEY_RE.findall(m.group(1)):
        v = v.strip().strip('"').strip("'")
        lm = LIST_RE.match(v)
        if lm:
            fm[k] = [x.strip().strip('"').strip("'")
                     for x in lm.group(1).split(",") if x.strip()]
        else:
            fm[k] = v
    return fm


def _slugify(title: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")
    return slug or "synthesis"


def _token_overlap(text: str, query: str) -> int:
    """Cheap relevance score: shared lowercased word tokens."""
    words = set(re.findall(r"[a-z0-9]+", (text or "").lower()))
    q = set(re.findall(r"[a-z0-9]+", (query or "").lower()))
    if not q:
        return 0
    return len(words & q)


class MyKBGateway:
    """Read/write access to the MyKB wiki from RSIS3 loops."""

    def __init__(self, mykb_root: Optional[str] = None):
        env = os.environ.get("RSIS_MYKB_PATH")
        if mykb_root:
            self.root = Path(mykb_root).resolve()
        elif env:
            self.root = Path(env).resolve()
        else:
            self.root = Path(CONFIG.workspace_dir).resolve().parent / "mykb"
        self.syntheses_dir = self.root / SYNTHESIS_DIR
        self.log_path = self.root / LOG_FILE

    # ── Availability ─────────────────────────────────────────────────

    @property
    def available(self) -> bool:
        return self.syntheses_dir.is_dir() and self.log_path.is_file()

    def status(self) -> dict:
        """Diagnostics for logs: root, availability, synthesis count."""
        count = 0
        if self.syntheses_dir.is_dir():
            count = len([p for p in self.syntheses_dir.glob("*.md")
                         if p.name != "00-index.md"])
        return {
            "root": str(self.root),
            "available": self.available,
            "syntheses": count,
        }

    # ── Reading (context for loops) ─────────────────────────────────

    def read_syntheses(self, limit: int = 10) -> list[dict]:
        """Return the most recent OKF syntheses, newest first."""
        if not self.syntheses_dir.is_dir():
            return []
        entries = []
        for p in sorted(self.syntheses_dir.glob("*.md")):
            if p.name == "00-index.md":
                continue
            text = p.read_text(encoding="utf-8", errors="ignore")
            fm = _parse_frontmatter(text)
            entries.append({
                "path": str(p),
                "rel": f"{SYNTHESIS_DIR}/{p.name}",
                "slug": p.stem,
                "title": fm.get("title", p.stem),
                "description": fm.get("description", ""),
                "tags": fm.get("tags", []) or [],
                "timestamp": fm.get("timestamp", ""),
                "status": fm.get("status", ""),
            })
        entries.sort(key=lambda e: e["timestamp"], reverse=True)
        return entries[:limit]

    def search_syntheses(self, query: str, limit: int = 5) -> list[dict]:
        """Rank syntheses by token overlap with the query (stdlib-only)."""
        hits = []
        for e in self.read_syntheses(limit=200):
            haystack = " ".join([
                e["title"], e["description"], " ".join(e["tags"]),
            ])
            score = _token_overlap(haystack, query)
            if score > 0:
                e["score"] = score
                hits.append(e)
        hits.sort(key=lambda e: e["score"], reverse=True)
        return hits[:limit]

    # ── Writing (L3 consolidation) ───────────────────────────────────

    def write_synthesis(
        self,
        title: str,
        description: str = "",
        tags: Optional[list[str]] = None,
        body: str = "",
        status: str = "growing",
        timestamp: Optional[str] = None,
    ) -> Path:
        """Write one OKF synthesis note; returns the written path.

        Filename is `<slug>-YYYY-MM-DD.md` (UTC date); an existing file for
        the same slug/date gets a numeric suffix so every cycle is durable.
        """
        if not self.available:
            raise FileNotFoundError(
                f"MyKB not available at {self.root} (need wiki/syntheses + log.md)")
        ts = timestamp or datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        date = ts[:10]
        base = _slugify(title)
        path = self.syntheses_dir / f"{base}-{date}.md"
        n = 2
        while path.exists():
            path = self.syntheses_dir / f"{base}-{date}-{n}.md"
            n += 1

        tag_list = tags or []
        fm = "\n".join([
            "---",
            'type: "synthesis"',
            f'title: "{title}"',
            f'description: "{description}"',
            'tags: [' + ', '.join('"' + t + '"' for t in tag_list) + ']',
            f'timestamp: "{ts}"',
            f'status: "{status}"',
            "---",
        ])
        content = fm + "\n\n" + (body.strip() or "") + "\n"
        self.syntheses_dir.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
        logger.info("MyKB synthesis written: %s", path)
        return path

    def append_log(self, title: str, bullets: list[str]) -> Path:
        """Prepend a dated entry block to log.md (newest first)."""
        if not self.log_path.is_file():
            raise FileNotFoundError(f"MyKB log not found: {self.log_path}")
        date = datetime.now(timezone.utc).strftime("%Y-%m-%d")
        block = "\n".join([f"## {date} ({title})"]
                          + [f"- {b}" for b in bullets])
        text = self.log_path.read_text(encoding="utf-8", errors="ignore")
        marker = "# Bundle Log"
        if marker in text:
            idx = text.index(marker) + len(marker)
            text = text[:idx] + "\n\n" + block + "\n\n" + text[idx:].lstrip("\n")
        else:
            text = text.rstrip() + "\n\n" + block + "\n"
        self.log_path.write_text(text, encoding="utf-8")
        logger.info("MyKB log entry appended: %s", self.log_path)
        return self.log_path
