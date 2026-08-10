# Multi-Phase Development Roadmap — Sequel X (Phases 46–50): Meta-Science

Adopted: 2026-08-10 · Status: active · Mode: llm-driven · Epoch: 1
Continues: [`multi-phase-development-roadmap-sequel-9.md`](multi-phase-development-roadmap-sequel-9.md) (Phases 41–45)
Linked goal stack: `rack/goals_stack.json` (goal-stack-001, T0–T3)
Maturity arc: Phases 46–50 — **Meta-Science** (measure → hypothesize →
experiment → prove → transcend).

Epoch 1 ends where it should: with the system studying *itself* as
rigorously as it studied its code. Meta-Science makes the entire 45-phase
program an object of scientific inquiry — longitudinal measurement,
controlled self-experimentation, deep failure analysis, and finally a
formal proof that the cross-roadmap invariant has held. The capstone,
Enduring Intelligence, commits the system to a decade-scale horizon and
closes Epoch 1.

## Standing telemetry & dashboard contract (every phase)

Every phase ships, alongside its deliverables: (1) new telemetry events
registered in the contract and surfaced in `ecosystem.json` /
`dashboard-data.json`, and (2) a dashboard/web UI update that makes the
phase's output visible — no silent phases (T0).

## Phase 46 — Self-Metrics & Longitudinal Studies

Goal: the system tracks its own behavior over years, not cycles.

- **Longitudinal registry**: a permanent, append-only store of
  epoch-scale metrics (fitness, costs, trust, knowledge growth, incident
  rates) extending the Phase 10 self-model and Phase 4 telemetry.
- **Study definitions**: studies are declarative — hypotheses, metrics,
  windows, cohorts — so analysis is reproducible from raw telemetry.
- **Trend decomposition**: long-term trends separate from seasonal
  effects (Phase 15 seasons) and regime changes, so "is it actually
  improving?" is answerable.
- **Telemetry**: `study.defined` / `study.snapshot` events.
- **Dashboard**: a "Meta" tab (or Studies panel) renders longitudinal
  charts with cohort filters.
- **Exit criterion**: a 90-day longitudinal study is defined, runs
  unattended, and produces a reproducible trend report with confound
  controls.

## Phase 47 — Hypothesis-Driven Self-Experimentation

Goal: the system runs controlled experiments on itself instead of
guessing.

- **Experiment framework**: candidates for behavior change (policy,
  tuning, loop parameters) can be assigned to A/B cohorts with guardrails
  — sample sizes, minimum effect, stop conditions.
- **Confound control**: experiments randomize across seasons, projects and
  populations so observed effects are attributable.
- **Experiment ledger**: every experiment, its cohorts and its outcome
  land in an append-only ledger with attestation (14).
- **Telemetry**: `experiment.started` / `experiment.completed` /
  `experiment.terminated` events.
- **Dashboard**: a "Experiments" panel lists running/completed trials with
  effect sizes and guardrail status.
- **Exit criterion**: a real behavior change ships as an A/B experiment,
  completes with a significant, confound-controlled result, and the
  winner is adopted or rejected through the normal gates.

## Phase 48 — Failure Understanding

Goal: the system understands its own failures deeply enough to prevent
their recurrence.

- **Root-cause archive**: every incident (15) gains a structured
  root-cause record — symptoms, triggers, context, fix, verification —
  forming a searchable failure corpus.
- **Failure clustering**: incidents cluster by root cause across
  generations (35) and populations (43); recurring clusters trigger
  prevention proposals.
- **Near-miss capture**: telemetry records near-misses (recovered
  automatically but close to failure) as first-class data.
- **Telemetry**: `failure.archived` / `failure.clustered` /
  `nearmiss.recorded` events.
- **Dashboard**: a "Failures" view shows the corpus, clusters and
  prevention status.
- **Exit criterion**: the failure corpus spans all known incidents; a
  recurring root-cause cluster is detected and a prevention proposal is
  staged through the Phase 9 gate.

