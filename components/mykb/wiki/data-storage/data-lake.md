---
type: "concept"
title: "Data Lake"
description: "Raw schema-flexible storage of diverse datasets"
tags: ["data-lake", "object-storage", "schema-on-read", "big-data"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://docs.aws.amazon.com/whitepapers/latest/building-data-lakes/building-data-lakes.html", "https://iceberg.apache.org/"]
---

# Data Lake

## Summary
A data lake is a central repository of raw data stored in its native form, typically on object storage like S3. Files are organized by convention, schemas are applied at read time, and cheap storage lets organizations keep data that a warehouse would discard.

## Details
- **Storage model** — objects (Parquet, Avro, JSON, images) in a flat namespace; partitions by date or key, and catalog entries that track table-like metadata.
- **Schema-on-read** — the same file can be interpreted differently by different consumers; flexibility is the point, but it pushes quality responsibility onto every reader.
- **Cost profile** — storage is a fraction of warehouse cost, so raw, exploratory, and ML data lives cheaply at scale; compute is decoupled and billed per query.
- **Failure modes** — without governance, lakes become swamps: unreadable formats, orphaned partitions, and conflicting conventions; catalogs, naming rules, and data contracts are the antidote.
- **Processing** — Spark, Trino, and Flink read lake files directly; orchestrated jobs land processed tables back into the lake, which is the "lakehouse" convergence.
- **Open table formats** — Iceberg, Delta, and Hudi add ACID, snapshots, and schema evolution on top of raw files, making the lake transactional without a central warehouse.

## Related
- [[wiki/data-storage/lakehouse-architecture|Lakehouse Architecture]] — lake plus warehouse semantics
- [[wiki/data-storage/open-table-formats|Open Table Formats]] — ACID over raw files
- [[wiki/data-storage/schema-on-read|Schema-on-Read vs Schema-on-Write]] — the central trade-off
- [[wiki/data-storage/object-storage|Object Storage]] — the physical layer
- [[wiki/data-storage/data-warehouse|Data Warehouse]] — the structured alternative
