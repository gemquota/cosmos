#!/usr/bin/env python3
"""Reflection Engine — Periodic self-analysis that generates meta-goals.

The reflection engine is called by the L3 loop between pulse cycles.
It consumes data from multiple memory subsystems:

  - **Knowledge gaps** (GapDetector) — low-coverage entities, undefined acronyms
  - **Trend reports** (TemporalMemory) — rising/falling topics, monthly focus
  - **Pulse outcomes** (ExperienceMemory) — recent pass/fail patterns
  - **Identity state** — layer scores, crisis history, narrative

It produces:

  - A structured **reflection report** (wiki page in ``wiki/reflections/``)
  - **Meta-goals** — higher-order goals for L3 self-direction
  - **Strategy recommendations** — tactical suggestions for the next pulse

Usage::

    from memory_bridge import ReflectionEngine

    refl = ReflectionEngine()
    result = refl.reflect({
        "identity_state": {"layer_scores": {"L3": 45, "L1": 72}},
    })
    for goal in result["meta_goals"]:
        print(goal["description"], goal["priority"])
"""

import json
import uuid
from datetime import datetime
from pathlib import Path
from typing import Optional

from memory_bridge.config import resolve_wiki_path
try:
    from src.rrp.state_machine import detect_contradictions, resolve_contradiction
except ImportError:
    detect_contradictions = None
    resolve_contradiction = None


# ── Helpers ─────────────────────────────────────────────────────

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


#  ── ReflectionEngine ──────────────────────────────────────────

