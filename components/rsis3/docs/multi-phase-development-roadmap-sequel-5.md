# Multi-Phase Development Roadmap — Sequel V (Phases 21–25): Ecosystem Autonomy

Adopted: 2026-08-10 · Status: active · Mode: llm-driven
Continues: [`multi-phase-development-roadmap-sequel-4.md`](multi-phase-development-roadmap-sequel-4.md) (Phases 16–20)
Linked goal stack: `rack/goals_stack.json` (goal-stack-001, T0–T3)
Maturity arc: Phases 21–25 — **Ecosystem Autonomy** (identify → exchange
→ coordinate → govern → survive).

Sequel IV made a single instance open: auditable, portable, and safely
programmable. Sequel V multiplies that instance into a *population*: many
Cosmos instances that recognize each other, exchange distilled knowledge
with value semantics, dispatch work with corroborated results, federate
governance, and survive churn and partition. Federation (Phase 13) was
two instances exchanging notes; Ecosystem Autonomy is a living network.

## Phase 21 — Instance Identity & Trust Graph

Goal: instances authenticate each other; federation stops trusting shared
tokens and starts trusting keys.

- **Identity keys**: `rsis identity init` generates an instance keypair;
  the fingerprint is published in the federation ledger (13).
- **Signed federation**: every published envelope (13) is signed by its
  origin; recipients verify provenance before adoption.
- **Peer registry**: `rack/federation/peers.json` (env-templated) carries
  peer fingerprints and trust levels; unknown peers are quarantined.
- **Key rotation**: identity keys rotate on a policy-defined cadence with
  a grace period; retired keys remain valid for verification only.
- **Exit criterion**: two instances exchange a signed synthesis and each
  verifies the other's fingerprint; a forged envelope is rejected.

## Phase 22 — Knowledge Economy & Exchange at Scale

Goal: distilled knowledge moves across the population with confidence and
value semantics, not just copies.

- **Confidence propagation**: envelope confidence (13) updates as a
  synthesis is corroborated or contradicted across instances.
- **Canonicalization**: duplicate/canonical detection across instances
  (title + content similarity) so the same durable rule is not adopted N
  times with divergent edits.
- **Exchange ledger**: the federation ledger (13) gains exchange records
  (provider, consumer, item, confidence delta) for cost/benefit
  accounting.
- **Provenance intactness**: a chain of three or more hops preserves
  origin and full federation history — no silent rewriting.
- **Exit criterion**: one synthesis propagates through three instances
  with intact provenance, deduplicated adoption, and a measurable
  confidence trajectory.

## Phase 23 — Swarm Coordination & Distributed Cycles

Goal: workloads dispatch across the population with corroborated results.

- **Work dispatch**: a cycle batch (11) or a candidate can be dispatched
  to trusted peers (21) under a result contract.
- **Corroboration**: a candidate's verification (7) is corroborated when
  two or more instances independently re-run the gates and agree.
- **Reconciliation**: divergent results resolve deterministically
  (majority + provenance), and every reconciliation is logged in the
  federation ledger (13).
- **Failure containment**: a peer that fails mid-dispatch does not block
  the population — the work re-dispatches or degrades gracefully (25).
- **Exit criterion**: a cross-instance cycle produces a candidate verified
  by two independent instances with a recorded reconciliation.

## Phase 24 — Population Governance

Goal: policy federates across the population without a single point of
trust.

- **Shared rule sets**: policy fragments (9) are shareable and versioned
  across instances; local policy always wins over foreign policy (13
  consensus extended).
- **Cross-instance approvals**: a Phase 9 approval can require peer
  corroboration for high-risk operations under a policy-defined quorum.
- **Rule divergence**: conflicting durable rules resolve deterministically
  — newest facts, local behavior policy, population quorum — with backlog
  logging on every instance.
- **Policy provenance**: every shared rule carries origin and
  ratification history; the audit trail (9) replays across instances.
- **Exit criterion**: a policy change propagates to a three-instance
  population; a deliberately conflicting rule resolves deterministically
  and is logged in every instance's backlog.

## Phase 25 — Ecosystem Resilience

Goal: the population survives churn, partition, and partial failure
without data loss.

- **Churn handling**: instances join and leave without data loss;
  re-sync flows through the federation ledger (13) and the attestation
  chain (16).
- **Partition tolerance**: a temporary loss of peers degrades to local
  operation (Phase 15 energy modes) and reconciles on reconnect.
- **Forked knowledge**: two instances that independently evolved the same
  rule merge deterministically (24) with both histories preserved.
- **Survival drills**: a kill-the-leader test — killing any one instance
  mid-cycle leaves the rest consistent.
- **Exit criterion**: killing one of three instances mid-cycle leaves the
  other two consistent and the knowledge intact; a reconnecting instance
  re-syncs with zero conflict.

## Sequencing notes (Sequel V)

- Identity (21) is the foundation: signed federation, exchange value and
  swarm dispatch are all meaningless until instances can authenticate each
  other; it extends the Phase 13 trust boundary and the Phase 12 identity
  chain.
- Exchange (22) and coordination (23) both depend on the federation ledger
  (13) and the verification mesh (7) — knowledge and work move with
  evidence, never anonymously.
- Population governance (24) extends Phase 9 policy and Phase 13
  consensus; local policy remains sovereign over foreign policy.
- Resilience (25) is the capstone of the arc: churn and partition can only
  be tested once identity, exchange, dispatch and governance exist.
- Every phase ends with a MyKB synthesis + snapshot regeneration per the
  standing L3 memory-consolidation practice.

## Status

| Phase | Area | Status |
|-------|------|--------|
| Phase 21 — Instance identity & trust graph | federation | ✅ delivered (implementation) · ⏳ two instances exchange a signed synthesis and each live validation pending |
| Phase 22 — Knowledge economy & exchange at scale | memory | ✅ delivered (implementation) · ⏳ one synthesis propagates through three instances live validation pending |
| Phase 23 — Swarm coordination & distributed cycles | orchestration | ✅ delivered (implementation) · ⏳ a cross-instance cycle produces a candidate verified live validation pending |
| Phase 24 — Population governance | governance | ✅ delivered (implementation) · ⏳ a policy change propagates to a three-instance live validation pending |
| Phase 25 — Ecosystem resilience | reliability | ✅ delivered (implementation) · ⏳ killing one of three instances mid-cycle leaves the live validation pending |
