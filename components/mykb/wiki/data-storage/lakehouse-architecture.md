---
type: "concept"
title: "Lakehouse Architecture"
description: "Combining lake storage with warehouse ACID and query semantics"
tags: ["lakehouse", "data-architecture", "open-table-formats", "delta-lake"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://docs.delta.io/latest/index.html", "https://iceberg.apache.org/"]
---

# Lakehouse Architecture

## Summary
A lakehouse keeps data on cheap object storage but adds warehouse features — ACID transactions, schema enforcement, indexing, and SQL — through open table formats. It collapses the lake/warehouse split so one copy of data serves BI, ML, and streaming workloads.

## Details
- **The core stack** — object storage for files, an open table format (Delta Lake, Apache Iceberg, Apache Hudi) for table metadata, and a query engine (Spark, Trino, DuckDB, Snowflake) that reads through the format.
- **Table format guarantees** — the format maintains transaction logs, snapshots, and schema versions, so concurrent writers get atomic commits and readers get consistent views without locking the files.
- **Why it emerged** — warehouses duplicated data and locked it behind proprietary engines; lakes were cheap but lacked transactions and quality. Lakehouses keep one canonical copy with both properties.
- **Time travel** — snapshot-based versioning lets analysts query the table as of any commit, a poor-man's point-in-time recovery that also powers reproducible ML datasets.
- **Trade-offs** — metadata and compaction (Z-order, clustering) add management burden; file-level operations need maintenance jobs (OPTIMIZE, VACUUM) that classic warehouses hide.
- **Ecosystem reality** — Delta's V2 format is now open, Iceberg has broad engine support, and vendors like Databricks, AWS, and Snowflake all speak at least one format, so the format choice is a long-lived decision.

## Related
- [[wiki/data-storage/open-table-formats|Open Table Formats]] — the metadata layer
- [[wiki/data-storage/data-lake|Data Lake]] — the storage base
- [[wiki/data-storage/data-warehouse|Data Warehouse]] — the semantics being added
- [[wiki/data-storage/compression-codecs|Compression Codecs]] — file-level efficiency
- [[wiki/data-storage/table-partitioning|Table Partitioning]] — layout inside the lakehouse
