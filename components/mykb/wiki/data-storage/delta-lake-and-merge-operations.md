---
type: "entity"
title: "Delta Lake and Merge Operations"
description: "ACID table format with transactional MERGE on object storage"
tags: ["delta-lake", "merge", "acid", "lakehouse"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Delta Lake and Merge Operations

## Summary

A stub to be expanded into a full article; frames the concept and open questions.

## Details

- Delta Lake adds a transaction log and ACID properties to Parquet files.
- MERGE enables upserts, deletes, and SCD Type 2 directly on lake tables.
- Time travel, vacuum, and change data feed round out the feature set.
- It is the storage layer behind Databricks lakehouse workloads.

## Related

- [[wiki/data-storage/open-table-formats|Open Table Formats]] — format family
- [[wiki/data-storage/lakehouse-architecture|Lakehouse Architecture]] — lakehouse pattern
- [[wiki/data-storage/merge-and-upsert-patterns|Merge And Upsert Patterns]] — merge semantics
- [[wiki/data-storage/time-travel-queries|Time Travel Queries]] — Delta time travel
- [[wiki/data-storage/data-engineering-fundamentals|Data Engineering Fundamentals]] — core data engineering concepts
