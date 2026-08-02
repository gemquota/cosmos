---
type: "concept"
title: "Saga Pattern"
description: "Coordinating distributed transactions as sequences of local transactions with compensating actions"
tags: ["saga", "distributed-systems", "transactions", "microservices"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://microservices.io/patterns/data/saga.html", "https://en.wikipedia.org/wiki/Compensating_transaction"]
---

# Saga Pattern

## Summary
A saga manages a business transaction spanning multiple services by chaining local transactions, each followed by a compensating action if a later step fails.

## Details
- Two styles: choreography (services react to events) and orchestration (a coordinator drives steps).
- Compensations undo partial work; sagas trade ACID atomicity for availability.
- Relevant wherever a single write fans out — payments, multi-store updates, agent tool calls.
- A saga is a sequence of local transactions across services, with each step publishing an event or invoking the next; when a step fails, compensating actions undo the earlier steps.
- It is the standard answer to distributed transactions without two-phase commit, which does not scale across microservices.
- Orchestration (a central coordinator) and choreography (event-driven handoffs) are the two coordination styles, each with different coupling and failure properties.
- Compensations must be designed as first-class operations, because they run on real failures and often long after the original step.
- **Worked example / comparison** — Worked example — a multi-service article publish saga: save draft, render export, deploy bundle, notify; if the deploy fails, the saga compensates by rolling back the export and marking the draft unpublished.
- For mykb, the saga pattern is documented as the reliability answer for multi-step pipelines like the wiki's export-and-publish flow.

## Related
- [[wiki/devops-infra/transactions|Transactions]]
- [[wiki/api-protocols/event-sourcing|Event Sourcing]]
- [[wiki/api-protocols/message-queues|Message Queues]]
- [[wiki/api-protocols/circuit-breaker|Circuit Breaker]]
- [[wiki/concepts/triad-architecture|Triad Architecture]]
- [[wiki/api-protocols/idempotency|Idempotency]]
- [[wiki/concepts/promotion-readiness|Promotion Readiness]]
- [[wiki/concepts/content-freshness-review|Content Freshness Review]]
- [[wiki/concepts/deep-dives|Deep Dives]]
