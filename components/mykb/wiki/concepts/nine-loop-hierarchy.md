---
type: concept
title: "Nine-Loop Hierarchy"
description: "RSIS3's original nine nested self-improvement loops — L1–L5 implemented, L6–L9 hypothetical"
tags: [concept, rsis3, architecture, loops, self-improvement]
timestamp: "2026-07-31T00:00:00Z"
status: stable
source: []
---

# Nine-Loop Hierarchy

## Summary

RSIS3 was conceived as **nine nested recursion loops**. The dashboard radar
and pulse scores (L1–L9) are this hierarchy, not RRP question-series axes.
Three loops are the original engine; L4 and L5 were added as bounded,
evaluator-gated cycles; L6–L9 remain hypothetical labels.

## The Loops

| Loop | Name | Status | Responsibility |
|------|------|--------|----------------|
| L1 | Execution | implemented | Per-task action loop: plan → tool calls → observe → retry |
| L2 | Planning / Improvement | implemented | Per-session improvement candidates, immutable-evaluator gate |
| L3 | Self-Direction / Evolution | implemented | Cross-session memory consolidation, strategy derivation, pruning |
| L4 | Optimizer | implemented | Fast-feedback tuning of bounded meta-parameters from outcomes |
| L5 | Evolution | implemented | Population-based strategy evolution (selection + mutation) |
| L6 | Identity | hypothetical | Tunes L3 evolution params (patience / timeout) |
| L7 | Meta-Cog | hypothetical | Tunes L4 optimizer params (window / thresholds) |
| L8 | Meta-Meta | hypothetical | Tunes L5 strategy params (population / mutation) |
| L9 | MMM | hypothetical | Tunes L6 identity params (the recursion guard) |

## Tuning Ownership: the +3 Diagonal

Loop *k*+3 tunes loop *k*: L4→L1, L5→L2, L6→L3, L7→L4, L8→L5, L9→L6.
Each loop tunes exactly one target — no two loops write the same key. L7–L9
are themselves untuned (no L10+), so the top three are fixed points: the
unbounded-recursion guard. Modification depth is exactly three meta-levels
(core L1–L3 → tuners L4–L6 → meta-tuners L7–L9), matching the max-3
self-modification depth limit in SPACE's recursive-depth analysis.

## Topology: Nested, Parallel, Overlapping

The nine loops are not one topology:

- **Nested** — L1 ⊂ L2 ⊂ L3 spawn/promote stack; L5 seeds from L3's KG
  strategies (one-way); L7–L9 would nest above L5.
- **Parallel** — L4 (`.rsis/optimizer_state.json`) and L5
  (`.rsis/strategies.json`) run with disjoint state; L6 (Meta-Cog) would be a
  parallel observer.
- **Overlapping** — shared reads (telemetry/KG: safe) and shared config
  writes (arbitrated by ownership partition: L4 owns `l1.*`, L5 owns
  `l2.max_attempts`). Startup `load_config()` is the single injection point
  where tuned state reaches L1/L2.

## Invariants (apply to every implemented loop)

- Evaluator is immutable — never in-scope for self-improvement
- Checkpoint before every mutation; rollback always possible
- Loops terminate — bounded budgets at every level
- Failures cascade up: L1 → L2 → L3 → L4 → L5
- Memory is hierarchical: git (truth) → KG (insight) → vectors (retrieval)

## Related

- [[wiki/concepts/triad-architecture|Triad Architecture]]
- [[wiki/syntheses/cosmos-dashboard-mykb-integration|Dashboard & MyKB Integration Patterns]]
- [[wiki/index|Wiki Index]]
