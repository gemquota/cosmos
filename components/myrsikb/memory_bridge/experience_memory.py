#!/usr/bin/env python3
"""ExperienceMemory — Episodic encoding of RSIS3 pulses as retrievable memories.

Every pulse cycle produces a pulse memory containing:

  - goal          : what was attempted
  - context       : system state, layer scores, active goals
  - reasoning     : evaluation phase outputs
  - actions       : patches applied, decisions made
  - outcome       : PASS / DISMISS / HOLD, confidence, test results
  - lessons       : extracted insights

Pulse memories are stored as wiki pages (``wiki/pulses/``) and indexed in the
vector database so future planning can retrieve similar past pulses.
"""

import re
import json
import time
import uuid
from datetime import datetime
from pathlib import Path
from typing import Optional

from memory_bridge.config import resolve_wiki_path


# ── Helpers (mirror wiki_writer helpers for self-containment) ──

def _frontmatter(**fields) -> str:
    lines = ["---"]
    for k, v in fields.items():
        if k == "tags" and isinstance(v, (list, tuple)):
            quoted = ", ".join(f'"{t}"' for t in v)
            lines.append(f"tags: [{quoted}]")
        elif isinstance(v, str):
            lines.append(f'{k}: "{v.replace(chr(34), chr(39))}"')
        elif isinstance(v, bool):
            lines.append(f"{k}: {'true' if v else 'false'}")
        elif isinstance(v, (int, float)):
            lines.append(f"{k}: {v}")
        else:
            lines.append(f"{k}: {json.dumps(v)}")
    lines.append("---")
    return "\n".join(lines)


def _iso_now() -> str:
    return datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")


#  ── ExperienceMemory ────────────────────────────────────────

