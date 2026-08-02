---
type: "concept"
title: "Index Selection"
description: "Choosing which columns to index for the queries that matter"
tags: ["index-selection", "indexes", "performance", "databases"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Index Selection

## Summary
Index selection picks columns and index shapes from real query patterns: filter columns, join keys, order-by columns, and covering needs. Every index costs writes and storage, so selection is a cost-benefit game.

## Details
- Start from the query log: filter, sort, and join columns of hot queries.
- Column order in composite indexes follows equality-then-range and selectivity rules.
- Drop unused indexes; measure write amplification before adding more.
- mykb relevance: the wiki DB indexes slug, status, and tag — nothing else until queries ask.

## Related
- [[wiki/compositions/index-types|Index Types]]
- [[wiki/compositions/query-plans|Query Plans]]
- [[wiki/compositions/explain-analyze|EXPLAIN ANALYZE]]
- [[wiki/compositions/query-optimization|Query Optimization]]
- [[wiki/compositions/slow-query-triage|Slow Query Triage]]
