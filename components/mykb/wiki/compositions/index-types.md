---
type: "concept"
title: "Index Types"
description: "B-tree, hash, GIN, GiST, BRIN and when each fits"
tags: ["index-types", "databases", "indexes", "design"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Index Types

## Summary
Index types trade structure for query shape: B-trees for ranges and equality, hash for exact lookups, GIN for arrays and full text, GiST for geometry, BRIN for huge sorted tables. Choosing the right type is most of index design.

## Details
- B-tree: general purpose, ranges, order, uniqueness — the default.
- Hash: fast exact equality, useless for ranges. GIN: containment and full text. BRIN: cheap on append-only data.
- Partial, expression, and covering indexes adapt a type to a workload.
- mykb relevance: wiki tag lookups favor GIN; slug lookups favor B-tree.

## Related
- [[wiki/compositions/b-tree-basics|B-Tree Basics]]
- [[wiki/compositions/index-selection|Index Selection]]
- [[wiki/devops-infra/database-indexing|Database Indexing]]
- [[wiki/compositions/query-plans|Query Plans]]
- [[wiki/compositions/query-optimization|Query Optimization]]
