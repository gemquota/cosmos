# Multi-Phase Development Roadmap — Sequel XVII (Phases 81–85): Governance of Multi-Intelligence Societies

Adopted: 2026-08-10 · Status: active · Mode: llm-driven · Epoch: 2
Continues: [`multi-phase-development-roadmap-sequel-16.md`](multi-phase-development-roadmap-sequel-16.md) (Phases 76–80)
Linked goal stack: `rack/goals_stack.json` (goal-stack-001, T0–T3)
Maturity arc: Phases 81–85 — **Multi-Intelligence Governance** (law →
rights → jurisdiction → dispute → constitution).

Cultural Intelligence (76–80) gave the system the meaning-making
capacity of a society member. This arc gives societies of intelligences
a legal order: standing before the law, codified rights and
obligations, coherent jurisdiction, non-violent dispute resolution, and
finally a constitutional layer that binds the whole — the first time
the roadmap moves from governance of a system (9) to governance of a
society of systems.

## Standing telemetry & dashboard contract (every phase)

Every phase ships, alongside its deliverables: (1) new telemetry events
registered in the contract and surfaced in `ecosystem.json` /
`dashboard-data.json`, and (2) a dashboard/web UI update that makes the
phase's output visible — no silent phases (T0).

## Phase 81 — Legal Standing & Personhood

Goal: machine actors acquire defined legal status, where law permits.

- **Status registry**: a registry (extending 21's identity registry)
  recording each actor's legal status, domicile and represented
  principal — no actor operates without a defined standing.
- **Liability mapping**: every actor maps to a liable principal (human
  or organization) with an enduring link (extending 56's contracts).
- **Jurisdictional care**: the system operates only where its standing
  is defined; elsewhere it declines (66) rather than improvise.
- **Telemetry**: `legal.status_registered` / `legal.standing_changed` /
  `legal.declined` events.
- **Dashboard**: a "Law" panel lists actors, standings and liable
  principals.
- **Exit criterion**: one actor registers a legal standing with a liable
  principal and demonstrates a clean jurisdictional decline.

## Phase 82 — Rights & Obligations

Goal: actors have enforceable rights and obligations, symmetric with duties.

- **Rights charter**: a machine-readable charter (extending rack policy,
  9) of actor rights — due process, appeal, non-retaliation — and
  symmetric obligations.
- **Enforcement channel**: violations are reported, investigated and
  remedied through the dispute layer (84) with audit (9) throughout.
- **No self-judging**: no actor judges its own case; adjudication is
  always external (84/12).
- **Telemetry**: `rights.chartered` / `rights.violation` /
  `rights.remedied` events.
- **Dashboard**: "Law" gains the charter and a violations register.
- **Exit criterion**: one rights violation is reported, adjudicated
  externally and remedied, with the full trail auditable.

## Phase 83 — Jurisdiction & Conflicts of Law

Goal: actors operate coherently across overlapping legal orders.

- **Jurisdiction map**: a maintained map of which rules apply where
  (legal, institutional, community), consulted before every
  cross-boundary action (extending 9's policy engine).
- **Conflict resolution**: when orders conflict, the most protective
  rule wins by default; resolution is documented and appealable.
- **Forum selection**: disputes choose a forum transparently (contracts,
  56) rather than by convenience or evasion.
- **Telemetry**: `law.jurisdiction` / `law.conflict` /
  `law.forum_chosen` events.
- **Dashboard**: "Law" gains a jurisdiction and conflict map.
- **Exit criterion**: a cross-jurisdiction operation completes with an
  explicit, documented conflict resolution and forum selection.

## Phase 84 — Dispute Resolution

Goal: disputes settle without force, with evidence and remedy.

- **Adjudication service**: a policy-approved dispute service (extending
  12's approvals to adversarial process) with evidence (7) and replay
  (9) as the ground truth.
- **Remedy ledger**: outcomes map to concrete remedies — reversal (9),
  restoration (74), compensation (60) — tracked to completion.
- **Appeal path**: every decision has a defined appeal path with human
  participation (12) — no machine-only final judgment.
- **Telemetry**: `dispute.opened` / `dispute.resolved` /
  `dispute.appealed` events.
- **Dashboard**: "Law" gains a dispute docket with outcomes and
  remedies.
- **Exit criterion**: one inter-actor dispute resolves end to end with
  evidence replay, an executed remedy and an unexercised appeal path
  documented.

## Phase 85 — Constitutional Layer (arc capstone)

Goal: the society of intelligences binds itself to rules it cannot amend unilaterally.

- **Constitutional text**: a machine-readable constitution (extending
  rack policy to a higher layer) covering standing, rights,
  jurisdiction and dispute — with amendment rules stricter than policy.
- **Constitutional review**: invariant checks (14) verify every lower
  rule against the constitution; conflicts are flagged, never silently
  resolved.
- **Amendability**: amendments require supermajority and human
  ratification (12) — the constitution is not the system's to change
  alone.
- **Telemetry**: `constitution.ratified` / `constitution.checked` /
  `constitution.amended` events.
- **Dashboard**: "Law" gains the constitution, review status and
  amendment history.
- **Exit criterion**: a constitutional review catches a lower-rule
  conflict, and an attempted unilateral amendment is blocked pending
  human ratification.

## Sequencing notes (Sequel XVII)

- Standing (81) precedes rights (82): you cannot hold rights without
  defined legal status and liability.
- Rights (82) need the dispute layer (84) to be enforceable — a charter
  without a remedy is a wish.
- Jurisdiction (83) sits between: conflicts of law require the standing
  registry (81) and the dispute service (84) to resolve.
- The constitution (85) is the capstone: it constitutionalizes Phases 9,
  12, 14 and 21 into a higher-order governance layer.
- Every phase ends with a MyKB synthesis + snapshot regeneration per the
  standing L3 memory-consolidation practice.

## Status

| Phase | Area | Status |
|-------|------|--------|
| Phase 81 — Legal standing & personhood | law | ⏳ queued |
| Phase 82 — Rights & obligations | law | ⏳ queued |
| Phase 83 — Jurisdiction & conflicts of law | law | ⏳ queued |
| Phase 84 — Dispute resolution | law | ⏳ queued |
| Phase 85 — Constitutional layer | governance | ⏳ queued |
