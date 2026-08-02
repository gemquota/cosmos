---
type: "concept"
title: "Memento Pattern"
description: "Capturing and restoring an object's state without exposing its internals"
tags: ["memento", "patterns", "design", "undo"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Memento Pattern

## Summary
The memento pattern snapshots an object's state in an opaque token so it can be restored later — undo systems, checkpoints, and rollback rely on it. The originator owns the snapshot; the caretaker holds tokens it cannot read.

## Details
- Mementos preserve encapsulation: the caretaker never touches internal fields.
- Memory cost grows with snapshot size; store deltas or compress for long undo histories.
- Restoring state invalidates derived objects — refresh caches and references after restore.
- mykb relevance: article revisions as mementos give the wiki cheap undo without breaking the format.

## Related
- [[wiki/software-engineering/command-pattern|Command Pattern]]
- [[wiki/concepts/checkpoint-rollback|Checkpoint Rollback]]
- [[wiki/software-engineering/state-pattern|State Pattern]]
- [[wiki/dev-tools/rollback-strategies|Rollback Strategies]]
- [[wiki/software-engineering/prototype-pattern|Prototype Pattern]]