class ExperienceMemory:
    """Episodic autobiographical memory for RSIS3.

    Every pulse cycle is encoded as a **pulse memory** — a structured wiki
    page with frontmatter, body, and vector index entry.  Past pulse memories
    can be retrieved by semantic similarity to inform future planning.

    Usage::

        from memory_bridge import ExperienceMemory

        mem = ExperienceMemory()
        pulse_id = mem.store_pulse({
            "pulse_id": 42,
            "goal": "Improve L3 goal generation",
            "context": {"layer_scores": {"L3": 45}, "crisis_active": False},
            "reasoning": "...agent evaluation text...",
            "actions": [{"type": "patch", "description": "Modified goal_generator.py"}],
            "outcome": {"decision": "PASS", "confidence": 0.85,
                        "test_summary": "45 passed, 0 failed"},
            "lessons": ["Goal priority calibration needs tuning"],
        })
        similar = mem.retrieve_similar_pulses("goal generation improvement")
        recent = mem.recent_pulses(limit=5)
    """

    def __init__(self, wiki_root: Optional[str | Path] = None):
        self._wiki = Path(wiki_root) if wiki_root else resolve_wiki_path()
        self._pulse_dir = self._wiki / "pulses"
        self._pulse_dir.mkdir(parents=True, exist_ok=True)

    # ── store ────────────────────────────────────────────────

    def store_pulse(self, pulse_data: dict) -> str:
        """Store a pulse cycle as a retrievable memory record.

        ``pulse_data`` keys (all optional except ``goal``):

          pulse_id   — integer pulse number
          goal       — what the cycle attempted (str)
          context    — system state dict (layer_scores, crisis_active, etc.)
          reasoning  — evaluation phase text
          actions    — list of ``{type, description, result}`` dicts
          outcome    — ``{decision, confidence, test_summary}``
          lessons    — list of strings
          timestamp  — ISO-8601 string (defaults to now)

        Returns the pulse id (``pulse-{id}``).
        """
        pulse_id = pulse_data.get("pulse_id", int(time.time()))
        pulse_id_str = f"pulse-{pulse_id}"
        timestamp = pulse_data.get("timestamp", _iso_now())
        date_key = timestamp[:10] if "T" in timestamp else datetime.utcnow().strftime("%Y-%m-%d")

        goal = pulse_data.get("goal", "Unknown goal")
        outcome = pulse_data.get("outcome", {})
        decision = outcome.get("decision", "UNKNOWN")
        confidence = outcome.get("confidence", 0.0)
        context = pulse_data.get("context", {})
        reasoning = pulse_data.get("reasoning", "")
        actions = pulse_data.get("actions", [])
        lessons = pulse_data.get("lessons", [])

        # ── body ───────────────────────────────────────────
        parts = [f"# Pulse Memory: {goal[:120]}\n"]
        parts.append(f"**Decision:** {decision} (confidence: {confidence})\n")
        parts.append(f"**Timestamp:** {timestamp}\n")

        # Context
        parts.append("\n## Context\n")
        ls = context.get("layer_scores", {})
        parts.append(f"- Layer scores: {ls}")
        parts.append(f"- Active goals: {context.get('active_goals', 0)}")
        parts.append(f"- Cycle count: {context.get('cycle_count', 0)}")
        parts.append(f"- Crisis active: {context.get('crisis_active', False)}")
        narrative = context.get("narrative", "")
        if narrative:
            parts.append(f"- Narrative: {narrative[:200]}")

        # Reasoning trace
        if reasoning:
            parts.append("\n## Reasoning\n")
            parts.append(reasoning[:3000])

        # Actions
        if actions:
            parts.append("\n## Actions\n")
            for i, a in enumerate(actions):
                atype = a.get("type", "action")
                desc = a.get("description", "")
                result = a.get("result", "")
                parts.append(f"{i+1}. **{atype}**: {desc}")
                if result:
                    parts.append(f"   → {result}")

        # Outcome detail
        test_summary = outcome.get("test_summary", "")
        if test_summary:
            parts.append(f"\n## Test Results\n{test_summary}\n")

        # Lessons
        if lessons:
            parts.append("\n## Lessons\n")
            for lesson in lessons:
                parts.append(f"- {lesson}")

        # Frontmatter
        tags = [
            "pulse",
            f"decision-{decision.lower()}",
            f"pulse-{date_key}",
        ]

        front = {
            "type": "pulse",
            "title": f"Pulse {pulse_id}: {goal[:80]}",
            "description": f"{decision} ({confidence}) — {goal[:150]}",
            "tags": tags,
            "timestamp": timestamp,
        }

        path = self._pulse_dir / f"{pulse_id_str}.md"
        content = _frontmatter(**front) + "\n\n" + "\n".join(parts) + "\n"
        path.write_text(content, encoding="utf-8")

        # ── index in vector DB ─────────────────────────────
        self._index_pulse(pulse_id_str, goal, outcome, parts)

        return pulse_id_str

    # ── retrieval ──────────────────────────────────────────

    def retrieve_similar_pulses(self, query: str, top_k: int = 5) -> list[dict]:
        """Find pulses semantically similar to ``query``.

        Returns up to ``top_k`` results sorted by relevance score.
        Each result has ``{id, score, title, snippet}``.
        """
        try:
            from memory_bridge.vector_search import SemanticMemory
            sm = SemanticMemory(self._wiki)
            return sm.search(f"pulse: {query}", top_k=top_k, filters={"type": "pulse"})
        except Exception as exc:
            return [{"error": str(exc)}]

    def retrieve_pulses_by_outcome(self, decision: str, limit: int = 10) -> list[dict]:
        """Return recent pulses that had a specific decision outcome."""
        decision = decision.upper()
        results = []
        for path in sorted(self._pulse_dir.glob("pulse-*.md"), reverse=True)[:limit * 3]:
            text = path.read_text(encoding="utf-8")
            m = re.match(r"^---\s*\n(.*?)\n---\n?(.*)", text, re.DOTALL)
            if m:
                desc = ""
                for line in m.group(1).split("\n"):
                    if line.strip().startswith("description:"):
                        desc = line.split(":", 1)[1].strip().strip('"')
                        break
                if desc.upper().startswith(decision):
                    body = (m.group(2) or "").strip()[:500]
                    results.append({"id": path.stem, "description": desc, "snippet": body})
                    if len(results) >= limit:
                        break
        return results

    def recent_pulses(self, limit: int = 5) -> list[dict]:
        """Most recently created pulse memories."""
        pulses = []
        for path in sorted(self._pulse_dir.glob("pulse-*.md"), reverse=True)[:limit]:
            text = path.read_text(encoding="utf-8")
            m = re.match(r"^---\s*\n(.*?)\n---\n?(.*)", text, re.DOTALL)
            if m:
                fm = {}
                for line in m.group(1).split("\n"):
                    if ":" not in line:
                        continue
                    k, v = line.strip().split(":", 1)
                    fm[k.strip()] = v.strip().strip('"')
                pulses.append(self._format_pulse_summary(fm, path.stem))
        return pulses

    def count(self) -> int:
        """Number of stored pulse memories."""
        return len(list(self._pulse_dir.glob("pulse-*.md")))

    # ── retrieval helpers ──────────────────────────────────

    def _format_pulse_summary(self, fm: dict, stem: str) -> dict:
        return {
            "id": stem,
            "title": fm.get("title", stem),
            "description": fm.get("description", ""),
            "tags": fm.get("tags", ""),
            "timestamp": fm.get("timestamp", ""),
        }

    # ── indexing ───────────────────────────────────────────

    def _index_pulse(self, pulse_id_str: str, goal: str,
                       outcome: dict, body_parts: list[str]) -> None:
        """Index a pulse memory in the vector DB for similarity search."""
        try:
            from memory_bridge.vector_search import SemanticMemory
            sm = SemanticMemory(self._wiki)
            decision = outcome.get("decision", "")

            index_text = (
                f"Pulse: {goal}\n"
                f"Decision: {decision}\n"
                f"Outcome: {outcome.get('test_summary', '')}\n"
                + "\n".join(body_parts[1:8])  # first ~8 body lines
            )

            sm.store(
                f"pulses/{pulse_id_str}",
                index_text,
                {
                    "type": "pulse",
                    "title": f"Pulse: {goal[:80]}",
                    "decision": decision,
                    "pulse_id": pulse_id_str.replace("pulse-", ""),
                },
            )
        except Exception:
            pass  # indexing is best-effort
