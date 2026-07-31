"""L4 — Meta-Parameter Optimizer Loop.

Fast-feedback tuning: aggregates recent L1/L2/L3 outcomes, proposes clamped
deltas to a small set of meta-parameters, gates the proposal through the
immutable evaluator, checkpoints before applying, and persists state to
`.rsis/optimizer_state.json`.

Follows the same invariants as the lower loops: evaluator is immutable,
checkpoint before mutation, bounded budget, failures cascade up to L5.
"""

import json
import logging
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

from rsis.checkpoint import CheckpointManager
from rsis.config import CONFIG, L1_TUNABLES
from rsis.evaluator import EvaluatorClient
from rsis.memory import MemoryManager
from rsis.telemetry import TelemetryCollector, TelemetryEvent
from rsis.timeout import Budget, TimeoutError

logger = logging.getLogger(__name__)

# L4 owns the L1 execution params (see RSIS_SPEC §1.4 — no overlap with L5).
_TUNABLES = {name: (lo, hi, 1, path) for name, (lo, hi, path) in L1_TUNABLES.items()}


@dataclass
class L4Result:
    """Outcome of an L4 optimizer cycle."""
    success: bool
    changed: bool = False
    skipped: bool = False
    params: dict = field(default_factory=dict)
    deltas: dict = field(default_factory=dict)
    outcome_stats: dict = field(default_factory=dict)
    error: Optional[str] = None


