---
type: "concept"
title: "Time Travel Queries"
description: "Querying data as it existed at a past timestamp"
tags: ["time-travel", "versioning", "lakehouse", "query"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Time Travel Queries

## Summary

A stub to be expanded into a full article; frames the concept and open questions.

## Details

- Time travel reads a consistent snapshot of a table as of an earlier timestamp or version.
- Delta Lake and Snowflake expose it natively; Iceberg snapshots give the same capability via snapshot IDs.
- Use cases: reproduce a report, audit what changed, repair bad runs without full reloads, and compare states.
- Costs are bounded by retained versions and storage; retention settings cap how far back you can travel.

## Related

- [[wiki/data-storage/data-versioning|Data Versioning]] — versioning as the mechanism behind time travel
- [[wiki/data-storage/point-in-time-recovery|Point-in-Time Recovery]] — database-side recovery analog
- [[wiki/data-storage/snapshot-isolation-and-timetravel|Snapshot Isolation And Timetravel]] — MVCC foundations
- [[wiki/data-storage/delta-lake-and-merge-operations|Delta Lake And Merge Operations]] — Delta time travel in practice
- [[wiki/data-storage/iceberg-table-format-and-versioning|Iceberg Table Format And Versioning]] — Iceberg snapshot reads
