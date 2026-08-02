---
type: "concept"
title: "Table Format Comparisons"
description: "Delta Lake vs Iceberg vs Hudi side by side"
tags: ["delta", "iceberg", "hudi", "comparison"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Table Format Comparisons

## Summary

A stub to be expanded into a full article; frames the concept and open questions.

## Details

- All three provide ACID on lakes; they differ in metadata model and engine integration.
- Iceberg emphasizes spec stability and multi-engine reads; Delta integrates deeply with Spark/Databricks.
- Hudi leads on record-level upsert throughput.
- Interoperability (Uniform tables, XTable) is converging the formats.

## Related

- [[wiki/data-storage/open-table-formats|Open Table Formats]] — format family
- [[wiki/data-storage/open-table-formats-and-interoperability|Open Table Formats And Interoperability]] — interop direction
- [[wiki/data-storage/delta-lake-and-merge-operations|Delta Lake And Merge Operations]] — Delta specifics
- [[wiki/data-storage/iceberg-table-format-and-versioning|Iceberg Table Format And Versioning]] — Iceberg specifics
- [[wiki/data-storage/data-engineering-fundamentals|Data Engineering Fundamentals]] — core data engineering concepts
