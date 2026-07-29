#!/usr/bin/env python3
"""GapDetector — knowledge gap analysis for RSIS3's L3 self-direction.

Wraps mykb's ``gap_detector.py`` so the goal generator can ask:

- "What knowledge am I missing?"
- "Which entities have low coverage?"
- "What acronyms haven't I defined?"
- "Where should I focus my learning?"

These gaps become high-priority goals in RSIS3's L3 loop.
"""

from pathlib import Path
from typing import Optional
from memory_bridge.mykb_loader import load_mykb_module


#  ── GapDetector ───────────────────────────────────────────────

class GapDetector:
    """Analyses mykb's wiki for knowledge gaps that RSIS3 can prioritise.

    Usage::

        gd = GapDetector()
        gaps = gd.analyze()
        for g in gaps['low_coverage']:
            print(g['title'], g['session_count'], g['body_len'])
    """

    def __init__(self, mykb_wiki: Optional[str | Path] = None):
        wiki_path = Path(mykb_wiki) if mykb_wiki else self._default_wiki()
        self._wiki_path = wiki_path
        self._gd = None

    @property
    def gd(self):
        if self._gd is None:
            self._gd = load_mykb_module("gap_detector")
        return self._gd

    def analyze(self) -> dict:
        """Run full gap analysis.

        Returns dict with keys:
            low_coverage — entities with 3+ sessions but tiny body
            stubs        — auto-extracted entities with minimal body
            acronyms     — uppercase entities without definitions
            missing_tags — entities with few/no tags
        """
        entities = self.gd.scan_entities()
        sessions = self.gd.scan_sessions()
        return self.gd.detect_gaps(entities)

    def low_coverage(self, min_sessions: int = 3) -> list[dict]:
        """Entities mentioned often but poorly documented."""
        gaps = self.analyze()
        return [e for e in gaps['low_coverage']
                if e.get('session_count', 0) >= min_sessions]

    def stubs(self) -> list[dict]:
        """Auto-extracted entities that are bare stubs."""
        gaps = self.analyze()
        return gaps['stubs']

    def undefined_acronyms(self) -> list[dict]:
        """Acronym-like entities with no body definition."""
        gaps = self.analyze()
        return gaps['acronyms']

    def missing_tags(self) -> list[dict]:
        """Entities with too few tags."""
        gaps = self.analyze()
        return gaps['missing_tags']

    def generate_questions(self) -> list[dict]:
        """Generate concrete questions for each gap.

        Returns list of ``{entity, question, priority, reason}`` dicts.
        These can be fed directly to RSIS3's GoalGenerator.
        """
        entities = self.gd.scan_entities()
        sessions = self.gd.scan_sessions()
        gaps = self.gd.detect_gaps(entities)
        return self.gd.generate_questions(gaps)

    def gap_report_path(self) -> Path:
        """Path to the generated gap report markdown file."""
        return self._wiki_path / 'ops' / 'gap-report.md'

    def cluster_sessions(self, min_cluster_size: int = 5) -> dict:
        """Cluster sessions by tag overlap to find topical groups."""
        sessions = self.gd.scan_sessions()
        return self.gd.detect_session_clusters(sessions, min_cluster_size=min_cluster_size)

    # ── convert gaps → goals for RSIS3 ───────────────────────

    def to_goals(self, max_goals: int = 10) -> list[dict]:
        """Turn knowledge gaps into structured goal dicts.

        Each goal has ``{id, description, priority, source_signal,
        value_alignment, suggested_tasks}`` — compatible with
        RSIS3's ``GoalGenerator``.
        """
        import uuid
        goals = []

        for gap in self.low_coverage()[:max_goals]:
            goals.append({
                'id': f'gap-{uuid.uuid4().hex[:8]}',
                'description': f"Document {gap['title']} — referenced in {gap['session_count']} sessions but only {gap['body_len']}b",
                'priority': round(min(0.5 + gap['session_count'] * 0.05, 0.95), 2),
                'source_signal': f'gap/low_coverage/{gap["slug"]}',
                'value_alignment': ['knowledge', 'coherence', 'documentation'],
                'suggested_tasks': [
                    f"Research {gap['title']}",
                    f"Write wiki page for {gap['slug']}",
                    f"Cross-link from related sessions",
                ],
            })

        for acro in self.undefined_acronyms()[:max_goals]:
            goals.append({
                'id': f'gap-{uuid.uuid4().hex[:8]}',
                'description': f"Define acronym '{acro['title']}' — used in {acro['session_count']} sessions without definition",
                'priority': 0.6,
                'source_signal': f'gap/acronym/{acro["slug"]}',
                'value_alignment': ['clarity', 'coherence', 'learning'],
                'suggested_tasks': [
                    f"Find what {acro['title']} stands for",
                    f"Write definition for {acro['slug']}",
                    f"Update existing references",
                ],
            })

        return goals

    @staticmethod
    def _default_wiki() -> Path:
        return resolve_wiki_path()
