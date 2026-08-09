---
type: "synthesis"
title: "RSIS3 Phases 4–5 — ops maturity + autonomy (daemon, convergence, nightly)"
description: "Durable rules for sustainable background operation: cycle daemon with lockfile/backoff, convergence monitoring and bounded auto-retuning, dynamic dashboard overlay, CI guards, nightly summaries, bridge self-heal — completes the multi-phase roadmap"
tags: ["rsis3", "phase-4", "phase-5", "ops", "daemon", "convergence", "ci", "autonomy", "nightly"]
timestamp: "2026-08-08T17:20:00Z"
status: "growing"
---

# RSIS3 Phases 4–5 — ops maturity + autonomy

Phases 4 (Ops Maturity) and 5 (Autonomy & Durable Ops) complete the
multi-phase roadmap. Durable patterns and rules for future work.

## Cadence daemon

- `python -m rsis cycle-daemon` is the single cadence driver:
  `launch --cycles 1` every `RSIS_CYCLE_INTERVAL_S` (default 180 s), with
  `ops/cycle_daemon.sh` as the shell wrapper.
- The fcntl lockfile (`rack/cycle-daemon.lock`) makes parallel sessions
  fail fast (`exit 2`); repeated failures back off 5/15/30 min
  (`RSIS_CYCLE_BACKOFF_S`), clamped to the sequence.
- The bridge `/health` endpoint is checked before every cycle; with
  `--supervise-bridge` the daemon restarts the Node bridge when its port
  is down (spawns `node rack/bridge/server.mjs` with `RSIS_BRIDGE_PORT`).

## Convergence handling (no silent no-ops)

- `python -m rsis convergence` detects two stalls: best fitness flat over
  N generations (default 5) and L4–L9 `*_complete` events with
  `changed: false` at/over a threshold (default 8 in a 10-cycle window).
- Proposals are create-only (`rack/proposals/convergence-*.json`,
  `applied` flag) and mirrored to MyKB backlog notes; the retune loop is
  chosen from the existing identity/meta commands (plateau → `identity`;
  bound no-ops → the loop with the most no-ops).
- `--auto-retune` applies the proposal bounded by
  `RSIS_RETUNE_MIN_INTERVAL_S` (default 6 h) and records every apply in
  `rack/proposals/applied.jsonl`.

## Dashboard dynamics

- `dashboard-data.json` is a cache; when `BRIDGE_URL` is up, `app.js`
  overlays `/api/cosmos` (KG, strategies gen/fitness, pulses, 24 h cost
  ledger) and shows a live badge — never a hard dependency.

## CI and daily automation

- `.github/workflows/ci.yml` gates every push/PR: check-practices,
  gen-static-data --check, contracts, wiki links, pytest, node --test,
  and `infra/health/bridge_smoke.sh` (offline-fallback /health + chat
  round-trip; must `unset GEMINI_API_KEY` to stay deterministic).
- `python -m rsis nightly-summary` aggregates one UTC day (cycles,
  events, no-ops, rc failures, strategies, KG, costs, commits) into an
  OKF daily-summary note + log.md entry; `.github/workflows/nightly.yml`
  runs it daily. Cost ledgers store epoch-second timestamps — parsers
  must accept both ISO and epoch.

## Verification rules

- Phase 4/5 matrix: `tests/test_convergence.py`, `tests/test_ops_daemon.py`,
  `tests/test_nightly.py`; full suite 205 pytest + 8 node --test.
- Exit criteria pending live validation: 24 h (P4) / 7 days (P5)
  unattended with zero manual intervention.

## Related

- [[wiki/syntheses/rsis3-phase-3-product-surface-2026-08-08|RSIS3 Phase 3 — product surface]]
- [[wiki/syntheses/rsis3-daily-summary-2026-08-08|RSIS3 daily summary — 2026-08-08]]
- [[wiki/backlog/convergence-2026-08-08|Convergence backlog — 2026-08-08]]
