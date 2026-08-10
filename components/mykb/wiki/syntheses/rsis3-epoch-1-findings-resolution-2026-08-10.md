---
type: "synthesis"
title: "Epoch 1 audit findings — all 8 resolved (2026-08-10)"
description: "Closed F1–F8 from the epoch-1 audit: verification ledger live, budgets materialized + drill, session persistence exercised, traversal gating fixed, date-rot tests fixed, portable key exclusion tested, exit-criteria tracker created"
tags: ["rsis3", "epoch-1", "audit", "findings", "verification", "budgets", "redteam", "policy"]
timestamp: "2026-08-10T14:25:00Z"
status: "growing"
---

# Epoch 1 audit findings — all 8 resolved (2026-08-10)

Resolved every finding from `components/rsis3/docs/epoch-1-audit-2026-08-10.md` (addendum section) in one pass. Full detail in the audit report; durable rules below.

## Durable conclusions

- **Verification ledger is live now (F1)**: `rack/verification/2026-08-10.jsonl` holds the verified gen-210 convergence retune (PASS, contracts 0 FAIL); `attestations replay --candidate-sha <sha>` reproduces it. Applied changes must keep landing in the ledger.
- **Budgets are materialized and drilled (F2)**: `.rsis/budgets.json` (evaluator $0.05/day, default $0.02, ceiling $0.50); new `python -m rsis budgets` CLI with `status` + `drill`; drill emits `cost_budget_hit` + `cost_budget_drill` telemetry (snake_case per contract).
- **Session persistence exercised (F3)**: a bridge chat round-trip produced `rack/bridge/sessions/epoch1-audit-f3-session.jsonl` (cosmos-envelope/1 exchanges).
- **Path traversal is policy-gated (F4)**: `requires_approval` canonicalizes target paths — absolute paths, `..` segments, and paths escaping the workspace always require approval (also applied in `check_unauthorized_writes`). Live `redteam run --ci`: 0 findings.
- **Date-rot tests fixed (F5)**: budget/season tests hardcoded 2026-08-09 timestamps; they now use the current UTC day. Budget checks are day-scoped by design — never pin fixed dates in P8/P15 tests.
- **Portable exports exclude the identity key (F7)**: `test_export_excludes_identity_key` pins it; rotate before production via `python -m rsis identity rotate` (7-day grace).
- **Exit criteria are tracked (F8)**: `docs/epoch-1-exit-criteria.md` is the tracker; the 7-day cadence validation (P5) = 3-min daemon cadence under lockfile, bounded retune per episode, daily summary, bridge heals ≤2 cycles, CI green — 7 consecutive days unattended.

## Related
- [[wiki/syntheses/rsis3-epoch-1-audit-2026-08-10|Epoch 1 audit — 50-phase review]]
- [[wiki/syntheses/rsis3-epoch-1-implementation-2026-08-10|RSIS3 Epoch 1 implementation — phases 16–50]]
