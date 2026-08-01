---
type: concept
title: "Nine-Loop Hierarchy"
description: "RSIS3's original nine nested self-improvement loops — L1–L9 all implemented as bounded, evaluator-gated cycles"
tags: [concept, rsis3, architecture, loops, self-improvement]
timestamp: "2026-07-31T00:00:00Z"
status: stable
source: []
---

# Nine-Loop Hierarchy

## Summary

RSIS3 was conceived as **nine nested recursion loops**. The dashboard radar
and pulse scores (L1–L9) are this hierarchy, not RRP question-series axes.
Three loops are the original engine; L4–L9 were added as bounded,
evaluator-gated cycles. All nine loops are implemented.

## The Loops

| Loop | Name | Status | Responsibility |
|------|------|--------|----------------|
| L0 | Substrate | n/a | Workspace/artifact layer loops mutate — files, config, `.rsis` state |
| L1 | Execution | implemented | Per-task action loop: plan → tool calls → observe → retry |
| L2 | Planning / Improvement | implemented | Per-session improvement candidates, immutable-evaluator gate |
| L3 | Self-Direction / Evolution | implemented | Cross-session memory consolidation, strategy derivation, pruning |
| L4 | Optimizer | implemented | Fast-feedback tuning of bounded meta-parameters from outcomes |
| L5 | Evolution | implemented | Population-based strategy evolution (selection + mutation) |
| L6 | Identity | implemented | Tunes L3 evolution params (plateau timeout) |
| L7 | Meta-Cog | implemented | Tunes L4 optimizer params (window / thresholds) |
| L8 | Meta-Meta | implemented | Tunes L5 strategy params (mutation ↑ on stagnation, population ↓ on volatility) |
| L9 | MMM | implemented | Tunes L6 identity params (band widened on oscillation, narrowed on stall) |

## Tuning Ownership: the +3 Diagonal

Loop *k*+3 tunes loop *k*: L4→L1, L5→L2, L6→L3, L7→L4, L8→L5, L9→L6.
L1 and L2 tune nothing (pure consumers; their retry/refinement is
self-adaptation, not tuning). Each loop tunes exactly one target — no two
loops write the same key. L0 is the shared substrate, not a loop. L7–L9
are themselves untuned (no L10+), so the top three are fixed points: the
unbounded-recursion guard. Modification depth is exactly three meta-levels
(core L1–L3 → tuners L4–L6 → meta-tuners L7–L9), matching the max-3
self-modification depth limit in SPACE's recursive-depth analysis.

## Topology: Nested, Parallel, Overlapping

The nine loops are not one topology:

- **Nested** — L1 ⊂ L2 ⊂ L3 spawn/promote stack; L5 seeds from L3's KG
  strategies (one-way).
- **Parallel** — L4 (`.rsis/optimizer_state.json`), L5
  (`.rsis/strategies.json`), L6 (`.rsis/identity_state.json`), L7
  (`.rsis/metacog_state.json`), L8 (`.rsis/metameta_state.json`) and L9
  (`.rsis/mmm_state.json`) run with disjoint state; L7–L9 are parallel
  observers over the stack.
- **Overlapping** — shared reads (telemetry/KG: safe) and shared config
  writes (arbitrated by ownership partition: L4 owns `l1.*`, L5 owns
  `l2.max_attempts`). Startup `load_config()` is the single injection point
  where tuned state reaches L1/L2.

## Invariants (apply to every implemented loop)

- Evaluator is immutable — never in-scope for self-improvement
- Checkpoint before every mutation; rollback always possible
- Loops terminate — bounded budgets at every level
- Failures cascade up: L1 → L2 → L3 → L4 → L5 → L8 (meta-tuners observe)
- Memory is hierarchical: git (truth) → KG (insight) → vectors (retrieval)

## L8 / L9 Details

- **L8 Meta-Meta** (`python -m rsis metameta`, `.rsis/metameta_state.json`):
  reads L5's generation-fitness history; `raise_mutation` when gains across
  `stagnation_window` generations stay under ε; `shrink_population` when
  best-fitness oscillates across `volatility_window` generations.
- **L9 MMM** (`python -m rsis mmm`, `.rsis/mmm_state.json`): reads L6's
  tuning history; `widen` when L6 alternates shrink/grow (band looser so L6
  stops thrashing); `narrow` when L6 stalls while success is low (band
  tighter so L6 reacts sooner).

## Related

- [[wiki/concepts/triad-architecture|Triad Architecture]]
- [[wiki/syntheses/cosmos-dashboard-mykb-integration|Dashboard & MyKB Integration Patterns]]
- [[wiki/index|Wiki Index]]
