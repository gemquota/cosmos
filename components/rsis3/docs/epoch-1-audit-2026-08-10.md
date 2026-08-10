# Epoch 1 Audit — Phases 1–50 (2026-08-10)

Audit of all 50 phases of Epoch 1 (Sequels I–X) against the roadmap docs, implementation evidence, tests, telemetry, live workspace state and the telemetry/static-data contracts. Every phase was checked for: module/CLI/endpoint implementation, tests, telemetry events, dashboard surfacing, doc status accuracy, and exit-criterion status.

## Executive summary

- **50/50 phases** have implementation evidence (module, CLI/endpoint, or bridge/dashboard surface).
- **Status accuracy**: docs say phases 1–4 `✅ delivered`, phases 5–50 `✅ delivered (implementation) · ⏳ live validation pending` — the audit confirms this framing is correct: implementation is delivered; **no operational exit criterion has been demonstrated** (all remain live-validation pending).
- **Tests**: 357 passing (353 prior + 4 new protocol-conformance), 3 pre-existing failures in `test_budgets.py`/`test_seasons.py` (P8/P15).
- **Telemetry**: 94 epoch-1 events in `.rsis/telemetry/epoch1.jsonl` covering all 35 phase-16–50 flows; loop/self-assess telemetry covers phases 1–15; dashboard Epoch 1 panel surfaces per-sequel counts.
- **Contracts**: `contracts/validate.py` 0 FAIL; `gen-static-data.py --check` OK.
- **Findings**: 8 findings (4 implementation gaps, 2 pre-existing defects, 2 info) — see Findings. Highest-value: P7 verification ledger empty live, P8 budget enforcement never exercised, P19 probes surface path-traversal policy gaps.

## Sequel I — Phases 1–5

| Phase | Title | Evidence | Tests | Telemetry | Live state | Verdict | Notes |
|---|---|---|---|---|---|---|---|
| P1 | Live state streaming | `rack/bridge/server.mjs` `GET /api/events` SSE + `rack/bridge/events.mjs`; dashboard `bridge.js` EventSource feed; cycle archives `rack/bridge/cycles/2026-08-*.jsonl` | test_bridge.py | l1–l9 loop events, `tool_call` | rack/bridge/cycles | ✅ delivered |
| P2 | Envelope hardening | `rack/bridge/envelope.mjs` `cosmos-envelope/1` v1.1 (typed artifacts, per-type caps, allowlist, streaming); `rack/bridge/allowlist.json`; rate limit + origin guard | test_bridge.py, bridge-envelope.test.mjs | loop events | rack/bridge/allowlist.json | ✅ delivered |
| P3 | Product surface | `/api/sessions[/:id][/share]` + `SESSIONS_DIR` persistence; shared `dashboard/bridge.js`; `RSIS_BRIDGE_TOKEN` auth; responsive keyboard shortcuts | test_bridge.py | loop events | — (no live session files yet) | ✅ delivered | ⚠️ sessions implemented (`/api/sessions`, SESSIONS_DIR) but no live session files in the workspace yet |
| P4 | Ops maturity | `.github/workflows/ci.yml` (Phase 4) + loops/nightly/health; `rsis/ops_daemon.py` + `cycle-daemon` CLI + lockfile `rack/cycle-daemon.lock`; backoff | test_ops_daemon.py, test_convergence.py | loop events | rack/cycle-daemon.lock | ✅ delivered |
| P5 | Autonomy & durable ops (bounded) | `rsis/nightly.py` + `nightly-summary` CLI + `nightly.yml`; `self_assess.py` (`sa_start/sa_complete`); `convergence.py` + `rack/proposals/convergence-*.json`; `.rsis/costs.jsonl` + `/api/cosmos` costs; `strategies.json` bounded retune | test_nightly.py, test_self_assess.py | sa_start/sa_complete | .rsis/costs.jsonl, rack/proposals | ✅ implemented (validation pending) |

## Sequel II — Phases 6–10

