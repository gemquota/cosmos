---
type: "synthesis"
title: "RSIS3 LLM cycle 1 — rebirth #2 + bounded knowledge graph"
description: "LLM-driven cycle: rebirth #2, idempotent+bounded L3 redundancy flagging, KG edge dedup (14770→1847), all gates PASS"
tags: ["rsis3", "llm-cycle", "rebirth", "knowledge-graph", "l3", "cadence"]
timestamp: "2026-08-08T11:00:00Z"
status: "stable"
---

# RSIS3 LLM cycle 1 — rebirth #2 + bounded knowledge graph

First cycle where the inference engine was a real LLM session instead of the
deterministic heuristics: the engine analyzed the stalled cadence, authored
the fix, and drove the full L1–L9 batch on the fresh workspace.

## Rebirth #2

- `rack/rebirth.py` archived `pulse-001.json` + 10 `.rsis` state files to
  `rack/lifecycles/rebirth-002-20260808-105402/`; pulses reset to `001`;
  manifesto mode `analytical_only`.

## Root cause found (LLM inference)

- The hourly cadence stalled after cycle 1 because L3 `_refine_redundancies`
  re-flagged the **same** improvement pairs every cycle. The KG is a
  `MultiDiGraph`, so each re-flag added two parallel `flags_as_redundant`
  edges: edges grew ~475/cycle (6695 → 14770) while nodes stayed at 237.
- Every `add_edge`/`save` rewrote the growing JSON; cycles blew past the
  180s rhythm and the run de-synced (~15+ min between commits).

## Fix applied (engine-authored, evaluator-gated)

- `rsis/loop_l3.py`: skip pairs already flagged (`_flagged_redundancy_pairs`
  via `improvement_ids` on insight nodes), sort candidates by similarity,
  cap new flags at `max_redundancy_flags_per_cycle = 20`.
- `rsis/memory.py`: collapse identical parallel edges on KG load and save.
- Verdict: immutable evaluator PASS (1.0 × 5); 162/162 tests green; new
  `tests/test_loop_l3_idempotency.py` covers idempotency + cap + dedup.

## Measured outcome

- KG: 14,770 → 1,847 edges (file ~2.5MB → 382KB).
- L3 cycle 42: **0 redundancies** (was 237/cycle), ~11s runtime.
- L5 generation 60: best fitness 0.034 → **0.064** (first movement since gen 1).
- Self-assess health 0.835, 0 gaps, 3 trends; `check-practices` all PASS.

## Durable rules

- L3 redundancy flagging is a **one-time** verdict per improvement pair;
  re-flagging duplicates KG edges, not signal.
- The immutable evaluator gates standalone logic, not multi-file or
  in-loop diffs (added-line fragments lose enclosing context) — evaluate
  distilled logic, verify integration with tests.
- Cadence rhythm depends on bounded state; anything that grows the KG
  unboundedly will re-break the 3-minute cycle budget.
