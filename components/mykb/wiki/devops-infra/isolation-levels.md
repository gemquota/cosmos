---
type: "concept"
title: "Isolation Levels"
description: "Policies governing how concurrent transactions see each other's uncommitted and committed changes"
tags: ["isolation", "transactions", "database", "concurrency", "sql"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
---

# Isolation Levels

## Summary

Isolation levels define what concurrent transactions may observe: read uncommitted, read committed, repeatable read, and serializable. Each trades consistency for concurrency. The choice determines which anomaly phenomena a transaction can experience and therefore which application logic must tolerate stale, inconsistent, or transient data.

## Details

- Phenomena controlled: dirty reads (reading uncommitted data), non-repeatable reads (the same row changing between two reads), and phantoms (a query returning different rows across executions because another transaction inserted or deleted matching rows).
- Read uncommitted: no isolation; dirty reads are possible. Rarely used in practice because committed-but-uncommitted visibility corrupts most business logic.
- Read committed: each statement sees only committed data, eliminating dirty reads, but a later statement in the same transaction may see new commits — hence non-repeatable reads.
- Repeatable read: a transaction sees a stable snapshot for reads, preventing non-repeatable reads; phantoms may still occur unless the engine locks ranges (PostgreSQL prevents them at this level using snapshotting plus conflict detection).
- Serializable: the strictest level, where the outcome equals some serial execution of the transactions; engines implement it via true serialization, predicate locking, or optimistic conflict detection with retries.
- Defaults vary — Postgres defaults to read committed; MySQL defaults to repeatable read; some engines default higher. Know your engine's default before reasoning about behavior.
- Performance: serializable is safest but costs throughput under contention; use it where correctness dominates, and prefer weaker levels plus explicit application-level checks elsewhere.

## Practical Guidance

- Keep transactions short: long transactions hold locks or snapshots, raise conflict rates, and bloat connection pools.
- Measure contention before raising isolation: if no conflicting writes occur, the extra safety costs little; if conflicts dominate, first shorten transactions and reduce write hotspots.
- Test concurrency explicitly: run parallel write tests to confirm which anomalies the chosen level actually permits in your engine.
- Related techniques: [[wiki/devops-infra/optimistic-locking|Optimistic Locking]] handles conflicts in application code, [[wiki/devops-infra/connection-pooling|Connection Pooling]] bounds concurrent connections, and [[wiki/devops-infra/database-indexing|Database Indexing]] reduces lock-held time by making writes fast.

## Related

- [[wiki/devops-infra/transactions|Transactions]] — isolation within the ACID frame
- [[wiki/devops-infra/acid|ACID]] — the I of ACID
- [[wiki/devops-infra/optimistic-locking|Optimistic Locking]] — application-level isolation
- [[wiki/devops-infra/postgresql|PostgreSQL]] — isolation in practice
- [[wiki/devops-infra/observability|Observability]] — lock-wait and contention monitoring
