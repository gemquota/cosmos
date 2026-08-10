# Multi-Phase Development Roadmap — Sequel IV (Phases 16–20): Open Autonomy

Adopted: 2026-08-10 · Status: active · Mode: llm-driven
Continues: [`multi-phase-development-roadmap-sequel-3.md`](multi-phase-development-roadmap-sequel-3.md) (Phases 11–15 ✅)
Linked goal stack: `rack/goals_stack.json` (goal-stack-001, T0–T3)
Maturity arc: Phases 16–20 — **Open Autonomy** (audit → standardize →
port → probe → open).

Sequel III made the system self-sufficient across projects, people and
instances, with behavior pinned by invariants over a 30-day horizon. The
next step is not more capability — it is *externalized trust*: the system
stops being trusted because it says so and becomes verifiable, portable
and safely programmable by anyone. Internal attestation (Phase 14)
becomes public audit; private interfaces become a protocol; one repo
becomes a portable instance; outsiders become first-class evaluators; and
third parties become governed users.

## Phase 16 — Public Attestation & External Audit

Goal: attestations are independently verifiable by third parties that do
not trust the instance at all.

- **Attestation chain**: `rack/attestations/` becomes a hash-linked
  transparency log — every record includes the previous record's sha256 —
  so tampering with any record is detectable without trusting the writer.
- **Verifier bundle**: `rsis attestations export` renders a self-contained
  bundle (attestation records + invariant registry + gate code shas) that
  a third party can replay offline.
- **Independent re-verification**: `rsis verify-replay <candidate-sha>`
  re-runs the Phase 7 gates from the recorded artifacts and compares the
  result to the ledger decision.
- **Standalone verifier**: a small tool that takes a bundle and reproduces
  the decision with zero access to instance state.
- **Exit criterion**: an external verifier replays a recorded candidate
  from the exported bundle and reproduces the ledger decision; altering
  one record breaks the chain detectably.

## Phase 17 — Open Interop Protocol

Goal: the loop stack's interfaces become a versioned protocol any client
can implement.

- **Protocol spec**: `docs/protocol.md` versions the memory API (6),
  verification API (7), federation envelope (13) and attestation bundle
  (16) as `cosmos-protocol/1`.
- **Conformance suite**: a protocol conformance test (extending the
  envelope tests) that runs against any implementation, RSIS or not.
- **Reference client**: a non-Python client (plain HTTP/curl or JS)
  drives the full read path from the spec alone.
- **Version negotiation**: `/api/version` + capability handshake; unknown
  or unsupported versions fail closed.
- **Exit criterion**: a non-Cosmos client implements the spec from the
  docs alone and passes the conformance suite against a live instance.

## Phase 18 — Portable Instances & Reproducible Workspaces

Goal: an instance moves between hosts without losing identity or state.

- **Workspace manifest**: `rsis export` writes a self-contained bundle
  (state, telemetry, registries, policy, users, invariants) with a
  manifest and per-file checksums.
- **Cold-start import**: `rsis import` reconstructs the workspace on a
  clean host; identity travels with the bundle.
- **Reproducible environment**: locked dependency manifest and pinned
  toolchain so the engine behaves identically across hosts.
- **Continuity check**: after import, `check-practices` and the invariant
  registry pass with zero drift; audit, verification and forecast history
  are intact.
- **Exit criterion**: an instance exported from host A cold-starts on host
  B and runs a full cycle with zero invariant drift and identical
  telemetry coverage.

## Phase 19 — External Evaluation & Red-Teaming

Goal: adversarial outsiders become a first-class input to the improvement
loop, not an afterthought.

- **Red-team harness**: `rsis redteam` probes policy gates (9), budget
  fail-closes (8), invariant checks (14) and authz (12) with adversarial
  inputs; every finding becomes a tracked incident (15) or a policy gap.
- **External feedback intake**: a structured feedback API where external
  reports enter the backlog as goal seeds (11).
- **Evaluation loop**: findings are triaged — repair (14), policy change
  (9), or backlog — and each resolution is attested (14).
- **CI integration**: the harness runs in CI; a regression in gate
  strength fails the build.
- **Exit criterion**: the harness runs in CI with zero un-triaged
  findings; at least one real policy or invariant gap found by the harness
  has been fixed and re-attested.

## Phase 20 — Public API Surface

Goal: third-party applications interact with the system safely at scale.

- **Versioned public API**: stable endpoints for context reads, candidate
  submission and verification results, behind per-app identity extending
  the Phase 12 user model to machine identities.
- **Quota & budgets**: per-app rate limits and cost budgets (8) enforced
  fail-close; app spend is accounted in the cost ledger.
- **App governance**: apps receive capabilities scoped by policy (9) —
  an app can never escalate roles; every app action is
  audit-attributable (9).
- **Developer surface**: an "Apps" view in the dashboard to issue app
  credentials and inspect usage.
- **Exit criterion**: an external app submits a candidate through the
  public API that flows policy → verification → (approval) →
  attestation with full attribution; a quota breach fails closed.

## Sequencing notes (Sequel IV)

- Phases are cumulative and intentionally ordered: audit (16) must precede
  protocol (17) because the protocol carries attestations; portability
  (18) needs the Phase 3 state + Phase 4 telemetry + Phase 11 profile
  patterns to package a workspace.
- Red-teaming (19) is deliberately last-but-one: it can only probe
  meaningfully once policy (9), budgets (8), invariants (14) and authz
  (12) exist — otherwise it tests scaffolding, not controls.
- Public API (20) reuses the Phase 12 identity chain and Phase 8 budgets;
  machine identities are users with capabilities, not a parallel system.
- Every phase ends with a MyKB synthesis + snapshot regeneration per the
  standing L3 memory-consolidation practice.

## Status

| Phase | Area | Status |
|-------|------|--------|
| Phase 16 — Public attestation & external audit | verification | ⏳ queued |
| Phase 17 — Open interop protocol | protocol | ⏳ queued |
| Phase 18 — Portable instances & reproducible workspaces | ops | ⏳ queued |
| Phase 19 — External evaluation & red-teaming | security | ⏳ queued |
| Phase 20 — Public API surface | product | ⏳ queued |