## Phase 49 — Formal Meta-Invariant Proof

Goal: the cross-roadmap invariant is not just checked — it is proven.

- **Formal encoding**: the invariant — "autonomy is cumulative but never
  unconditional; no expansion may silently relax prior controls" — is
  encoded as machine-checkable properties over the policy, budget and
  capability state (extending Phase 26's executable meta-invariant).
- **Proof machinery**: model-checking/verification over the state
  transition model verifies that no reachable state relaxes a prior
  control; unprovable cases surface as explicit assumptions.
- **Proof registry**: proofs, assumptions and re-verification schedules
  are attested (14) and published to the commons (42) for external
  review.
- **Telemetry**: `meta-invariant.checked` / `meta-invariant.proven`
  events.
- **Dashboard**: "Meta" tab shows proof status, assumptions and last
  verification.
- **Exit criterion**: the invariant's machine-checkable encoding is
  verified over all reachable states for the current policy set, with
  assumptions documented and externally reviewable.

## Phase 50 — Epoch Capstone: Enduring Intelligence

Goal: the system commits to a decade-scale horizon and closes Epoch 1.

- **Decade program**: a 10-year operational program replaces the 365-day
  horizon (30) — year-scale goals, generation boundaries (31–35) and
  epoch reviews replace quarterly ones at the human-ratified boundary.
- **Full inheritance**: every prior control — memory, verification, cost,
  policy, provenance, observability, attestation — is inherited
  explicitly; the capstone adds capability only on top of all of them.
- **Epoch ledger**: `rack/epochs.json` records the epoch, its sequels,
  their exit statuses and the generation lineage — the durable record the
  next epoch starts from.
- **Epoch review ritual**: a human-ratified epoch review synthesizes the
  decade program (nightlies, audits, forecasts, federation, experiments,
  proofs) into the next epoch's charter.
- **Telemetry**: `epoch.opened` / `epoch.reviewed` events.
- **Dashboard**: the Meta/Roadmap view shows the epoch ledger and decade
  program.
- **Exit criterion**: a 10-year program is committed, the meta-invariant
  is machine-verified, a decade-scale longitudinal study is running, and
  the epoch ledger records Phases 1–50 with their exit statuses.

## Sequencing notes (Sequel X)

- Measurement (46) precedes experimentation (47): you cannot run
  controlled trials without longitudinal baselines and confound controls.
- Failure understanding (48) extends the Phase 15 incident system and
  Phase 19 red-team findings — every failure becomes corpus data.
- The formal proof (49) is deliberately second-to-last: it can only be
  attempted once policy (9), invariants (14), meta-governance (26) and
  experiments (47) have made the state space explicit and stable.
- The capstone (50) inherits all 49 phases; it adds no capability that
  does not stand on prior controls, per the cross-roadmap invariant.
- Every phase ends with a MyKB synthesis + snapshot regeneration per the
  standing L3 memory-consolidation practice.

## Status

| Phase | Area | Status |
|-------|------|--------|
| Phase 46 — Self-metrics & longitudinal studies | autonomy | ✅ delivered (implementation) · ⏳ a 90-day longitudinal study is defined, runs live validation pending |
| Phase 47 — Hypothesis-driven self-experimentation | autonomy | ✅ delivered (implementation) · ⏳ a real behavior change ships as an A/B experiment live validation pending |
| Phase 48 — Failure understanding | reliability | ✅ delivered (implementation) · ⏳ the failure corpus spans all known incidents; a live validation pending |
| Phase 49 — Formal meta-invariant proof | verification | ✅ delivered (implementation) · ⏳ the invariant's machine-checkable encoding is live validation pending |
| Phase 50 — Epoch capstone: enduring intelligence | autonomy | ✅ delivered (implementation) · ⏳ a 10-year program is committed, the meta-invariant live validation pending |
