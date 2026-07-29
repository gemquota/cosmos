#!/usr/bin/env python3
"""Meta-Learning Engine — Improves RSIS3's own improvement algorithms.

Analyzes historical data across all memory subsystems to generate
concrete parameter tuning recommendations for RSIS3's internal
configuration.

What it analyzes:

  - **Variant performance** — which RRP variants / strategies produce
    the highest pass rates across different problem types.
  - **Efficiency trends** — is the system improving over time, plateauing,
    or declining?  Pass rate trajectory across temporal windows.
  - **Experiment outcomes** — what kinds of hypotheses have been tested
    and which treatments won.
  - **Pulse patterns** — which evaluation phase lengths correlate with
    success, how goal priority relates to pass rate, etc.

What it produces:

  - **Parameter recommendations** — tuned values for RSIS3 config knobs
    like ``rrp_variant_selection``, ``evaluation_threshold``, etc.
  - **Meta-learning reports** — wiki pages in ``wiki/meta-learning/``
  - **Strategy suggestions** — tactical direction for the next N cycles

Usage::

    from memory_bridge import MetaLearningEngine

    mle = MetaLearningEngine()
    analysis = mle.analyze()
    for rec in analysis["parameter_recommendations"]:
        print(f"{rec['parameter']}: {rec['current']} → {rec['recommended']}")
"""

import json
import re
import math
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path
from typing import Optional

from memory_bridge.config import resolve_wiki_path


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


#  ── MetaLearningEngine ────────────────────────────────────────

