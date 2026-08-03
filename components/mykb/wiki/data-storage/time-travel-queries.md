---
type: "concept"
title: "Time Travel Queries"
description: "Querying data as it existed at a past timestamp"
tags: ["time-travel", "versioning", "lakehouse", "query"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Time Travel Queries

## Summary
Time travel reads a consistent snapshot of a table as of an earlier timestamp or version. Delta Lake and Snowflake expose it natively; Iceberg snapshots give the same capability via snapshot IDs — the mechanism behind reproducing reports, auditing changes, and repairing bad loads without full reloads.

## Details
- Mechanism: storage systems keep immutable versions (Delta transactions, Iceberg snapshots, Snowflake time-travel retention); a query specifies a timestamp or version and the engine reads that snapshot; retention settings bound how far back travel is possible.
- Concrete example: a bad load overwrites a warehouse table; an analyst queries the table as of before the load and recovers the numbers for a report; a data engineer compares current and prior versions to see exactly what changed; an audit query reproduces a historical state for compliance.
- Failure modes: retention too short, so the needed snapshot is gone; version bloat consuming storage; time travel on tables without versioning support, silently returning current data; vacuum/cleanup jobs deleting snapshots still referenced by long-running queries; timestamps with clock skew selecting the wrong snapshot.
- Tradeoffs: time travel trades storage and retention management for reproducibility and repair — the alternative, full reloads and manual diffing, is expensive and error-prone; the mature pattern is declared retention per table, snapshot-based reads for anything auditable, and repair-by-snapshot as the standard recovery path.
- Operational notes: set retention deliberately, monitor snapshot counts, and test snapshot-based recovery in drills.
- RSIS3 relevance: RSIS3's state and checkpoint tables could use time travel — a bad loop step becomes a snapshot read away instead of a replay.

## Related

- [[wiki/data-storage/data-versioning|Data Versioning]] — versioning as the mechanism behind time travel
- [[wiki/data-storage/point-in-time-recovery|Point-in-Time Recovery]] — database-side recovery analog
- [[wiki/data-storage/snapshot-isolation-and-timetravel|Snapshot Isolation And Timetravel]] — MVCC foundations
- [[wiki/data-storage/delta-lake-and-merge-operations|Delta Lake And Merge Operations]] — Delta time travel in practice
- [[wiki/data-storage/iceberg-table-format-and-versioning|Iceberg Table Format And Versioning]] — Iceberg snapshot reads
