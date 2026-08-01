"""L8 — Meta-Meta Loop.

Tunes L5 strategy params (the +3 diagonal: L8 → L5). Observes the
generation-fitness history in `.rsis/strategies.json`: on stagnation (no
best-fitness gain across generations) it raises the L5 mutation rate to
explore; on volatility (best fitness oscillating between generations) it
shrinks the L5 population size to damp the swings. Evaluator-gated,
checkpointed, persisted to `.rsis/metameta_state.json`.
"""

import json
import logging
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

from rsis.checkpoint import CheckpointManager
from rsis.config import CONFIG, L5_TUNABLES
from rsis.evaluator import EvaluatorClient
from rsis.memory import MemoryManager
from rsis.telemetry import TelemetryCollector, TelemetryEvent
from rsis.timeout import Budget, TimeoutError

logger = logging.getLogger(__name__)

_MUTATION = "l5.mutation_rate"
_POPULATION = "l5.population_size"
_MUT_BOUNDS = L5_TUNABLES[_MUTATION][:2]
_POP_BOUNDS = L5_TUNABLES[_POPULATION][:2]


@dataclass
class L8Result:
    """Outcome of an L8 meta-meta cycle."""
    success: bool
    changed: bool = False
    deltas: dict = field(default_factory=dict)
    params: dict = field(default_factory=dict)
    signal: Optional[str] = None
    error: Optional[str] = None


