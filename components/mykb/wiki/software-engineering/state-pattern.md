---
type: "concept"
title: "State Pattern"
description: "Encapsulating state-specific behavior in separate state objects"
tags: ["state", "patterns", "design", "state-machines"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# State Pattern

## Summary
The state pattern moves state-specific behavior into objects — each state is a class with its own behavior, and the context delegates to the current state. It tames sprawling switch statements in state machines.

## Details
- Transitions become state changes; each state object decides what the next state is.
- Compare with enum-based machines: state pattern scales better when behavior differs per state.
- Overkill for two-state booleans; right-sized for protocols, orders, and workflows.
- mykb relevance: article lifecycle (draft, stub, growing, verified) maps naturally to state objects.

## Related
- [[wiki/software-engineering/strategy-pattern|Strategy Pattern]]
- [[wiki/software-engineering/command-pattern|Command Pattern]]
- [[wiki/agent-systems/session-state-machine|Session State Machine]]
- [[wiki/software-engineering/observer-pattern|Observer Pattern]]
- [[wiki/software-engineering/software-design-principles|Software Design Principles]]
