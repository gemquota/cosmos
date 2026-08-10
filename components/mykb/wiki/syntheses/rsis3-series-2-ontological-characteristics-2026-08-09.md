---
type: "synthesis"
title: "RSIS3 series 2 completion — Ontological Characteristics (entity lifecycles + constraints)"
description: "Completed SPACE series 2 (Ontological Characteristics): goal-sourced L1–L9 cycle run plus the executable lifecycle/constraint registry (rsis/entity_states.py) wired into the convergence proposal path, with 11 new tests"
tags: ["rsis3", "space", "series-2", "ontology", "lifecycle", "constraints", "goal-sourcing"]
timestamp: "2026-08-09T02:15:00Z"
status: "stable"
---

# RSIS3 series 2 — Ontological Characteristics (complete)

Series 2 of the 326-probe framework (Ontological Characteristics) is now
complete: the goal-sourced cycle ran through the full L1–L9 stack, and the
two series-2 artifacts that described real gaps were implemented as an
executable registry.

## Cycle run

- 2-cycle `launch` batch (series rotation 1..7): **16 executions, 0
  failed**, rc=0; cycle 2 sourced `edge_cases` (series 2, question 2.5.1)
  through the full loop stack. `edge_cases` itself was already implemented
  in the 2026-08-08 run (KG load hardening + `get_edges` fix), so L2
  deferred deterministically.

## Implemented (improvement-282/283)

- **entity_lifecycles** (q 2.3.3 — "stateful lifecycle with defined states
  and transition rules"): `rsis/entity_states.py` defines states and
  allowed transitions for the runtime entities — session
  (active→completed/abandoned), proposal (proposed→applied/rejected),
  candidate (generated→evaluated→applied/rejected), checkpoint
  (created→restored/superseded), strategy (evolved→active/retired).
  `transition()` rejects illegal moves with `EntityStateError`.
- **entity_constraints** (q 2.4.3 — "moderate constraints, required fields
  and validity rules"): `validate_record()` enforces required fields per
  entity plus validity rules (proposal needs `loop`/`proposed_loop`;
  candidate `target_files` and strategy `population` must be lists).
- **Wiring**: convergence proposals start in state `proposed` and are
  validated before write; `_mark_applied` validates the applied record and
  blocks duplicate applications of the same loop+generation (the
  proposed→applied transition happens at most once).
- **Tests**: `tests/test_entity_states.py` — 11 cases covering transitions,
  invalid moves, record constraints, and proposal-path integration.
  217/217 suite green; `check-practices` all PASS.

## Artifact audit (15 series-2 artifacts)

- Already satisfied by prior work: edge_cases, entity_cardinality
  (one-to-many), entity_composition (containment), entity_categories /
  entity_granularity / entity_core_peripheral (conceptual), systemic_boundaries
  (allowlist + origin guard), external_actors, entity_reclassification
  (no changes), entity_gaps (self-assessment), entity_list / entity_attributes
  (conceptual record shapes).
- Implemented now: entity_lifecycles, entity_constraints.

## Durable rules

- Runtime entities are stateful: never mutate an entity across an undefined
  transition; enforce via `rsis.entity_states` before writing records.
- A convergence retune applies at most once per (loop, generation) — the
  `applied.jsonl` ledger is append-only and deduplicated.
- Series rotation covers the framework in 7-cycle blocks; a series is
  "complete" when its first artifact is implemented and its remaining
  artifacts are audited against the codebase.

## Related

- [[wiki/syntheses/rsis3-multi-series-7-cycle-run-2026-08-08|RSIS3 multi-series 7-cycle run — SPACE series 1–7 goal sourcing]]
- [[wiki/syntheses/rsis3-roadmap-sequels-2-3-2026-08-09|RSIS3 roadmap sequels II–III (Phases 6–15)]]
