"""SPACE spec gateway — spec artifacts feed L2 ideation (pass 9: spec link).

Maps the exported SPACE specification (326-probe framework output) to
candidate L2 goals. Every goal string embeds the artifact id and its source
question, so telemetry traces (`l2_start` metadata `goal`) reference a SPACE
spec artifact — the pass-9 verification chain.

Spec path resolution order:
  1. explicit ``spec_path`` argument
  2. ``RSIS_SPACE_SPEC`` environment override
  3. default cosmos export:
     ``<workspace>/../../components/space/exports/recursive-self-improvement-specification.json``
"""

from __future__ import annotations

import json
import logging
import os
import re
from pathlib import Path
from typing import Optional

from rsis.config import CONFIG

logger = logging.getLogger(__name__)

DEFAULT_EXPORT = (
    "components/space/exports/recursive-self-improvement-specification.json"
)


def _token_overlap(text: str, query: str) -> int:
    words = set(re.findall(r"[a-z0-9]+", (text or "").lower()))
    q = set(re.findall(r"[a-z0-9]+", (query or "").lower()))
    if not q:
        return 0
    return len(words & q)


class SpaceSpec:
    """Loads a SPACE spec export and derives candidate L2 goals."""

    def __init__(self, spec_path: Optional[str] = None):
        env = os.environ.get("RSIS_SPACE_SPEC")
        if spec_path:
            self.path = Path(spec_path).resolve()
        elif env:
            self.path = Path(env).resolve()
        else:
            ws = Path(CONFIG.workspace_dir).resolve()
            self.path = ws.parent.parent / DEFAULT_EXPORT
        self._data: dict = {}
        if self.path.is_file():
            try:
                self._data = json.loads(self.path.read_text(encoding="utf-8"))
            except (OSError, json.JSONDecodeError) as e:
                logger.warning("Failed to load SPACE spec %s: %s", self.path, e)
                self._data = {}

    @property
    def available(self) -> bool:
        return bool(self._data)

    def status(self) -> dict:
        arts = self.artifacts()
        return {
            "path": str(self.path),
            "available": self.available,
            "artifacts": len(arts),
            "project": (self._data.get("meta") or {}).get("project_name", ""),
            "completion_pct": (self._data.get("meta") or {}).get(
                "completion_pct", 0),
        }

    def artifacts(self) -> list[dict]:
        """Flatten spec artifacts: {id, value, series_id, question_id, confidence}."""
        out = []
        for aid, a in (self._data.get("artifacts") or {}).items():
            if not isinstance(a, dict):
                continue
            value = (a.get("value") or "").strip()
            if not value:
                continue
            out.append({
                "id": aid,
                "value": value,
                "question_id": a.get("source_question_id", ""),
                "series_id": a.get("source_series_id", 0),
                "confidence": a.get("confidence", 0),
            })
        out.sort(key=lambda a: (-(a["confidence"] or 0), a["id"]))
        return out

    def answer_text(self, question_id: str) -> str:
        """Raw open-ended answer text for a question id (context seed)."""
        a = (self._data.get("answers") or {}).get(question_id) or {}
        return (a.get("open_ended_text") or a.get("multi_choice_text") or "").strip()

    def candidate_goals(self, limit: int = 8) -> list[str]:
        """Ranked L2 goal strings, each referencing a spec artifact."""
        goals = []
        for a in self.artifacts():
            value = a["value"]
            if len(value) > 300:
                value = value[:297] + "..."
            goals.append(
                f"Implement the {a['id']} spec artifact: {value} "
                f"(SPACE spec artifact {a['id']}, series {a['series_id']}, "
                f"question {a['question_id']})"
            )
            if len(goals) >= limit:
                break
        return goals

    def search(self, query: str, limit: int = 5) -> list[dict]:
        """Rank artifacts by token overlap with the query."""
        hits = []
        for a in self.artifacts():
            haystack = " ".join([
                a["id"], a["value"],
                self.answer_text(a["question_id"]),
            ])
            score = _token_overlap(haystack, query)
            if score > 0:
                a["score"] = score
                hits.append(dict(a))
        hits.sort(key=lambda a: a["score"], reverse=True)
        return hits[:limit]
