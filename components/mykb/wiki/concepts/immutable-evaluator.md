---
type: "concept"
title: "Immutable Evaluator"
description: "The frozen, read-only judge that gates every proposed change — never in-scope for self-improvement"
tags: [evaluator, guardrail, rsis3, safety, verification]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: []
---

# Immutable Evaluator

## Summary
The immutable evaluator is a separate process with read-only code that scores candidate changes before they are applied. It is the one component the system is forbidden to modify, because it is the judge — a judge that rewrites its own rules stops being a judge. Every loop's mutation (L4 tuning, L5 generations, L6/L7/L8/L9 meta-tuning) is submitted to it and applied only on PASS.

## Details
- **Interface**: a subprocess that reads a JSON candidate (`description`, `target_files`, `diff`, `rationale`, `attempt`, `goal`) on stdin and returns `decision` (PASS/FAIL) plus scores.
- **Verification**: startup `--verify <sha256>` digests the evaluator binary so a tampered judge is detected before use.
- **Design rule**: the evaluator has no write path — it cannot modify workspace state, only report.
- RSIS3's stub evaluator always PASSes so loops run headlessly; production swaps in an API-backed judge with the same interface.
- Failure handling: a rejected proposal is logged, recorded in the loop's history as `accepted: False`, and the loop terminates that cycle (no silent retry).

## Related
- [[wiki/concepts/checkpoint-rollback|Checkpoint & Rollback]] — mutation safety before submission
- [[wiki/concepts/telemetry|Workspace Telemetry]] — every evaluation decision is logged
- [[wiki/concepts/nine-loop-hierarchy|Nine-Loop Hierarchy]] — all gated loops share this judge
- [[wiki/concepts/triad-architecture|Triad Architecture]] — the evaluator sits outside the mutable system