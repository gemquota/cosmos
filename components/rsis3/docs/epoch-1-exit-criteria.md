# Epoch 1 — Exit-Criteria Validation Tracking

Status tracker for the operational exit criteria of all 50 Epoch 1 phases.
Implementation is delivered for every phase (see
`docs/epoch-1-audit-2026-08-10.md`); **no exit criterion is demonstrated
yet** — each row below becomes `✅ demonstrated` only when its evidence
appears in the listed location. This file is the single source of truth
for the `⏳ live validation pending` wording used in the roadmap docs.

## Validation tracker (machine-readable)

Exit criteria are tracked as **validation windows** in
`rack/validation/windows.json`:

- `python -m rsis validation start --kind p4-24h` — seeds the Phase 4
  24 h window with a start timestamp and expected end.
- `python -m rsis validation checkin` — evaluates the running window
  against live evidence (cycle cards, lockfile, costs, daily summaries,
  retunes, incidents, contracts gate) and appends a dated check-in.
- `python -m rsis validation status` — elapsed/remaining per window.
- When P4's window ends with all criteria passing, P5's 7-day window
  auto-starts with the P4 completion timestamp as its clean start point.
- The nightly summary (`nightly-summary`) runs a check-in automatically
  every day; telemetry events `validation_window_started`,
  `validation_checkin`, `validation_window_completed` record the lifecycle.

## The 7-day cadence validation (Phase 5)

Phase 5's exit criterion is the first long-horizon operational gate in the
program. It requires **7 consecutive days of unattended operation**:

- The `cycle-daemon` runs `launch --cycles 1` every 3 minutes under the
  `rack/cycle-daemon.lock` lockfile (no double-runs, no manual restarts).
- One bounded auto-retune is applied per convergence episode
  (`cycle-daemon --auto-retune`, `RSIS_RETUNE_MIN_INTERVAL_S` = 6 h),
  recorded in `rack/proposals/applied.jsonl`.
- One daily summary note lands in MyKB per day (`nightly-summary`), with a
  `log.md` entry.
- The bridge self-heals within 2 cycles if `/health` fails
  (`--supervise-bridge`).
- CI stays green on every commit (`check-practices` +
  `gen-static-data.py --check` + test suite).

Evidence locations: `rack/bridge/cycles/*.jsonl` (per-cycle cards),
`.rsis/costs.jsonl` (24 h cost ledger), `rack/proposals/applied.jsonl`,
MyKB `syntheses/rsis3-daily-summary-*.md`, `components/mykb/log.md`,
`rack/cycle-daemon.lock`, CI run history. Phase 4's 24 h criterion is the
same cadence proven for one day; Phase 5 extends it to seven.

## Phases 1–5 (Sequels I)

| Phase | Criterion | Validation procedure | Evidence | Status |
|---|---|---|---|---|
| P1 | ≥5 live cards in 3-min cadence, no refresh; deltas <2 s | Watch Bridge tab during a cadence window | `rack/bridge/cycles/` | ⏳ |
| P2 | Envelope/HTTP matrix green (traversal, oversized, rate limit, missing file, text+image) | `python3 -m pytest tests/test_bridge.py` + `bridge-envelope.test.mjs` | tests + allowlist.json | ⏳ (unit matrix green; live matrix pending) |
| P3 | Fresh visitor chats with cosmos context, attaches image, reloads, resumes — no console errors | Manual/scripted fresh-session chat through the bridge | `rack/bridge/sessions/*.jsonl` | ⏳ (one drill session exists; full matrix pending) |
| P4 | 24 h unattended 3-min cadence, rc=0, CI green, nightly summary in MyKB | Run the daemon for 24 h untouched | `rack/bridge/cycles/`, MyKB daily summaries | ⏳ |
| P5 | 7 days unattended: 3-min cadence, 1 bounded retune/episode, 1 daily summary/day, bridge heals ≤2 cycles, CI green | Run the daemon for 7 days untouched | See “7-day cadence validation” above | ⏳ |

## Phases 6–10 (Sequel II)

| Phase | Criterion | Evidence | Status |
|---|---|---|---|
| P6 | 2-session shared memory with coordination | `.rsis/vectors`, `rack/` session records | ⏳ |
| P7 | 100% verification coverage on applied changes | `rack/verification/*.jsonl` (1 record as of 2026-08-10) | ⏳ |
| P8 | Budget-breach fail-close demonstrated | `.rsis/budgets.json`, `.rsis/budget_hits.jsonl`, `cost_budget_drill` telemetry | ⏳ (drill evidence exists; live breach pending) |
| P9 | Approve / reject / rollback cycle | `rack/approvals/*.json`, `.rsis/audit.jsonl` | ⏳ |
| P10 | 7-day forecast coverage ≥80% | `rack/forecast/` + nightly summaries | ⏳ |

