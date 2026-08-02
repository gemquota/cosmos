---
type: "concept"
title: "SQL on Lakehouse"
description: "Warehouse-class SQL over open lake tables"
tags: ["sql", "lakehouse", "delta", "iceberg"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://docs.delta.io/latest/", "https://en.wikipedia.org/wiki/Data_lakehouse"]
---

# SQL on Lakehouse

## Summary

SQL on lakehouse runs warehouse-grade queries directly on open table formats.
Engines like Spark, Trino, and DuckDB read Delta, Iceberg, and Hudi tables.
It delivers warehouse semantics without warehouse lock-in.
SQL on lakehouse delivers warehouse capabilities without warehouse lock-in.

## Details

- Open formats give ACID, time travel, and schema evolution on lakes.
- Engines share tables through shared catalogs.
- Query optimization uses format statistics and metadata.
- Cost control comes from partition pruning and skip indexes.
- Lakehouse SQL is the centerpiece of modern data platforms.
- Catalogs make tables shareable across engines.
- Format and engine choice should follow workload, not habit.
- Lakehouse SQL is the payoff of open formats: warehouse semantics without lock-in.

## Related

- [[wiki/data-storage/lakehouse-architecture|Lakehouse Architecture]] — pattern
- [[wiki/data-storage/open-table-formats-and-interoperability|Open Table Formats And Interoperability]] — formats
- [[wiki/data-storage/presto-and-trino|Presto and Trino]] — engine
- [[wiki/data-storage/lakehouse-architecture|Lakehouse Architecture]] — existing note
- [[wiki/data-storage/data-lake-file-layouts|Data Lake File Layouts]] — layout
- [[wiki/data-storage/data-warehouse|Data Warehouse]] — warehouse reference

