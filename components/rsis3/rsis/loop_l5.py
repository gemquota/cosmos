"""L5 — Strategy Evolution Loop.

Population-based evolution across sessions (slow feedback): maintains a
persistent population of strategy variants in `.rsis/strategies.json`,
scores fitness from outcome telemetry, selects elites, and mutates /
recombines to produce the next generation. Seeded from L3's derived
strategies when available.

Same invariants as the lower loops: evaluator gate is immutable,
checkpoint before mutation, bounded budget, failures cascade to the
next level.
"""

import json
import logging
import random
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

from rsis.checkpoint import CheckpointManager
from rsis.config import CONFIG, L2_TUNABLES
from rsis.evaluator import EvaluatorClient
from rsis.loop_l4 import OptimizerLoop
from rsis.memory import MemoryManager
from rsis.telemetry import TelemetryCollector, TelemetryEvent
from rsis.timeout import Budget, TimeoutError

logger = logging.getLogger(__name__)

# Strategy variant bounds — L5 owns the L2 improvement params (spec §1.4).
_L2_ATTEMPTS = L2_TUNABLES["l2.max_attempts"][:2]
_BUDGET_FACTOR = (0.5, 2.0)
_FOCI = ["general", "regressions", "memory", "speed"]


@dataclass
class L5Result:
    """Outcome of an L5 evolution cycle."""
    success: bool
    generation: int = 0
    population_size: int = 0
    elites_kept: int = 0
    variants_generated: int = 0
    avg_fitness: float = 0.0
    best_strategy: Optional[dict] = None
    error: Optional[str] = None


