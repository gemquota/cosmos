---
type: "concept"
title: "Two-Phase Locking"
description: "Lock acquisition and release rules for serializability"
tags: ["two-phase-locking", "locking", "serializability", "concurrency-control"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://www.postgresql.org/docs/current/explicit-locking.html", "https://dev.mysql.com/doc/refman/8.4/en/innodb-locking.html"]
---

# Two-Phase Locking

## Summary
Two-phase locking (2PL) is the classic concurrency-control protocol for serializable execution: transactions acquire locks as they go, then enter a shrinking phase where they release locks and acquire no new ones. The discipline guarantees that schedules are equivalent to some serial order.

## Details
- **Growing phase** — a transaction may acquire locks on rows or tables it will touch but cannot release any; locks accumulate until the transaction finishes.
- **Shrinking phase** — once the first lock is released, no further locks may be taken; all locks are held to commit or rollback. This is what produces serializability — the release order defines the serial order.
- **Strictness** — strict 2PL holds all locks until commit, which is what real engines (InnoDB, PostgreSQL's explicit locks) implement, because it makes cascading aborts impossible.
- **Shared/exclusive modes** — readers take shared locks that are compatible with each other but not with exclusive writer locks; writers take exclusive locks; upgrades (S to X) must follow the same rules.
- **Costs** — 2PL causes blocking and deadlocks under contention, so engines pair it with deadlock detection and fall back to MVCC snapshot reads that do not lock at all.

## Related
- [[wiki/data-storage/transaction-isolation-levels|Transaction Isolation Levels]] — what 2PL guarantees at each level
- [[wiki/data-storage/deadlock-detection|Deadlock Detection]] — resolving cycles 2PL creates
- [[wiki/data-storage/lock-granularity|Lock Granularity]] — row, page, and table locks
- [[wiki/data-storage/multiversion-concurrency-control|Multiversion Concurrency Control]] — the non-blocking alternative
- [[wiki/data-storage/optimistic-concurrency-control|Optimistic Concurrency Control]] — validation instead of blocking