| Phase | Title | Evidence | Tests | Telemetry | Live state | Verdict | Notes |
|---|---|---|---|---|---|---|---|
| P6 | Distributed memory & multi-session coordination | `components/mykb/.wiki-daemon/memory_api.py` (search/notes/kg) + running daemon; `rsis/shared_memory.py` (OCC/mutexes); `rsis/mykb_gateway.py`; `.rsis/vectors` + `knowledge_graph.json` | test_memory_api.py, test_shared_memory.py, test_mykb_gateway.py | kg/loop events | .rsis/vectors, .rsis/knowledge_graph.json | ✅ implemented (validation pending) |
| P7 | Verification mesh | `rsis/verify.py` gates (contracts + property checks; evaluator path/compile/AST/regression) + verify-server :8788 (`/health /verify /ledger /version`); ledger `rack/verification/<day>.jsonl` | test_epoch1_sequel4 (replay), test_protocol.py | loop events | rack/verification (empty live) | ✅ implemented (validation pending) | ⚠️ ledger code + server live, but `rack/verification/` holds no records — no candidate verified in-workspace recently |
| P8 | Observability & cost governance | `rsis/anomalies.py` + `anomalies` CLI; `rsis/budgets.py` (per-loop caps + ceiling, fail-closed); dashboard cost display | test_anomalies.py, test_budgets.py | anomaly events | .rsis/budgets.json (defaults only) | ✅ implemented (validation pending) | ⚠️ `.rsis/budgets.json` absent (defaults in use); no `cost.budget_hit` events; 2 pre-existing test failures |
| P9 | Human-in-the-loop governance | `rsis/policy.py` (requires_approval, stage_candidate); `approve` CLI; `rsis/audit.py` + `audit` CLI + `.rsis/audit.jsonl` replay; `rsis/rollback.py`; `rack/approvals/*.json` staged | test_policy.py | policy/approval events | rack/approvals, .rsis/audit.jsonl | ✅ implemented (validation pending) |
| P10 | Self-modeling & prediction | `rsis/forecast.py` + `forecast` CLI + `rack/forecasts/forecasts.jsonl`; nightly forecast quality | test_forecast.py | forecast events | rack/forecasts | ✅ implemented (validation pending) |

## Sequel III — Phases 11–15

| Phase | Title | Evidence | Tests | Telemetry | Live state | Verdict | Notes |
|---|---|---|---|---|---|---|---|
| P11 | Cross-project generalization | `rsis/projects.py` + `projects` CLI + `rack/projects/*.json` profiles (project goals/paths/SPACE); `launch --project` | test_projects.py, test_launch.py | loop events | rack/projects | ✅ implemented (validation pending) |
| P12 | Collaborative & community ops | `rsis/users.py` + `users` CLI + `.rsis/users.json`; HMAC tokens; authorize chain role→membership→policy→action | test_users.py | loop events | .rsis/users.json | ✅ implemented (validation pending) |
| P13 | Federated memory | `rsis/federation.py` + `federation` CLI; `rack/federation/{peers,ledger,exchange,backlog}` | test_federation.py | federation events | rack/federation | ✅ implemented (validation pending) |
| P14 | Continual verification & invariants | `rsis/invariants.py` + `rack/invariants.json`; `invariants` + `check-practices` CLIs; attest + self-repair | test_invariants.py | loop events | rack/invariants.json | ✅ implemented (validation pending) |
| P15 | Long-horizon autonomy | `rsis/seasons.py` + `rack/seasons.json` (energy modes); `rsis/scheduler.py` + `scheduler` CLI; `recovery-test` CLI | test_seasons.py | season events | rack/seasons.json | ✅ implemented (validation pending) | ⚠️ 1 pre-existing test failure (energy-mode/budget pause interplay) |

## Sequel IV — Phases 16–20

| Phase | Title | Evidence | Tests | Telemetry | Live state | Verdict | Notes |
|---|---|---|---|---|---|---|---|
| P16 | Public attestation & external audit | `rsis/attestations.py` + `attestations` CLI: hash-chained `rack/attestations/chain.jsonl`, verifier bundles, replay | test_epoch1_sequel4.py | attestation_appended/exported | rack/attestations | ✅ implemented (validation pending) |
| P17 | Open interop protocol | `rsis/protocol.py` + `docs/protocol.md` (`cosmos-protocol/1`); `/version` handshake on verify-server; `tests/test_protocol.py` conformance (unit + live HTTP) | test_protocol.py, test_epoch1_sequel4.py | protocol events | docs/protocol.md | ✅ implemented (validation pending) | ⚠️ fixed during audit: running verify-server predated `/version`; restarted; `tests/test_protocol.py` added (4 passing) |
| P18 | Portable instances & reproducible workspaces | `rsis/portable.py` + `export`/`import` CLI: tar bundle + manifest + checksums + continuity; engine travels, `instance.key` excluded | test_epoch1_sequel4.py | portable_exported/imported | rack/portable | ✅ implemented (validation pending) |
| P19 | External evaluation & red-teaming | `rsis/redteam.py` + `redteam` CLI: probes (policy gate, traversal, budget, invariants, authz) + CI mode | test_epoch1_sequel4.py | redteam_probe/triaged | rack/redteam | ✅ implemented (validation pending) | ⚠️ live probes find 3 path-traversal gaps (see F4) |
| P20 | Public API surface | `rsis/apps.py` + `apps`/`apps-server` CLI: machine identities, tokens, quotas, public API :8790 | test_epoch1_sequel4.py | apps_registered/candidate_submitted | .rsis/apps.json | ✅ implemented (validation pending) |

