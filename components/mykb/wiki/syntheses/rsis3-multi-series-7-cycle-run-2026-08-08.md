---
type: "synthesis"
title: "RSIS3 multi-series 7-cycle run — SPACE series 1–7 goal sourcing"
description: "Expanded from-space goal sourcing across all 7 SPACE series; per-series real improvements; 56 executions, 0 failed"
tags: ["rsis3", "space", "series", "goal-sourcing", "llm-cycle", "knowledge-graph"]
timestamp: "2026-08-08T13:15:00Z"
status: "stable"
---

# RSIS3 multi-series 7-cycle run — SPACE series 1–7 goal sourcing

Expanded the SPACE integration from "always the first artifact of series 1"
to the whole 326-probe framework: every cycle's L2 goal now sources from a
rotating series (1..7), just like the original series-1 goal but across all
seven series.

## Expansion (code)

- `SpaceSpec.candidate_goals(limit, series_id=N)` — series-filtered goals.
- `RSIS_SPACE_SERIES` env selects the series; `launch` and `run-batch.sh`
  rotate per cycle (`(i-1) % 7 + 1`); `loops.yml` exports it per CI cycle.
- `plan_batch` now sources `from-space` for **every** cycle (was cycle 1
  only), so a full batch covers all series by construction.
- Goal strings carry `series <N>` / `question <Q>`; telemetry
  `l2_start.goal` traces each run to its spec artifact.

## Per-series real improvements (LLM inference, evaluator-gated)

| Series | Artifact | Improvement | Eval |
|--------|----------|-------------|------|
| 1 | abstraction_level | KG growth fix (idempotent flagging + edge dedup) — prior run | PASS |
| 2 | edge_cases | KG load hardening (skip malformed nodes/edges) + `get_edges` in-edge traversal bugfix | PASS |
| 3 | association_types | `KNOWN_RELS` relationship vocabulary validation on `add_edge` | PASS |
| 4 | decision_points | (machinery — no code change needed this pass) | — |
| 5 | availability_targets | atomic KG save (tmp + `os.replace`, no truncated KG on crash) | PASS |
| 6 | communication_patterns | batched `add_edges` (one save per batch) + docs §10 | PASS |
| 7 | deployment_process | `loops.yml` + `run-batch.sh` series rotation wiring | PASS |

All four new improvements recorded as `improvement-278..281`; 169/169 tests
green (new `tests/test_kg_robustness.py`).

## Measured outcome

- 7-cycle batch: **56 executions, 0 failed**; telemetry shows all **7/7
  series** with their first artifact (abstraction_level, edge_cases,
  association_types, decision_points, availability_targets,
  communication_patterns, deployment_process).
- KG stable at 475 edges / 282 nodes across the run.
- Self-assess health 0.833, 0 gaps; `check-practices` all PASS.

## Durable rules

- Goal diversity comes from series rotation, not artifact repetition: one
  series per cycle covers the framework in 7-cycle blocks.
- The immutable evaluator gates each per-series improvement independently;
  tests cover the integration (KG robustness, batch edges, atomic save).
- `get_edges(node_id)` must traverse `edges()` + `in_edges()`, not
  `edges(None, node_id, ...)`.
