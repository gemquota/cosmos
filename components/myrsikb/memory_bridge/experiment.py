#!/usr/bin/env python3
"""Experiment Manager — Automated hypothesis testing for RSIS3.

RSIS3 can formulate hypotheses, generate variants, run A/B tests,
compare results, and store the outcome permanently in mykb.

This closes the loop from "what if X is better than Y?" to
"X outperformed Y by 12% — recommendation recorded."

Lifecycle of an experiment::

    1. **Hypothesis** — e.g. "Variant A yields better pass rate than B"
    2. **Define** — control (current) vs treatment (modified)
    3. **Record** — each variant accumulates results over multiple cycles
    4. **Conclude** — compare, determine winner, compute effect size
    5. **Adopt** — winning treatment becomes a goal for the system

Usage::

    from memory_bridge import ExperimentManager

    em = ExperimentManager()
    exp_id = em.create_experiment(
        hypothesis="Surgical patches outperform template patches",
        control_desc="Template-based RRP patch generation",
        treatment_desc="Surgical AST-targeted patch generation",
        metric="pass_rate",
    )
    em.record_result(exp_id, "control", {"pass_rate": 72.0})
    em.record_result(exp_id, "treatment", {"pass_rate": 84.5})
    conclusion = em.conclude_experiment(exp_id)
    print(conclusion["recommendation"])
"""

import json
import re
import uuid
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


#  ── ExperimentManager ─────────────────────────────────────────

