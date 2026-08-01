"""L9 — MMM (Meta-Meta-Meta) Loop.

Tunes L6 identity params (the +3 diagonal: L9 → L6). Observes L6's tuning
history in `.rsis/identity_state.json`: on oscillation (L6 flipping shrink /
grow) it widens the identity band (lower `shrink_below`, raise `grow_above`)
to stop the thrash; on stall (L6 silent or rejected while success is low) it
narrows the band so L6 reacts sooner. Evaluator-gated, checkpointed,
persisted to `.rsis/mmm_state.json`.
"""

import json
import logging
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

from rsis.checkpoint import CheckpointManager
from rsis.config import CONFIG, L6_TUNABLES
from rsis.evaluator import EvaluatorClient
from rsis.loop_l4 import OptimizerLoop
from rsis.memory import MemoryManager
from rsis.telemetry import TelemetryCollector, TelemetryEvent
from rsis.timeout import Budget, TimeoutError

logger = logging.getLogger(__name__)

_LOW = "l6.shrink_below"
_HIGH = "l6.grow_above"
_LO_BOUNDS = L6_TUNABLES[_LOW][:2]
_HI_BOUNDS = L6_TUNABLES[_HIGH][:2]
_MIN_GAP = 0.05


@dataclass
class L9Result:
    """Outcome of an L9 MMM cycle."""
    success: bool
    changed: bool = False
    deltas: dict = field(default_factory=dict)
    params: dict = field(default_factory=dict)
    signal: Optional[str] = None
    error: Optional[str] = None


