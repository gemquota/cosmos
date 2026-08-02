---
type: "concept"
title: "Deadlock Detection"
description: "Wait-for graphs, cycle detection, and victim selection"
tags: ["deadlock", "locking", "concurrency", "database-internals"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://www.postgresql.org/docs/current/explicit-locking.html", "https://dev.mysql.com/doc/refman/8.4/en/innodb-deadlocks.html"]
---

# Deadlock Detection

## Summary
A deadlock occurs when transactions wait on each other in a cycle, each holding a lock the other needs. Databases detect cycles in the wait-for graph and abort a chosen victim so the remaining transactions can proceed; timeouts are the simpler fallback.

## Details
- **Wait-for graph** — nodes are transactions, edges point from a waiting transaction to the transaction holding the lock it wants; a cycle in this graph is a deadlock.
- **Detection timing** — InnoDB scans the graph when a lock wait exceeds a threshold (default deadlock detection is always on for InnoDB) and aborts the transaction with the fewest undo records; Postgres detects cycles lazily when a process waits and finds a cycle among active transactions.
- **Victim selection** — engines prefer aborting the transaction that did the least work to minimize wasted effort; the aborted transaction rolls back and the application usually retries.
- **Lock timeouts** — a second line of defense: `innodb_lock_wait_timeout` and `lock_timeout` abort waits that exceed a bound, bounding worst-case latency even when detection is disabled or distributed.
- **Prevention** — consistent lock ordering (always acquire locks in the same order), short transactions, and index-based access paths reduce deadlock frequency; monitoring tools report deadlock graphs for analysis.

## Related
- [[wiki/data-storage/two-phase-locking|Two-Phase Locking]] — the protocol that creates deadlocks
- [[wiki/data-storage/lock-granularity|Lock Granularity]] — what gets held while waiting
- [[wiki/data-storage/optimistic-concurrency-control|Optimistic Concurrency Control]] — avoiding waits entirely
- [[wiki/data-storage/transaction-isolation-levels|Transaction Isolation Levels]] — retry semantics after aborts
- [[wiki/devops-infra/incident-response|Incident Response]] — diagnosing lock storms in production
