# Multi-Phase Development Roadmap — Sequel III (Phases 11–15): Frontiers

Adopted: 2026-08-09 · Status: active · Mode: llm-driven
Continues: [`multi-phase-development-roadmap-sequel-2.md`](multi-phase-development-roadmap-sequel-2.md) (Phases 6–10)
Linked goal stack: `rack/goals_stack.json` (goal-stack-001, T0–T3)
Maturity arc: Phases 11–15 — **Distributed Autonomy** (generalize →
collaborate → federate → attest → persist).

Sequel II made the system a governed, self-modeling organization. Sequel
III pushes beyond a single repo: the loop stack generalizes to other
projects, opens to collaborators, federates memory across instances,
pins behavior with invariants, and finally runs over a 30-day horizon
with human oversight as the exception, not the default.

## Phase 11 — Cross-Project Generalization

Goal: RSIS3's loop stack stops being Cosmos-only and becomes a reusable
engine for any repository.

- **Project profile**: `rsis init --project <repo>` scaffolds a profile
  (goals, allowed paths, loop tuning, SPACE series) so the same L1–L9
  engine runs against an external repo with its own workspace and state.
- **Goal sourcing**: `from-space` rotation and MyKB goal sourcing work
  per-project; each project gets its own synthesis namespace under a
  shared MyKB (project-tagged).
- **Shared infrastructure**: one bridge/daemon process can host N
  projects (`--project` routing in `/api/cosmos` and `/api/chat`), so
  the ops investment (Phases 4–5) amortizes.
- **Cross-project learning**: syntheses distilled in one project become
  goal seeds for another via the memory API (Phase 6), with provenance.
- **Exit criterion**: two external repositories run the full loop stack
  for a week (CI green, nightly summaries per project) with zero changes
  to the core engine files.

## Phase 12 — Collaborative & Community Ops

Goal: humans other than the maintainer can observe, question, and steer
the system safely.

- **Multi-user auth**: bridge and dashboard move from a shared
  `RSIS_BRIDGE_TOKEN` to per-user sessions (OAuth2/OIDC or a stdlib
  signed-token scheme), with role levels: observer, contributor,
  approver (Phase 9 gates keyed to roles). Authorization is scoped by
  project membership and policy-defined capability, not role alone:
  User → Identity → Role → Project membership → Policy → Capability →
  Action — an approver may not approve every project or every class of
  operation.
- **Proposal review UI**: staged approvals (Phase 9) render in the
  dashboard with diff views and approve/reject actions; activity is
  attributed to the acting user.
- **Shared sessions**: bridge sessions gain optional
  `share/<session-id>` links — read-only public views for collaborators,
  with the token guard retained for writes.
- **Contribution docs**: a CONTRIBUTING-style note in MyKB documents how
  a new collaborator runs the stack, gets a role, and is onboarded by
  the system itself (goal-sourced L2 candidates).
- **Exit criterion**: an observer can read live telemetry and a shared
  session; a contributor can submit a candidate through the normal
  pipeline; an approver can gate and apply it — all with per-user audit
  attribution, no console errors.

## Phase 13 — Federated Memory

Goal: multiple Cosmos instances exchange distilled knowledge without
losing their identity or creating conflicts.

- **Synthesis exchange**: instances publish distilled syntheses
  (subsets, tagged by project/domain) to a federation endpoint or repo;
  subscribers adopt foreign syntheses carrying explicit provenance —
  origin, source, project, session, producer, verification state,
  confidence, transformations and federation history — never silently
  overwriting local notes.
- **Consensus rules**: conflicting durable rules from two instances
  resolve deterministically (newest-by-timestamp for facts, policy wins
  for behavior), and conflicts are logged as federation backlog items.
- **Federation ledger**: `rack/federation/` records publishes, pulls,
  and merges; the nightly summary includes federation activity.
- **Trust boundary**: federation traffic flows over the existing token
  auth + origin guard; private notes never leave an instance unless
  tagged `publishable`.
- **Exit criterion**: two instances (a test pair and the live one)
  exchange ≥1 synthesis each way with zero conflicts; a deliberately
  conflicting rule is resolved deterministically and logged.

## Phase 14 — Continual Verification & Invariant Attestation

Goal: behavior is pinned by checks that run every cycle, not just at
release time.

- **Invariant registry**: `rack/invariants.json` declares invariants
  (state-file disjointness, telemetry coverage, KG idempotency, envelope
  additivity) as executable checks; `check-practices` runs them every
  cycle.
- **Lightweight formal checks**: Python candidates get type-check and
  AST invariant passes; state files get schema checks; the envelope gets
  a conformance test against the spec (already covered by unit tests —
  promoted to the registry).
- **Attestation**: every applied candidate and every nightly summary
  carries a signed (sha256) attestation of the invariant set it passed;
  CI fails on any drift. This extends the Phase 7 regression ledger and
  verification mesh into a per-cycle attestation layer.
- **Drift repair**: a failed invariant files a backlog note and, for
  self-repairable ones (e.g., stale flag edges — already proven
  fixable), the system repairs and re-attests.
- **Exit criterion**: 30 consecutive cycles with zero invariant drift;
  an injected drift is detected, repaired, and re-attested within one
  cycle; attestations exist for every applied candidate.

## Phase 15 — Long-Horizon Autonomy

Goal: the system runs itself over months; humans review, not drive.
Phase 15 does not introduce autonomy — it extends Phase 5's *bounded*
autonomy into a persistent lifecycle: seasonal goal rotation,
energy-aware scheduling, configuration self-repair, and human approval
only at the policy-revision boundary.

- **Seasonal goal rotation**: the goal stack rotates through
  domain/tier seasons on a policy-defined cadence, so L2 keeps finding
  new work instead of repeating plateaued patterns.
- **Energy-aware scheduling**: the daemon adapts cadence and LLM use to
  cost budgets (Phase 8) and forecast (Phase 10) — sprint during
  improvement phases, coast at plateau, pause under budget pressure.
- **Self-repair of configuration**: policy violations, broken state
  files, and stuck locks trigger defined recovery procedures (extends
  `--supervise-bridge` to the whole stack), each logged as an incident.
- **Quarterly review loop**: a scheduled review synthesizes the quarter
  (nightlies, audits, forecasts, federation) into a policy-revision
  proposal for human approval — the only required human touchpoint.
- **Exit criterion**: 30 days unattended with zero manual intervention:
  cycles on cadence, one bounded retune per convergence episode, nightly
  + quarterly summaries present, budgets respected, all incidents
  self-recovered and logged, CI green on every commit.

## Sequencing notes (Sequel III)

- Cross-project (11) depends on distributed memory (6) and the
  verification mesh (7); collaboration (12) depends on governance (9);
  federation (13) depends on the publish/subscribe memory API (6) and
  trust boundaries (9).
- Invariants (14) must land before long-horizon autonomy (15) — you
  cannot leave the system alone for 30 days until behavior is pinned
  and attestable.
- Every phase ends with a MyKB synthesis + snapshot regeneration per the
  standing L3 memory-consolidation practice.

## Status

| Phase | Area | Status |
|-------|------|--------|
| Phase 11 — Cross-project generalization | engine | ⏳ queued |
| Phase 12 — Collaborative & community ops | governance | ⏳ queued |
| Phase 13 — Federated memory | memory | ⏳ queued |
| Phase 14 — Continual verification & invariants | verification | ⏳ queued |
| Phase 15 — Long-horizon autonomy | autonomy | ⏳ queued |
