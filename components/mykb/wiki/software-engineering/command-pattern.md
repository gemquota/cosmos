---
type: "concept"
title: "Command Pattern"
description: "Encapsulating an action and its arguments as an object"
tags: ["command", "patterns", "design", "undo"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Command Pattern

## Summary
The command pattern turns an action into an object — execute(), undo(), serializable parameters — enabling queues, undo stacks, macros, and audit logs. It separates the requester from the executor of an action.

## Details
- Commands carry all data needed to act, making them queuable, retryable, and journalable.
- Undo/redo stacks are the classic payoff; transactional scripts extend it.
- Command objects can bloat; keep them small and prefer immutable parameters.
- mykb relevance: wiki mutations as commands give a replayable audit trail for the graph.

## Related
- [[wiki/software-engineering/state-pattern|State Pattern]]
- [[wiki/software-engineering/memento-pattern|Memento Pattern]]
- [[wiki/software-engineering/cqrs-pattern|CQRS Pattern]]
- [[wiki/software-engineering/chain-of-responsibility|Chain of Responsibility]]
- [[wiki/software-engineering/software-design-principles|Software Design Principles]]
