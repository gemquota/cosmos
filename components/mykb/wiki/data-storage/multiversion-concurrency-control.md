---
type: "concept"
title: "Multiversion Concurrency Control"
description: "Versioned rows that let readers avoid blocking writers"
tags: ["mvcc", "concurrency-control", "snapshot-isolation", "database-internals"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://www.postgresql.org/docs/current/mvcc.html", "https://dev.mysql.com/doc/refman/8.4/en/innodb-multi-versioning.html"]
---

# Multiversion Concurrency Control

## Summary
Multiversion concurrency control (MVCC) keeps multiple versions of each row so readers see a consistent snapshot without blocking writers. Writers may still conflict with each other, but the read/write separation is what makes PostgreSQL and InnoDB scale on mixed OLTP loads.

## Details
- **Row versions** — each update inserts a new row version rather than overwriting; versions carry creation and expiration markers (transaction IDs or commit timestamps) that decide visibility.
- **Snapshot visibility** — a transaction sees versions committed before its snapshot and not yet deleted; the engine applies a visibility rule per tuple, making long-running readers immune to concurrent writes.
- **Garbage collection** — old versions must be reclaimed once no snapshot can see them; Postgres runs autovacuum, InnoDB uses purge threads, both keyed to the oldest active transaction.
- **Write conflicts** — two writers to the same row still serialize; on conflict, the later writer may block, abort, or overwrite depending on isolation level (repeatable read aborts, read committed waits or overwrites).
- **Trade-offs** — version overhead increases table size and index bloat, but eliminates reader-writer blocking and enables statement- and transaction-level snapshots cheaply.

## Related
- [[wiki/data-storage/transaction-isolation-levels|Transaction Isolation Levels]] — snapshot semantics per level
- [[wiki/data-storage/vacuuming-and-compaction|Vacuuming & Compaction]] — reclaiming dead versions
- [[wiki/data-storage/two-phase-locking|Two-Phase Locking]] — the blocking alternative
- [[wiki/data-storage/optimistic-concurrency-control|Optimistic Concurrency Control]] — related validation approach
- [[wiki/data-storage/crash-recovery|Crash Recovery]] — restoring version state after failure
