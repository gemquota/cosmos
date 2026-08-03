---
type: "concept"
title: "Snapshot Isolation and Time Travel"
description: "Reading a consistent historical state through MVCC-style snapshotting"
tags: ["mvcc", "snapshot-isolation", "time-travel", "consistency"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Snapshot Isolation and Time Travel

## Summary
Snapshot isolation gives each transaction a consistent view of committed data at its start time. Databases implement it with version chains or copy-on-write storage, and lakehouses implement it with immutable snapshots; time travel is the same mechanism exposed as a query feature over historical versions.

## Details
- Mechanism: each transaction sees the database as of its start timestamp; writers create new versions rather than overwriting in place (MVCC version chains, or immutable files in lakehouses); readers never block writers; time travel queries specify a timestamp or version and read that snapshot.
- Concrete example: an analytics query runs for an hour while ingestion writes new rows — the query still sees a consistent start-of-hour state; a user queries the warehouse as of yesterday and reproduces a report exactly; a lakehouse table keeps N versions, rolling back a bad load by reading the prior snapshot.
- Failure modes: write skew — the classic anomaly snapshot isolation does not prevent (two transactions read overlapping data and both write, violating a constraint); version bloat exhausting storage or slowing reads; snapshot retention too short for the time-travel window needed; vacuuming that deletes versions still referenced by long-running queries.
- Tradeoffs: snapshot isolation trades some concurrency anomalies for non-blocking reads — the most important practical guarantee; the alternative, strict serializability, adds conflict checks and contention; the mature pattern is snapshot isolation by default, serializable where constraints demand, with retention tuned to the query and audit window.
- Operational notes: monitor version bloat and retention, test long-query-versus-writer behavior, and define the time-travel window per table.
- RSIS3 relevance: RSIS3's state snapshots benefit from the same idea — a bad loop step can be rolled back by reading the prior snapshot instead of replaying history.

## Related

- [[wiki/data-storage/multiversion-concurrency-control|Multiversion Concurrency Control]] — MVCC mechanics
- [[wiki/data-storage/transaction-isolation-levels|Transaction Isolation Levels]] — isolation level spectrum
- [[wiki/data-storage/time-travel-queries|Time Travel Queries]] — query-side time travel
- [[wiki/data-storage/wal-and-consistency|Wal And Consistency]] — WAL as the durability companion
- [[wiki/data-storage/data-engineering-fundamentals|Data Engineering Fundamentals]] — core data engineering concepts
