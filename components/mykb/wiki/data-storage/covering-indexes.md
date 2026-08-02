---
type: "concept"
title: "Covering Indexes"
description: "Including extra columns so queries skip table access"
tags: ["covering-index", "index-only-scan", "indexing", "query-tuning"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://www.postgresql.org/docs/current/indexes-index-only-scans.html", "https://dev.mysql.com/doc/refman/8.4/en/glossary.html#glos_covering_index"]
---

# Covering Indexes

## Summary
A covering index contains every column a query needs, so the engine answers the query from index pages alone. PostgreSQL calls this an index-only scan; MySQL and SQLite call it a covering index. Avoiding heap access can cut read I/O dramatically for hot, narrow queries.

## Details
- **Mechanism** — B-tree leaves store indexed keys plus, for INCLUDE columns or secondary indexes, extra payload values. When all referenced columns are in the index, no row fetch is needed.
- **PostgreSQL INCLUDE** — `CREATE INDEX ... INCLUDE (col)` adds non-key columns to the leaves without widening the sort key; non-key columns cannot be used in predicates but can be returned or filtered after fetch.
- **MySQL secondary indexes** — InnoDB secondary indexes implicitly append the primary key; a query that needs only indexed columns plus the PK is automatically covered, which is why InnoDB tables usually have a compact synthetic PK.
- **Visibility check** — Postgres still must check row visibility for MVCC, so it consults the visibility map; a mostly-visible page avoids heap reads entirely.
- **Trade-offs** — extra INCLUDE columns bloat the index and slow writes, so covering indexes fit read-heavy, narrow, frequently executed queries (dashboards, auth lookups, join probes).

## Related
- [[wiki/data-storage/composite-indexes|Composite Indexes]] — multi-column keys that often cover
- [[wiki/data-storage/b-tree-indexing|B-Tree Indexing]] — the leaf layout covering relies on
- [[wiki/data-storage/index-maintenance|Index Maintenance]] — bloat costs of wide indexes
- [[wiki/data-storage/query-tuning|Query Tuning]] — spotting index-only scans in plans
- [[wiki/devops-infra/database-indexing|Database Indexing]] — operational index strategies