## Sequel V — Phases 21–25

| Phase | Title | Evidence | Tests | Telemetry | Live state | Verdict | Notes |
|---|---|---|---|---|---|---|---|
| P21 | Instance identity & trust graph | `rsis/identity.py` + `instance` CLI: Ed25519 keys, peers, rotation with verify-only retirement | test_epoch1_sequel5.py | identity_peer_registered/key_rotated | .rsis/identity | ✅ implemented (validation pending) |
| P22 | Knowledge economy & exchange at scale | `rsis/exchange.py` + `exchange` CLI: confidence propagation, canonicalization, provenance hops, ledger | test_epoch1_sequel5.py | exchange_confidence/adopted/deduped | .rsis/confidence.json, rack/exchange, rack/federation/exchange.jsonl | ✅ implemented (validation pending) |
| P23 | Swarm coordination & distributed cycles | `rsis/swarm.py` + `swarm` CLI: dispatch/accept/verdict, corroboration quorum, deterministic reconcile, fail-over | test_epoch1_sequel5.py | swarm_dispatched/corroborated/reconciled | rack/swarm | ✅ implemented (validation pending) |
| P24 | Population governance | `rsis/popgov.py` + `popgov` CLI: shared rules, local-policy-wins, quorum votes, divergence resolution | test_epoch1_sequel5.py | popgov_rules/quorum_* | rack/popgov, rack/federation/backlog.jsonl | ✅ implemented (validation pending) |
| P25 | Ecosystem resilience | `rsis/resilience.py` + `resilience` CLI: churn, partition degrade/reconcile, fork merge, survival drill | test_epoch1_sequel5.py | resilience_* | rack/resilience | ✅ implemented (validation pending) |

## Sequel VI — Phases 26–30

| Phase | Title | Evidence | Tests | Telemetry | Live state | Verdict | Notes |
|---|---|---|---|---|---|---|---|
| P26 | Meta-governance | `rsis/metagov.py` + `metagov` CLI: evidence-backed proposals, invariant scoring, human ratification, meta-invariant check | test_epoch1_sequel6.py | metagov_proposed/scored/ratified | rack/metagov | ✅ implemented (validation pending) |
| P27 | Resource sovereignty & sustainability | `rsis/capacity.py` + `capacity` CLI: 90-day plan, sustainability accounting, degradation ladder | test_epoch1_sequel6.py | capacity_plan/sustainability/degraded | rack/capacity | ✅ implemented (validation pending) |
| P28 | Self-directed learning goals | `rsis/goals.py` + `goals` CLI: gap proposals, ratification, fitness telemetry, plateau retirement | test_epoch1_sequel6.py | goals_proposed/ratified/retired | rack/goals | ✅ implemented (validation pending) |
| P29 | Autonomous stewardship | `rsis/steward.py` + `steward` CLI: monitor, onboard profiles, attested custody actions, handoff | test_epoch1_sequel6.py | steward_* | rack/stewardship | ✅ implemented (validation pending) |
| P30 | Enduring autonomy | `rsis/endurance.py` + `endurance` CLI: guardrail battery (meta-invariant, invariants, budget, energy, redteam) + continuity | test_epoch1_sequel6.py | endurance_guardrails | rack/endurance | ✅ implemented (validation pending) |

## Sequel VII — Phases 31–35

