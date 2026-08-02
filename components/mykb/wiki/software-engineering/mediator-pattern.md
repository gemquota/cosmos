---
type: "concept"
title: "Mediator Pattern"
description: "Centralizing interactions between many objects through one coordinator"
tags: ["mediator", "patterns", "design", "decoupling"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Mediator Pattern

## Summary
The mediator pattern routes communication between many components through a single coordinator, so they interact with the mediator instead of each other. It reduces tangled references at the cost of a possible god object.

## Details
- Colleagues notify the mediator; the mediator decides who else needs to react.
- Chat rooms, UI dialogs, and orchestrators are classic mediators.
- Event buses generalize the idea: a mediator with a publish/subscribe core.
- mykb relevance: a mediator coordinates the article pipeline stages so they never know each other directly.

## Related
- [[wiki/software-engineering/observer-pattern|Observer Pattern]]
- [[wiki/software-engineering/facade-pattern|Facade Pattern]]
- [[wiki/software-engineering/chain-of-responsibility|Chain of Responsibility]]
- [[wiki/software-engineering/event-driven-architecture|Event-Driven Architecture]]
- [[wiki/software-engineering/software-design-principles|Software Design Principles]]
