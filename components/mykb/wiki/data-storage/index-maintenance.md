---
type: "concept"
title: "Index Maintenance"
description: "Fragmentation, bloat, rebuilds, and fill factors"
tags: ["index-maintenance", "bloat", "rebuild", "database-tuning"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://www.postgresql.org/docs/current/sql-reindex.html", "https://dev.mysql.com/doc/refman/8.4/en/optimizing-innodb-diskio.html"]
---

# Index Maintenance

## Summary
Indexes degrade as data changes: page splits fragment the key order, dead versions bloat B-trees, and fill factors leave wasteful gaps. Maintenance — reindexing, rebuilding, and vacuuming — restores scan efficiency and reclaims storage, but every rebuild costs locks and I/O.

## Details
- **Bloat** — in MVCC databases, every update leaves a dead index entry that vacuum or purge must remove; heavy update patterns can bloat an index to many times its logical size.
- **Fill factor** — `fillfactor` (Postgres and InnoDB page settings) reserves free space per leaf page for in-place updates; 70–90% is common for update-heavy tables, while append-only tables use 100%.
- **Rebuilds** — `REINDEX` (Postgres) or `ALTER TABLE ... DROP/ADD INDEX` (MySQL) writes a fresh, compact index; Postgres 12+ allows `REINDEX CONCURRENTLY` to avoid blocking writes, at the cost of extra work.
- **Fragmentation** — unordered inserts into random keys cause page splits and scattered reads; sequential keys keep pages dense but create hot-spot contention on the rightmost page.
- **Monitoring** — track index size versus table size, bloat estimators (pgstattuple, pg_bloat_check-style queries), and scan efficiency; drop unused indexes detected via `pg_stat_user_indexes` or MySQL's `sys.schema_unused_indexes`.
- **Cadence** — automatic vacuum keeps Postgres steady state; scheduled rebuilds fit MySQL and heavily updated tables; empty or duplicate indexes should be dropped, not rebuilt.

## Related
- [[wiki/data-storage/vacuuming-and-compaction|Vacuuming & Compaction]] — dead-row reclamation feeding bloat
- [[wiki/data-storage/b-tree-indexing|B-Tree Indexing]] — structure being maintained
- [[wiki/data-storage/database-performance-monitoring|Database Performance Monitoring]] — spotting bloat and unused indexes
- [[wiki/data-storage/composite-indexes|Composite Indexes]] — wider indexes bloat faster
- [[wiki/devops-infra/database-indexing|Database Indexing]] — operational index lifecycle
