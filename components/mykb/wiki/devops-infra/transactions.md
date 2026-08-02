---
type: "concept"
title: "Database Transactions"
description: "Atomic units of work that group operations to commit or roll back together"
tags: ["transactions", "database", "acid", "concurrency", "sql"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
---

# Database Transactions

## Summary

A transaction groups multiple operations into one atomic unit: either all commit or all roll back. Transactions preserve consistency under concurrency and crashes, and they provide the recovery boundary that makes multi-statement workflows safe. Without them, a partial failure can leave related rows in inconsistent states that are expensive to repair manually.

## Details

- Framing: `BEGIN` opens a transaction, `COMMIT` makes its changes durable and visible, and `ROLLBACK` discards them. Savepoints (`SAVEPOINT`/`ROLLBACK TO`) allow partial rollback to an earlier point without aborting the whole unit.
- ACID guarantees: atomicity (all-or-nothing), consistency (constraints hold), isolation (concurrent transactions do not interfere beyond their level), and durability (committed data survives crashes). See [[wiki/devops-infra/acid|ACID]] and [[wiki/devops-infra/isolation-levels|Isolation Levels]].
- Concurrency: transactions are the unit against which isolation levels are defined; the engine serializes or snapshots their effects so readers and writers coordinate safely.
- Failure handling: applications must decide what to do on commit failure — retry, roll back, or record the outcome — because a failed commit may or may not have applied, which is where idempotency and [[wiki/api-protocols/idempotency|Idempotency]] keys help.
- Long transactions: keeping a transaction open while doing slow I/O, network calls, or user interaction holds locks and snapshots, increasing contention and bloat. Move such work outside the transaction whenever possible.

## Practical Guidance

- Keep transactions short: long ones hold locks and bloat connection pools; batch writes and commit in small units where correctness allows.
- Choose isolation per workload: read-heavy analytics may tolerate weaker isolation, while financial or inventory logic often needs stricter guarantees.
- Handle deadlocks: engines abort one participant when locks cycle; retry the aborted transaction with backoff.
- Logging and monitoring: lock-wait times and rollback rates are leading indicators of transaction design problems; see [[wiki/devops-infra/observability|Observability]].
- Durability options: synchronous commits and group commit settings trade fsync cost against crash-loss windows; [[wiki/devops-infra/backups|Backups]] remain essential regardless.
- Frameworks: ORMs and [[wiki/devops-infra/connection-pooling|Connection Pooling]] wrap transaction boundaries, but the same rules — short, explicit, and retry-aware — apply underneath.

## Related

- [[wiki/devops-infra/acid|ACID]] — the guarantees behind transactions
- [[wiki/devops-infra/isolation-levels|Isolation Levels]] — concurrency semantics
- [[wiki/devops-infra/optimistic-locking|Optimistic Locking]] — conflict handling without locks
- [[wiki/api-protocols/idempotency|Idempotency]] — application-level dedup around transactions
- [[wiki/devops-infra/sqlite|SQLite]] — transactional by default
