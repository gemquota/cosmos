---
type: "synthesis"
title: "RSIS3 LLM 20-cycle run — rebirth #2, bounded KG, stable rhythm"
description: "20 LLM-driven cycles (L3 #43–62) after rebirth #2: KG flat at 1847 edges, then pruned to 475; fitness 0.064; all gates PASS"
tags: ["rsis3", "llm-cycle", "rebirth", "cadence", "knowledge-graph", "20-cycles"]
timestamp: "2026-08-08T11:45:00Z"
status: "stable"
---

# RSIS3 LLM 20-cycle run — rebirth #2, bounded KG, stable rhythm

Twenty consecutive cycles driven with a live LLM as the inference engine,
each a full L1–L9 batch (`launch --cycles 1 --goal-space-cycle 1`), run
after rebirth #2. Every cycle committed individually.

## Per-cycle summary

| # | L3 | rc | best fitness | KG edges | flag edges | commit |
|---|----|----|--------------|----------|------------|--------|
| 1  | 43 | 0 | 0.064 | 1847 | 1846 | c43927ea |
| 2  | 44 | 0 | 0.064 | 1847 | 1846 | ed9d1c48 |
| 3  | 45 | 0 | 0.064 | 1847 | 1846 | fc6e6abb |
| 4  | 46 | 0 | 0.064 | 1847 | 1846 | 57188eb7 |
| 5  | 47 | 0 | 0.064 | 1847 | 1846 | 66c3bfab |
| 6  | 48 | 0 | 0.064 | 1847 | 1846 | d9c8cabe |
| 7  | 49 | 0 | 0.064 | 1847 | 1846 | c5e00c6f |
| 8  | 50 | 0 | 0.064 | 1847 | 1846 | f5e46ba5 |
| 9  | 51 | 0 | 0.064 | 1847 | 1846 | 1d5335e0 |
| 10 | 52 | 0 | 0.064 | 1847 | 1846 | 87d4f9a5 |
| 11 | 53 | 0 | 0.064 | 1847 | 1846 | 063363fa |
| 12 | 54 | 0 | 0.064 | 1847 | 1846 | a3736ea4 |
| 13 | 55 | 0 | 0.064 | 1847 | 1846 | 70619b02 |
| 14 | 56 | 0 | 0.064 | 1847 | 1846 | 190a70d0 |
| 15 | 57 | 0 | 0.064 | 1847 | 1846 | f72a74c9 |
| 16 | 58 | 0 | 0.064 | 1847 | 1846 | e5fb110a |
| 17 | 59 | 0 | 0.064 | 1847 | 1846 | b5d20f72 |
| 18 | 60 | 0 | 0.064 | 1847 | 1846 | e64d637d |
| 19 | 61 | 0 | 0.064 | 1847 | 1846 | (folded into #20) |
| 20 | 62 | 0 | 0.064 | 1847 | 1846 | af799b59 |

## Inference findings (the LLM part)

- **KG growth is dead**: the idempotent + bounded flagging fix held for all
  20 cycles — edges flat at 1847 (0 growth), cycles ~1.5 min each.
- **Stale flag edges found & pruned**: 1846 flag edges referenced pairings
  superseded by later pre-fix cycles. Pruned on save against the
  `improvement_ids` attr (source of truth): 1846 → **474** (237 pairs × 2),
  total edges 1847 → **475**. Gated by the immutable evaluator (PASS 1.0×5),
  163/163 tests green.
- **Fitness plateau is an information signal, not a bug**: L5 best stayed at
  0.064 because deterministic L2 applied no new improvements — the only
  real fitness movement came from the authored fix (0.034 → 0.064). Real
  fitness evolution requires real code changes per cycle.
- **`rsis/tools/base.py` stub flag is a false positive**: `Tool.run` raising
  `NotImplementedError` is an abstract-method contract, not a missing
  implementation — pulse-001's stub scan should treat abstract methods as
  intentional.
- **Steady state**: cycle 19 committed nothing new (all deterministic
  outputs identical) — the system reached a fixed point; further movement
  needs new inference, not more repetitions.

## Durable rules

- Redundancy flagging is one-time per improvement pair; flag edges must be
  pruned against the node's current pair, not accumulated.
- A flat fitness plateau with zero applied improvements means the loop is
  converged; inject real changes (LLM-authored candidates) to move it.
- Rebirth archives state but must not resurrect unbounded-growth bugs in
  the next lifecycle.
