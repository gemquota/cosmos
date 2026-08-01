---
type: "concept"
title: "Compensating Transactions"
description: "Undo actions that roll back the effects of completed steps in a distributed operation"
tags: ["distributed-systems", "transactions", "saga", "consistency"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
---

# Compensating Transactions

## Summary
In distributed systems there is no single rollback; a compensating transaction applies an inverse operation to undo a step that already succeeded. It is the building block of saga-based consistency.

## Details
- Each step must be designed with a compensation from the start, or it cannot be undone later.
- Compensations are often best-effort and asynchronous; they cannot restore history, only return to a sensible state.
- RSIS3 relevance: agent actions that mutate memory should define compensations before they run.

## Related
- [[wiki/software-engineering/transactional-outbox|Transactional Outbox]] — helps publish the events that trigger compensations
- [[wiki/api-protocols/saga-pattern|Saga Pattern]] — the orchestration of compensations across a workflow
- [[wiki/api-protocols/idempotency|Idempotency]] — makes compensations safe to retry
- [[wiki/devops-infra/transactions|Database Transactions]] — the local guarantee compensations cannot replace
- [[wiki/software-engineering/event-driven-architecture|Event-Driven Architecture]] — saga steps are event-driven transactions
