---
type: "concept"
title: "Lock Granularity"
description: "Row, page, and table locks plus escalation trade-offs"
tags: ["locking", "lock-granularity", "concurrency", "database-internals"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://www.postgresql.org/docs/current/explicit-locking.html", "https://dev.mysql.com/doc/refman/8.4/en/innodb-locking.html"]
---

# Lock Granularity

## Summary
Lock granularity decides how much data a single lock covers: rows, pages, tables, or whole databases. Fine granularity maximizes concurrency but multiplies lock overhead; coarse granularity is cheap but blocks unrelated work, so engines pick granularity per operation.

## Details
- **Row locks** — the finest common unit; InnoDB and Postgres lock individual rows for writes, so concurrent transactions can touch different rows in the same table.
- **Page locks** — cover a fixed-size page of rows; used by some engines and index structures to reduce lock count, with the cost that unrelated rows on the same page serialize.
- **Table locks** — serialize whole-table access; used by MyISAM, SQLite's writer lock, and DDL operations. They are simple and fast but destroy write concurrency on hot tables.
- **Lock escalation** — engines like SQL Server automatically promote many row locks to a table lock when a threshold is exceeded; InnoDB and Postgres generally avoid escalation in favor of more lock entries.
- **Intent locks** — before locking rows, transactions take intent locks at table level so DDL can detect active access without scanning every row lock.
- **Trade-off framing** — the right granularity follows the workload: point lookups want row locks, bulk loads and DDL want table locks, and mixed OLTP wants intent-lock hierarchies.

## Related
- [[wiki/data-storage/two-phase-locking|Two-Phase Locking]] — the protocol granularity serves
- [[wiki/data-storage/deadlock-detection|Deadlock Detection]] — more granularity, more cycles
- [[wiki/data-storage/transaction-isolation-levels|Transaction Isolation Levels]] — what locks must guarantee
- [[wiki/data-storage/database-constraints|Database Constraints]] — operations that take stronger locks
- [[wiki/devops-infra/connection-pooling|Connection Pooling]] — how lock contention surfaces operationally
