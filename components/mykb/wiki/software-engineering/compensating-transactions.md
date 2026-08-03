---
type: "concept"
title: "Compensating Transactions"
description: "Undo actions that roll back the effects of completed steps in a distributed operation"
tags: ["distributed-systems", "transactions", "saga", "consistency"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
---
# Compensating Transactions

## Summary

Compensating transactions undo the effects of a completed step when a later step fails — the recovery mechanism for sagas and distributed workflows where atomicity is impossible. They must be designed as first-class operations, not afterthoughts.

## Details
- Mechanism: each step in a saga defines a compensation (book the hotel, cancel the booking); on failure, the workflow executes compensations in reverse order; compensations are themselves operations that can fail, so they need retries, idempotency, and their own failure handling. Contrast with two-phase commit (locking, synchronous, unavailable across services) — compensation is the practical distributed alternative.
- Concrete example: an order saga: charge card → reserve inventory → ship; if shipping fails, refund the card and release inventory. The refund must be idempotent (a retried refund does not double-refund), and the inventory release must be safe to run twice. A compensation that cannot run (card expired) becomes a manual escalation path.
- Failure modes: compensations that assume the original operation state (must be derived from workflow state); non-idempotent compensations causing double-effects on retry; partial compensation leaving the system in an inconsistent but visible state; and forgetting compensation for a step, so failures leave permanent side effects.
- Operational tradeoffs: compensating design costs extra operations and testing but is the only sane way to span services; the discipline is write compensations alongside the forward operation, make them idempotent, and simulate failures in tests. Log every compensation for audit.
- RSIS3/mykb relevance: the wiki's agent workflows document compensation steps for multi-step operations, so loop-driven side effects stay reversible.
- State machine: persist saga state (step, compensation pointer) so restarts resume correctly; in-memory sagas lose compensation ability on crash.
- Failure injection: test compensations by deliberately failing each step; the untested compensation is the one that runs during the worst incident.

## Related
- [[wiki/software-engineering/transactional-outbox|Transactional Outbox]] — helps publish the events that trigger compensations
- [[wiki/api-protocols/saga-pattern|Saga Pattern]] — the orchestration of compensations across a workflow
- [[wiki/api-protocols/idempotency|Idempotency]] — makes compensations safe to retry
- [[wiki/devops-infra/transactions|Database Transactions]] — the local guarantee compensations cannot replace
- [[wiki/software-engineering/event-driven-architecture|Event-Driven Architecture]] — saga steps are event-driven transactions
