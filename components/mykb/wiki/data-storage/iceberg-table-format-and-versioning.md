---
type: "entity"
title: "Iceberg Table Format and Versioning"
description: "Snapshot-based table format for ACID on the lake"
tags: ["iceberg", "table-format", "snapshots", "lakehouse"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Iceberg Table Format and Versioning

## Summary

A stub to be expanded into a full article; frames the concept and open questions.

## Details

- Iceberg separates metadata (manifest files) from data files, enabling atomic commits.
- Snapshots give time travel, rollback, and incremental reads.
- Hidden partitioning and schema evolution without rewrites are headline features.
- Engines implement Iceberg's spec for multi-engine lakehouse reads.

## Related

- [[wiki/data-storage/open-table-formats|Open Table Formats]] — format family
- [[wiki/data-storage/schema-evolution|Schema Evolution]] — evolution support
- [[wiki/data-storage/time-travel-queries|Time Travel Queries]] — snapshot reads
- [[wiki/data-storage/table-format-comparisons|Table Format Comparisons]] — vs Delta/Hudi
- [[wiki/data-storage/data-engineering-fundamentals|Data Engineering Fundamentals]] — core data engineering concepts