class EvolutionLoop:
    """Evolve a persistent population of strategy variants."""

    def __init__(
        self,
        telemetry: TelemetryCollector,
        memory: Optional[MemoryManager] = None,
        evaluator: Optional[EvaluatorClient] = None,
        checkpoint_mgr: Optional[CheckpointManager] = None,
    ):
        self.config = CONFIG.l5
        self.telemetry = telemetry
        self.memory = memory or MemoryManager(CONFIG.workspace_dir)
        self.evaluator = evaluator or EvaluatorClient()
        self.checkpoint = checkpoint_mgr or CheckpointManager(CONFIG.workspace_dir)
        self.state_path = Path(CONFIG.workspace_dir) / self.config.state_path
        self._rng = random.Random(self.config.seed)
        self._cycle_count = 0

    # ── State ──────────────────────────────────────────────────────

    def _load_state(self) -> dict:
        if self.state_path.exists():
            try:
                data = json.loads(self.state_path.read_text())
                data.setdefault("generation", 0)
                data.setdefault("population", [])
                return data
            except (json.JSONDecodeError, OSError) as e:
                logger.warning("Failed to read strategy state (%s); reseeding", e)
        return {"generation": 0, "population": []}

    def _save_state(self, state: dict) -> None:
        self.state_path.parent.mkdir(parents=True, exist_ok=True)
        self.state_path.write_text(json.dumps(state, indent=2) + "\n")

    # ── Population helpers ─────────────────────────────────────────

    @classmethod
    def _default_variant(cls, suffix: str) -> dict:
        return {
            "id": f"strategy-{suffix}",
            "params": {
                "l2_attempts": int(CONFIG.l2.max_improvement_attempts),
                "budget_factor": 1.0,
                "focus": "general",
            },
            "fitness": 0.0,
            "evals": 0,
        }

    def _seed_from_l3(self, population: list[dict]) -> list[dict]:
        """Seed the population from L3-derived strategies when available."""
        if len(population) >= self.config.population_size:
            return population

        existing_ids = {s["id"] for s in population}
        for node in self.memory.kg.get_strategies():
            if len(population) >= self.config.population_size:
                break
            sid = node.get("id", "strategy-l3")
            if sid in existing_ids:
                continue
            variant = EvolutionLoop._default_variant(sid.replace("strategy-", ""))
            focus = "regressions" if "regression" in node.get("description", "") else "general"
            variant["params"]["focus"] = focus
            variant["params"]["l2_attempts"] = max(
                _L2_ATTEMPTS[0], min(_L2_ATTEMPTS[1],
                                     int(node.get("optimal_iterations", 5)))
            )
            variant["params"]["budget_factor"] = 1.0
            population.append(variant)
            existing_ids.add(sid)

        while len(population) < self.config.population_size:
            variant = EvolutionLoop._default_variant(f"seed-{len(population)}")
            population.append(variant)
        return population

    def _score(self, variant: dict, stats: dict) -> float:
        """Fitness = outcome stats blended with prior fitness (smoothed)."""
        fresh = 0.6 * stats["success_rate"] + 0.4 * (stats["avg_score"] / 100.0)
        prior = variant.get("fitness", 0.0)
        blend = 0.3 + 0.7 * min(1.0, variant.get("evals", 0) / 5)
        return blend * fresh + (1.0 - blend) * prior

    def _mutate(self, variant: dict, gen: int) -> dict:
        p = dict(variant["params"])
        if self._rng.random() < self.config.mutation_rate:
            p["l2_attempts"] = max(_L2_ATTEMPTS[0], min(
                _L2_ATTEMPTS[1], p["l2_attempts"] + self._rng.choice([-1, 1])))
        if self._rng.random() < self.config.mutation_rate:
            p["budget_factor"] = round(max(_BUDGET_FACTOR[0], min(
                _BUDGET_FACTOR[1], p["budget_factor"] +
                self._rng.uniform(-0.2, 0.2))), 2)
        if self._rng.random() < self.config.mutation_rate * 0.5:
            p["focus"] = self._rng.choice([f for f in _FOCI if f != p["focus"]])
        return {
            "id": f"strategy-g{gen}-{variant['id'].split('-')[-1]}-{self._rng.randint(0, 999)}",
            "params": p,
            "fitness": 0.0,
            "evals": 0,
            "lineage": variant["id"],
        }

    def _recombine(self, a: dict, b: dict, gen: int) -> dict:
        pa, pb = a["params"], b["params"]
        p = {
            "l2_attempts": max(_L2_ATTEMPTS[0], min(
                _L2_ATTEMPTS[1], (pa["l2_attempts"] + pb["l2_attempts"]) // 2)),
            "budget_factor": round((pa["budget_factor"] + pb["budget_factor"]) / 2, 2),
            "focus": pa["focus"] if self._rng.random() < 0.5 else pb["focus"],
        }
        return {
            "id": f"strategy-g{gen}-cross-{self._rng.randint(0, 999)}",
            "params": p,
            "fitness": 0.0,
            "evals": 0,
            "lineage": f"{a['id']}x{b['id']}",
        }

    # ── Cycle ──────────────────────────────────────────────────────

    def run_cycle(self, budget: Optional[Budget] = None) -> L5Result:
        budget = budget or Budget(
            max_iterations=1, max_time_s=self.config.cycle_timeout_s,
            label="L5 evolution",
        )

        logger.info("L5 evolution cycle %d starting", self._cycle_count + 1)
        self.telemetry.record(TelemetryEvent(
            event_type="l5_start", metadata={"cycle": self._cycle_count},
        ))
        self._cycle_count += 1

        try:
            if not budget.tick():
                raise TimeoutError("L5 budget exhausted before starting")

            state = self._load_state()
            state["population"] = self._seed_from_l3(state["population"])
            stats = OptimizerLoop.aggregate_outcomes(
                self.memory, CONFIG.l4.outcome_window)

            # Score the current generation
            for variant in state["population"]:
                variant["fitness"] = self._score(variant, stats)
                variant["evals"] = int(variant.get("evals", 0)) + 1

            ranked = sorted(
                state["population"], key=lambda s: s["fitness"], reverse=True)
            avg_fitness = sum(s["fitness"] for s in ranked) / len(ranked) if ranked else 0.0

            elite_count = max(
                1, int(round(self.config.population_size * self.config.elite_fraction)))
            elites = ranked[:elite_count]
            next_gen = [dict(e) for e in elites]

            # Fill the rest with mutants / recombinants
            while len(next_gen) < self.config.population_size:
                gen = state["generation"] + 1
                if len(next_gen) < self.config.population_size - 1 and len(elites) >= 2:
                    a, b = self._rng.sample(elites, 2)
                    child = self._recombine(a, b, gen)
                else:
                    child = self._mutate(self._rng.choice(elites), gen)
                next_gen.append(child)

            # Checkpoint before mutating persistent state
            if CONFIG.checkpoint_before_mutation:
                self.checkpoint.checkpoint("l5-evolution")

            # Gate the new generation through the immutable evaluator
            eval_result = self.evaluator.evaluate({
                "description": "Evolve strategy population for next generation",
                "target_files": [self.config.state_path],
                "diff": json.dumps(
                    [s["params"] for s in next_gen[:5]], indent=2),
                "rationale": (
                    f"generation={state['generation'] + 1} "
                    f"avg_fitness={avg_fitness:.3f} stats={stats}"
                ),
                "attempt": 1,
                "goal": "evolve improvement strategies",
            })
            self.telemetry.record(TelemetryEvent(
                event_type="l5_evaluation",
                metadata={
                    "decision": eval_result.decision,
                    "score_avg": eval_result.score_avg,
                },
            ))

            if not eval_result.passed:
                logger.info("L5 generation rejected: %s", eval_result.rationale[:60])
                self._save_state(state)
                return L5Result(
                    success=True, generation=state["generation"],
                    population_size=len(state["population"]),
                    avg_fitness=avg_fitness,
                    best_strategy=ranked[0] if ranked else None,
                )

            state["generation"] += 1
            state["population"] = next_gen
            self._save_state(state)

            logger.info("L5 evolved generation %d (%d variants, %d elites)",
                        state["generation"], len(next_gen), len(elites))
            self.telemetry.record(TelemetryEvent(
                event_type="l5_complete",
                metadata={
                    "generation": state["generation"],
                    "population": len(next_gen),
                    "elites": len(elites),
                    "avg_fitness": round(avg_fitness, 3),
                    "best": ranked[0]["id"] if ranked else None,
                },
            ))
            return L5Result(
                success=True, generation=state["generation"],
                population_size=len(next_gen), elites_kept=len(elites),
                variants_generated=len(next_gen) - len(elites),
                avg_fitness=avg_fitness,
                best_strategy=ranked[0] if ranked else None,
            )

        except TimeoutError:
            raise
        except Exception as e:
            logger.exception("L5 evolution failed")
            self.telemetry.record(TelemetryEvent(
                event_type="l5_error", metadata={"error": str(e)},
            ))
            return L5Result(success=False, error=str(e))
