---
type: "concept"
title: "Saga Pattern"
description: "Coordinating distributed transactions as sequences of local transactions with compensating actions"
tags: ["saga", "distributed-systems", "transactions", "microservices"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Saga Pattern

## Summary
A saga manages a business transaction spanning multiple services by chaining local transactions, each followed by a compensating action if a later step fails.

## Details
- Two styles: choreography (services react to events) and orchestration (a coordinator drives steps).
- Compensations undo partial work; sagas trade ACID atomicity for availability.
- Relevant wherever a single write fans out — payments, multi-store updates, agent tool calls.

## Related
- [[wiki/devops-infra/transactions|Transactions]] — local atomicity inside saga steps
- [[wiki/api-protocols/event-sourcing|Event Sourcing]] — events coordinate choreographed sagas
- [[wiki/api-protocols/message-queues|Message Queues]] — step triggers and replies
- [[wiki/api-protocols/circuit-breaker|Circuit Breaker]] — step failure handling
- [[wiki/concepts/triad-architecture|Triad Architecture]] — multi-component write flows
- [[wiki/api-protocols/idempotency|Idempotency]] — saga steps retry safely with idempotency keys
