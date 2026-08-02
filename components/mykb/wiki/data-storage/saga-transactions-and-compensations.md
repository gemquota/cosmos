---
type: "concept"
title: "Saga Transactions and Compensations"
description: "Long-running business transactions as compensable steps"
tags: ["saga", "compensation", "microservices", "transactions"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Saga Transactions and Compensations

## Summary

A stub to be expanded into a full article; frames the concept and open questions.

## Details

- A saga splits a transaction into steps, each with a compensating action for rollback.
- Orchestrated sagas use a central coordinator; choreographed sagas use events.
- Sagas are eventually consistent; partial failures are normal and expected.
- Compensations must be idempotent and handle non-transactional side effects.

## Related

- [[wiki/data-storage/distributed-transactions|Distributed Transactions]] — transactions
- [[wiki/data-storage/distributed-transactions-and-2pc|Distributed Transactions And 2Pc]] — ACID alternative
- [[wiki/data-storage/outbox-pattern-for-transactions|Outbox Pattern For Transactions]] — reliability pattern
- [[wiki/data-storage/event-sourcing-databases|Event Sourcing Databases]] — event-based state
- [[wiki/data-storage/data-engineering-fundamentals|Data Engineering Fundamentals]] — core data engineering concepts
