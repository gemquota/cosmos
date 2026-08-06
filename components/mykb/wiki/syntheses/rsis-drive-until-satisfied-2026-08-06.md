---
type: "synthesis"
title: "RSIS3 drive — run loops automatically until completion requirements are satisfied"
description: "New `python -m rsis drive` command that repeats a loop until its completion requirement is met, with per-loop predicates, safety budgets, and exit-code semantics for automation"
tags: ["rsis3", "loops", "automation", "drive", "completion-requirements", "scheduling"]
timestamp: "2026-08-06T00:00:00Z"
status: "growing"
---

# RSIS3 drive — run loops automatically until completion requirements are satisfied

## Summary
RSIS3 loops are on-demand (CLI per session/cadence) and each one-shot
command runs exactly one cycle, so the dashboard's honest IDLE state is the
default. To keep a loop running automatically until its completion
requirement is met, `python -m rsis drive` repeats the loop and checks a
per-loop predicate after every cycle:

- **L2** — until an improvement candidate passes the evaluator and is
  applied (`l2.max_improvement_attempts` per session; terminal-stuck when
  the attempts are exhausted without an application).
- **L3** — until consolidation plateaus: no new insights, no
  regression-driven focus strategies, no pruned redundancies (the routine
  `budget=` strategy L3 always emits does not count as progress).
- **L4** — until the observed success rate is inside
  `[l4.target_success_low, l4.target_success_high]` (no deltas proposed);
  terminal-stuck while `l4.min_outcomes` outcomes are missing — run L2
  sessions first.
- **L5** — until best strategy fitness plateaus (no improvement over the
  previous generation, tracked across cycles with a 0.005 epsilon).
- **L6–L9** — until the tuned band is stable (no tuning signal).

## Rules / patterns
- Drive exit codes compose with cron/systemd/shell: `0` satisfied · `1`
  error · `2` time budget · `3` max cycles · `4` terminal-stuck. A driver
  loop (`--max-cycles 1` on a timer, or `timeout 6h drive ...`) stops
  itself as soon as the requirement is met.
- Drive cycles reuse the same loop classes as the one-shot commands, so
  checkpoints, evaluator gates, and `l{N}_start`/`l{N}_complete` telemetry
  are written normally — the dashboard Loops tab flips IDLE → RECENT after
  a drive finishes, keeping snapshots truthful.
