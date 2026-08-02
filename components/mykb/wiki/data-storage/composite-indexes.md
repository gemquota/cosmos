---
type: "concept"
title: "Composite Indexes"
description: "Multi-column ordering and leftmost-prefix usage rules"
tags: ["composite-index", "indexing", "query-tuning", "b-tree"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://www.postgresql.org/docs/current/indexes-multicolumn.html", "https://dev.mysql.com/doc/refman/8.4/en/multiple-column-indexes.html"]
---

# Composite Indexes

## Summary
A composite (multicolumn) index sorts rows by several columns in order. Queries that filter or order by the leading columns can use it, but the index helps less once a predicate skips a column, because keys are ordered left to right.

## Details
- **Leftmost prefix rule** — an index on `(a, b, c)` serves predicates on `a`, `a+b`, and `a+b+c`, but not `b` or `b+c` alone; the planner may still scan a range if `a` is constrained.
- **Ordering matters** — equality columns should come before range columns, and the column order should follow query frequency, not table definition. `WHERE a = ? AND b BETWEEN ...` works best when `a` leads.
- **Sort support** — a composite index can satisfy `ORDER BY a, b` and, in Postgres, descending sorts via `DESC` columns or `NULLS FIRST/LAST` options; MySQL 8 supports descending index columns too.
- **Costs** — each composite index is a full second copy of the keyed data, so width and count multiply write overhead and storage; Postgres limits index columns to 32, MySQL to 16.
- **Design practice** — start from the workload: collect slow queries, group their equality and range predicates, then choose the fewest indexes covering the most queries rather than one index per query.

## Related
- [[wiki/data-storage/b-tree-indexing|B-Tree Indexing]] — the structure composites extend
- [[wiki/data-storage/covering-indexes|Covering Indexes]] — composites that skip the heap
- [[wiki/data-storage/partial-indexes|Partial Indexes]] — filtering rows before indexing
- [[wiki/data-storage/query-tuning|Query Tuning]] — turning EXPLAIN output into index choices
- [[wiki/devops-infra/database-indexing|Database Indexing]] — operational indexing workflow
