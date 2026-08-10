---
type: synthesis
title: "RSIS3 Cycle-Daemon Commit Policy — Targeted Artifacts, No Snapshot Churn (2026-08-10)"
description: "The cycle daemon now commits only its own cycle artifacts (.rsis/ state, bridge cycles, MyKB syntheses/log), skips commits when nothing new was produced, and leaves snapshot regeneration to CI (opt-in --snapshots) — ending per-cycle 10k-line dashboard-data.json churn"
tags: [synthesis, rsis3, ops, daemon, commit, snapshot, ci, cadence]
timestamp: "2026-08-10T12:13:00Z"
status: stable
source: []
---
# RSIS3 Cycle-Daemon Commit Policy — Targeted Artifacts, No Snapshot Churn

## Context
The 3-minute `cycle-daemon` cadence ran with a `git add -A` sweep plus
snapshot regeneration on every cycle. Each cadence commit rewrote
`rack/pulses/dashboard-data.json` (~10k lines) and regenerated graph/files
snapshots from unchanged inputs — pure churn — and the sweep could also pick
up unrelated in-progress edits. Locally this produced 201 unpushed commits
whose cadence entries carried no new information. CI (`.github/workflows`,
push + daily) already regenerates snapshots, so the daemon's regeneration
was redundant work on every cycle.

## Policy (durable rules)
1. **The daemon stages only its own artifacts.** `_daemon_artifacts()` limits
   `git add` to `.rsis/` state, `rack/bridge/cycles`, `mykb/wiki/syntheses`,
   and `mykb/log.md|log.json` — never `git add -A`, so unrelated working-tree
   edits are never swept into a cadence commit.
2. **Empty cycles produce no commit.** After staging, the daemon checks
   `git diff --cached --quiet` and skips the commit when nothing new was
   produced. A cadence commit now guarantees new cycle output.
3. **Snapshots are opt-in, off by default.** The flag flipped from
   `--no-snapshots` (snapshots on) to `--snapshots` / `RSIS_CYCLE_SNAPSHOTS=1`
   (snapshots off by default). CI regenerates snapshots on push and daily, so
   the daemon only regenerates when explicitly asked.
4. **Generated snapshot files are still excluded from cadence commits** even
   with `--snapshots` off: `dashboard-data.json` and the dashboard tree are
   only staged when this cycle regenerated them, matching CODEBASE.md's
   exclusion intent for `.rsis/` state and generated snapshots.

## Verification
- `tests/test_ops_daemon.py`: cycle commit stages `mykb/log.md`; a stray file
  written by the executor is *not* swept into the commit; a no-op cycle
  produces no cadence commit; `_daemon_artifacts()` returns owned paths only
  and adds snapshot paths only when snapshots are enabled and files exist.
- 371 pytest suite green; `cycle-daemon --dry-run` reports `snapshots: False`
  by default and `True` with `--snapshots`.

## Related
- [[wiki/syntheses/rsis3-phase-4-5-ops-autonomy-2026-08-08|RSIS3 Phases 4–5 — Ops Maturity & Autonomy]]
- [[wiki/syntheses/nine-loop-stack-implementation|Nine-Loop Stack Implementation & Dashboard Wiring]]
- [[wiki/syntheses/cosmos-dashboard-mykb-integration|Cosmos Dashboard & MyKB Integration Patterns]]
- [[wiki/syntheses/wiki-self-improvement|Wiki Self-Improvement]]
