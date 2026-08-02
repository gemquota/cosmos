---
type: "concept"
title: "Query Optimization"
description: "Improving slow queries via indexing, rewriting, and plan shaping"
tags: ["query-optimization", "databases", "performance", "practice"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Query Optimization

## Summary
Query optimization is the systematic process of making slow queries fast: measure, inspect the plan, fix the index or rewrite, re-measure. The big wins come from eliminating scans, bad joins, and row-by-row processing.

## Details
- Order of attack: index gaps, join strategy, query rewrite, schema change, then caching.
- Rewrite for set-based operations; avoid per-row function calls in WHERE clauses.
- Every optimization needs a before/after measurement or it is a guess.
- mykb relevance: the wiki link-resolution query was optimized from a scan to an index seek.

## Related
- [[wiki/compositions/query-plans|Query Plans]]
- [[wiki/compositions/explain-analyze|EXPLAIN ANALYZE]]
- [[wiki/compositions/slow-query-triage|Slow Query Triage]]
- [[wiki/compositions/index-selection|Index Selection]]
- [[wiki/software-engineering/performance-engineering|Performance Engineering]]
