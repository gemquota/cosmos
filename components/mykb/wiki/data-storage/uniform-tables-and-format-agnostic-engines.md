---
type: "concept"
title: "Uniform Tables and Format-Agnostic Engines"
description: "Reading one table through multiple format views"
tags: ["uniform-tables", "interoperability", "lakehouse", "engines"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Uniform Tables and Format-Agnostic Engines

## Summary

A stub to be expanded into a full article; frames the concept and open questions.

## Details

- Uniform tables maintain multiple format metadata views over one set of data files.
- Databricks Uniform and similar projects expose Delta tables as Iceberg/Hudi.
- Format-agnostic engines (Trino, DuckDB, Spark) read whatever catalog points at files.
- Tradeoffs: metadata consistency overhead vs engine choice freedom.

## Related

- [[wiki/data-storage/open-table-formats|Open Table Formats]] — format family
- [[wiki/data-storage/open-table-formats-and-interoperability|Open Table Formats And Interoperability]] — interop context
- [[wiki/data-storage/sql-on-lakehouse|Sql On Lakehouse]] — engine access
- [[wiki/data-storage/lakehouse-engines-comparison|Lakehouse Engines Comparison]] — engine capabilities
- [[wiki/data-storage/data-engineering-fundamentals|Data Engineering Fundamentals]] — core data engineering concepts
