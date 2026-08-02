---
type: "concept"
title: "ACID Transactions"
description: "Atomicity, consistency, isolation, and durability semantics"
tags: ["acid", "transactions", "concurrency-control", "databases"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://www.postgresql.org/docs/current/transaction-iso.html", "https://en.wikipedia.org/wiki/ACID"]
---

# ACID Transactions

## Summary
ACID is the contract that makes database state changes reliable: transactions are Atomic, leave the database Consistent, are Isolated from each other, and their effects are Durable. Together the four properties turn multi-step operations into all-or-nothing units.

## Details
- **Atomicity** — every statement in a transaction either commits as a whole or rolls back as a whole; the write-ahead log and undo records make partial failure impossible to observe.
- **Consistency** — transactions move the database between valid states, preserving constraints, triggers, and foreign keys; consistency is largely the application's schema contract enforced by the engine.
- **Isolation** — concurrent transactions must not see each other's uncommitted work beyond the chosen isolation level; engines implement isolation with locking, multiversion concurrency control, or optimistic validation.
- **Durability** — committed changes survive crashes; engines flush the write-ahead log to stable storage before acknowledging commit, and replicated databases add remote durability.
- **Implementation** — a transaction manager assigns IDs, tracks lock or version state per row, and coordinates commit with the log; distributed systems extend this with two-phase commit or consensus.
- **Practical note** — isolation is configurable, so "ACID" claims mean little without knowing the isolation level and durability mode in use.

## Related
- [[wiki/data-storage/transaction-isolation-levels|Transaction Isolation Levels]] — the configurable part of ACID
- [[wiki/data-storage/write-ahead-logging|Write-Ahead Logging]] — the durability mechanism
- [[wiki/data-storage/multiversion-concurrency-control|Multiversion Concurrency Control]] — a common isolation implementation
- [[wiki/data-storage/crash-recovery|Crash Recovery]] — restoring state after failure
- [[wiki/devops-infra/transactions|Transactions]] — operational transaction management
