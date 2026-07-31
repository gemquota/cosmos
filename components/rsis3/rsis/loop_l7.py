"""L7 — Meta-Cog Loop.

Tunes L4 optimizer params (the +3 diagonal: L7 → L4). Observes L4's tuning
history in `.rsis/optimizer_state.json`: on oscillation (L4 flipping deltas
back and forth) it widens the success deadband; on stall (L4 silent while
success is low) it narrows the deadband. Evaluator-gated, checkpointed,
persisted to `.rsis/metacog_state.json`.
"""

import json
import logging
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

from rsis.checkpoint import CheckpointManager
from rsis.config import CONFIG, L4_TUNABLES
from rsis.evaluator import EvaluatorClient
from rsis.loop_l4 import OptimizerLoop
from rsis.memory import MemoryManager
from rsis.telemetry import TelemetryCollector, TelemetryEvent
from rsis.timeout import Budget, TimeoutError

logger = logging.getLogger(__name__)

_LOW = "l4.target_success_low"
_HIGH = "l4.target_success_high"
_LO_BOUNDS = L4_TUNABLES[_LOW][:2]
_HI_BOUNDS = L4_TUNABLES[_HIGH][:2]
_MIN_GAP = 0.05


@dataclass
class L7Result:
    """Outcome of an L7 meta-cog cycle."""
    success: bool
    changed: bool = False
    deltas: dict = field(default_factory=dict)
    params: dict = field(default_factory=dict)
    signal: Optional[str] = None
    error: Optional[str] = None


