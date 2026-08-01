---
type: "concept"
title: "Checkpoint & Rollback"
description: "Git-based snapshots taken before every mutation so any change can be reverted — the self-improvement safety net"
tags: [checkpoint, rollback, git, rsis3, safety]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: []
---

# Checkpoint & Rollback

## Summary
Checkpointing is the practice of committing a git snapshot before every state mutation, so a failed improvement can be rolled back to the last known-good state. It is what makes autonomous modification safe: you can always undo. RSIS3 wraps git commits in a CheckpointManager; loops call `checkpoint("l4-tune")` etc. before writing new state.

## Details
- **Invariant**: checkpoint-before-mutation — the commit lands *before* the write, so rollback targets a verified state.
- **Format**: commits use `rsis-checkpoint: <message> [ISO timestamp]` subjects, making them greppable across history.
- **Rollback**: `rollback(<hash>)` restores the workspace and hard-resets, used by the recovery manager after application failures.
- **No-op awareness**: if there are no changes, checkpoint returns None — pure read cycles don't churn history.
- Worked example: L2 checkpoints before each candidate submission (`l2-candidate-1`) and again after applying (`l2-applied-1-optimize-imports`).

## Related
- [[wiki/concepts/immutable-evaluator|Immutable Evaluator]] — approval gate before checkpointed writes
- [[wiki/concepts/telemetry|Workspace Telemetry]] — the audit trail alongside checkpoints
- [[wiki/concepts/memory-hierarchy|Memory Hierarchy]] — git is the truth tier this pattern builds on
- [[wiki/agent-systems/rollback-and-recovery|Rollback and Recovery]] — the agent-level framing