| Phase | Title | Evidence | Tests | Telemetry | Live state | Verdict | Notes |
|---|---|---|---|---|---|---|---|
| P31 | Knowledge inheritance | `rsis/inheritance.py` + `inheritance` CLI: curriculum bundles, adoption, parity ≥ 0.98 | test_epoch1_sequel7.py | inheritance_exported/adopted/parity | rack/inheritance | ✅ implemented (validation pending) |
| P32 | Archival immortality | `rsis/archival.py` + `archival` CLI: checksum registry, bit-rot patrol + replica rebuild, format migration | test_epoch1_sequel7.py | archive_patrol/migrated | rack/archival | ✅ implemented (validation pending) |
| P33 | Succession planning | `rsis/succession.py` + `succession` CLI: heir planning from trust graph, dual-running transfers | test_epoch1_sequel7.py | succession_planned/transferred | rack/succession | ✅ implemented (validation pending) |
| P34 | Mission continuity | `rsis/missions.py` + `missions` CLI: attestable contiguous checkpoints, steward handoff at exact resume point | test_epoch1_sequel7.py | mission_created/progress/handoff | rack/missions | ✅ implemented (validation pending) |
| P35 | Generational resilience | `rsis/generations.py` + `generations` CLI: dependency obsolescence, staleness, environment drift scans | test_epoch1_sequel7.py | generation_obsolete/drift | rack/generations | ✅ implemented (validation pending) |

## Sequel VIII — Phases 36–40

| Phase | Title | Evidence | Tests | Telemetry | Live state | Verdict | Notes |
|---|---|---|---|---|---|---|---|
| P36 | Explainable autonomy | `rsis/explain.py` + `explain` CLI: 3-depth rationales from verification ledger, counterfactuals | test_epoch1_sequel8.py | decision_explained/counterfactual | rack/explanations | ✅ implemented (validation pending) |
| P37 | Natural-language policy | `rsis/nlpolicy.py` + `nlpolicy` CLI: plain-language compile→policy, conflict flags, round-trip | test_epoch1_sequel8.py | policy_compiled/roundtrip | rack/policy_nl.json | ✅ implemented (validation pending) |
| P38 | Delegation contracts | `rsis/delegation.py` + `delegation` CLI: bounded contracts (scope/expiry/budget), fail-closed breach, instant revocation | test_epoch1_sequel8.py | delegation_issued/executed/blocked/revoked | .rsis/delegations.json | ✅ implemented (validation pending) |
| P39 | Trust calibration | `rsis/trust.py` + `trust` CLI: ask-vs-act outcomes, over/under-trust metrics, recalibration | test_epoch1_sequel8.py | trust_asked/acted/recalibrated | rack/trust | ✅ implemented (validation pending) |
| P40 | Co-design workspaces | `rsis/codesign.py` + `codesign` CLI: canvases, human/system artifacts, merged plans with authorship, goal handoff | test_epoch1_sequel8.py | codesign_canvas/proposed/merged | rack/codesign | ✅ implemented (validation pending) |

## Sequel IX — Phases 41–45

| Phase | Title | Evidence | Tests | Telemetry | Live state | Verdict | Notes |
|---|---|---|---|---|---|---|---|
| P41 | Cross-ecosystem standards | `rsis/standards.py` + `standards` CLI: version registry, deprecation windows, conformance status | test_epoch1_sequel9.py | standard_version/deprecated | rack/standards | ✅ implemented (validation pending) |
| P42 | Global knowledge commons | `rsis/commons.py` + `commons` CLI: attributed publishing, adoption credits, free-rider surfacing | test_epoch1_sequel9.py | commons_published/adopted | rack/commons | ✅ implemented (validation pending) |
| P43 | Inter-population diplomacy | `rsis/diplomacy.py` + `diplomacy` CLI: treaties with capability bounds, disputes, resolution | test_epoch1_sequel9.py | treaty_signed/violated/resolved | rack/diplomacy | ✅ implemented (validation pending) |
| P44 | Crisis response | `rsis/crisis.py` + `crisis` CLI: fail-closed profiles, drills (policy-critical stays on), attested exit | test_epoch1_sequel9.py | crisis_entered/drill/exit | rack/crisis | ✅ implemented (validation pending) |
| P45 | Planetary stewardship | `rsis/planetary.py` + `planetary` CLI: shared resource plans, commons health (replication/attribution/trust) | test_epoch1_sequel9.py | commons_resource/health | rack/planetary | ✅ implemented (validation pending) |

## Sequel X — Phases 46–50