class MetaCogLoop:
    """Meta-tune the L4 optimizer's success deadband."""

    def __init__(
        self,
        telemetry: TelemetryCollector,
        memory: Optional[MemoryManager] = None,
        evaluator: Optional[EvaluatorClient] = None,
        checkpoint_mgr: Optional[CheckpointManager] = None,
    ):
        self.config = CONFIG.l7
        self.telemetry = telemetry
        self.memory = memory or MemoryManager(CONFIG.workspace_dir)
        self.evaluator = evaluator or EvaluatorClient()
        self.checkpoint = checkpoint_mgr or CheckpointManager(CONFIG.workspace_dir)
        self.state_path = Path(CONFIG.workspace_dir) / self.config.state_path
        self.l4_state_path = Path(CONFIG.workspace_dir) / CONFIG.l4.state_path
        self._cycle_count = 0

    # ── State ──────────────────────────────────────────────────────

    def _default_params(self) -> dict:
        params = {}
        for name, (_lo, _hi, path, _kind) in L4_TUNABLES.items():
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
                logger.warning("Failed to read metacog state (%s); resetting", e)
        return {"params": self._default_params(), "history": [], "cycle": 0}

    def _save_state(self, state: dict) -> None:
        self.state_path.parent.mkdir(parents=True, exist_ok=True)
        self.state_path.write_text(json.dumps(state, indent=2) + "\n")

    # ── Signal ─────────────────────────────────────────────────────

    def _l4_history(self) -> list[dict]:
        if not self.l4_state_path.exists():
            return []
        try:
            data = json.loads(self.l4_state_path.read_text())
            return data.get("history", [])
        except (json.JSONDecodeError, OSError) as e:
            logger.warning("Failed to read L4 state: %s", e)
            return []

    def _signal(self, history: list[dict], stats: dict) -> Optional[str]:
        accepted = [h for h in history if h.get("accepted")][-self.config.oscillation_window:]
        if accepted:
            signs = {}
            for entry in accepted:
                for key, delta in (entry.get("deltas") or {}).items():
                    signs.setdefault(key, set()).add(1 if delta > 0 else -1)
            if any(len(v) > 1 for v in signs.values()):
                return "widen"

        recent = history[-self.config.stall_window:] if self.config.stall_window else []
        if len(recent) >= self.config.stall_window and not any(
            h.get("accepted") for h in recent
        ):
            low = self._load_state()["params"].get(_LOW, _LO_BOUNDS[0])
            if stats["success_rate"] < float(low):
                return "narrow"
        return None

    # ── Cycle ──────────────────────────────────────────────────────

    def run_cycle(self, budget: Optional[Budget] = None) -> L7Result:
        budget = budget or Budget(
            max_iterations=1, max_time_s=self.config.cycle_timeout_s,
            label="L7 meta-cog",
        )

        logger.info("L7 meta-cog cycle %d starting", self._cycle_count + 1)
        self.telemetry.record(TelemetryEvent(
            event_type="l7_start", metadata={"cycle": self._cycle_count},
        ))
        self._cycle_count += 1

        try:
            if not budget.tick():
                raise TimeoutError("L7 budget exhausted before starting")

            stats = OptimizerLoop.aggregate_outcomes(
                self.memory, CONFIG.l4.outcome_window)
            history = self._l4_history()
            signal = self._signal(history, stats)

            state = self._load_state()
            if signal is None:
                self.telemetry.record(TelemetryEvent(
                    event_type="l7_complete", metadata={"changed": False},
                ))
                return L7Result(success=True, changed=False, params=state["params"])

            low = float(state["params"].get(_LOW, _LO_BOUNDS[0]))
            high = float(state["params"].get(_HIGH, _HI_BOUNDS[0]))
            step = self.config.deadband_step
            if signal == "widen":
                new_low = max(_LO_BOUNDS[0], low - step)
                new_high = min(_HI_BOUNDS[1], high + step)
            else:
                new_low = min(_LO_BOUNDS[1], low + step)
                new_high = max(_HI_BOUNDS[0], high - step)
            if new_high - new_low < _MIN_GAP:
                logger.info("L7 no-op: deadband gap would collapse (%s)", signal)
                return L7Result(
                    success=True, changed=False, params=state["params"], signal=signal,
                )

            # Checkpoint before mutation
            if CONFIG.checkpoint_before_mutation:
                self.checkpoint.checkpoint("l7-deadband-tune")

            # Gate through the immutable evaluator
            deltas = {_LOW: new_low - low, _HIGH: new_high - high}
            eval_result = self.evaluator.evaluate({
                "description": "Meta-tune L4 success deadband",
                "target_files": [self.config.state_path],
                "diff": json.dumps(deltas, indent=2),
                "rationale": f"signal={signal} success_rate={stats['success_rate']:.2f}",
                "attempt": 1,
                "goal": "tune L4 optimizer params",
            })
            self.telemetry.record(TelemetryEvent(
                event_type="l7_evaluation",
                metadata={"decision": eval_result.decision, "signal": signal},
            ))

            if not eval_result.passed:
                logger.info("L7 proposal rejected: %s", eval_result.rationale[:60])
                state["history"].append({
                    "cycle": state["cycle"], "deltas": deltas,
                    "accepted": False, "signal": signal,
                })
                self._save_state(state)
                return L7Result(
                    success=True, changed=False, params=state["params"],
                    deltas=deltas, signal=signal,
                )

            state["params"][_LOW] = new_low
            state["params"][_HIGH] = new_high
            state["cycle"] += 1
            state["history"].append({
                "cycle": state["cycle"], "deltas": deltas,
                "accepted": True, "signal": signal,
            })
            self._save_state(state)

            # Mirror into runtime CONFIG
            setattr(CONFIG.l4, "target_success_low", new_low)
            setattr(CONFIG.l4, "target_success_high", new_high)
            logger.info("L7 tuned deadband -> [%.2f, %.2f] (%s)", new_low, new_high, signal)

            self.telemetry.record(TelemetryEvent(
                event_type="l7_complete",
                metadata={"changed": True, "signal": signal, "deltas": deltas},
            ))
            return L7Result(
                success=True, changed=True, params=state["params"],
                deltas=deltas, signal=signal,
            )

        except TimeoutError:
            raise
        except Exception as e:
            logger.exception("L7 meta-cog failed")
            self.telemetry.record(TelemetryEvent(
                event_type="l7_error", metadata={"error": str(e)},
            ))
            return L7Result(success=False, error=str(e))
