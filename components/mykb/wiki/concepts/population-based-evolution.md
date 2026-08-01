---
type: "concept"
title: "Population-Based Evolution"
description: "Elitism, mutation, and recombination over a persistent population of strategy variants — L5's engine"
tags: [evolution, population, elitism, mutation, rsis3]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: []
---

# Population-Based Evolution

## Summary
Population-based evolution maintains a set of candidate strategies, scores them against outcome telemetry, keeps the elites, and produces the next generation by mutation and recombination. Unlike gradient methods it needs no differentiability — only a fitness signal. RSIS3's L5 uses it to evolve improvement strategies (`l2.max_attempts`, budget factor, focus) across sessions.

## Details
- **Cycle**: score → rank → keep elites → mutate/recombine to fill population → evaluator gate → persist generation.
- **Fitness**: a blend of fresh outcome stats and prior fitness, smoothed by evaluation count so early generations don't overreact.
- **Seeding**: the population is seeded from L3-derived strategy nodes in the knowledge graph, then padded with defaults.
- **Telemetry**: every generation writes `l5_complete` with generation, population, elites, and avg/best fitness — the history L8 reads.
- Worked example: 8 variants → top 4 elites → 4 children (mutated l2_attempts or recombined focus) → generation 2.

## Related
- [[wiki/concepts/fitness-stagnation|Fitness Stagnation]] — when evolution plateaus, L8 raises mutation
- [[wiki/concepts/meta-parameter-tuning|Meta-Parameter Tuning]] — L8 tunes this loop's params
- [[wiki/concepts/exploration-exploitation|Exploration-Exploitation]] — mutation explores, elitism exploits
- [[wiki/concepts/nine-loop-hierarchy|Nine-Loop Hierarchy]] — L5's place in the stack