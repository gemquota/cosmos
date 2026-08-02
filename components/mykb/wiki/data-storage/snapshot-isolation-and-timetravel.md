---
type: "concept"
title: "Snapshot Isolation and Time Travel"
description: "Reading a consistent historical state through MVCC-style snapshotting"
tags: ["mvcc", "snapshot-isolation", "time-travel", "consistency"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Snapshot Isolation and Time Travel

## Summary

A stub to be expanded into a full article; frames the concept and open questions.

## Details

- Snapshot isolation gives each transaction a consistent view of committed data at its start time.
- Databases implement it with version chains or copy-on-write storage; lakehouses implement it with immutable snapshots.
- Time travel is snapshot isolation exposed as a query feature over historical versions.
- Write skew is the classic anomaly snapshot isolation does not prevent; serializable isolation adds conflict checks.

## Related

- [[wiki/data-storage/multiversion-concurrency-control|Multiversion Concurrency Control]] — MVCC mechanics
- [[wiki/data-storage/transaction-isolation-levels|Transaction Isolation Levels]] — isolation level spectrum
- [[wiki/data-storage/time-travel-queries|Time Travel Queries]] — query-side time travel
- [[wiki/data-storage/wal-and-consistency|Wal And Consistency]] — WAL as the durability companion
- [[wiki/data-storage/data-engineering-fundamentals|Data Engineering Fundamentals]] — core data engineering concepts
