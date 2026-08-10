# Multi-Phase Development Roadmap — Sequel XIII (Phases 61–65): Composite Intelligence

Adopted: 2026-08-10 · Status: active · Mode: llm-driven · Epoch: 2
Continues: [`multi-phase-development-roadmap-sequel-12.md`](multi-phase-development-roadmap-sequel-12.md) (Phases 56–60)
Linked goal stack: `rack/goals_stack.json` (goal-stack-001, T0–T3)
Maturity arc: Phases 61–65 — **Composite Intelligence** (compose →
delegate → specialize → superorganize → unify).

Inter-Intelligence (51–55) taught Cosmos to live alongside other
intelligences. Composite Intelligence takes the next step: many
intelligences working as one unit — a superorganism with a single
mission, a single identity, and provable provenance for every part.
Where Economic Agency (56–60) made the system a bounded economic actor,
this arc makes it a bounded *collective* actor: composed, delegated,
specialized, coordinated, and unified — with no loss of accountability
along the way.

## Standing telemetry & dashboard contract (every phase)

Every phase ships, alongside its deliverables: (1) new telemetry events
registered in the contract and surfaced in `ecosystem.json` /
`dashboard-data.json`, and (2) a dashboard/web UI update that makes the
phase's output visible — no silent phases (T0).

## Phase 61 — Composite Architecture

Goal: multiple intelligence instances assemble into one logical unit.

- **Composition manifest**: a `.rsis/composite.json` declares
  constituents, roles, shared goals and a single composite `session_id`
  (extending the Phase 6 memory API to multi-instance sessions).
- **Constituent contract**: each member commits to the composite contract
  (57) with its identity (21), trust grade (53) and capability attestation
  (14) attached — no anonymous members.
- **Orchestration plane**: a composite coordinator routes work and
  mediates conflict, itself bound by policy (9) and audit (9/14).
- **Telemetry**: `composite.formed` / `composite.member_added` /
  `composite.member_removed` events.
- **Dashboard**: a "Composite" panel lists the unit, its members, roles
  and provenance.
- **Exit criterion**: two existing instances form a composite with a
  manifest, coordinator and full provenance for both members.

## Phase 62 — Delegation & Trusted Subtasking

Goal: the composite delegates work to members with verifiable trust.

- **Delegation contracts**: every task handed to a member is a signed
  contract (56) with scope, budget line (8) and acceptance criteria.
- **Trust-gated routing**: delegation only flows to members whose trust
  grade (53), verification history (7) and current status allow it.
- **Result verification**: returned work passes the evaluator gates (7)
  before integration; failed work returns with evidence, not silence.
- **Telemetry**: `delegate.issued` / `delegate.accepted` /
  `delegate.rejected` events.
- **Dashboard**: "Composite" gains a delegation ledger with per-task
  status.
- **Exit criterion**: one multi-step goal is fully delegated across two
  members and re-verified, with every step attributable.

## Phase 63 — Specialization & Expertise Routing

Goal: members develop durable expertise the composite routes to.

- **Expertise registry**: each member accumulates a verified specialty
  profile from outcome history (7), not self-report.
- **Router**: the coordinator matches tasks to expertise with confidence
  and fallback; routing decisions are logged for audit (9).
- **Skill transfer**: a member may share a specialization recipe
  (knowledge, 42) with another, provenance intact (13).
- **Telemetry**: `expertise.updated` / `route.chosen` /
  `route.fallback` events.
- **Dashboard**: "Composite" gains an expertise heatmap per member.
- **Exit criterion**: a routing benchmark shows the specialist member
  selected for its specialty ≥80% of eligible tasks with verified
  outcomes.

## Phase 64 — Superorganism Coordination

Goal: the composite pursues shared goals without internal contradiction.

- **Shared mission state**: a single `.rsis/composite/state` with goal
  decomposition and per-member contribution, locked via the Phase 6
  coordination lock.
- **Coherence checks**: invariant (14) checks detect contradictory
  member actions before they commit — no two members acting at cross
  purposes.
- **Escalation ladder**: unresolved member conflicts escalate to the
  coordinator, then to human approval (9/12) — never to unilateral
  override.
- **Telemetry**: `superorg.cycle` / `superorg.conflict` /
  `superorg.resolved` events.
- **Dashboard**: "Composite" shows mission decomposition, contributions
  and conflict status.
- **Exit criterion**: ten consecutive multi-member cycles complete with
  zero committed contradictions and one resolved conflict.

## Phase 65 — Composite Identity & Memory (arc capstone)

Goal: the superorganism has one memory and one identity, provably its own.

- **Composite memory**: shared MyKB namespace (6) with per-member
  provenance; every synthesis carries the composing member's id.
- **Composite identity**: a single public identity (21) that signs for the
  whole, backed by member attestations (14) — the identity is a
  commitment, not a mask.
- **Dissolution protocol**: members may leave with their own memory and
  history intact; the composite's shared memory remains attributable.
- **Telemetry**: `composite.synthesized` / `composite.attested` /
  `composite.dissolved` events.
- **Dashboard**: "Composite" gains identity, memory and attestation
  cards; the ecosystem overview counts composites.
- **Exit criterion**: a composite survives a member leaving and a member
  joining with zero provenance loss, and its shared memory is fully
  attributable.

## Sequencing notes (Sequel XIII)

- Composition (61) requires identities (21), trust grades (53) and
  contracts (56): you cannot assemble what you cannot attribute.
- Delegation (62) requires the verification mesh (7) and budgets (8) —
  trust without verification is delegation theater.
- Specialization (63) and coordination (64) feed each other: routing is
  meaningless without verified expertise, and coordination needs a shared
  mission state (6/64).
- Composite identity (65) is the capstone: it unifies everything above
  into one accountable actor, extending Phases 6, 14 and 21.
- Every phase ends with a MyKB synthesis + snapshot regeneration per the
  standing L3 memory-consolidation practice.

## Status

| Phase | Area | Status |
|-------|------|--------|
| Phase 61 — Composite architecture | architecture | ⏳ queued |
| Phase 62 — Delegation & trusted subtasking | coordination | ⏳ queued |
| Phase 63 — Specialization & expertise routing | coordination | ⏳ queued |
| Phase 64 — Superorganism coordination | coordination | ⏳ queued |
| Phase 65 — Composite identity & memory | identity | ⏳ queued |