class MetaMetaLoop:
    """Meta-tune the L5 strategy loop's exploration profile."""

    def __init__(
        self,
        telemetry: TelemetryCollector,
        memory: Optional[MemoryManager] = None,
        evaluator: Optional[EvaluatorClient] = None,
        checkpoint_mgr: Optional[CheckpointManager] = None,
    ):
        self.config = CONFIG.l8
        self.telemetry = telemetry
        self.memory = memory or MemoryManager(CONFIG.workspace_dir)
        self.evaluator = evaluator or EvaluatorClient()
        self.checkpoint = checkpoint_mgr or CheckpointManager(CONFIG.workspace_dir)
        self.state_path = Path(CONFIG.workspace_dir) / self.config.state_path
        self.l5_state_path = Path(CONFIG.workspace_dir) / CONFIG.l5.state_path
        self._cycle_count = 0

    # ── State ──────────────────────────────────────────────────────

    def _default_params(self) -> dict:
        params = {}
        for name, (_lo, _hi, path, _kind) in L5_TUNABLES.items():
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
                logger.warning("Failed to read meta-meta state (%s); resetting", e)
        return {"params": self._default_params(), "history": [], "cycle": 0}

    def _save_state(self, state: dict) -> None:
        self.state_path.parent.mkdir(parents=True, exist_ok=True)
        self.state_path.write_text(json.dumps(state, indent=2) + "\n")

    # ── Signal ─────────────────────────────────────────────────────

    def _l5_history(self) -> list[dict]:
        if not self.l5_state_path.exists():
            return []
        try:
            data = json.loads(self.l5_state_path.read_text())
            return data.get("history", [])
        except (json.JSONDecodeError, OSError) as e:
            logger.warning("Failed to read L5 state: %s", e)
            return []

    def _signal(self, history: list[dict]) -> Optional[str]:
        accepted = [h for h in history if h.get("accepted")]
        recent = accepted[-self.config.volatility_window:]
        if len(recent) >= 3:
            deltas = []
            for prev, cur in zip(recent, recent[1:]):
                d = cur.get("best_fitness", 0.0) - prev.get("best_fitness", 0.0)
                if d > self.config.fitness_epsilon:
                    deltas.append(1)
                elif d < -self.config.fitness_epsilon:
                    deltas.append(-1)
                else:
                    deltas.append(0)
            signs = [d for d in deltas if d != 0]
            if len(set(signs)) == 2 and all(
                signs[i] != signs[i + 1] for i in range(len(signs) - 1)
            ):
                return "shrink_population"

        if len(accepted) >= self.config.stagnation_window:
            last_n = accepted[-self.config.stagnation_window:]
            gains = [
                last_n[i + 1].get("best_fitness", 0.0)
                - last_n[i].get("best_fitness", 0.0)
                for i in range(len(last_n) - 1)
            ]
            if all(g < self.config.fitness_epsilon for g in gains):
                return "raise_mutation"
        return None

    # ── Cycle ──────────────────────────────────────────────────────

    def run_cycle(self, budget: Optional[Budget] = None) -> L8Result:
        budget = budget or Budget(
            max_iterations=1, max_time_s=self.config.cycle_timeout_s,
            label="L8 meta-meta",
        )

        logger.info("L8 meta-meta cycle %d starting", self._cycle_count + 1)
        self.telemetry.record(TelemetryEvent(
            event_type="l8_start", metadata={"cycle": self._cycle_count},
        ))
        self._cycle_count += 1

        try:
            if not budget.tick():
                raise TimeoutError("L8 budget exhausted before starting")

            history = self._l5_history()
            signal = self._signal(history)

            state = self._load_state()
            if signal is None:
                self.telemetry.record(TelemetryEvent(
                    event_type="l8_complete", metadata={"changed": False},
                ))
                return L8Result(success=True, changed=False, params=state["params"])

            mutation = float(state["params"].get(_MUTATION, _MUT_BOUNDS[0]))
            population = int(state["params"].get(_POPULATION, _POP_BOUNDS[0]))
            deltas = {}
            if signal == "raise_mutation" and mutation < _MUT_BOUNDS[1]:
                deltas[_MUTATION] = min(self.config.mutation_step, _MUT_BOUNDS[1] - mutation)
            if signal == "shrink_population" and population > _POP_BOUNDS[0]:
                deltas[_POPULATION] = -min(self.config.population_step, population - _POP_BOUNDS[0])
            if not deltas:
                logger.info("L8 no-op: %s already at bound", signal)
                self.telemetry.record(TelemetryEvent(
                    event_type="l8_complete", metadata={"changed": False},
                ))
                return L8Result(
                    success=True, changed=False, params=state["params"], signal=signal,
                )

            # Checkpoint before mutation
            if CONFIG.checkpoint_before_mutation:
                self.checkpoint.checkpoint("l8-l5-tune")

            # Gate through the immutable evaluator
            eval_result = self.evaluator.evaluate({
                "description": "Meta-tune L5 strategy loop from generation fitness history",
                "target_files": [self.config.state_path],
                "diff": json.dumps(deltas, indent=2),
                "rationale": f"signal={signal} history_len={len(history)}",
                "attempt": 1,
                "goal": "tune L5 strategy params",
            })
            self.telemetry.record(TelemetryEvent(
                event_type="l8_evaluation",
                metadata={"decision": eval_result.decision, "signal": signal},
            ))

            if not eval_result.passed:
                logger.info("L8 proposal rejected: %s", eval_result.rationale[:60])
                state["history"].append({
                    "cycle": state["cycle"], "deltas": deltas,
                    "accepted": False, "signal": signal,
                })
                self._save_state(state)
                return L8Result(
                    success=True, changed=False, params=state["params"],
                    deltas=deltas, signal=signal,
                )

            new_mutation = max(
                _MUT_BOUNDS[0], min(_MUT_BOUNDS[1],
                                     mutation + deltas.get(_MUTATION, 0.0)))
            new_population = max(
                _POP_BOUNDS[0], min(_POP_BOUNDS[1],
                                     population + deltas.get(_POPULATION, 0)))
            state["params"][_MUTATION] = new_mutation
            state["params"][_POPULATION] = new_population
            state["cycle"] += 1
            state["history"].append({
                "cycle": state["cycle"], "deltas": deltas,
                "accepted": True, "signal": signal,
            })
            self._save_state(state)

            # Mirror into runtime CONFIG
            setattr(CONFIG.l5, "mutation_rate", new_mutation)
            setattr(CONFIG.l5, "population_size", new_population)
            logger.info("L8 tuned l5: mutation_rate=%.2f population_size=%d (%s)",
                        new_mutation, new_population, signal)

            self.telemetry.record(TelemetryEvent(
                event_type="l8_complete",
                metadata={"changed": True, "signal": signal, "deltas": deltas},
            ))
            return L8Result(
                success=True, changed=True, params=state["params"],
                deltas=deltas, signal=signal,
            )

        except TimeoutError:
            raise
        except Exception as e:
            logger.exception("L8 meta-meta failed")
            self.telemetry.record(TelemetryEvent(
                event_type="l8_error", metadata={"error": str(e)},
            ))
            return L8Result(success=False, error=str(e))
