"""L6 — Identity Loop.

Tunes L3 evolution params (the +3 diagonal: L6 → L3). Reads outcome stats
and regression trends to adjust the L3 plateau timeout: shorter cycles when
regressions are detected or success is dropping (react faster), longer
patience when stable. Evaluator-gated, checkpointed, persisted to
`.rsis/identity_state.json`.
"""

import json
import logging
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

from rsis.checkpoint import CheckpointManager
from rsis.config import CONFIG, L3_TUNABLES
from rsis.evaluator import EvaluatorClient
from rsis.extrapolation import TelemetryExtrapolator
from rsis.loop_l4 import OptimizerLoop
from rsis.memory import MemoryManager
from rsis.telemetry import TelemetryCollector, TelemetryEvent
from rsis.timeout import Budget, TimeoutError

logger = logging.getLogger(__name__)

_NAME = "l3.plateau_timeout_s"
_LO, _HI, _PATH, _KIND = L3_TUNABLES[_NAME]


@dataclass
class L6Result:
    """Outcome of an L6 identity cycle."""
    success: bool
    changed: bool = False
    deltas: dict = field(default_factory=dict)
    params: dict = field(default_factory=dict)
    signal: Optional[str] = None
    error: Optional[str] = None


class IdentityLoop:
    """Tune the L3 plateau timeout from evolution signals."""

    def __init__(
        self,
        telemetry: TelemetryCollector,
        memory: Optional[MemoryManager] = None,
        evaluator: Optional[EvaluatorClient] = None,
        checkpoint_mgr: Optional[CheckpointManager] = None,
    ):
        self.config = CONFIG.l6
        self.telemetry = telemetry
        self.memory = memory or MemoryManager(CONFIG.workspace_dir)
        self.evaluator = evaluator or EvaluatorClient()
        self.checkpoint = checkpoint_mgr or CheckpointManager(CONFIG.workspace_dir)
        self.extrapolator = TelemetryExtrapolator(CONFIG.telemetry_dir)
        self.state_path = Path(CONFIG.workspace_dir) / self.config.state_path
        self._cycle_count = 0

    # ── State ──────────────────────────────────────────────────────

    def _default_params(self) -> dict:
        obj = CONFIG
        for part in _PATH[:-1]:
            obj = getattr(obj, part)
        return {_NAME: float(getattr(obj, _PATH[-1]))}

    def _load_state(self) -> dict:
        if self.state_path.exists():
            try:
                data = json.loads(self.state_path.read_text())
                data.setdefault("params", {})
                data.setdefault("history", [])
                data.setdefault("cycle", 0)
                return data
            except (json.JSONDecodeError, OSError) as e:
                logger.warning("Failed to read identity state (%s); resetting", e)
        return {"params": self._default_params(), "history": [], "cycle": 0}

    def _save_state(self, state: dict) -> None:
        self.state_path.parent.mkdir(parents=True, exist_ok=True)
        self.state_path.write_text(json.dumps(state, indent=2) + "\n")

    # ── Signal ─────────────────────────────────────────────────────

    def _signal(self, stats: dict, trends: list[dict]) -> Optional[str]:
        regressions = [
            t for t in trends
            if t.get("trend") == "regression" and t.get("severity") == "high"
        ]
        if regressions or stats["success_rate"] < self.config.shrink_below:
            return "shrink"
        if not regressions and stats["success_rate"] >= self.config.grow_above:
            return "grow"
        return None

    # ── Cycle ──────────────────────────────────────────────────────

    def run_cycle(self, budget: Optional[Budget] = None) -> L6Result:
        budget = budget or Budget(
            max_iterations=1, max_time_s=self.config.cycle_timeout_s,
            label="L6 identity",
        )

        logger.info("L6 identity cycle %d starting", self._cycle_count + 1)
        self.telemetry.record(TelemetryEvent(
            event_type="l6_start", metadata={"cycle": self._cycle_count},
        ))
        self._cycle_count += 1

        try:
            if not budget.tick():
                raise TimeoutError("L6 budget exhausted before starting")

            stats = OptimizerLoop.aggregate_outcomes(
                self.memory, CONFIG.l4.outcome_window)
            try:
                trends = self.extrapolator.detect_regression_trends()
            except Exception:
                trends = []
            signal = self._signal(stats, trends)

            state = self._load_state()
            if signal is None:
                self.telemetry.record(TelemetryEvent(
                    event_type="l6_complete",
                    metadata={"changed": False, **stats},
                ))
                return L6Result(success=True, changed=False, params=state["params"])

            current = float(state["params"].get(_NAME, _LO))
            delta = -self.config.timeout_step_s if signal == "shrink" else self.config.timeout_step_s
            if (signal == "shrink" and current <= _LO) or (signal == "grow" and current >= _HI):
                logger.info("L6 no-op: %s already at bound (%s)", signal, current)
                self.telemetry.record(TelemetryEvent(
                    event_type="l6_complete", metadata={"changed": False, **stats},
                ))
                return L6Result(
                    success=True, changed=False, params=state["params"], signal=signal,
                )

            # Checkpoint before mutation
            if CONFIG.checkpoint_before_mutation:
                self.checkpoint.checkpoint("l6-plateau-tune")

            # Gate through the immutable evaluator
            eval_result = self.evaluator.evaluate({
                "description": "Tune L3 plateau timeout from evolution signal",
                "target_files": [self.config.state_path],
                "diff": json.dumps({_NAME: delta}, indent=2),
                "rationale": f"signal={signal} success_rate={stats['success_rate']:.2f}",
                "attempt": 1,
                "goal": "tune L3 evolution params",
            })
            self.telemetry.record(TelemetryEvent(
                event_type="l6_evaluation",
                metadata={"decision": eval_result.decision, "signal": signal},
            ))

            if not eval_result.passed:
                logger.info("L6 proposal rejected: %s", eval_result.rationale[:60])
                state["history"].append({
                    "cycle": state["cycle"], "delta": delta,
                    "accepted": False, "signal": signal,
                })
                self._save_state(state)
                return L6Result(
                    success=True, changed=False, params=state["params"],
                    deltas={_NAME: delta}, signal=signal,
                )

            new_value = max(_LO, min(_HI, current + delta))
            state["params"][_NAME] = new_value
            state["cycle"] += 1
            state["history"].append({
                "cycle": state["cycle"], "delta": delta,
                "accepted": True, "signal": signal,
            })
            self._save_state(state)

            # Mirror into runtime CONFIG
            obj = CONFIG
            for part in _PATH[:-1]:
                obj = getattr(obj, part)
            setattr(obj, _PATH[-1], int(round(new_value)))
            logger.info("L6 tuned %s -> %d (%s)", _NAME, new_value, signal)

            self.telemetry.record(TelemetryEvent(
                event_type="l6_complete",
                metadata={"changed": True, "signal": signal, "delta": delta, **stats},
            ))
            return L6Result(
                success=True, changed=True, params=state["params"],
                deltas={_NAME: delta}, signal=signal,
            )

        except TimeoutError:
            raise
        except Exception as e:
            logger.exception("L6 identity failed")
            self.telemetry.record(TelemetryEvent(
                event_type="l6_error", metadata={"error": str(e)},
            ))
            return L6Result(success=False, error=str(e))
