# Multi-Phase Development Roadmap — Sequel VII (Phases 31–35): Generational Autonomy

Adopted: 2026-08-10 · Status: active · Mode: llm-driven · Epoch: 1
Continues: [`multi-phase-development-roadmap-sequel-6.md`](multi-phase-development-roadmap-sequel-6.md) (Phases 26–30)
Linked goal stack: `rack/goals_stack.json` (goal-stack-001, T0–T3)
Maturity arc: Phases 31–35 — **Generational Autonomy** (inherit →
archive → succeed → migrate → endure).

Phase 30 proved a single instance can run for a year with quarterly human
ratification. Generational Autonomy confronts the next wall: *no instance
is immortal*. Work that matters must survive its stewards, its hosts and
even its own obsolescence. This arc turns knowledge and custody into
inheritable assets — distilled so the next generation starts where the
last ended, archived so nothing decays, and handed over through planned
succession instead of crisis.

## Standing telemetry & dashboard contract (every phase)

Every phase ships, alongside its deliverables: (1) new telemetry events
registered in the contract and surfaced in `ecosystem.json` /
`dashboard-data.json`, and (2) a dashboard/web UI update that makes the
phase's output visible — no silent phases (T0).

## Phase 31 — Knowledge Inheritance

Goal: the distilled knowledge of one generation becomes the curriculum of
the next.

- **Inheritance bundles**: `rsis inheritance export` renders the full
  durable knowledge (syntheses, durable rules, KG, verification history,
  policy rationale) as a versioned bundle a successor instance can adopt.
- **Curriculum distillation**: L3 consolidation (existing loop) gains a
  "what a successor must know first" ordering — a boot curriculum per
  domain, project and population.
- **Lossless handoff check**: after adoption, the successor answers a
  probe set derived from the predecessor's knowledge with parity ≥ 0.98,
  and `check-practices` + invariants pass.
- **Telemetry**: `inheritance.exported` / `inheritance.adopted` events
  with bundle sha and size.
- **Dashboard**: MyKB tab gains an "Inheritance" panel showing the current
  generation's curriculum coverage.
- **Exit criterion**: a successor instance cold-starts from an inheritance
  bundle and passes a generation-parity probe set with no manual
  re-education.

## Phase 32 — Archival Immortality

Goal: knowledge outlives its media, formats and hosts.

- **Bit-rot resilience**: every durable artifact gets redundancy + checksum
  patrol (extending the Phase 16 attestation chain); corrupt copies are
  detected and rebuilt from peers or archives.
- **Format migration**: a standing migration job re-encodes archives when
  schemas, formats or dependency versions change (extending Phase 18
  reproducibility).
- **Geographic redundancy**: archives replicate across hosts/populations
  (Phase 25 resilience) with a minimum replication factor in policy.
- **Telemetry**: `archive.patrol` / `archive.migrated` events with
  corruption counts.
- **Dashboard**: Overview gains an "Archive health" card (replication
  factor, last patrol, corrupted/rebuilt).
- **Exit criterion**: a simulated media failure corrupts one copy and the
  patrol detects + rebuilds it from a peer within one cycle, with the
  attestation chain intact.

## Phase 33 — Succession Planning

Goal: stewardship passes to a chosen successor deliberately, not by
accident.

- **Heir selection**: policy defines succession criteria (capability,
  provenance, trust); `rsis succession plan` proposes an ordered heir list
  from the population (Phase 21 identity).
- **Custody transfer**: the steward (Phase 29) hands over monitoring,
  repair and attestation duties with a signed transfer record audited in
  `.rsis/audit.jsonl`.
- **Dual-running overlap**: predecessor and successor run in parallel for
  a policy-defined overlap window so continuity is verified before cutover.
- **Telemetry**: `succession.planned` / `succession.transferred` events
  with heir identity.
- **Dashboard**: a "Succession" view lists planned heirs, overlap status
  and transfer history.
- **Exit criterion**: a full custody transfer completes with overlap
  verification; the successor's first 100 cycles show zero continuity
  drift.

## Phase 34 — Mission Continuity

Goal: long-horizon missions outlive any single instance.

- **Mission state**: missions (goal-stack level goals) carry explicit
  state — objective, progress, constraints, next actions — that travels
  with inheritance (31) and succession (33), not with any instance.
- **Generation checkpoints**: mission progress checkpoints every cycle are
  attestable (14) so a mission can be resumed by a successor at the exact
  logical point.
- **Mission telemetry**: `mission.progress` events track objective drift,
  staleness and blockage across generations.
- **Dashboard**: Overview "Missions" strip shows mission age, progress and
  current steward.
- **Exit criterion**: a mission started under one generation is resumed by
  a successor and completes with its progress ledger contiguous (no lost
  or double-applied steps).

## Phase 35 — Generational Resilience

Goal: the system remains sound across decades, not just months.

- **Dependency obsolescence**: a standing scan flags obsolete toolchains,
  formats and dependencies (Phase 18 pins) and stages migration work as
  goal seeds (11).
- **Knowledge staleness**: syntheses older than a policy-defined age are
  re-validated or retired; stale-durable-rule counts are a first-class
  metric.
- **Environment drift**: workspace manifests (18) are re-verified against
  the live environment on every epoch boundary; drift triggers the
  degradation ladder (27).
- **Telemetry**: `generation.drift` / `generation.obsolete` events.
- **Dashboard**: a "Generations" timeline shows the instance lineage and
  each generation's knowledge/health deltas.
- **Exit criterion**: a simulated decade of dependency and format churn is
  absorbed with zero knowledge loss and zero silent behavioral drift.

## Sequencing notes (Sequel VII)

- Inheritance (31) is the foundation: succession (33) and mission
  continuity (34) both hand off distilled knowledge, so the curriculum
  must exist first; it extends Phase 18 portability and Phase 22 exchange.
- Archival immortality (32) protects the asset inheritance preserves; it
  extends the Phase 16 attestation chain and Phase 25 resilience.
- Succession (33) builds on Phase 29 stewardship and Phase 21 identity —
  you can only hand custody to a known, trusted instance.
- Mission continuity (34) and generational resilience (35) are the
  stress tests: missions that outlive stewards, and churn that outlives
  environments.
- Every phase ends with a MyKB synthesis + snapshot regeneration per the
  standing L3 memory-consolidation practice.

## Status

| Phase | Area | Status |
|-------|------|--------|
| Phase 31 — Knowledge inheritance | memory | ✅ delivered (implementation) · ⏳ a successor instance cold-starts from an inheritance live validation pending |
| Phase 32 — Archival immortality | ops | ✅ delivered (implementation) · ⏳ a simulated media failure corrupts one copy and the live validation pending |
| Phase 33 — Succession planning | governance | ✅ delivered (implementation) · ⏳ a full custody transfer completes with overlap live validation pending |
| Phase 34 — Mission continuity | autonomy | ✅ delivered (implementation) · ⏳ a mission started under one generation is resumed by live validation pending |
| Phase 35 — Generational resilience | reliability | ✅ delivered (implementation) · ⏳ a simulated decade of dependency and format churn is live validation pending |
