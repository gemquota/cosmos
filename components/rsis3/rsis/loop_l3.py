"""L3 — Cross-Session Evolution Loop.

The outermost loop: consolidates memory into the knowledge graph,
derives meta-strategies from session history, prunes redundant code
paths, evolves L2 improvement heuristics, and generates reports.

Phase 4: budget enforcement and exception safety.
"""

import json
import logging
import time
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

from rsis.config import CONFIG
from rsis.extrapolation import TelemetryExtrapolator
from rsis.memory import KnowledgeGraph, MemoryManager
from rsis.mykb_gateway import MyKBGateway
from rsis.telemetry import TelemetryCollector, TelemetryEvent
from rsis.timeout import Budget, TimeoutError

logger = logging.getLogger(__name__)


@dataclass
class L3Result:
    """Outcome of an L3 evolution cycle."""
    success: bool
    sessions_analysed: int = 0
    insights_added: int = 0
    strategies_evolved: list[str] = field(default_factory=list)
    redundancies_pruned: int = 0
    trends_detected: list[dict] = field(default_factory=list)
    mykb_written: bool = False
    mykb_path: Optional[str] = None
    error: Optional[str] = None


class L3EvolutionLoop:
    """Cross-session evolution loop with full memory consolidation."""

    def __init__(
        self,
        telemetry: TelemetryCollector,
        memory: Optional[MemoryManager] = None,
        mykb: Optional[MyKBGateway] = None,
    ):
        self.config = CONFIG.l3
        self.telemetry = telemetry
        self.memory = memory or MemoryManager(CONFIG.workspace_dir)
        self.mykb = mykb if mykb is not None else MyKBGateway()
        self.extrapolator = TelemetryExtrapolator()
        self._cycle_count = 0

    def run_cycle(self, budget: Optional[Budget] = None) -> L3Result:
        """Run one L3 evolution cycle with budget enforcement."""
        budget = budget or Budget(
            max_iterations=1,
            max_time_s=self.config.plateau_timeout_s,
            label="L3 evolution",
        )

        logger.info("L3 evolution cycle %d starting", self._cycle_count + 1)

        self.telemetry.record(TelemetryEvent(
            event_type="l3_start", metadata={"cycle": self._cycle_count},
        ))

        self._cycle_count += 1
        insights_added = 0
        strategies: list[str] = []
        redundancies = 0
        trends: list[dict] = []

        try:
            if not budget.tick():
                raise TimeoutError("L3 budget exhausted before starting")

            # Phase 1: Analyse telemetry for trends
            trends = self._detect_trends()

            # Phase 2: Consolidate memory into knowledge graph
            insights_added = self._consolidate_memory(trends)

            # Phase 3: Derive and evolve meta-strategies
            strategies = self._evolve_strategies(insights_added, trends)

            # Phase 4: Redundancy refinement
            redundancies = self._refine_redundancies()

            # Persist consolidated memory (KG + vectors)
            self.memory.save()

            # Phase 5: durable MyKB consolidation (memory link)
            mykb_meta = self._write_mykb_consolidation(
                insights_added, strategies, redundancies, trends)

            logger.info(
                "L3 cycle complete: %d insights, %d strategies, %d redundancies",
                insights_added, len(strategies), redundancies,
            )

        except TimeoutError:
            raise
        except Exception as e:
            logger.exception("L3 evolution failed")
            self.telemetry.record(TelemetryEvent(
                event_type="l3_error", metadata={"error": str(e)},
            ))
            return L3Result(success=False, error=str(e))

        self.telemetry.record(TelemetryEvent(
            event_type="l3_complete",
            metadata={
                "cycle": self._cycle_count,
                "insights": insights_added,
                "strategies": len(strategies),
                "redundancies": redundancies,
                "trends": len(trends),
                "mykb_written": bool(mykb_meta),
            },
        ))

        return L3Result(
            success=True,
            sessions_analysed=self._cycle_count,
            insights_added=insights_added,
            strategies_evolved=strategies,
            redundancies_pruned=redundancies,
            trends_detected=trends,
            mykb_written=bool(mykb_meta),
            mykb_path=(mykb_meta or {}).get("path"),
        )


    # ── Phase 5: Durable MyKB Consolidation (memory link) ────────────────

    def _write_mykb_consolidation(
        self,
        insights_added: int,
        strategies: list[str],
        redundancies: int,
        trends: list[dict],
    ) -> dict:
        """Write a durable OKF synthesis + log.md entry for this cycle.

        The MyKB gateway makes L3's consolidation step self-writing: the
        synthesis note and bundle-log entry are produced by the loop itself,
        not by a human post-processing step. Failures are logged and reported
        via telemetry but never fail the evolution cycle.
        """
        if not self.mykb.available:
            logger.info("MyKB gateway unavailable — skipping durable synthesis "
                        "(root=%s)", self.mykb.root)
            return {}

        cycle = self._cycle_count
        # Cycle ordinal is per-process; use the durable sequence of
        # L3-cycle syntheses already in MyKB so every write gets a
        # distinct, stable title across separate loop invocations.
        prior = [p for p in self.mykb.syntheses_dir.glob("rsis3-l3-cycle-*")
                 if p.name != "00-index.md"]
        cycle = len(prior) + 1
        title = f"RSIS3 L3 cycle {cycle} \u2014 cross-session memory consolidation"
        description = (
            f"L3 evolution cycle {cycle}: {insights_added} insight(s), "
            f"{len(strategies)} strategy(ies), {redundancies} redundancy "
            f"candidate(s), {len(trends)} trend(s) consolidated into MyKB"
        )
        tags = ["rsis3", "l3", "memory", "consolidation", "mykb"]

        lines = [
            f"# {title}",
            "",
            f"L3 cycle {cycle} consolidated workspace telemetry into durable "
            "MyKB memory: session insights, evolved strategies, redundancy "
            "candidates and detected trends.",
            "",
        ]
        if insights_added:
            lines.append(f"- **Insights added**: {insights_added} session "
                         "insight node(s) in the workspace KG.")
        if strategies:
            lines.append("- **Strategies evolved**: " + "; ".join(strategies) + ".")
        if redundancies:
            lines.append(f"- **Redundancies**: {redundancies} candidate(s) "
                         "flagged for refinement.")
        if trends:
            for t in trends:
                lines.append(f"- **Trend**: {t['context']} \u2014 {t['trend']} "
                             f"(slope={t['slope']}).")
        lines.append("")

        # Context read from MyKB: link the most relevant existing syntheses.
        related = self.mykb.search_syntheses(
            " ".join(tags) + " " + " ".join(strategies), limit=3)
        if related:
            lines.append("## Related")
            for hit in related:
                lines.append(f"- [[{hit['rel'][:-3]}|{hit['title']}]]")
            lines.append("")

        try:
            path = self.mykb.write_synthesis(
                title=title, description=description, tags=tags,
                body="\n".join(lines),
            )
            self.mykb.append_log(
                title=f"RSIS3 L3 cycle {cycle} \u2014 memory consolidation",
                bullets=[
                    f"L3 cycle {cycle} wrote OKF synthesis `{path.name}` "
                    f"({insights_added} insight(s), {len(strategies)} strategy(ies), "
                    f"{redundancies} redundancy candidate(s), {len(trends)} trend(s)).",
                    f"Gateway root: `{self.mykb.root}`.",
                ],
            )
        except Exception as e:
            logger.warning("MyKB consolidation failed (cycle continues): %s", e)
            self.telemetry.record(TelemetryEvent(
                event_type="l3_mykb_error", metadata={"error": str(e)},
            ))
            return {}
        meta = {"path": str(path), "log": str(self.mykb.log_path)}
        self.telemetry.record(TelemetryEvent(
            event_type="l3_mykb_write", metadata=meta,
        ))
        logger.info("MyKB consolidation written: %s", path)
        return meta

    # ── Phase 1: Trend Detection ───────────────────────────────────

    def _detect_trends(self) -> list[dict]:
        trends = self.extrapolator.detect_regression_trends()
        for t in trends:
            logger.info("Trend: %(context)s — %(trend)s (slope=%(slope)s)", t)
            if t["trend"] == "regression" and t["severity"] == "high":
                self.memory.kg.add_node(
                    node_id=f"trend-{self._cycle_count}-{len(trends)}",
                    node_type="insight",
                    description=f"Regression in {t['context']}: slope={t['slope']}",
                    context=t["context"],
                    slope=t["slope"],
                    severity=t["severity"],
                    detected_at=datetime.now(timezone.utc).isoformat(),
                )
        return trends

    # ── Phase 2: Memory Consolidation ───────────────────────────────

    def _consolidate_memory(self, trends: list[dict]) -> int:
        sessions = self.extrapolator.get_sessions()
        recent = sessions[-5:] if len(sessions) > 5 else sessions
        count = 0

        for session in recent:
            if session["type"] not in ("L2", "L3"):
                continue
            events = session["events"]
            l2_results = [e for e in events if e.get("type") == "l2_complete"]
            eval_events = [e for e in events if e.get("type") == "l2_evaluation"]

            if l2_results or eval_events:
                successes = sum(
                    1 for e in eval_events
                    if e.get("decision") == "PASS"
                )
                total = len(eval_events)
                outcome = f"{successes}/{total} evaluations passed"
                node_id = f"session-{session['session_id'][:8]}"

                self.memory.kg.add_node(
                    node_id=node_id,
                    node_type="insight",
                    description=f"Session {session['session_id'][:8]}: {outcome}",
                    session_id=session["session_id"],
                    success_rate=successes / max(total, 1),
                    event_count=session["event_count"],
                    timestamp=session["timestamp"],
                )
                count += 1

                for t in trends:
                    self.memory.kg.add_edge(
                        node_id, f"trend-{self._cycle_count}-{trends.index(t)}",
                        rel="exhibits_trend",
                    )

        vec_count = len(self.memory.vectors._documents)
        logger.info("Vector store has %d documents", vec_count)
        return count

    # ── Phase 3: Strategy Evolution ─────────────────────────────────

    def _evolve_strategies(self, insights_added: int, trends: list[dict]) -> list[str]:
        strategies = []
        existing = self.memory.kg.get_strategies()
        recent_improvements = self.memory.kg.get_insights(limit=5)

        optimal_iters = self.extrapolator.predict_optimal_iterations()
        strategy_id = f"strategy-budget-{self._cycle_count}"
        self.memory.kg.add_node(
            node_id=strategy_id,
            node_type="strategy",
            description=f"Optimal L2 iterations: {optimal_iters}",
            optimal_iterations=optimal_iters,
            cycle=self._cycle_count,
        )
        strategies.append(f"budget={optimal_iters}")

        regressions = [t for t in trends if t["trend"] == "regression"]
        if regressions:
            areas = ", ".join(t["context"] for t in regressions[:3])
            strategy_id2 = f"strategy-focus-{self._cycle_count}"
            self.memory.kg.add_node(
                node_id=strategy_id2,
                node_type="strategy",
                description=f"Focus improvement on: {areas}",
                target_areas=[t["context"] for t in regressions[:3]],
                cycle=self._cycle_count,
            )
            strategies.append(f"focus={areas}")

        if existing:
            prev = existing[-1]
            self.memory.kg.add_edge(
                strategy_id, prev["id"], rel="evolves_from",
            )

        return strategies

    # ── Phase 4: Redundancy Refinement ──────────────────────────────

    def _flagged_redundancy_pairs(self) -> set[frozenset]:
        """Return improvement pairs already flagged by prior cycles."""
        flagged: set[frozenset] = set()
        for node in self.memory.kg.query(node_type="insight"):
            ids = node.get("improvement_ids")
            if isinstance(ids, list) and len(ids) >= 2:
                flagged.add(frozenset(ids))
        return flagged

    def _refine_redundancies(self) -> int:
        candidates = self.extrapolator.find_redundancy_candidates(self.memory.kg)
        # Idempotent + bounded: re-flagging the same improvement pairs on
        # every cycle added two parallel edges per flag and grew the KG
        # edge list unboundedly, pushing cycle time past budget. Skip pairs
        # already flagged by an earlier cycle and cap new flags per cycle.
        already_flagged = self._flagged_redundancy_pairs()
        candidates.sort(key=lambda c: c.get("similarity", 0.0), reverse=True)
        pruned = 0

        for c in candidates:
            if pruned >= self.config.max_redundancy_flags_per_cycle:
                break
            pair = frozenset(c["improvement_ids"])
            if pair in already_flagged:
                continue
            already_flagged.add(pair)
            logger.info(
                "Redundancy: %s — similarity=%.2f",
                c["file"], c["similarity"],
            )
            self.memory.kg.add_node(
                node_id=f"redundancy-{self._cycle_count}-{pruned}",
                node_type="insight",
                description=f"Redundant patterns in {c['file']} "
                            f"({', '.join(c['descriptions'])})",
                file=c["file"],
                similarity=c["similarity"],
                improvement_ids=c["improvement_ids"],
            )
            for imp_id in c["improvement_ids"]:
                self.memory.kg.add_edge(
                    f"redundancy-{self._cycle_count}-{pruned}",
                    imp_id, rel="flags_as_redundant",
                )
            pruned += 1

        if pruned > 0:
            logger.info("Identified %d redundancy candidates", pruned)
        return pruned
