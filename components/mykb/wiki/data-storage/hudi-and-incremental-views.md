---
type: "concept"
title: "Apache Hudi and Incremental Views"
description: "Table format with record-level upserts and incremental processing"
tags: ["hudi", "upserts", "incremental", "lakehouse"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Apache Hudi and Incremental Views

## Summary

A stub to be expanded into a full article; frames the concept and open questions.

## Details

- Hudi supports record-level upserts/deletes with Copy-on-Write and Merge-on-Read tables.
- Incremental queries read only changed records since a commit.
- It powers streaming ingestion into lakes with change tracking.
- Choose Hudi when near-real-time upserts into lake tables dominate.

## Related

- [[wiki/data-storage/open-table-formats|Open Table Formats]] — format family
- [[wiki/data-storage/cdc-change-data-capture|Change Data Capture]] — change capture
- [[wiki/data-storage/iceberg-table-format-and-versioning|Iceberg Table Format And Versioning]] — Iceberg comparison
- [[wiki/data-storage/incremental-loading-strategies|Incremental Loading Strategies]] — incremental patterns
- [[wiki/data-storage/data-engineering-fundamentals|Data Engineering Fundamentals]] — core data engineering concepts