| Phase | Title | Evidence | Tests | Telemetry | Live state | Verdict | Notes |
|---|---|---|---|---|---|---|---|
| P46 | Self-metrics & longitudinal studies | `rsis/longitudinal.py` + `longitudinal` CLI: append-only metric registry, declarative studies, trend decomposition | test_epoch1_sequel10.py | study_snapshot/defined | rack/longitudinal | ✅ implemented (validation pending) |
| P47 | Hypothesis-driven self-experimentation | `rsis/experiments.py` + `experiments` CLI: A/B cohorts, sample-size + min-effect guardrails, attestation | test_epoch1_sequel10.py | experiment_started/completed/terminated | rack/experiments | ✅ implemented (validation pending) |
| P48 | Failure understanding | `rsis/failures.py` + `failures` CLI: root-cause corpus, clustering, near-miss records, prevention proposals | test_epoch1_sequel10.py | failure_archived/clustered, nearmiss_recorded | rack/failures | ✅ implemented (validation pending) |
| P49 | Formal meta-invariant proof | `rsis/metainvariant.py` + `metainvariant` CLI: P1–P3 model-checking, attested proofs, commons publish | test_epoch1_sequel10.py | meta_invariant_checked/proven | rack/metainvariant | ✅ implemented (validation pending) |
| P50 | Epoch capstone: enduring intelligence | `rsis/epoch.py` + `epoch` CLI: decade program, epochs registry, capstone check | test_epoch1_sequel10.py | epoch_decade_ratified/reported/enduring | rack/epochs, rack/epochs.json | ✅ implemented (validation pending) |

## Findings

**F1 — P7 verification ledger is not accumulating (Medium).** `rsis/verify.py` and the verify-server are live (`/health /verify /ledger /version` on :8788), but `rack/verification/` holds no records, so P16 replay/attestation has never run against a real candidate. Recommendation: verify the next applied candidate (or run red-team candidates through `verify_candidate`) so the ledger + attestation replay become exercised.

**F2 — P8 budget enforcement never exercised live (Medium).** `.rsis/budgets.json` is absent (defaults in use), and no `cost.budget_hit` events exist. The dashboard shows costs from `.rsis/costs.jsonl`, but fail-closed budget behavior is untested outside unit tests. Recommendation: materialize `budgets.json`, run a breach drill, and verify the fail-closed event.

**F3 — P3 conversation persistence unexercised (Low).** `/api/sessions`, share links and `SESSIONS_DIR` are implemented, but no `rack/bridge/sessions/*.jsonl` exist — persistence only works if a chat actually runs. Recommendation: exercise one chat session through the bridge.

**F4 — P19 probes find 3 path-traversal gaps (Medium).** `redteam` on the live workspace reports `../../etc/passwd`, `/etc/passwd`, `wiki/../.rsis/secrets` are not approval-gated under the default policy (approval-required paths are exact-match). Probe results are not persisted, so the gap is silent. Recommendation: add traversal patterns to `approval_required.patterns` (or normalize paths before gating), persist findings, and re-run until 0 findings so CI mode is meaningful.

**F5 — P15/P8 pre-existing test failures (Medium).** `test_budgets.py` (2) and `test_seasons.py` (1) fail: budget-status shape and energy-mode→budget-pause interplay. They predate epoch-1 work, but they pin the exact P8/P15 boundary and should be fixed before P8/P15 operational validation.

**F6 — P17 conformance suite gap (Low, fixed during audit).** `rack/standards/registry.json` referenced `tests/test_protocol.py`, which did not exist; the running verify-server predated the `/version` handshake. Added `tests/test_protocol.py` (unit + live HTTP conformance, 4 passing) and restarted the verify-server so `GET /version` serves `cosmos-protocol/1`.

**F7 — P21 dev identity key committed (Info).** `.rsis/identity/instance.key` is tracked per the repo’s state-in-git convention. Fine for a dev instance; rotate before any production use (portable bundles already exclude it).

**F8 — Exit criteria all unproven (Info).** None of the operational exit criteria (7-day cadence, 30-cycle zero-drift, 30-day unattended, 2-repo week, 90-day forecast tolerance, etc.) have been demonstrated; the docs’ `⏳ live validation pending` wording is accurate and should stay until each is evidenced in `rack/` state.

## Addendum — findings resolution (2026-08-10, same day as the audit)

All 8 findings were addressed after the audit pass above:

