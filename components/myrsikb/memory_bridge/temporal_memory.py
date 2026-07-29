#!/usr/bin/env python3
"""TemporalMemory — timeline queries and trend detection.

Wraps mykb's ``temporal.py`` so RSIS3 can ask questions like:

- "What topics have I been focused on this month?"
- "Which entities are rising / falling in attention?"
- "Show me the timeline for a specific concept."
"""

from pathlib import Path
from typing import Optional
from datetime import datetime
from memory_bridge.mykb_loader import load_mykb_module


#  ── TemporalMemory ────────────────────────────────────────────

class TemporalMemory:
    """RSIS3's temporal / episodic memory — what happened when.

    Delegates to mykb's co-occurrence timeline built from session
    files and daily notes.
    """

    def __init__(self, mykb_wiki: Optional[str | Path] = None):
        wiki_path = Path(mykb_wiki) if mykb_wiki else self._default_wiki()
        self._wiki_path = wiki_path
        self._tm = None  # lazy import

    @property
    def tm(self):
        if self._tm is None:
            self._tm = load_mykb_module("temporal")
        return self._tm

    # ── entity timelines ─────────────────────────────────────

    def entity_timeline(self, entity_slug: str) -> list[dict]:
        """Get all dated mentions for an entity.

        Returns list of ``{date, session, session_tags}`` dicts sorted
        chronologically.
        """
        tl, _ = self.tm.extract_timeline()
        return tl.get(entity_slug, [])

    def all_timelines(self) -> dict:
        """Return the full entity→timeline map."""
        tl, _ = self.tm.extract_timeline()
        return tl

    # ── frequency ────────────────────────────────────────────

    def entity_frequency(self, entity_slug: str) -> dict:
        """Monthly frequency, first/last seen for an entity."""
        tl, _ = self.tm.extract_timeline()
        freqs = self.tm.compute_frequencies(tl)
        return freqs.get(entity_slug, {})

    def monthly_activity(self, year_month: Optional[str] = None) -> dict:
        """Entities active in a given month (defaults to current)."""
        if year_month is None:
            year_month = datetime.utcnow().strftime('%Y-%m')
        tl, _ = self.tm.extract_timeline()
        active = {}
        for eid, entries in tl.items():
            count = sum(
                1 for e in entries if e['date'].startswith(year_month)
            )
            if count:
                active[eid] = count
        return dict(sorted(active.items(), key=lambda x: -x[1]))

    # ── trends ───────────────────────────────────────────────

    def rising_entities(self, top_n: int = 10) -> list[dict]:
        """Entities with fastest-growing mention frequency."""
        tl, _ = self.tm.extract_timeline()
        freqs = self.tm.compute_frequencies(tl)
        trends = self.tm.detect_trends(freqs)
        return trends.get('rising', [])[:top_n]

    def falling_entities(self, top_n: int = 10) -> list[dict]:
        """Entities with declining mention frequency."""
        tl, _ = self.tm.extract_timeline()
        freqs = self.tm.compute_frequencies(tl)
        trends = self.tm.detect_trends(freqs)
        return trends.get('falling', [])[:top_n]

    def trend_summary(self) -> dict:
        """Full trend report (rising, falling, stable counts)."""
        tl, _ = self.tm.extract_timeline()
        freqs = self.tm.compute_frequencies(tl)
        return self.tm.detect_trends(freqs)

    # ── recent activity ──────────────────────────────────────

    def recent_sessions(self, days: int = 7) -> list[str]:
        """Session slugs active in the last N days."""
        from datetime import timedelta
        cutoff = (datetime.utcnow() - timedelta(days=days)).strftime('%Y-%m-%d')
        tl, sessions = self.tm.extract_timeline()
        recent = []
        for sid, info in sessions.items():
            if info.get('date', '') >= cutoff:
                recent.append(sid)
        return sorted(recent)

    @staticmethod
    def _default_wiki() -> Path:
        return resolve_wiki_path()
