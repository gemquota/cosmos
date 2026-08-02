---
type: "concept"
title: "B-Tree Basics"
description: "The balanced tree structure behind most database indexes"
tags: ["b-tree", "indexes", "databases", "internals"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# B-Tree Basics

## Summary
A B-tree keeps sorted keys in a balanced, wide tree where each node holds many keys, so lookups, inserts, and range scans touch few pages. It is the default index structure in almost every relational database.

## Details
- Wide nodes exploit page-sized I/O: one disk read fetches dozens of keys.
- Range queries are cheap because leaves are linked in key order.
- Structure matters for index design: prefix columns, order, and selectivity decide usefulness.
- mykb relevance: the wiki search index over slugs uses a B-tree for prefix lookups.

## Related
- [[wiki/compositions/index-types|Index Types]]
- [[wiki/compositions/index-selection|Index Selection]]
- [[wiki/compositions/query-plans|Query Plans]]
- [[wiki/devops-infra/database-indexing|Database Indexing]]
- [[wiki/compositions/query-optimization|Query Optimization]]