## Phases 11–15 (Sequel III)

| Phase | Criterion | Evidence | Status |
|---|---|---|---|
| P11 | 2 external repos run full loop stack 1 week, core engine unchanged | project profiles + daemon logs | ⏳ |
| P12 | Multi-user authz (observer/contributor/approver) | `.rsis/users.json`, bridge users mode | ⏳ |
| P13 | 2-instance signed exchange | `rack/exchange/`, federation ledger | ⏳ |
| P14 | 30 consecutive cycles zero invariant drift; injected drift repaired ≤1 cycle | `rack/invariants.json`, attestations | ⏳ |
| P15 | 30-day unattended run | `rack/seasons.json`, `rack/incidents.jsonl`, nightlies | ⏳ |

## Phases 16–50 (Sequels IV–X)

| Group | Criteria | Evidence rack/ | Status |
|---|---|---|---|
| P16–20 | external bundle replay; non-Cosmos client conformance; cold-start export/import; CI red-team 0 untriaged; app submission | `attestations/`, `portable/`, `redteam/findings.jsonl`, `apps.json` | ⏳ |
| P21–25 | 2-instance signed exchange; 3-hop propagation; cross-instance cycle; 3-instance policy propagation; kill-one-mid-cycle | `federation/`, `swarm/`, `popgov/`, `resilience/` | ⏳ |
| P26–30 | 1 season evidence-driven policy; 90-day forecast tolerance; 1 season self-directed goals; 2 peer instances maintained; 365 days with quarterly ratification | `metagov/`, `capacity/`, `goals/`, `stewardship/`, `endurance/` | ⏳ |
| P31–35 | cold-start inheritance + parity; simulated media failure; custody transfer with overlap; mission across generations; simulated decade churn | `inheritance/`, `archival/`, `succession/`, `missions/`, `generations/` | ⏳ |
| P36–40 | non-expert why-answer; 3 plain-language rules; bounded delegation; trust-rate targets; joint goal | `explanations/`, `policy_nl.json`, `.rsis/delegations.json`, `trust/`, `codesign/` | ⏳ |
| P41–45 | external standard implementation; commons publish→adopt; reciprocity treaty + dispute; crisis drill; 3-ecosystem coordination | `standards/`, `commons/`, `diplomacy/`, `crisis/`, `planetary/` | ⏳ |
| P46–50 | 90-day study; A/B behavior change; corpus completeness; machine-checkable proof; 10-year program committed | `longitudinal/`, `experiments/`, `failures/`, `metainvariant/` | ⏳ |

## Ops procedures

- **Identity rotation (F7)**: the dev keypair
  `.rsis/identity/{instance.key,instance.pub}` is committed per the
  state-in-git convention. Before any production use, rotate it with
  `python -m rsis identity rotate` (grace period keeps the retired key
  verifiable for 7 days, `GRACE_DAYS`), re-publish the new fingerprint to
  peers, and confirm portable bundles never include `instance.key`
  (covered by `tests/test_epoch1_sequel4.py` →
  `test_export_excludes_identity_key`).
- **Budget breach drill (F8/P2)**: `python -m rsis budgets drill` runs an
  isolated fail-close breach and records `cost_budget_drill` telemetry;
  `python -m rsis budgets status` shows the live posture.
- **Verification coverage (P7)**: `python -m rsis attestations replay
  --candidate-sha <sha>` re-runs a candidate from the
  `rack/verification/` ledger.

## Status roll-up

| Group | Demonstrated | Pending |
|---|---|---|
| Phases 1–5 | — | 5/5 |
| Phases 6–10 | — | 5/5 |
| Phases 11–15 | — | 5/5 |
| Phases 16–20 | — | 5/5 |
| Phases 21–25 | — | 5/5 |
| Phases 26–30 | — | 5/5 |
| Phases 31–35 | — | 5/5 |
| Phases 36–40 | — | 5/5 |
| Phases 41–45 | — | 5/5 |
| Phases 46–50 | — | 5/5 |

Update this file when a criterion is evidenced; the roadmap status tables
mirror it.
