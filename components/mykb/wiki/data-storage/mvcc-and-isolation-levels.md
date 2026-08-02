---
type: "concept"
title: "MVCC and Isolation Levels"
description: "Multi-version concurrency control and the isolation spectrum"
tags: ["mvcc", "isolation", "transactions", "concurrency"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://www.postgresql.org/docs/current/mvcc.html", "https://en.wikipedia.org/wiki/Multiversion_concurrency_control"]
---

# MVCC and Isolation Levels

## Summary

Multi-version concurrency control lets readers see a consistent snapshot while writers proceed.
Isolation levels define which anomalies readers may observe.
Choosing levels balances consistency guarantees against concurrency and throughput.
Isolation levels are contracts with users; defaulting to serializable is safer, weaker levels are faster.

## Details

- MVCC keeps old row versions so readers never block on writers.
- Levels: read committed, repeatable read, snapshot, serializable.
- Anomalies: dirty reads, non-repeatable reads, phantoms, write skew.
- Serializable isolation prevents anomalies but costs conflict detection.
- Postgres implements snapshot isolation; SQL Server and Oracle differ in defaults.
- Deadlock and write-skew handling differ by level; test under concurrency.
- Vacuum/version cleanup keeps MVCC overhead bounded.
- Isolation expectations should be documented per application so developers do not discover them in production incidents.

## Related

- [[wiki/data-storage/transactions-and-acid-revisited|Transactions And Acid Revisited]] — ACID context
- [[wiki/data-storage/snapshot-isolation-and-timetravel|Snapshot Isolation And Timetravel]] — snapshot reads
- [[wiki/data-storage/multiversion-concurrency-control|Multiversion Concurrency Control]] — existing note
- [[wiki/data-storage/transaction-isolation-levels|Transaction Isolation Levels]] — isolation levels
- [[wiki/data-storage/optimistic-concurrency-control|Optimistic Concurrency Control]] — alternative
- [[wiki/data-storage/data-quality-dimensions|Data Quality Dimensions]] — quality dimensions
- [[wiki/data-storage/data-observability-and-monitoring|Data Observability and Monitoring]] — observability
- [[wiki/data-storage/data-testing-frameworks|Data Testing Frameworks]] — testing
- [[wiki/data-storage/feature-stores-and-ml-features|Feature Stores and ML Features]] — ML features
- [[wiki/data-storage/data-contracts-and-agreements|Data Contracts and Agreements]] — data contracts
- [[wiki/data-storage/incremental-loading-strategies|Incremental Loading Strategies]] — incremental loading
- [[wiki/data-storage/schema-evolution-in-streams|Schema Evolution In Streams]] — schema evolution

