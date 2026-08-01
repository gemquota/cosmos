---
type: "concept"
title: "Workspace Telemetry"
description: "Structured, append-only event records of every loop action — the audit trail that makes self-improvement observable"
tags: [telemetry, observability, rsis3, audit, events]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: []
---

# Workspace Telemetry

## Summary
Workspace telemetry is the append-only record of everything a self-improving system does: loop starts, tool calls, evaluations, completions, and errors, each with a timestamp and structured metadata. It matters because a system that rewrites itself is only trustworthy if every mutation is observable and replayable from logs. In RSIS3 every loop writes telemetry events (l1_start … l9_complete) to `.rsis/telemetry/*.jsonl`, one file per session.

## Details
- **Event shape**: `type`, `timestamp`, and loop-specific metadata (cycle, decision, deltas, stats). Events are JSONL lines so they can be tailed and aggregated with standard tools.
- **Session scoping**: each run opens a fresh session file (`<uuid>_<ts>.jsonl`); a full L1–L9 run is one session, so per-loop coverage is auditable in one place.
- **Coverage rule**: every loop emits at least `start` and `complete`; evaluator-gated loops also emit `evaluation` with the decision; failures emit `error`.
- **Consumers**: the dashboard Loops tab (via `loops.json`), the extrapolation engine (regression trends for L6), and the practices checker (start+complete presence per loop).
- Worked example: an L4 optimizer cycle writes `l4_start`, `l4_evaluation` (decision=PASS), and `l4_complete` with the tuned deltas.

## Related
- [[wiki/concepts/immutable-evaluator|Immutable Evaluator]] — the gate whose decisions are logged
- [[wiki/concepts/checkpoint-rollback|Checkpoint & Rollback]] — the mutation safety net telemetry complements
- [[wiki/concepts/nine-loop-hierarchy|Nine-Loop Hierarchy]] — every loop writes its own events
- [[wiki/concepts/pulse-cycle|Pulse Cycle]] — the evaluation protocol whose outcomes are logged