class MetaLearningEngine:
    """Analyzes RSIS3's own performance data to tune its internal parameters.

    The engine reads from ``wiki/pulses/``, ``wiki/experiments/``,
    and subsystem metrics to build a picture of how well the system is
    improving and what parameters should be adjusted.

    Call ``analyze()`` periodically (e.g. every 5-10 pulse cycles) to
    keep RSIS3's configuration optimally tuned.
    """

    def __init__(self, wiki_root: Optional[str | Path] = None):
        self._wiki = Path(wiki_root) if wiki_root else resolve_wiki_path()
        self._learn_dir = self._wiki / "meta-learning"
        self._learn_dir.mkdir(parents=True, exist_ok=True)

    # ── public API ──────────────────────────────────────────

    def analyze(self) -> dict:
        """Run a full meta-learning analysis pass.

        Gathers data from pulses, experiments, and system state,
        then produces performance analysis and parameter recommendations.

        Returns::

            {
                "variant_performance": { str: {pass_rate, total} },
                "efficiency_trends": {trend, pass_rate_trend, windows},
                "parameter_recommendations": [
                    {parameter, current, recommended, reason, confidence}
                ],
                "report_path": str,
            }
        """
        pulses = self._load_pulses()
        experiments = self._load_completed_experiments()

        variant_perf = self._analyze_variant_performance(pulses)
        efficiency = self._analyze_efficiency_trends(pulses)
        experiment_insights = self._analyze_experiments(experiments)

        recommendations = self._generate_recommendations(
            variant_perf, efficiency, experiment_insights,
        )

        report_path = self._write_report(
            variant_perf, efficiency, experiment_insights, recommendations,
        )

        return {
            "variant_performance": variant_perf,
            "efficiency_trends": efficiency,
            "experiment_insights": experiment_insights,
            "parameter_recommendations": recommendations,
            "report_path": str(report_path),
            "total_pulses_analyzed": len(pulses),
            "total_experiments_analyzed": len(experiments),
        }

    def get_parameter_updates(self) -> list[dict]:
        """Convenience: return just the parameter recommendations."""
        return self.analyze().get("parameter_recommendations", [])

    # ── data loading ───────────────────────────────────────

    def _load_pulses(self) -> list[dict]:
        """Load pulse memory wiki pages."""
        pulses = []
        pulse_dir = self._wiki / "pulses"
        for path in sorted(pulse_dir.glob("pulse-*.md"), reverse=True)[:200]:
            text = path.read_text(encoding="utf-8")
            m = re.match(r"^---\s*\n(.*?)\n---\n?(.*)", text, re.DOTALL)
            if m:
                fm = {}
                for line in m.group(1).split("\n"):
                    if ":" not in line:
                        continue
                    k, v = line.strip().split(":", 1)
                    fm[k.strip()] = v.strip().strip('"')
                body = (m.group(2) or "").strip()
                pulses.append({"fm": fm, "body": body, "path": str(path)})
        return pulses

    def _load_completed_experiments(self) -> list[dict]:
        """Load completed experiments from wiki."""
        experiments = []
        exp_dir = self._wiki / "experiments"
        for path in exp_dir.glob("exp-*.md"):
            text = path.read_text(encoding="utf-8")
            if "## Conclusion" not in text:
                continue
            m = re.search(r"-\s+\*\*Winner:\*\*\s+(.+)$", text, re.MULTILINE)
            winner = m.group(1).strip() if m else "unknown"
            m2 = re.search(r"-\s+\*\*Effect:\*\*\s+(.+)$", text, re.MULTILINE)
            effect = m2.group(1).strip() if m2 else "0.0%"
            m3 = re.search(r"^# Experiment:\s*(.+)$", text, re.MULTILINE)
            hypothesis = m3.group(1).strip() if m3 else "Unknown"
            experiments.append({
                "id": path.stem,
                "hypothesis": hypothesis,
                "winner": winner,
                "effect": effect,
            })
        return experiments

    # ── analysis ───────────────────────────────────────────

    def _analyze_variant_performance(self, pulses: list[dict]) -> dict:
        """Analyze which approaches / variants produce the best outcomes.

        Scans pulse bodies for variant keywords and correlates them
        with PASS/DISMISS decisions.
        """
        variant_keywords = [
            "surgical", "template", "direct", "exploration",
            "conservative", "aggressive", "ast", "rrp",
        ]

        variant_stats = defaultdict(lambda: {"pass": 0, "fail": 0, "hold": 0, "total": 0})

        for ep in pulses:
            body = ep.get("body", "")
            desc = ep.get("fm", {}).get("description", "")
            decision = desc.split()[0] if desc else "UNKNOWN"

            # Find the first matching variant keyword
            matched = None
            body_lower = body.lower()
            for kw in variant_keywords:
                if kw in body_lower:
                    matched = kw
                    break

            if matched:
                variant_stats[matched]["total"] += 1
                if "PASS" in decision.upper():
                    variant_stats[matched]["pass"] += 1
                elif "DISMISS" in decision.upper() or "FAIL" in decision.upper():
                    variant_stats[matched]["fail"] += 1
                else:
                    variant_stats[matched]["hold"] += 1

        performance = {}
        for variant, stats in variant_stats.items():
            if stats["total"] >= 2:  # Need at least 2 samples
                performance[variant] = {
                    "total": stats["total"],
                    "pass_rate": round((stats["pass"] / stats["total"]) * 100, 1),
                    "fail_rate": round((stats["fail"] / stats["total"]) * 100, 1),
                    "hold_rate": round((stats["hold"] / stats["total"]) * 100, 1),
                }

        return dict(sorted(performance.items(), key=lambda x: -x[1].get("pass_rate", 0)))

    def _analyze_efficiency_trends(self, pulses: list[dict]) -> dict:
        """Analyze whether the system is improving over time.

        Divides pulses into sequential windows and tracks pass rate
        progression to detect improvement, stagnation, or decline.
        """
        if len(pulses) < 4:
            return {"trend": "insufficient_data", "pass_rate_trend": 0.0, "windows": []}

        # Reverse so oldest first
        ordered = list(reversed(pulses))

        window_size = max(1, len(ordered) // 4)
        windows = []

        for i in range(0, len(ordered), window_size):
            window = ordered[i : i + window_size]
            passes = sum(
                1 for e in window
                if "PASS" in e.get("fm", {}).get("description", "").upper()
            )
            rate = round((passes / len(window)) * 100, 1) if window else 0.0
            windows.append({"window_start": i, "pass_rate": rate, "count": len(window)})

        # Determine trend from first vs last window
        if len(windows) >= 2:
            first_rate = windows[0]["pass_rate"]
            last_rate = windows[-1]["pass_rate"]
            delta = last_rate - first_rate
        else:
            delta = 0.0

        if delta > 10:
            trend = "improving"
        elif delta < -10:
            trend = "declining"
        elif abs(delta) <= 10 and len(windows) >= 3:
            # Check if it's plateauing (stable with low variance)
            rates = [w["pass_rate"] for w in windows]
            if max(rates) - min(rates) < 15:
                trend = "plateauing"
            else:
                trend = "stable"
        else:
            trend = "stable"

        return {
            "trend": trend,
            "pass_rate_trend": round(delta, 1),
            "windows": windows,
            "first_window_pass_rate": windows[0]["pass_rate"] if windows else 0,
            "last_window_pass_rate": windows[-1]["pass_rate"] if windows else 0,
        }

    def _analyze_experiments(self, experiments: list[dict]) -> dict:
        """Summarize completed experiment outcomes."""
        if not experiments:
            return {"total": 0, "treatment_wins": 0, "control_wins": 0, "ties": 0}

        treatment_wins = sum(1 for e in experiments if e["winner"] == "treatment")
        control_wins = sum(1 for e in experiments if e["winner"] == "control")
        ties = sum(1 for e in experiments if e["winner"] == "tie")

        return {
            "total": len(experiments),
            "treatment_wins": treatment_wins,
            "control_wins": control_wins,
            "ties": ties,
            "treatment_win_rate": round((treatment_wins / len(experiments)) * 100, 1),
        }

    # ── recommendation generation ──────────────────────────

    def _generate_recommendations(self, variant_perf: dict,
                                   efficiency: dict,
                                   experiment_insights: dict) -> list[dict]:
        """Generate concrete parameter tuning recommendations."""
        recommendations = []

        # 1. Variant selection
        if variant_perf:
            best_variant = list(variant_perf.keys())[0]
            best_rate = variant_perf[best_variant]["pass_rate"]
            recommendations.append({
                "parameter": "rrp_variant_selection",
                "current": "default",
                "recommended": best_variant,
                "reason": (
                    f"'{best_variant}' has the highest pass rate ({best_rate}%) "
                    f"across {variant_perf[best_variant]['total']} samples"
                ),
                "confidence": "high" if variant_perf[best_variant]["total"] >= 5 else "medium",
            })

            # If there's a clear worst performer, suggest dropping it
            worst_variant = list(variant_perf.keys())[-1]
            worst_rate = variant_perf[worst_variant]["pass_rate"]
            if worst_rate < best_rate - 30 and variant_perf[worst_variant]["total"] >= 3:
                recommendations.append({
                    "parameter": "rrp_variant_exclusion",
                    "current": "none",
                    "recommended": f"avoid '{worst_variant}'",
                    "reason": (
                        f"'{worst_variant}' has only {worst_rate}% pass rate "
                        f"({best_rate - worst_rate:.0f}% below best variant)"
                    ),
                    "confidence": "medium",
                })

        # 2. Evaluation threshold tuning based on efficiency
        trend = efficiency.get("trend", "insufficient_data")
        if trend == "declining":
            recommendations.append({
                "parameter": "evaluation_threshold",
                "current": "standard",
                "recommended": "relaxed",
                "reason": (
                    "Declining pass rate trend suggests evaluation criteria "
                    "may be too strict; consider relaxing thresholds temporarily"
                ),
                "confidence": "low",
            })
            recommendations.append({
                "parameter": "checkpoint_frequency",
                "current": "per-pulse",
                "recommended": "every-2-pulses",
                "reason": "Declining performance warrants more frequent checkpoints for safety",
                "confidence": "medium",
            })
        elif trend == "plateauing":
            recommendations.append({
                "parameter": "evaluation_threshold",
                "current": "standard",
                "recommended": "raise",
                "reason": "System is plateauing — raising the bar may push for higher quality improvements",
                "confidence": "low",
            })
            recommendations.append({
                "parameter": "variant_exploration_rate",
                "current": "default",
                "recommended": "increase",
                "reason": "Plateau suggests need for more diverse approaches; increase exploration rate",
                "confidence": "medium",
            })
        elif trend == "improving":
            recommendations.append({
                "parameter": "confidence_threshold",
                "current": "standard",
                "recommended": "raise",
                "reason": "System is improving — raising the confidence threshold will filter for higher-quality changes",
                "confidence": "low",
            })

        # 3. Experiment-driven recommendations
        exp = experiment_insights
        if exp.get("total", 0) >= 3:
            if exp.get("treatment_win_rate", 0) > 60:
                recommendations.append({
                    "parameter": "experiment_adoption_rate",
                    "current": "manual-review",
                    "recommended": "auto-adopt",
                    "reason": (
                        f"Treatment wins {exp['treatment_win_rate']}% of the time "
                        f"({exp['treatment_wins']}/{exp['total']}) — safe to auto-adopt"
                    ),
                    "confidence": "medium",
                })
            elif exp.get("treatment_win_rate", 0) < 30:
                recommendations.append({
                    "parameter": "hypothesis_quality",
                    "current": "current",
                    "recommended": "improve",
                    "reason": (
                        f"Only {exp['treatment_win_rate']}% of hypotheses are winning — "
                        "need better hypothesis formulation before running experiments"
                    ),
                    "confidence": "medium",
                })

        # 4. Goal priority calibration
        if efficiency.get("total_pulses_analyzed", 0) > 0:
            recommendations.append({
                "parameter": "goal_priority_calibration",
                "current": "linear",
                "recommended": "adaptive",
                "reason": (
                    f"Based on {efficiency.get('total_pulses_analyzed', 0)} pulses analyzed, "
                    "adaptive priority scoring may better reflect changing conditions"
                ),
                "confidence": "low",
            })

        return recommendations

    # ── reporting ──────────────────────────────────────────

    def _write_report(self, variant_perf: dict, efficiency: dict,
                       experiment_insights: dict,
                       recommendations: list[dict]) -> Path:
        """Persist a meta-learning analysis report as a wiki page."""
        timestamp = _iso_now()
        date_key = timestamp[:10] if "T" in timestamp else datetime.utcnow().strftime("%Y-%m-%d")

        body = [
            f"# Meta-Learning Analysis — {date_key}",
            f"_Generated: {timestamp}_",
            "",
            "## Summary",
            "",
        ]

        # Variant performance
        body.append("### Variant Performance\n")
        if variant_perf:
            body.append("| Variant | Pass Rate | Fail Rate | Samples |")
            body.append("|---------|-----------|-----------|---------|")
            for v, perf in variant_perf.items():
                body.append(
                    f"| {v} | {perf['pass_rate']}% | {perf['fail_rate']}% | {perf['total']} |"
                )
        else:
            body.append("_Insufficient data — need at least 2 samples per variant._")
        body.append("")

        # Efficiency trends
        body.append("### Efficiency Trends\n")
        trend = efficiency.get("trend", "unknown")
        body.append(f"- **Trend:** {trend}")
        body.append(f"- **Pass rate change:** {efficiency.get('pass_rate_trend', 0):+.1f}%")
        body.append(f"- **Windows analyzed:** {len(efficiency.get('windows', []))}")
        windows = efficiency.get("windows", [])
        if windows:
            body.append("\n| Window | Pass Rate | Samples |")
            body.append("|--------|-----------|---------|")
            for w in windows:
                body.append(f"| {w['window_start']} | {w['pass_rate']}% | {w['count']} |")
        body.append("")

        # Experiment insights
        body.append("### Experiment Insights\n")
        ei = experiment_insights
        if ei.get("total", 0) > 0:
            body.append(f"- **Total completed:** {ei['total']}")
            body.append(f"- **Treatment wins:** {ei['treatment_wins']} ({ei.get('treatment_win_rate', 0)}%)")
            body.append(f"- **Control wins:** {ei['control_wins']}")
            body.append(f"- **Ties:** {ei['ties']}")
        else:
            body.append("_No completed experiments yet._")
        body.append("")

        # Recommendations
        body.append("### Parameter Recommendations\n")
        if recommendations:
            for rec in recommendations:
                body.append(f"- **{rec['parameter']}**: {rec['current']} → {rec['recommended']}")
                body.append(f"  - Reason: {rec['reason']}")
                body.append(f"  - Confidence: {rec['confidence']}")
        else:
            body.append("_No recommendations at this time._")
        body.append("")

        front = {
            "type": "meta-learning",
            "title": f"Meta-Learning Analysis {date_key}",
            "description": f"{len(recommendations)} recommendations — trend: {trend}",
            "tags": ["meta-learning", "analysis", date_key[:7], trend],
            "timestamp": timestamp,
        }

        path = self._learn_dir / f"meta-learning-{date_key}.md"
        content = _frontmatter(**front) + "\n\n" + "\n".join(body) + "\n"
        path.write_text(content, encoding="utf-8")
        return path

    # ── utility ─────────────────────────────────────────────

    def get_recent_reports(self, limit: int = 5) -> list[dict]:
        """Return the most recent meta-learning reports."""
        reports = []
        for path in sorted(self._learn_dir.glob("meta-learning-*.md"), reverse=True)[:limit]:
            text = path.read_text(encoding="utf-8")
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
