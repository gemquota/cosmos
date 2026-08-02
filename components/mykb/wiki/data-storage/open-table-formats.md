---
type: "concept"
title: "Open Table Formats"
description: "Iceberg/Delta-style table metadata, snapshots, and transactions"
tags: ["iceberg", "delta-lake", "hudi", "table-formats"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://iceberg.apache.org/spec/", "https://docs.delta.io/latest/index.html"]
---

# Open Table Formats

## Summary
Open table formats (Apache Iceberg, Delta Lake, Apache Hudi) manage collections of files as tables: metadata tracks schema, partitions, and snapshots, and a transaction log makes commits atomic across many engines. They bring warehouse behavior to object storage.

## Details
- **Metadata layer** — Iceberg keeps a catalog pointer to a metadata file per snapshot; Delta keeps a transaction log (JSON + checkpoints) in `_delta_log/`; both describe which data files belong to which version.
- **Atomic commits** — writers append new files and update metadata atomically (catalog conditional put or log append); readers always see a consistent snapshot even mid-write, which is impossible with bare Parquet listings.
- **Schema evolution** — adding, renaming, or reordering columns is recorded in metadata, and readers resolve per-file schemas; old snapshots remain readable, enabling time travel.
- **Partitioning** — partition layout is metadata (Iceberg hidden partitioning) rather than a storage convention, so queries prune by partition transforms without knowing the directory scheme.
- **Maintenance** — expired snapshots, orphan files, and small-file proliferation need compaction and cleanup jobs (Iceberg `expire_snapshots`, Delta `VACUUM`); this is the operational tax of file-based tables.
- **Ecosystem** — all three formats are open-source with multi-engine support; the format choice determines which engines, catalogs, and vendor features are available, so treat it as an architecture decision.

## Related
- [[wiki/data-storage/lakehouse-architecture|Lakehouse Architecture]] — the system these formats power
- [[wiki/data-storage/data-lake|Data Lake]] — the raw storage underneath
- [[wiki/data-storage/schema-evolution|Schema Evolution]] — format-managed compatibility
- [[wiki/data-storage/table-partitioning|Table Partitioning]] — metadata-driven layout
- [[wiki/data-storage/vacuuming-and-compaction|Vacuuming & Compaction]] — snapshot cleanup