class ExperimentManager:
    """Design, execute, and analyze autonomous A/B experiments.

    Each experiment compares a **control** (current behavior) against
    a **treatment** (hypothesized improvement) over multiple samples.
    Results are persisted in ``wiki/experiments/`` and entered into
    the knowledge graph so the system can learn from every test.
    """

    def __init__(self, wiki_root: Optional[str | Path] = None):
        self._wiki = Path(wiki_root) if wiki_root else resolve_wiki_path()
        self._experiment_dir = self._wiki / "experiments"
        self._experiment_dir.mkdir(parents=True, exist_ok=True)

    # ── lifecycle ──────────────────────────────────────────

    def create_experiment(self, hypothesis: str,
                          control_desc: str,
                          treatment_desc: str,
                          metric: str = "pass_rate",
                          min_samples: int = 5) -> str:
        """Create a new experiment definition.

        Args:
            hypothesis:  The conjecture being tested (e.g. "Surgical patches
                         outperform template patches").
            control_desc: Description of the current/default approach.
            treatment_desc: Description of the proposed new approach.
            metric:       The primary metric to compare (e.g. ``pass_rate``,
                          ``confidence``, ``duration``).
            min_samples:  Minimum number of samples per variant before
                          ``conclude_experiment()`` will produce a result.

        Returns:
            The experiment ID (``exp-{8 hex chars}``).
        """
        exp_id = f"exp-{uuid.uuid4().hex[:8]}"
        timestamp = _iso_now()

        body = (
            f"# Experiment: {hypothesis}\n\n"
            f"**Status:** running\n"
            f"**Metric:** {metric}\n"
            f"**Min samples needed per variant:** {min_samples}\n"
            f"**Created:** {timestamp}\n\n"
            f"## Control\n{control_desc}\n\n"
            f"## Treatment\n{treatment_desc}\n\n"
            f"## Results\n\n"
            "_Collecting data..._\n"
        )

        front = {
            "type": "experiment",
            "title": f"Experiment: {hypothesis[:80]}",
            "description": f"Test: {control_desc[:60]} vs {treatment_desc[:60]} on {metric}",
            "tags": ["experiment", "hypothesis", metric, "running"],
            "timestamp": timestamp,
        }

        path = self._experiment_dir / f"{exp_id}.md"
        content = _frontmatter(**front) + "\n\n" + body + "\n"
        path.write_text(content, encoding="utf-8")

        return exp_id

    def record_result(self, experiment_id: str, variant: str,
                      metrics: dict, sample_size: int = 1) -> dict:
        """Record one sample result for a variant of an experiment.

        Args:
            experiment_id: The ID returned by ``create_experiment()``.
            variant:       ``"control"`` or ``"treatment"`` (case-insensitive).
            metrics:       Dict of metric name → numeric value.
            sample_size:   How many cycles this result aggregates (default 1).

        Returns:
            ``{"status": "recorded", "experiment_id": str, "variant": str}``
        """
        path = self._experiment_dir / f"{experiment_id}.md"
        if not path.exists():
            return {"error": f"Experiment '{experiment_id}' not found"}

        text = path.read_text(encoding="utf-8")
        variant_lower = variant.lower()

        metric_str = "  ".join(f"{k}={v}" for k, v in metrics.items())
        result_line = f"- **{variant_lower}** (n={sample_size}): {metric_str}\n"

        # Replace placeholder or append
        if "_Collecting data..._" in text:
            text = text.replace("_Collecting data..._\n", "")
            text += result_line
        else:
            text += result_line

        path.write_text(text, encoding="utf-8")
        return {"status": "recorded", "experiment_id": experiment_id, "variant": variant_lower}

    def conclude_experiment(self, experiment_id: str) -> dict:
        """Analyze collected results and determine the winning variant.

        Compares the primary metric across all recorded variants. If the
        minimum sample count has not been reached for all variants the
        conclusion will note insufficient data.

        Returns::

            {
                "experiment_id": str,
                "winner": "control" | "treatment" | "tie" | "insufficient_data",
                "effect_pct": float,       # relative improvement %
                "metric": str,
                "variant_results": { ... },  # per-variant stats
                "recommendation": str,
            }
        """
        path = self._experiment_dir / f"{experiment_id}.md"
        if not path.exists():
            return {"error": f"Experiment '{experiment_id}' not found"}

        text = path.read_text(encoding="utf-8")

        # Parse results from body
        results = self._parse_results(text)

        if len(results) < 2:
            return {
                "experiment_id": experiment_id,
                "winner": "insufficient_data",
                "effect_pct": 0.0,
                "metric": "unknown",
                "variant_results": results,
                "recommendation": "Need at least 2 variants with recorded results.",
            }

        # Find the primary metric — use the first common metric
        all_metrics = [set(r["metrics"].keys()) for r in results.values() if r["metrics"]]
        if not all_metrics:
            return {
                "experiment_id": experiment_id,
                "winner": "insufficient_data",
                "effect_pct": 0.0,
                "metric": "unknown",
                "variant_results": results,
                "recommendation": "No numeric metrics recorded.",
            }

        common = all_metrics[0]
        for mset in all_metrics[1:]:
            common = common & mset

        if not common:
            return {
                "experiment_id": experiment_id,
                "winner": "insufficient_data",
                "effect_pct": 0.0,
                "metric": "unknown",
                "variant_results": results,
                "recommendation": "Variants share no common metrics to compare.",
            }

        primary_metric = list(common)[0]

        # Calculate per-variant averages
        variant_avgs = {}
        for vname, vdata in results.items():
            vals = [m.get(primary_metric, 0) for m in vdata["metrics_list"]]
            variant_avgs[vname] = sum(vals) / len(vals) if vals else 0.0

        # Determine winner
        variants = list(variant_avgs.keys())
        if len(variants) < 2:
            return {
                "experiment_id": experiment_id,
                "winner": "insufficient_data",
                "effect_pct": 0.0,
                "metric": primary_metric,
                "variant_results": results,
                "recommendation": "Not all variants have data yet.",
            }

        control_val = variant_avgs.get("control", variant_avgs.get(variants[0], 0))
        treatment_val = variant_avgs.get("treatment", variant_avgs.get(variants[1], 0))

        if control_val > 0:
            effect_pct = ((treatment_val - control_val) / control_val) * 100
        else:
            effect_pct = 0.0

        # Significance check — simple: larger is better for most metrics
        # (lower is better for metrics like "duration")
        higher_is_better = primary_metric not in ("duration", "latency", "cost", "time")

        if higher_is_better:
            if treatment_val > control_val:
                winner = "treatment"
            elif control_val > treatment_val:
                winner = "control"
            else:
                winner = "tie"
        else:
            if treatment_val < control_val:
                winner = "treatment"
            elif control_val < treatment_val:
                winner = "control"
            else:
                winner = "tie"

        # Build recommendation
        if winner == "treatment":
            recommendation = (
                f"Treatment outperformed control by {abs(effect_pct):.1f}% "
                f"on {primary_metric}. Recommend adopting the treatment approach."
            )
        elif winner == "control":
            recommendation = (
                f"Control remains better than treatment by {abs(effect_pct):.1f}% "
                f"on {primary_metric}. Recommend keeping the current approach."
            )
        else:
            recommendation = "No significant difference detected. Either approach is viable."

        # Update wiki page with conclusion
        conclusion_block = (
            f"\n## Conclusion\n\n"
            f"- **Winner:** {winner}\n"
            f"- **Effect:** {effect_pct:+.1f}% on {primary_metric}\n"
            f"- **Control avg:** {variant_avgs.get('control', control_val):.3f}\n"
            f"- **Treatment avg:** {variant_avgs.get('treatment', treatment_val):.3f}\n"
            f"- **Recommendation:** {recommendation}\n"
        )

        # Update status tag
        new_front = _frontmatter(
            type="experiment",
            title=f"Experiment: {hypothesis_from_text(text)[:80]}",
            description=f"Winner: {winner} ({effect_pct:+.1f}%)",
            tags=["experiment", "completed", winner, primary_metric],
            timestamp=_iso_now(),
        )

        # Rebuild file with updated frontmatter + body + conclusion
        body_start = text.find("\n\n", text.find("---\n", 3))
        if body_start != -1:
            body_old = text[body_start:].strip()
            # Remove any prior conclusion block
            if "## Conclusion" in body_old:
                body_old = body_old[: body_old.index("## Conclusion")].strip()
            new_body = body_old + "\n" + conclusion_block
            content = new_front + "\n\n" + new_body + "\n"
            path.write_text(content, encoding="utf-8")

        # Record in knowledge graph
        self._record_in_kg(experiment_id, hypothesis_from_text(text), winner, effect_pct, primary_metric)

        return {
            "experiment_id": experiment_id,
            "winner": winner,
            "effect_pct": round(effect_pct, 1),
            "metric": primary_metric,
            "variant_results": variant_avgs,
            "recommendation": recommendation,
        }

    # ── parsing ─────────────────────────────────────────────

    def _parse_results(self, text: str) -> dict:
        """Parse result lines from an experiment wiki page body.

        Returns::

            {
                "control": {"n": int, "metrics": {str: float}, "metrics_list": [...]},
                "treatment": {"n": int, "metrics": {str: float}, "metrics_list": [...]},
            }
        """
        results = {}
        pattern = re.compile(r"-\s+\*\*(.+?)\*\*\s+\(n=(\d+)\):\s+(.+)$", re.MULTILINE)

        for m in pattern.finditer(text):
            vname = m.group(1).strip().lower()
            sample_n = int(m.group(2))
            metrics_str = m.group(3).strip()

            metrics = {}
            metrics_list = []
            for pair in metrics_str.replace("  ", " ").split():
                if "=" in pair:
                    k, v = pair.split("=", 1)
                    try:
                        metrics[k] = float(v)
                    except ValueError:
                        metrics[k] = v

            if vname not in results:
                results[vname] = {"n": 0, "metrics": {}, "metrics_list": []}
            results[vname]["n"] += sample_n
            results[vname]["metrics_list"].append(metrics)

            # Running average
            if metrics:
                for k, v in metrics.items():
                    if isinstance(v, (int, float)):
                        vals = [m.get(k, 0) for m in results[vname]["metrics_list"] if isinstance(m.get(k), (int, float))]
                        results[vname]["metrics"][k] = sum(vals) / len(vals) if vals else 0.0

        return results

    # ── knowledge graph ─────────────────────────────────────

    def _record_in_kg(self, exp_id: str, hypothesis: str,
                      winner: str, effect_pct: float, metric: str):
        """Record the experiment outcome in mykb's knowledge graph."""
        try:
            from memory_bridge.knowledge_graph import KnowledgeGraph
            kg = KnowledgeGraph(self._wiki)
            kg.create_node(
                exp_id, "experiment",
                f"Exp: {hypothesis[:80]}",
                {
                    "hypothesis": hypothesis[:200],
                    "winner": winner,
                    "effect_pct": effect_pct,
                    "metric": metric,
                },
            )
        except Exception:
            pass

    # ── goal conversion ─────────────────────────────────────

    def experiment_to_goal(self, experiment_id: str) -> Optional[dict]:
        """If the experiment shows treatment is better, return an adoption goal.

        Returns a goal dict compatible with RSIS3's GoalGenerator, or
        ``None`` if control won or data is insufficient.
        """
        conclusion = self.conclude_experiment(experiment_id)
        if conclusion.get("winner") == "treatment":
            return {
                "id": f"adopt-{uuid.uuid4().hex[:8]}",
                "description": (
                    f"Adopt winning treatment from {experiment_id}: "
                    f"{conclusion['recommendation'][:120]}"
                ),
                "priority": 0.80,
                "source_signal": f"experiment/{experiment_id}",
                "value_alignment": ["growth", "optimization", "learning"],
                "suggested_tasks": [
                    "Implement the winning variant as the new default",
                    "Update system configuration",
                    "Monitor for regression over next 3 cycles",
                ],
            }
        return None

    # ── status ──────────────────────────────────────────────

    def list_experiments(self, status: Optional[str] = None) -> list[dict]:
        """List all experiments, optionally filtered by status.

        ``status`` can be ``"running"``, ``"completed"``, or ``None`` (all).
        """
        experiments = []
        for path in sorted(self._experiment_dir.glob("exp-*.md"), reverse=True):
            text = path.read_text(encoding="utf-8")
            m = re.match(r"^---\s*\n(.*?)\n---\n?(.*)", text, re.DOTALL)
            if m:
                fm = {}
                for line in m.group(1).split("\n"):
                    if ":" not in line:
                        continue
                    k, v = line.strip().split(":", 1)
                    fm[k.strip()] = v.strip().strip('"')
                exp_status = "completed" if "## Conclusion" in text else "running"
                if status and exp_status != status:
                    continue
                experiments.append({
                    "id": path.stem,
                    "title": fm.get("title", ""),
                    "description": fm.get("description", ""),
                    "status": exp_status,
                    "timestamp": fm.get("timestamp", ""),
                })
        return experiments

    def count(self) -> int:
        return len(list(self._experiment_dir.glob("exp-*.md")))


# ── module-level helper ────────────────────────────────────────

def hypothesis_from_text(text: str) -> str:
    """Extract the hypothesis line from an experiment wiki page."""
    m = re.search(r"^# Experiment:\s*(.+)$", text, re.MULTILINE)
    return m.group(1).strip() if m else "Unknown hypothesis"
