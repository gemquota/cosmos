---
type: "concept"
title: "Event-Driven Design"
description: "Designing systems around events that trigger reactions"
tags: ["event-driven", "architecture", "events", "design"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Event-Driven Design

## Summary
Event-driven design models the system as producers emitting facts and consumers reacting — decoupled in space and time. It suits integrations, analytics, and workflows, at the cost of harder reasoning about flow and ordering.

## Details
- Events are facts in the past tense: OrderPlaced, LinkBroken — immutable, named, timestamped.
- Decoupling is the win; eventual consistency and replay are the taxes.
- Design event contracts and schema evolution as carefully as API contracts.
- mykb relevance: wiki events (ArticleCreated, LinkAdded) drive index rebuilds and sync.

## Related
- [[wiki/software-engineering/event-driven-architecture|Event-Driven Architecture]]
- [[wiki/software-engineering/event-notification|Event Notification]]
- [[wiki/software-engineering/event-carried-state|Event-Carried State]]
- [[wiki/software-engineering/cqrs-pattern|CQRS Pattern]]
- [[wiki/software-engineering/saga-orchestration|Saga Orchestration]]
