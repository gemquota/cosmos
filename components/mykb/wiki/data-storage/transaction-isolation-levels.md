---
type: "concept"
title: "Transaction Isolation Levels"
description: "Read committed, repeatable read, serializable, and anomalies"
tags: ["isolation-levels", "transactions", "concurrency", "anomalies"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://www.postgresql.org/docs/current/transaction-iso.html", "https://dev.mysql.com/doc/refman/8.4/en/innodb-transaction-isolation-levels.html"]
---

# Transaction Isolation Levels

## Summary
Isolation levels define how much concurrent transactions may see of each other's changes. The SQL standard names four levels — read uncommitted, read committed, repeatable read, serializable — each permitting a different set of anomalies.

## Details
- **Read uncommitted** — transactions can see uncommitted changes (dirty reads); rarely used because it trades correctness for marginal speed.
- **Read committed** — each statement sees only committed data; dirty reads are prevented but non-repeatable reads remain: two statements in one transaction can see different values for the same row. This is Postgres's and Oracle's default.
- **Repeatable read** — a snapshot taken at the first read stays stable for the whole transaction, preventing non-repeatable reads; in Postgres (and InnoDB, its default) it also prevents phantoms via snapshot or gap locks.
- **Serializable** — transactions behave as if executed one at a time. Postgres uses Serializable Snapshot Isolation with conflict detection; InnoDB uses next-key locking. Anomalies like write skew and read skew are only eliminated here.
- **Anomaly table** — dirty read, non-repeatable read, phantom, write skew, and read skew form a hierarchy; each stronger level eliminates a subset.
- **Choice guidance** — default levels fit most OLTP; serializable costs contention but guarantees correctness for financial or inventory logic.

## Related
- [[wiki/data-storage/acid-transactions|ACID Transactions]] — the umbrella contract
- [[wiki/data-storage/multiversion-concurrency-control|Multiversion Concurrency Control]] — how snapshot isolation works
- [[wiki/data-storage/lock-granularity|Lock Granularity]] — row versus table level locking
- [[wiki/data-storage/optimistic-concurrency-control|Optimistic Concurrency Control]] — validation-based isolation
- [[wiki/devops-infra/isolation-levels|Isolation Levels]] — operational trade-offs