class MMMLoop:
    """Meta-tune the L6 identity loop's sensitivity band."""

    def __init__(
        self,
        telemetry: TelemetryCollector,
        memory: Optional[MemoryManager] = None,
        evaluator: Optional[EvaluatorClient] = None,
        checkpoint_mgr: Optional[CheckpointManager] = None,
    ):
        self.config = CONFIG.l9
        self.telemetry = telemetry
        self.memory = memory or MemoryManager(CONFIG.workspace_dir)
        self.evaluator = evaluator or EvaluatorClient()
        self.checkpoint = checkpoint_mgr or CheckpointManager(CONFIG.workspace_dir)
        self.state_path = Path(CONFIG.workspace_dir) / self.config.state_path
        self.l6_state_path = Path(CONFIG.workspace_dir) / CONFIG.l6.state_path
        self._cycle_count = 0

    # ── State ──────────────────────────────────────────────────────

    def _default_params(self) -> dict:
        params = {}
        for name, (_lo, _hi, path, _kind) in L6_TUNABLES.items():
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
                logger.warning("Failed to read MMM state (%s); resetting", e)
        return {"params": self._default_params(), "history": [], "cycle": 0}

    def _save_state(self, state: dict) -> None:
        self.state_path.parent.mkdir(parents=True, exist_ok=True)
        self.state_path.write_text(json.dumps(state, indent=2) + "\n")

    # ── Signal ─────────────────────────────────────────────────────

    def _l6_history(self) -> list[dict]:
        if not self.l6_state_path.exists():
            return []
        try:
            data = json.loads(self.l6_state_path.read_text())
            return data.get("history", [])
        except (json.JSONDecodeError, OSError) as e:
            logger.warning("Failed to read L6 state: %s", e)
            return []

    def _signal(self, history: list[dict], stats: dict) -> Optional[str]:
        accepted = [h for h in history if h.get("accepted")]
        recent = accepted[-self.config.oscillation_window:]
        if len(recent) >= 2:
            signs = []
            for entry in recent:
                delta = entry.get("delta") or 0
                signs.append(1 if delta > 0 else (-1 if delta < 0 else 0))
            non_zero = [s for s in signs if s != 0]
            if len(set(non_zero)) == 2 and all(
                non_zero[i] != non_zero[i + 1] for i in range(len(non_zero) - 1)
            ):
                return "widen"

        recent_all = history[-self.config.stall_window:] if self.config.stall_window else []
        if len(recent_all) >= self.config.stall_window and not any(
            h.get("accepted") for h in recent_all
        ):
            low = self._load_state()["params"].get(_LOW, _LO_BOUNDS[0])
            if stats["success_rate"] < float(low):
                return "narrow"
        return None

    # ── Cycle ──────────────────────────────────────────────────────

    def run_cycle(self, budget: Optional[Budget] = None) -> L9Result:
        budget = budget or Budget(
            max_iterations=1, max_time_s=self.config.cycle_timeout_s,
            label="L9 MMM",
        )

        logger.info("L9 MMM cycle %d starting", self._cycle_count + 1)
        self.telemetry.record(TelemetryEvent(
            event_type="l9_start", metadata={"cycle": self._cycle_count},
        ))
        self._cycle_count += 1

        try:
            if not budget.tick():
                raise TimeoutError("L9 budget exhausted before starting")

            stats = OptimizerLoop.aggregate_outcomes(
                self.memory, CONFIG.l4.outcome_window)
            history = self._l6_history()
            signal = self._signal(history, stats)

            state = self._load_state()
            if signal is None:
                self.telemetry.record(TelemetryEvent(
                    event_type="l9_complete", metadata={"changed": False},
                ))
                return L9Result(success=True, changed=False, params=state["params"])

            low = float(state["params"].get(_LOW, _LO_BOUNDS[0]))
            high = float(state["params"].get(_HIGH, _HI_BOUNDS[0]))
            step = self.config.band_step
            if signal == "widen":
                new_low = max(_LO_BOUNDS[0], low - step)
                new_high = min(_HI_BOUNDS[1], high + step)
            else:
                new_low = min(_LO_BOUNDS[1], low + step)
                new_high = max(_HI_BOUNDS[0], high - step)
            if new_high - new_low < _MIN_GAP:
                logger.info("L9 no-op: band gap would collapse (%s)", signal)
                return L9Result(
                    success=True, changed=False, params=state["params"], signal=signal,
                )

            # Checkpoint before mutation
            if CONFIG.checkpoint_before_mutation:
                self.checkpoint.checkpoint("l9-l6-tune")

            # Gate through the immutable evaluator
            deltas = {_LOW: new_low - low, _HIGH: new_high - high}
            eval_result = self.evaluator.evaluate({
                "description": "Meta-tune L6 identity band from L6 tuning history",
                "target_files": [self.config.state_path],
                "diff": json.dumps(deltas, indent=2),
                "rationale": f"signal={signal} success_rate={stats['success_rate']:.2f}",
                "attempt": 1,
                "goal": "tune L6 identity params",
            })
            self.telemetry.record(TelemetryEvent(
                event_type="l9_evaluation",
                metadata={"decision": eval_result.decision, "signal": signal},
            ))

            if not eval_result.passed:
                logger.info("L9 proposal rejected: %s", eval_result.rationale[:60])
                state["history"].append({
                    "cycle": state["cycle"], "deltas": deltas,
                    "accepted": False, "signal": signal,
                })
                self._save_state(state)
                return L9Result(
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
            setattr(CONFIG.l6, "shrink_below", new_low)
            setattr(CONFIG.l6, "grow_above", new_high)
            logger.info("L9 tuned l6 band -> [%.2f, %.2f] (%s)",
                        new_low, new_high, signal)

            self.telemetry.record(TelemetryEvent(
                event_type="l9_complete",
                metadata={"changed": True, "signal": signal, "deltas": deltas},
            ))
            return L9Result(
                success=True, changed=True, params=state["params"],
                deltas=deltas, signal=signal,
            )

        except TimeoutError:
            raise
        except Exception as e:
            logger.exception("L9 MMM failed")
            self.telemetry.record(TelemetryEvent(
                event_type="l9_error", metadata={"error": str(e)},
            ))
            return L9Result(success=False, error=str(e))
