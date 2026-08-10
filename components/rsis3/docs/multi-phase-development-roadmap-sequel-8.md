# Multi-Phase Development Roadmap — Sequel VIII (Phases 36–40): Human–AI Symbiosis

Adopted: 2026-08-10 · Status: active · Mode: llm-driven · Epoch: 1
Continues: [`multi-phase-development-roadmap-sequel-7.md`](multi-phase-development-roadmap-sequel-7.md) (Phases 31–35)
Linked goal stack: `rack/goals_stack.json` (goal-stack-001, T0–T3)
Maturity arc: Phases 36–40 — **Human–AI Symbiosis** (explain → delegate →
co-design → calibrate → collaborate).

So far humans have been ratifiers, approvers and operators. Symbiosis
flips the default: the system makes itself legible enough that a
non-expert can read why it acted, trusted enough that they will delegate
bounded authority, and collaborative enough that they co-design the work
rather than merely approve it. Trust is no longer assumed — it is
measured, calibrated and maintained per human, per context.

## Standing telemetry & dashboard contract (every phase)

Every phase ships, alongside its deliverables: (1) new telemetry events
registered in the contract and surfaced in `ecosystem.json` /
`dashboard-data.json`, and (2) a dashboard/web UI update that makes the
phase's output visible — no silent phases (T0).

## Phase 36 — Explainable Autonomy

Goal: every autonomous decision carries a rationale a non-expert can
read.

- **Decision rationales**: every applied candidate, policy change and
  rejection carries a structured rationale — evidence, alternatives,
  trade-offs — derived from the Phase 7 ledger and Phase 14 attestations.
- **Explanation depth ladder**: rationales render at three levels —
  one-line, paragraph, full evidence trace — with the full trace always
  one click away.
- **Counterfactuals**: for gated decisions, the system records what it
  would have done under the rejected alternative (extending Phase 10
  prediction to decisions).
- **Telemetry**: `decision.explained` events with rationale depth and
  readability score.
- **Dashboard**: Bridge/Overview gain an "Explanations" feed where every
  recent decision shows its one-line rationale with drill-down.
- **Exit criterion**: a non-expert panel answers "why did it do that?"
  correctly for 9/10 recent decisions using only the dashboard.

## Phase 37 — Natural-Language Policy

Goal: humans amend rules in plain language; the system compiles them to
machine checks.

- **Policy compiler**: `rack/policy.json` edits can be authored as plain
  sentences ("never spend more than $1/day on identity", "always ask
  before touching the bridge") and compiled to executable policy with a
  deterministic, reviewable mapping.
- **Round-trip validation**: compiled policy renders back to natural
  language for human confirmation before it is staged (Phase 9 gate).
- **Conflict detection**: natural-language rules that contradict existing
  policy are flagged at authoring time (extending Phase 26 meta-governance
  scoring).
- **Telemetry**: `policy.compiled` / `policy.roundtrip` events with
  conflict counts.
- **Dashboard**: a "Policy" view shows rules as human sentences with their
  compiled form and last-ratified actor.
- **Exit criterion**: a non-technical user authors three rules in plain
  language, the compiler rejects one conflict, and the remaining two pass
  round-trip confirmation and the Phase 9 approval gate.

## Phase 38 — Delegation Contracts

Goal: humans delegate bounded authority with explicit scope and instant
revocation.

- **Contracts**: a delegation is a signed, policy-encoded record — scope
  (actions × projects × budget), expiry, and revocation conditions —
  extending the Phase 12 authz chain without a new identity system.
- **Bounded execution**: delegated actions run inside the contract's
  limits; any breach is fail-closed and logged as an incident (15).
- **Revocation**: revocation takes effect within one cycle and is
  audit-attributable; revocations cascade to in-flight delegated work.
- **Telemetry**: `delegation.issued` / `delegation.executed` /
  `delegation.revoked` events with scope hashes.
- **Dashboard**: an "Delegations" view lists active contracts, remaining
  budget and one-click revoke.
- **Exit criterion**: a human delegates a bounded task, the system
  executes within scope, and revocation stops new delegated work within
  one cycle with a full audit trail.

## Phase 39 — Trust Calibration

Goal: the system knows when to ask and when to act, per human and
context.

- **Ask-vs-act model**: extending Phase 10's self-model, the system
  predicts for each (human, action, project) whether to ask first —
  trained on approval outcomes and post-hoc corrections.
- **Trust metrics**: per-human over-trust (acted when they wanted to be
  asked) and under-trust (asked when they wanted autonomy) are first-class
  metrics with targets.
- **Calibration loop**: periodic recalibration adjusts ask thresholds from
  measured outcomes (extending Phase 26 evidence-driven revision).
- **Telemetry**: `trust.asked` / `trust.acted` / `trust.recalibrated`
  events.
- **Dashboard**: a "Trust" panel shows each human's ask-vs-act ratio and
  calibration trend.
- **Exit criterion**: over- and under-trust rates each drop below a
  policy-defined target over a 30-day window without manual tuning.

## Phase 40 — Co-Design Workspaces

Goal: humans and the system design goals, plans and artifacts together.

- **Shared canvases**: projects (11) gain co-design workspaces where human
  drafts, system proposals and merged plans live with full provenance
  (13-style envelopes).
- **Joint planning**: L2 goal formulation (28) becomes interactive — the
  system proposes, the human edits, the merged goal enters the normal
  pipeline with dual authorship recorded.
- **Review surfaces**: every co-design artifact shows which parts are
  human-authored, system-authored, or merged, with the reasoning for
  system suggestions.
- **Telemetry**: `codesign.proposed` / `codesign.merged` events with
  authorship split.
- **Dashboard**: MyKB/Projects gain a co-design canvas view per project.
- **Exit criterion**: a human and the system jointly produce a goal and
  plan that runs through the full pipeline; authorship is attributable on
  every line.

## Sequencing notes (Sequel VIII)

- Explainability (36) precedes everything: you cannot delegate to or
  co-design with a system you cannot read; it renders the Phase 7/14
  evidence into human form.
- Natural-language policy (37) extends Phase 26 meta-governance and the
  Phase 9 gate — the human authors at the level they think, the system
  compiles down.
- Delegation (38) and trust calibration (39) both extend the Phase 12
  authz chain and the Phase 10 self-model; revocation must exist before
  delegation can be trusted.
- Co-design (40) is the capstone: it needs goals (28), projects (11),
  shared sessions (12) and provenance (13) all present.
- Every phase ends with a MyKB synthesis + snapshot regeneration per the
  standing L3 memory-consolidation practice.

## Status

| Phase | Area | Status |
|-------|------|--------|
| Phase 36 — Explainable autonomy | governance | ⏳ queued |
| Phase 37 — Natural-language policy | governance | ⏳ queued |
| Phase 38 — Delegation contracts | governance | ⏳ queued |
| Phase 39 — Trust calibration | autonomy | ⏳ queued |
| Phase 40 — Co-design workspaces | product | ⏳ queued |
