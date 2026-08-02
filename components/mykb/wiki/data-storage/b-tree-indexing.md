---
type: "concept"
title: "B-Tree Indexing"
description: "Balanced tree pages, node splits, and range-scan support"
tags: ["b-tree", "indexing", "database-internals", "range-queries"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://www.postgresql.org/docs/current/btree-intro.html", "https://dev.mysql.com/doc/refman/8.4/en/index-btree-hash.html"]
---

# B-Tree Indexing

## Summary
The B-tree (usually B+-tree) is the default index in most relational databases: a balanced, multi-way tree whose node pages hold ordered keys and child pointers. It gives logarithmic point lookups and efficient ordered range scans with bounded height.

## Details
- **Structure** — internal pages route by key ranges; leaf pages hold keys plus row pointers (heap CTIDs in Postgres, primary keys in InnoDB) and are linked for sequential range traversal.
- **Balance and height** — every leaf sits at the same depth; a fanout of a few hundred keys per page keeps height around 3–4 even for billions of rows, so lookups cost a handful of page reads.
- **Splits and merges** — inserts into full pages split them, growing the tree at the top when the root splits; deletes can merge underfull pages to bound bloat.
- **Range support** — ordered keys plus leaf links make `BETWEEN`, prefix, and `ORDER BY` scans fast; hash indexes cannot do this.
- **Access patterns** — the optimizer chooses index scans, bitmap scans, and index-only scans based on selectivity; random page access on large ranges can lose to sequential scans.
- **mykb relevance** — wiki slugs, timestamps, and FK-like references are textbook B-tree keys; a growing corpus benefits from range scans over note creation time and tag lookups.

## Related
- [[wiki/data-storage/composite-indexes|Composite Indexes]] — multi-column B-trees and prefix rules
- [[wiki/data-storage/covering-indexes|Covering Indexes]] — indexes that answer queries without the heap
- [[wiki/data-storage/hash-indexes|Hash Indexes]] — the exact-match alternative
- [[wiki/data-storage/index-maintenance|Index Maintenance]] — bloat, rebuilds, and fill factors
- [[wiki/data-storage/buffer-pool-management|Buffer Pool Management]] — where index pages are cached
- [[wiki/devops-infra/database-indexing|Database Indexing]] — operational indexing practice
