---
type: "concept"
title: "Clustered Tables"
description: "Heap versus clustered-index table organization"
tags: ["clustered-index", "heap", "table-organization", "innodb"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://dev.mysql.com/doc/refman/8.4/en/innodb-index-types.html", "https://www.postgresql.org/docs/current/sql-cluster.html"]
---

# Clustered Tables

## Summary
In a clustered table, row data is stored inside the primary-key B-tree, ordered by that key; in a heap-organized table, rows live in unsorted pages and indexes point at them. InnoDB is clustered on the primary key; PostgreSQL is heap-based with `CLUSTER` available as an optional one-time reordering.

## Details
- **InnoDB clustered index** — the primary key's B-tree leaves contain whole rows; secondary indexes store the primary key instead of a pointer, so a secondary lookup does two B-tree traversals. Missing a PK makes InnoDB use a hidden row ID.
- **PostgreSQL heap** — rows are placed wherever free space exists; every index leaf stores a `(block, offset)` CTID. `CLUSTER` or `pg_repack` physically reorders the heap by an index, but only until the next updates.
- **Range-scan behavior** — clustered layout makes PK range scans sequential and cheap; heap scans of scattered rows touch many pages, which is why `CLUSTER` helps before big analytical jobs.
- **Update cost** — clustered tables pay more on updates that move rows (PK changes or page splits), while heaps leave a dead tuple and a new version elsewhere, deferring cleanup to vacuum.
- **Index-organization tables** — Oracle supports IOTs (index-organized tables) for lookup-heavy small rows, and SQL Server clustered indexes work like InnoDB's; the design axis is the same everywhere.

## Related
- [[wiki/data-storage/b-tree-indexing|B-Tree Indexing]] — the structure clustered tables are built on
- [[wiki/data-storage/vacuuming-and-compaction|Vacuuming & Compaction]] — reclaiming heap bloat
- [[wiki/data-storage/composite-indexes|Composite Indexes]] — clustering on composite keys
- [[wiki/data-storage/surrogate-keys|Surrogate vs Natural Keys]] — what you cluster on matters
- [[wiki/devops-infra/postgresql|PostgreSQL]] — heap engine with CLUSTER support
