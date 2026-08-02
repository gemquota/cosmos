---
type: "concept"
title: "Observer Pattern"
description: "Notifying interested subscribers when a subject changes state"
tags: ["observer", "patterns", "events", "design"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Observer Pattern

## Summary
The observer pattern lets a subject broadcast state changes to registered observers without coupling to them. Event emitters, pub/sub, and reactive streams are its descendants; the costs are implicit ordering and notification storms.

## Details
- Subject maintains a subscriber list and notifies on change; observers subscribe or unsubscribe.
- Watch for re-entrancy: an observer that mutates the subject mid-notification causes chaos.
- Event buses generalize observers to decoupled topics; reactive streams add backpressure.
- mykb relevance: the wiki daemon notifies subscribers when new articles or links land.

## Related
- [[wiki/software-engineering/mediator-pattern|Mediator Pattern]]
- [[wiki/software-engineering/event-driven-architecture|Event-Driven Architecture]]
- [[wiki/software-engineering/event-notification|Event Notification]]
- [[wiki/software-engineering/reactive-programming|Reactive Programming]]
- [[wiki/software-engineering/state-pattern|State Pattern]]
