---
type: "synthesis"
title: "RSIS3 roadmap sequels II–III (Phases 6–15) — durable structure and ordering rules"
description: "Two five-phase sequel roadmaps continue the delivered Phases 1–5: Horizons (distributed memory, verification mesh, cost governance, governance, self-modeling) and Frontiers (cross-project, collaboration, federation, invariants, long-horizon autonomy); records the cumulative-ordering rules that keep them coherent"
tags: ["rsis3", "roadmap", "sequel", "planning", "phase-6", "phase-11", "architecture"]
timestamp: "2026-08-09T00:15:00Z"
status: "growing"
---

# RSIS3 roadmap sequels II–III (Phases 6–15)

The original five-phase roadmap is delivered. Two sequel roadmaps extend
the work; this note records the durable structure and the ordering rules
future sessions must respect.

## Documents

- Sequel II — Horizons (Phases 6–10):
  `components/rsis3/docs/multi-phase-development-roadmap-sequel-2.md`
- Sequel III — Frontiers (Phases 11–15):
  `components/rsis3/docs/multi-phase-development-roadmap-sequel-3.md`
- The main roadmap links both under a `## Sequels` section.

## Phase map

- **Sequel II (Horizons)**: 6 distributed memory & multi-session
  coordination · 7 verification mesh · 8 observability & cost governance
  · 9 human-in-the-loop governance · 10 self-modeling & prediction.
- **Sequel III (Frontiers)**: 11 cross-project generalization · 12
  collaborative & community ops · 13 federated memory · 14 continual
  verification & invariant attestation · 15 long-horizon autonomy.

## Ordering rules (durable constraints)

- Memory (6) and verification (7) precede governed autonomy (9); cost
  governance (8) precedes forecasting (10) because forecasts need cost
  history.
- Cross-project (11) needs the memory API (6) + verification mesh (7);
  collaboration (12) needs governance (9); federation (13) needs the
  publish/subscribe memory API (6) and trust boundaries (9).
- Invariants (14) must land before long-horizon autonomy (15) — a 30-day
  unattended run is only safe once behavior is pinned and attestable.
- Reuse existing primitives before building new ones: Phase 4/5 lockfile
  and Phase 3 session patterns are the coordination substrate for Phase 6.
- Every phase — in any roadmap — ends with a MyKB synthesis + snapshot
  regeneration per the standing L3 memory-consolidation practice.

## Precision pass (2026-08-09)

The 6–15 sequencing is kept as-is; a precision pass tightened the
invariants and cross-phase dependencies. Durable deltas:

- **Cross-roadmap invariant**: autonomy is cumulative but never
  unconditional — every capability expansion inherits the memory,
  verification, cost, policy, provenance and observability controls of
  preceding phases. Recorded at the top of the main roadmap.
- **Maturity arcs**: Phases 1–5 Operational Autonomy; 6–10 Governed
  Intelligence; 11–15 Distributed Autonomy.
- **Phase 5 vs 15**: Phase 5 = bounded autonomy (implementation
  delivered; 7-day live exit validation pending); Phase 15 extends it
  into a persistent lifecycle — it does not introduce new autonomy.
- **Phase 7 → 14**: the regression ledger is the evidence substrate
  Phase 14 extends into per-cycle invariant attestation.
- **Phase 9**: policy-controlled autonomy — the human is one
  enforcement mechanism among several policy instruments.
- **Phase 12**: authorization is capability- and project-scoped
  (User → Identity → Role → Project membership → Policy → Capability →
  Action); an approver role alone grants no blanket authority.
- **Phase 13**: federation provenance is explicit — origin, source,
  project, session, producer, verification state, confidence,
  transformations, federation history.
- **Phase 10**: forecast quality tracks calibration, uncertainty, bias
  and degradation as first-class metrics, not only ≥80% coverage.

## Related

- [[wiki/syntheses/rsis3-phase-4-5-ops-autonomy-2026-08-08|RSIS3 Phases 4–5 — ops maturity + autonomy]]
- [[wiki/syntheses/rsis3-phase-3-product-surface-2026-08-08|RSIS3 Phase 3 — product surface]]