class ReflectionEngine:
    """Periodic self-analysis for RSIS3's L3 meta-cognitive loop.

    Call ``reflect()`` after a pulse cycle completes to generate
    meta-goals and strategy recommendations from current knowledge
    state and identity metrics.
    """

    def __init__(self, wiki_root: Optional[str | Path] = None):
        self._wiki = Path(wiki_root) if wiki_root else resolve_wiki_path()
        self._reflection_dir = self._wiki / "reflections"
        self._reflection_dir.mkdir(parents=True, exist_ok=True)

    # ── public API ──────────────────────────────────────────

    def reflect(self, context: Optional[dict] = None) -> dict:
        """Run one reflection cycle.

        ``context`` may contain:

          - identity_state — dict with ``layer_scores``, ``crisis_active``
          - pulse_limit  — how many recent pulses to analyze (default 10)
          - skip_subsystems — list of subsystem names to skip (e.g. ``["gaps"]``)

        Returns::

            {
                "findings": { ... },       # categorized findings
                "meta_goals": [ ... ],     # goals for L3
                "report_path": "str",      # path to wiki page
            }
        """
        context = context or {}
        skip = set(context.get("skip_subsystems", []))

        # Gather data from all subsystems
        gaps = self._get_gaps() if "gaps" not in skip else {"low_coverage": [], "acronyms": []}
        trends = self._get_trends() if "trends" not in skip else {"rising": [], "falling": []}
        pulses = self._get_recent_pulses(context.get("pulse_limit", 10)) if "episodes" not in skip else []
        identity_state = context.get("identity_state", {})

        # Analyze each source
        findings = {
            "knowledge_gaps": self._analyze_gaps(gaps),
            "temporal_trends": self._analyze_trends(trends),
            "performance_outcomes": self._analyze_outcomes(pulses),
            "identity_health": self._analyze_identity(identity_state),
        }

        # Flatten all findings for priority ranking
        all_findings = []
        for cat in findings.values():
            all_findings.extend(cat)

        # Generate meta-goals from high-severity findings
        meta_goals = self._generate_meta_goals(all_findings)

        # Persist report
        report_path = self._write_report(findings, meta_goals)

        return {
            "findings": findings,
            "meta_goals": meta_goals,
            "report_path": str(report_path),
        }

    # ── data gathering ──────────────────────────────────────

    def _get_gaps(self) -> dict:
        """Pull knowledge gaps from mykb gap detector."""
        try:
            from memory_bridge.gap_detector import GapDetector
            gd = GapDetector(self._wiki)
            return gd.analyze()
        except Exception:
            return {"low_coverage": [], "stubs": [], "acronyms": [], "missing_tags": []}

    def _get_trends(self) -> dict:
        """Pull temporal trend data from mykb temporal memory."""
        try:
            from memory_bridge.temporal_memory import TemporalMemory
            tm = TemporalMemory(self._wiki)
            return tm.trend_summary()
        except Exception:
            return {"rising": [], "falling": [], "stable": 0}

    def _get_recent_pulses(self, limit: int = 10) -> list[dict]:
        """Pull recent pulse memory outcomes."""
        try:
            from memory_bridge.experience_memory import ExperienceMemory
            em = ExperienceMemory(self._wiki)
            return em.recent_pulses(limit=limit)
        except Exception:
            return []

    # ── analysis ────────────────────────────────────────────

    def _analyze_gaps(self, gaps: dict) -> list[dict]:
        """Analyze knowledge gap data for actionable findings."""
        findings = []
        lc = gaps.get("low_coverage", [])
        if lc:
            findings.append({
                "type": "knowledge_gap",
                "severity": "medium",
                "label": "Low-coverage entities",
                "description": f"{len(lc)} entities referenced in 3+ sessions but with <500b body",
                "count": len(lc),
                "samples": [e.get("title", e.get("slug", "?")) for e in lc[:5]],
            })
        ac = gaps.get("acronyms", [])
        if ac:
            findings.append({
                "type": "definition_gap",
                "severity": "low",
                "label": "Undefined acronyms",
                "description": f"{len(ac)} acronyms in use without definitions",
                "count": len(ac),
                "samples": [a.get("title", a.get("slug", "?")) for a in ac[:5]],
            })
        return findings

    def _analyze_trends(self, trends: dict) -> list[dict]:
        """Analyze temporal trend data for patterns."""
        findings = []
        rising = trends.get("rising", [])
        falling = trends.get("falling", [])
        if rising:
            findings.append({
                "type": "rising_focus",
                "severity": "info",
                "label": "Rising topics",
                "description": f"{len(rising)} topics gaining attention",
                "samples": [r.get("entity", "") for r in rising[:5]],
            })
        if falling:
            findings.append({
                "type": "falling_focus",
                "severity": "info",
                "label": "Falling topics",
                "description": f"{len(falling)} topics losing attention",
                "samples": [f.get("entity", "") for f in falling[:5]],
            })
        return findings

    def _analyze_outcomes(self, pulses: list[dict]) -> list[dict]:
        """Analyze recent pulse outcomes for performance patterns."""
        findings = []
        if not pulses:
            findings.append({
                "type": "no_pulses",
                "severity": "info",
                "label": "No pulses recorded",
                "description": "No pulse memories exist yet. The first few cycles will establish a baseline.",
            })
            return findings

        # Count decisions
        pass_count = 0
        fail_count = 0
        hold_count = 0
        for ep in pulses:
            desc = ep.get("description", "")
            if desc.upper().startswith("PASS"):
                pass_count += 1
            elif desc.upper().startswith("DISMISS") or desc.upper().startswith("FAIL"):
                fail_count += 1
            else:
                hold_count += 1

        total = len(pulses)
        pass_rate = (pass_count / total * 100) if total > 0 else 0

        findings.append({
            "type": "pass_rate",
            "severity": "high" if pass_rate < 40 else ("medium" if pass_rate < 60 else "info"),
            "label": f"Pass rate: {pass_rate:.0f}%",
            "description": f"{pass_count} PASS / {fail_count} FAIL / {hold_count} HOLD out of {total} recent episodes",
            "pass_rate": round(pass_rate, 1),
            "total": total,
        })

        if pass_rate < 40 and total >= 3:
            findings.append({
                "type": "performance_warning",
                "severity": "high",
                "label": "Performance declining",
                "description": "Pass rate below 40% — consider changing variant strategy or taking a checkpoint",
            })

        return findings

    def _analyze_identity(self, identity_state: dict) -> list[dict]:
        """Analyze identity state for low scores and risks."""
        findings = []
        layer_scores = identity_state.get("layer_scores", {})

        if not layer_scores:
            return findings

        low_layers = []
        for lid, ls in layer_scores.items():
            score = ls.get("score", 0) if isinstance(ls, dict) else ls
            if isinstance(score, (int, float)) and score < 20:
                low_layers.append({"layer": lid, "score": score})

        if low_layers:
            for ll in low_layers:
                findings.append({
                    "type": "low_layer_score",
                    "severity": "high",
                    "label": f"{ll['layer']} score is {ll['score']}",
                    "description": f"{ll['layer']} capability score ({ll['score']}) is below the 20-point threshold",
                    "layer": ll["layer"],
                    "score": ll["score"],
                })

        if identity_state.get("crisis_active"):
            findings.append({
                "type": "active_crisis",
                "severity": "critical",
                "label": "Identity crisis active",
                "description": "An identity crisis is ongoing — crisis resolution should be the highest priority",
            })

        # ── RRP contradiction detection ─────────────────────
        if detect_contradictions is not None:
            try:
                # Extract decisions and constraints from identity state for analysis
                past_decisions = identity_state.get("decisions", [])
                if past_decisions:
                    contradictions = detect_contradictions(past_decisions)
                    for cd in contradictions:
                        severity = "high" if cd.get("confidence", 0) > 0.7 else "medium"
                        findings.append({
                            "type": "contradiction",
                            "severity": severity,
                            "label": f"Contradiction detected: {cd.get('dimension', 'unknown')}",
                            "description": cd.get("description", ""),
                            "confidence": cd.get("confidence", 0),
                            "suggested_resolution": cd.get("resolution", ""),
                        })
            except Exception:
                pass  # RRP detection is best-effort

        return findings

    # ── meta-goal generation ────────────────────────────────

    def _generate_meta_goals(self, all_findings: list[dict]) -> list[dict]:
        """Convert prioritized findings into structured meta-goals.

        Returns goals compatible with RSIS3's GoalGenerator format:
        ``{id, description, priority, source_signal, value_alignment, suggested_tasks}``
        """
        # Sort by severity
        severity_order = {"critical": 0, "high": 1, "medium": 2, "info": 3}
        sorted_findings = sorted(all_findings, key=lambda f: severity_order.get(f.get("severity", "info"), 99))

        goals = []
        for finding in sorted_findings[:5]:  # top 5
            ftype = finding.get("type", "")
            sev = finding.get("severity", "info")

            if ftype == "low_layer_score":
                layer = finding.get("layer", "?")
                score = finding.get("score", 0)
                goals.append({
                    "id": f"meta-{uuid.uuid4().hex[:8]}",
                    "description": f"Raise {layer} capability score from {score} above the 20-point threshold",
                    "priority": round(0.95 if sev == "critical" else 0.85, 2),
                    "source_signal": f"reflection/{ftype}/{layer}",
                    "value_alignment": ["growth", "robustness"],
                    "suggested_tasks": [
                        f"Analyze {layer} metrics for root causes",
                        "Generate a targeted improvement plan",
                        "Execute a recovery-focused pulse cycle",
                    ],
                })

            elif ftype == "active_crisis":
                goals.append({
                    "id": f"meta-{uuid.uuid4().hex[:8]}",
                    "description": "Resolve active identity crisis immediately",
                    "priority": 0.99,
                    "source_signal": "reflection/active_crisis",
                    "value_alignment": ["stability", "survival"],
                    "suggested_tasks": [
                        "Identify crisis trigger events",
                        "Execute crisis resolution protocol",
                        "Verify all layer scores stabilize",
                    ],
                })

            elif ftype == "performance_warning":
                goals.append({
                    "id": f"meta-{uuid.uuid4().hex[:8]}",
                    "description": f"Address declining performance — {finding.get('description', 'pass rate too low')}",
                    "priority": 0.80,
                    "source_signal": "reflection/performance_warning",
                    "value_alignment": ["learning", "adaptation"],
                    "suggested_tasks": [
                        "Review recent failed pulses for patterns",
                        "Try different RRP variants or strategies",
                        "Take a system checkpoint before making changes",
                    ],
                })

            elif ftype == "knowledge_gap":
                goals.append({
                    "id": f"meta-{uuid.uuid4().hex[:8]}",
                    "description": f"Document knowledge gaps — {finding.get('description', '')}",
                    "priority": 0.65,
                    "source_signal": "reflection/knowledge_gap",
                    "value_alignment": ["knowledge", "coherence"],
                    "suggested_tasks": [
                        f"Write wiki pages for: {', '.join(finding.get('samples', [])[:3])}",
                        "Add definitions for unknown terms",
                        "Cross-link from related entities",
                    ],
                })

            elif ftype == "definition_gap":
                goals.append({
                    "id": f"meta-{uuid.uuid4().hex[:8]}",
                    "description": f"Define {finding.get('count', 0)} undefined acronyms",
                    "priority": 0.50,
                    "source_signal": "reflection/definition_gap",
                    "value_alignment": ["clarity", "coherence"],
                    "suggested_tasks": [
                        f"Find what these mean: {', '.join(finding.get('samples', [])[:5])}",
                        "Write definition stubs",
                    ],
                })

        return goals

    # ── report persistence ──────────────────────────────────

    def _write_report(self, findings: dict, meta_goals: list[dict]) -> Path:
        """Persist a structured reflection report as a wiki page."""
        timestamp = _iso_now()
        date_key = timestamp[:10] if "T" in timestamp else datetime.utcnow().strftime("%Y-%m-%d")

        # Count total findings
        total_findings = sum(len(v) for v in findings.values())

        body = [
            f"# Reflection Report — {date_key}",
            f"_Generated: {timestamp}_",
            "",
            "## Summary",
            "",
            f"- **Total findings:** {total_findings}",
            f"- **Meta-goals generated:** {len(meta_goals)}",
            "",
        ]

        # Meta-goals section
        if meta_goals:
            body.append("## Meta-Goals\n")
            for g in meta_goals:
                body.append(f"- **[P={g['priority']}]** {g['description']}")
            body.append("")

        # Findings by category
        for cat_name, cat_findings in findings.items():
            if not cat_findings:
                continue
            heading = cat_name.replace("_", " ").title()
            body.append(f"## {heading}\n")
            for f in cat_findings:
                sev = f.get("severity", "info").upper()
                label = f.get("label", f.get("description", ""))
                body.append(f"- **[{sev}]** {label}")
                desc = f.get("description", "")
                if desc and desc != label:
                    body.append(f"  — {desc}")
            body.append("")

        # Frontmatter
        front = {
            "type": "reflection",
            "title": f"Reflection Report {date_key}",
            "description": f"{total_findings} findings, {len(meta_goals)} meta-goals",
            "tags": ["reflection", "meta-analysis", date_key[:7]],
            "timestamp": timestamp,
        }

        path = self._reflection_dir / f"reflection-{date_key}.md"
        content = _frontmatter(**front) + "\n\n" + "\n".join(body) + "\n"
        path.write_text(content, encoding="utf-8")
        return path

    # ── utility ─────────────────────────────────────────────

    def get_recent_reports(self, limit: int = 5) -> list[dict]:
        """Return the most recent reflection reports."""
        reports = []
        for path in sorted(self._reflection_dir.glob("reflection-*.md"), reverse=True)[:limit]:
            text = path.read_text(encoding="utf-8")
            import re
            m = re.match(r"^---\s*\n(.*?)\n---", text, re.DOTALL)
            if m:
                fm = {}
                for line in m.group(1).split("\n"):
                    if ":" not in line:
                        continue
                    k, v = line.strip().split(":", 1)
                    fm[k.strip()] = v.strip().strip('"')
                reports.append({
                    "path": str(path),
                    "title": fm.get("title", ""),
                    "description": fm.get("description", ""),
                    "timestamp": fm.get("timestamp", ""),
                })
        return reports
