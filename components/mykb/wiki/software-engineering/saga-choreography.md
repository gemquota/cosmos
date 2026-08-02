---
type: "concept"
title: "Saga Choreography"
description: "Distributed transactions coordinated by services reacting to each other's events"
tags: ["saga", "choreography", "distributed-transactions", "events"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Saga Choreography

## Summary
Choreographed sagas distribute the workflow: each service does its step and emits an event that triggers the next, with compensation events on failure. There is no central coordinator — more decoupled, but harder to see the whole flow.

## Details
- Each participant owns its step and its compensation; the event trail IS the workflow.
- Visibility suffers: tracing the saga means following the event chain across services.
- Design event contracts carefully so a schema change does not break the choreography.
- mykb relevance: link-verification steps could choreograph: article saved emits CheckLinks, which emits ReportResult.

## Related
- [[wiki/software-engineering/saga-orchestration|Saga Orchestration]]
- [[wiki/software-engineering/choreography-vs-orchestration|Choreography vs Orchestration]]
- [[wiki/software-engineering/compensating-transactions|Compensating Transactions]]
- [[wiki/software-engineering/event-driven-architecture|Event-Driven Architecture]]
- [[wiki/software-engineering/event-notification|Event Notification]]