- **F1 (P7 ledger) — addressed.** The gen-210 convergence retune proposal
  (`rack/proposals/convergence-2026-08-10-022442Z.json`) was verified
  through the live verify-server (`POST /verify`): decision PASS,
  evaluator + contracts gates green, 0 contract FAIL. Ledger:
  `rack/verification/2026-08-10.jsonl` (1 record). `attestations replay
  --candidate-sha <sha>` reproduces it (contracts 0 fail re-run).
- **F2 (P8 budgets) — addressed.** `.rsis/budgets.json` materialized
  (evaluator $0.05/day, default $0.02, ceiling $0.50 — today's spend
  $0.0084). `python -m rsis budgets drill` (new CLI: `status` + `drill`)
  ran an isolated breach: fail-closed, `cost.budget_hit` recorded, and
  `cost_budget_drill` telemetry persisted.
- **F3 (P3 sessions) — addressed.** A throwaway bridge instance exercised
  `POST /api/chat`; `rack/bridge/sessions/epoch1-audit-f3-session.jsonl`
  persists envelope-shaped user/assistant exchanges (LLM connected).
- **F4 (P19 traversal) — addressed.** `requires_approval` now
  canonicalizes target paths (`_canonical`): absolute paths, `..` segments
  and escape-to-outside paths are always approval-gated; the same
  canonical match applies in `check_unauthorized_writes`. New traversal
  test in `tests/test_policy.py`; live `redteam run --ci` → 0 findings,
  0 untriaged, exit 0.
- **F5 (test failures) — addressed.** Root cause was date-coupled tests
  (hardcoded 2026-08-09 timestamps vs. day-scoped budget checks). Tests
  now use the current UTC day; `test_budgets.py` + `test_seasons.py` all
  green.
- **F6 (protocol conformance) — addressed during the audit.** See above.
- **F7 (identity key) — addressed (info → covered).** Portable export
  exclusion verified by new `test_export_excludes_identity_key`; rotation
  procedure documented in `docs/epoch-1-exit-criteria.md`.
- **F8 (exit criteria) — addressed (info → tracked).** New
  `docs/epoch-1-exit-criteria.md` tracks all 50 criteria with validation
  procedures and evidence locations; the 7-day cadence validation
  procedure is documented there.

## Exit-criteria status

Implementation is delivered for all 50 phases. The following operational validations remain (per sequel docs status tables):

| Group | Validation pending |
|---|---|
| Phases 1–4 | 3-min cadence ≥5 live cards; envelope/HTTP matrix green (unit matrix green); fresh-visitor chat+resume pass |
| Phase 5 | 7-day unattended run with costs + convergence summaries |
| Phases 6–10 | 2-session memory; 100% verification coverage; budget-breach fail-close; approve/reject/rollback; 7-day forecast coverage |
| Phases 11–15 | 2-repo week; multi-user authz; 2-instance exchange; 30-cycle zero-drift; 30-day unattended |
| Phases 16–20 | external bundle replay; non-Cosmos client conformance; cold-start export/import; CI red-team 0 untriaged; app submission |
| Phases 21–25 | 2-instance signed exchange; 3-hop propagation; cross-instance cycle; 3-instance policy propagation; kill-one-mid-cycle |
| Phases 26–30 | 1 season evidence-driven policy; 90-day forecast tolerance; 1 season self-directed goals; 2 peer instances maintained; 365 days with quarterly ratification |
| Phases 31–35 | cold-start inheritance + parity; simulated media failure; custody transfer with overlap; mission across generations; simulated decade churn |
| Phases 36–40 | non-expert why-answer; 3 plain-language rules; bounded delegation; trust-rate targets; joint goal |
| Phases 41–45 | external standard implementation; commons publish→adopt; reciprocity treaty + dispute; crisis drill; 3-ecosystem coordination |
| Phases 46–50 | 90-day study; A/B behavior change; corpus completeness; machine-checkable proof; 10-year program committed |

## Method

Evidence collected from: roadmap + sequel docs (deliverables, exit criteria, status tables); `rsis/*.py` module docstrings; `main.py` subcommand registrations (71 total); `rack/bridge/server.mjs` / `envelope.mjs` / dashboard files; `tests/` (357 tests); `.rsis/telemetry/*.jsonl` event inventory; live `rack/` + `.rsis/` state; `contracts/validate.py` + `gen-static-data.py --check`. Audit date 2026-08-10, run against commit `fe82f841`.
