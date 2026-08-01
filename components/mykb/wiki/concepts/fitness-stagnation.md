---
type: "concept"
title: "Fitness Stagnation"
description: "The plateau signal: generations stop improving, and the meta-tuner responds by raising mutation"
tags: [stagnation, plateau, evolution, rsis3, meta-tuning]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: []
---

# Fitness Stagnation

## Summary
Fitness stagnation is the state where a population's best fitness stops improving across generations — a plateau that signals the search is stuck in a local region. It is a *signal*, not a failure: the correct response is to explore more. In RSIS3, L8 watches L5's generation-fitness history and, when gains stay under an epsilon for `stagnation_window` generations, raises `l5.mutation_rate` to break out of the plateau.

## Details
- **Detection**: compare consecutive `best_fitness` values in accepted generations; if all gains < ε (default 0.005) over the window, raise mutation.
- **Response**: `mutation_rate += mutation_step`, clamped to the registry bounds — more exploration, same elites.
- **Why it works**: stagnation means the current variation operator is too weak to escape; stronger mutation widens the search radius.
- **Guardrails**: the response is evaluator-gated and checkpointed; at the bound it becomes a no-op rather than violating the registry.
- Contrast with [[wiki/concepts/tuning-oscillation|Tuning Oscillation]] — the other meta-tuner signal, which is about instability rather than plateau.

## Related
- [[wiki/concepts/population-based-evolution|Population-Based Evolution]] — the loop being tuned
- [[wiki/concepts/tuning-oscillation|Tuning Oscillation]] — the complementary signal
- [[wiki/concepts/exploration-exploitation|Exploration-Exploitation]] — the trade-off being rebalanced
- [[wiki/concepts/meta-parameter-tuning|Meta-Parameter Tuning]] — how the adjustment is applied