class OptimizerLoop:
    """Tune bounded meta-parameters from outcome telemetry."""

    def __init__(
        self,
        telemetry: TelemetryCollector,
        memory: Optional[MemoryManager] = None,
        evaluator: Optional[EvaluatorClient] = None,
        checkpoint_mgr: Optional[CheckpointManager] = None,
    ):
        self.config = CONFIG.l4
        self.telemetry = telemetry
        self.memory = memory or MemoryManager(CONFIG.workspace_dir)
        self.evaluator = evaluator or EvaluatorClient()
        self.checkpoint = checkpoint_mgr or CheckpointManager(CONFIG.workspace_dir)
        self.state_path = Path(CONFIG.workspace_dir) / self.config.state_path
        self._cycle_count = 0

    # ── State ──────────────────────────────────────────────────────

    def _default_params(self) -> dict:
        params = {}
        for name, (_lo, _hi, _step, path) in _TUNABLES.items():
            obj = CONFIG
            for part in path[:-1]:
                obj = getattr(obj, part)
            params[name] = float(getattr(obj, path[-1]))
        return params

    def _load_state(self) -> dict:
        if self.state_path.exists():
            try:
                data = json.loads(self.state_path.read_text())
                data.setdefault("params", {})
                data.setdefault("history", [])
                data.setdefault("cycle", 0)
                return data
            except (json.JSONDecodeError, OSError) as e:
                logger.warning("Failed to read optimizer state (%s); resetting", e)
        return {"params": self._default_params(), "history": [], "cycle": 0}

    def _save_state(self, state: dict) -> None:
        self.state_path.parent.mkdir(parents=True, exist_ok=True)
        self.state_path.write_text(json.dumps(state, indent=2) + "\n")

    # ── Outcome aggregation ────────────────────────────────────────

    @staticmethod
    def aggregate_outcomes(memory: MemoryManager, limit: int) -> dict:
        """Aggregate recent KG outcomes into success-rate / score stats."""
        outcomes = memory.kg.get_insights(limit=limit)
        if not outcomes:
            return {"count": 0, "success_rate": 0.0, "avg_score": 0.0}
        applied = sum(1 for o in outcomes if o.get("outcome") == "applied")
        scores = []
        for o in outcomes:
            s = o.get("scores") or {}
            if s:
                scores.append(sum(s.values()) / len(s))
        return {
            "count": len(outcomes),
            "success_rate": applied / len(outcomes),
            "avg_score": sum(scores) / len(scores) if scores else 0.0,
        }

    # ── Tuning ─────────────────────────────────────────────────────

    def _propose_deltas(self, success_rate: float, current: dict) -> dict:
        deltas = {}
        for name, (lo, hi, step, _path) in _TUNABLES.items():
            cur = float(current.get(name, lo))
            if success_rate < self.config.target_success_low and cur < hi:
                deltas[name] = min(step, hi - cur)
            elif success_rate > self.config.target_success_high and cur > lo:
                deltas[name] = -min(step, cur - lo)
        return deltas

    def _apply(self, new_params: dict) -> None:
        """Persist tuned params and mirror them into the runtime CONFIG."""
        for name, (_lo, _hi, _step, path) in _TUNABLES.items():
            value = int(round(new_params[name]))
            obj = CONFIG
            for part in path[:-1]:
                obj = getattr(obj, part)
            setattr(obj, path[-1], value)
            logger.info("L4 tuned %s -> %d", name, value)

    # ── Cycle ──────────────────────────────────────────────────────

    def run_cycle(self, budget: Optional[Budget] = None) -> L4Result:
        budget = budget or Budget(
            max_iterations=1, max_time_s=self.config.cycle_timeout_s,
            label="L4 optimizer",
        )

        logger.info("L4 optimizer cycle %d starting", self._cycle_count + 1)
        self.telemetry.record(TelemetryEvent(
            event_type="l4_start", metadata={"cycle": self._cycle_count},
        ))
        self._cycle_count += 1

        try:
            if not budget.tick():
                raise TimeoutError("L4 budget exhausted before starting")

            stats = self.aggregate_outcomes(self.memory, self.config.outcome_window)
            if stats["count"] < self.config.min_outcomes:
                logger.info("L4 skipping: %d outcomes < %d minimum",
                            stats["count"], self.config.min_outcomes)
                self.telemetry.record(TelemetryEvent(
                    event_type="l4_skip", metadata=stats,
                ))
                return L4Result(success=True, skipped=True, outcome_stats=stats)

            state = self._load_state()
            deltas = self._propose_deltas(stats["success_rate"], state["params"])
            if not deltas:
                self.telemetry.record(TelemetryEvent(
                    event_type="l4_complete",
                    metadata={"changed": False, **stats},
                ))
                return L4Result(
                    success=True, changed=False, params=state["params"],
                    outcome_stats=stats,
                )

            # Checkpoint before any mutation
            if CONFIG.checkpoint_before_mutation:
                self.checkpoint.checkpoint("l4-param-tune")

            # Gate the proposal through the immutable evaluator
            eval_result = self.evaluator.evaluate({
                "description": "Tune meta-parameters from outcome telemetry",
                "target_files": [self.config.state_path],
                "diff": json.dumps(deltas, indent=2),
                "rationale": (
                    f"success_rate={stats['success_rate']:.2f} "
                    f"avg_score={stats['avg_score']:.1f}"
                ),
                "attempt": 1,
                "goal": "optimize meta-parameters",
            })
            self.telemetry.record(TelemetryEvent(
                event_type="l4_evaluation",
                metadata={
                    "decision": eval_result.decision,
                    "score_avg": eval_result.score_avg,
                    "deltas": deltas,
                },
            ))

            if not eval_result.passed:
                logger.info("L4 proposal rejected: %s", eval_result.rationale[:60])
                state["history"].append({
                    "cycle": state["cycle"], "deltas": deltas,
                    "accepted": False, "stats": stats,
                })
                self._save_state(state)
                return L4Result(
                    success=True, changed=False, params=state["params"],
                    deltas=deltas, outcome_stats=stats,
                )

            new_params = dict(state["params"])
            for name, delta in deltas.items():
                lo, hi, _step, _path = _TUNABLES[name]
                new_params[name] = max(lo, min(hi, float(new_params.get(name, lo)) + delta))

            self._apply(new_params)
            state["params"] = new_params
            state["cycle"] += 1
            state["history"].append({
                "cycle": state["cycle"], "deltas": deltas,
                "accepted": True, "stats": stats,
            })
            self._save_state(state)

            logger.info("L4 tuned %d parameter(s)", len(deltas))
            self.telemetry.record(TelemetryEvent(
                event_type="l4_complete",
                metadata={"changed": True, "deltas": deltas, **stats},
            ))
            return L4Result(
                success=True, changed=True, params=new_params,
                deltas=deltas, outcome_stats=stats,
            )

        except TimeoutError:
            raise
        except Exception as e:
            logger.exception("L4 optimizer failed")
            self.telemetry.record(TelemetryEvent(
                event_type="l4_error", metadata={"error": str(e)},
            ))
            return L4Result(success=False, error=str(e))
