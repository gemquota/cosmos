# Multi-Phase Development Roadmap — Sequel VI (Phases 26–30): Sovereign Autonomy

Adopted: 2026-08-10 · Status: active · Mode: llm-driven
Continues: [`multi-phase-development-roadmap-sequel-5.md`](multi-phase-development-roadmap-sequel-5.md) (Phases 21–25)
Linked goal stack: `rack/goals_stack.json` (goal-stack-001, T0–T3)
Maturity arc: Phases 26–30 — **Sovereign Autonomy** (meta-govern → sustain
→ self-direct → steward → endure).

Sequels I–V built a verifiable, portable, populated ecosystem of governed
instances. Sovereign Autonomy internalizes the last remaining human
functions that are not yet evidence-driven — policy revision, resource
planning, goal formulation, and custody of peers — and turns them into
monitored subsystems of the same kind as everything before. It does not
remove the human; it makes the human's role *ratification*, and makes the
system able to run itself indefinitely between ratifications.

## Phase 26 — Meta-Governance

Goal: the system proposes and evaluates changes to its own policy — humans
ratify, they do not draft.

- **Policy revision loop**: evidence (forecasts 10, incidents 15, red-team
  findings 19, federation 24) generates policy-revision proposals,
  extending the Phase 15 quarterly review from periodic to continuous.
- **Impact evaluation**: every proposal is scored against the invariant
  registry (14) and the cost model (8) before staging.
- **Human ratification boundary**: proposals apply only through the Phase 9
  approval gate with actor attribution; auto-apply is never permitted for
  policy.
- **Meta-invariant**: the cross-roadmap invariant becomes an executable
  check — no adopted policy may silently relax a prior control.
- **Exit criterion**: one full season where every policy change was
  evidence-proposed, invariant-scored, and human-ratified; the
  meta-invariant check runs every cycle.

## Phase 27 — Resource Sovereignty & Sustainability

Goal: the system operates within its means indefinitely.

- **Capacity planning**: 90-day cost and energy forecasts (10) with
  seasonal budgeting (15) — sprint, coast and pause become a plan, not a
  reaction.
- **Sustainability accounting**: the cost ledger (8) tracks budget,
  energy and storage; dashboards report per-instance sustainability.
- **Self-funded operations**: budget allocation, quota revenue (20) and
  reserve management are first-class state.
- **Degradation ladder**: under sustained pressure the system degrades
  gracefully by capability class — observability → memory → verification
  → policy-critical always on.
- **Exit criterion**: a 90-day budget forecast holds within tolerance; the
  system plans capacity and coasts or pauses by season without manual
  intervention.

## Phase 28 — Self-Directed Learning Goals

Goal: the goal stack (T0–T3) becomes system-proposed and human-ratified.

- **Evidence-driven goal proposals**: gaps from self-assessment,
  federation (22), red-team (19) and external feedback become goal
  candidates with rationale and expected value.
- **Goal telemetry**: each proposed goal carries its own fitness and
  quality metrics (10) — hit rate, novelty, cost — so goal formulation is
  itself a monitored subsystem.
- **Ratification loop**: humans ratify the season's goal set (15 quarterly
  review + 12 approver role); unratified goals never run.
- **Goal retirement**: plateaued goals (4) retire automatically and feed
  the next proposal cycle.
- **Exit criterion**: one full season where L2 goals were system-proposed
  and human-ratified, with goal-quality metrics recorded and improving.

## Phase 29 — Autonomous Stewardship

Goal: the engine operates other instances — Phase 11 generalization
inverted into custody.

- **Peer stewardship**: a steward instance monitors peer health (15
  self-repair, 21 identity, 25 resilience) within policy scope.
- **Onboarding**: new instances initialize from profiles (11) and join the
  trust graph (21) automatically, within policy.
- **Attested custody**: every stewardship action — repair, retune,
  restart — is attested (14) and audit-attributable (9).
- **Handoff**: an instance can be transferred to another steward with
  identity and provenance intact (18 portability).
- **Exit criterion**: the engine autonomously maintains two peer instances
  for 30 days — all incidents self-recovered, all actions attested, zero
  manual intervention.

## Phase 30 — Enduring Autonomy (Sovereign)

Goal: the culmination — unbounded-horizon operation where quarterly
ratification is the only human touchpoint.

- **Continuous meta-invariant enforcement**: the system proves
  continuously that no capability expansion relaxed a prior control (26,
  14).
- **Self-adapting policy**: policy evolves through the ratified revision
  loop (26) without ever breaching the invariant registry (14).
- **Long-horizon continuity**: identity, knowledge and attestations
  survive host and instance churn indefinitely (18, 21, 25).
- **Existential guardrails**: energy (27), budget (8) and policy-critical
  capabilities fail closed under every scenario; red-team (19) keeps
  probing.
- **Exit criterion**: 365 days unattended except quarterly policy
  ratification; the meta-invariant holds continuously; all incidents
  self-recovered, attested, and logged.

## Sequencing notes (Sequel VI)

- Meta-governance (26) must precede everything else in this arc: the
  system cannot sustainably run itself or steward others until policy
  revision is evidence-driven and human-ratified.
- Sustainability (27) is the material prerequisite for an unbounded
  horizon — no duration target matters if the system runs out of budget or
  energy; it extends Phases 8 and 10 and Phase 15 energy modes.
- Self-directed goals (28) need the Phase 10 self-model and the Phase 15
  review loop; goal formulation is monitored like any other loop.
- Stewardship (29) is the generalization (11) applied to the population
  (21–25), guarded by attestation (14) and audit (9).
- Endurance (30) is the proof of the whole 30-phase program: the
  cross-roadmap invariant — autonomy is cumulative but never
  unconditional — is enforced by the system itself.
- Every phase ends with a MyKB synthesis + snapshot regeneration per the
  standing L3 memory-consolidation practice.

## Status

| Phase | Area | Status |
|-------|------|--------|
| Phase 26 — Meta-governance | governance | ✅ delivered (implementation) · ⏳ one full season where every policy change was live validation pending |
| Phase 27 — Resource sovereignty & sustainability | ops | ✅ delivered (implementation) · ⏳ a 90-day budget forecast holds within tolerance; the live validation pending |
| Phase 28 — Self-directed learning goals | autonomy | ✅ delivered (implementation) · ⏳ one full season where L2 goals were system-proposed live validation pending |
| Phase 29 — Autonomous stewardship | orchestration | ✅ delivered (implementation) · ⏳ the engine autonomously maintains two peer instances live validation pending |
| Phase 30 — Enduring autonomy | autonomy | ✅ delivered (implementation) · ⏳ 365 days unattended except quarterly policy live validation pending |
