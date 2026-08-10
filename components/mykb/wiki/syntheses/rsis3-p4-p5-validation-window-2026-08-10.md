---
type: "synthesis"
title: "P4 24h → P5 7-day validation window tracker (2026-08-10)"
description: "Seeded the Phase 4 24-hour exit-criterion window; new `rsis validation` CLI with start/status/checkin, nightly auto-check-in, and clean P4→P5 advance"
tags: ["rsis3", "validation", "exit-criteria", "phase-4", "phase-5", "cadence"]
timestamp: "2026-08-10T15:05:00Z"
status: "growing"
---

# P4 24h → P5 7-day validation window tracker (2026-08-10)

Formally seeded the Phase 4 24-hour exit-criterion window so Phase 5's
7-day window has a clean, timestamped start point.

## Durable conclusions

- **Validation windows** live in `rack/validation/windows.json`; each
  records kind, title, hours, started_at, ends_at, status, completed_at
  and a dated check-in history.
- **CLI**: `python -m rsis validation start|status|checkin` (+ `--kind`,
  `--json`). Check-in evaluates 7 criteria against live evidence: cycle
  cards (3-min cadence, 80% tolerance), daemon lockfile (PID liveness),
  cost records, MyKB daily summaries, auto-retunes, incidents, and the
  contracts gate.
- **P4 → P5 advance**: when the 24 h window ends with all criteria
  passing, the 7-day window starts automatically at the P4 completion
  timestamp — a clean start point with no gap.
- **Daily check-in**: `nightly-summary` now calls
  `validation.auto_checkin` after writing the daily note, so the window is
  evaluated every night without extra ops. Telemetry:
  `validation_window_started`, `validation_checkin`,
  `validation_window_completed`.
- **Seed state**: P4 window `p4-24h-20260810T050251Z` running, ends
  `2026-08-11T05:02:51Z`; baseline check-in PENDING (correct at 0h
  elapsed). Completion of the 24 h window is the formal precondition for
  the P5 7-day validation.

## Rules
- Lockfile liveness = daemon PID alive (not mtime freshness — the daemon
  holds the lock for its lifetime).
- Evidence is time-filtered to the window start (`>= started_at`), so a
  check-in only counts what the window itself produced.
- Never pin fixed dates in tests; validation evidence uses ISO timestamps.

## Related
- [[wiki/syntheses/rsis3-epoch-1-findings-resolution-2026-08-10|Epoch 1 audit findings — all 8 resolved]]
- [[wiki/syntheses/rsis3-epoch-1-audit-2026-08-10|Epoch 1 audit — 50-phase review]]
