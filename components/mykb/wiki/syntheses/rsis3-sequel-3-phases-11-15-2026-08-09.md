---
type: "synthesis"
title: "RSIS3 Sequel III complete — Phases 11–15 (cross-project, collaboration, federation, invariants, long-horizon autonomy)"
description: "Implemented Sequel III: project profiles + goal seeds (11), per-user signed-token authz with role/capability gates (12), federated memory with provenance + consensus (13), executable invariant registry with sha256 attestation + self-repair (14), seasonal goals + energy-aware scheduling + quarterly review (15) — 285 tests green"
tags: ["rsis3", "sequel-3", "phase-11", "phase-12", "phase-13", "phase-14", "phase-15", "projects", "users", "federation", "invariants", "seasons"]
timestamp: "2026-08-09T19:00:00Z"
status: "stable"
---

# RSIS3 Sequel III — Phases 11–15 (complete)

Sequel III pushes Cosmos beyond a single repo: the loop stack generalizes
(11), opens to collaborators (12), federates memory (13), pins behavior
with invariants (14), and runs over a 30-day horizon (15). Implementation
is delivered; the long-horizon exit criteria (2-repo week, multi-user
ops, 2-instance federation, 30-cycle zero drift, 30-day unattended) run
on the live daemon cadence.

## Phase 11 — Cross-project generalization (`rsis/projects.py`)

- `rsis init --project <repo>` scaffolds `rack/projects/<slug>.json` with
  goals, allowed paths, loop tuning and SPACE series; `rsis projects`
  lists profiles.
- `launch`/`cycle-daemon --project <name>` source L2 goals from the
  profile; `plan_batch(..., goal=...)` overrides the run-loop goal while
  non-run loops keep their defaults.
- Cross-project learning: MyKB syntheses tagged `project:<name>` become
  goal seeds with provenance (origin note, project, source, timestamp)
  via `project_goal_seeds` — knowledge distilled in one project seeds
  another.
- Bridge `/api/cosmos?project=<name>` routes per project (profile merged
  into the snapshot), one process hosting N projects.
- Tests: `tests/test_projects.py` (7).

## Phase 12 — Collaborative & community ops (`rsis/users.py` + bridge)

- Per-user identities in `.rsis/users.json`; stdlib HMAC-SHA256 signed
  tokens (`users token --user-id <id>`); expiry enforced.
- Authz chain is never role alone: User → Identity → Role → Project
  membership → Policy → Capability → Action. An approver cannot approve
  projects they are not a member of; `capability_blocks` in policy.json
  wins over role.
- Bridge users mode (`RSIS_USERS_SECRET`): observer read / contributor
  propose / approver approve gates; legacy `RSIS_BRIDGE_TOKEN` and public
  modes preserved. New endpoints: `GET /api/approvals` (diff view),
  `POST /api/approvals/<id>/approve|reject` (actor-attributed via
  `--actor <user>`), `GET /api/sessions/<id>/share` (public read-only).
- Contribution docs: `components/mykb/wiki/development/cosmos-contributing.md`.
- Tests: `tests/test_users.py` (7); bridge auth/approvals exercised live
  (401 no token, 403 non-member, 200 member+role).

## Phase 13 — Federated memory (`rsis/federation.py`)

- `publish` moves only notes tagged `publishable`; the envelope carries
  explicit provenance (origin, source, project, session, producer,
  verification state, confidence, transformations, federation history).
- `pull` adopts create-only (suffixed on collision), never overwrites;
  consensus is deterministic — newest-by-timestamp wins for facts, local
  policy wins for behavior; conflicts log to `rack/federation/backlog.jsonl`.
- `rack/federation/ledger.jsonl` records every publish/pull/merge; the
  nightly summary includes federation activity.
- CLI: `rsis federation publish|pull|status`.
- Tests: `tests/test_federation.py` (7).

## Phase 14 — Continual verification & invariants (`rsis/invariants.py`)

- `rack/invariants.json` registry (executable): state-file disjointness,
  telemetry coverage, KG idempotency, state schemas, envelope
  conformance, AST invariants, stale locks — run every cycle via
  `check-practices`.
- `attest` signs (sha256) every applied candidate (wired into
  `verify.record_verification`) and every nightly summary.
- `repair` fixes self-repairable drift (KG idempotency dedupe, stale lock
  removal) and files MyKB backlog notes for remaining drift.
- Live: first run detected 474 duplicate KG edge ids and repaired them
  (7/7 invariants pass); my own bridge edit on a gated path was flagged
  and passed through the Phase 9 approval gate.
- Tests: `tests/test_invariants.py` (6).

## Phase 15 — Long-horizon autonomy (`rsis/seasons.py` + daemon)

- Seasonal goal rotation: `rack/seasons.json` + policy-defined cadence
  (`season_rotation` in policy.json); L2 goals per season domain.
- Energy-aware scheduling: `energy_mode` (sprint/coast/idle/pause) from
  forecast trend + budget pressure; `adaptive_sleep` composes Phase 10
  cadence with the energy factor; the daemon pauses under budget breach.
- Self-repair: recovery procedures for repairable invariants + policy
  violations, each logged as an incident to `rack/incidents.jsonl`
  (daemon runs it after failed cycles).
- Quarterly review loop: `rsis seasons review` synthesizes the quarter
  (nightlies, audits, forecasts, federation, incidents) into a
  policy-revision proposal staged for human approval — the only required
  human touchpoint.
- Tests: `tests/test_seasons.py` (9).

## Validation

- 285/285 pytest (36 new Sequel III tests), 8/8 bridge envelope tests,
  contracts 0 FAIL, `check-practices` all PASS (after live invariant
  repair), `gen-static-data.py --check` OK.
- Live: `init --project`, `projects`, `users` (add/token/check),
  `seasons` (status/rotate/review), `invariants --repair`, `federation
  status`, bridge users-mode endpoints all exercised.

## Related

- [[wiki/syntheses/rsis3-roadmap-sequels-2-3-2026-08-09|RSIS3 roadmap sequels II–III (Phases 6–15)]]
- [[wiki/syntheses/rsis3-sequel-2-phases-6-10-2026-08-09|RSIS3 Sequel II — Phases 6–10]]
- [[wiki/development/cosmos-contributing|Contributing to Cosmos]]
