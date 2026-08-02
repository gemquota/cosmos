---
type: "concept"
title: "Query Plans"
description: "The execution strategy a database chooses for a query"
tags: ["query-plans", "databases", "performance", "optimization"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Query Plans

## Summary
A query plan is the database's chosen strategy — which indexes, join orders, and scan methods to run. Reading plans (EXPLAIN output) is how you find out why a query is slow instead of guessing.

## Details
- Plans show scan types (index vs seq), join methods (hash, nested loop, merge), and row estimates.
- Estimate drift is the usual cause of bad plans — update statistics and test with real data.
- Plan shape changes with data volume; what is fast at 1k rows may invert at 1M.
- mykb relevance: the wiki DB explains slow index queries before adding a new index.

## Related
- [[wiki/compositions/explain-analyze|EXPLAIN ANALYZE]]
- [[wiki/compositions/index-selection|Index Selection]]
- [[wiki/compositions/slow-query-triage|Slow Query Triage]]
- [[wiki/compositions/query-optimization|Query Optimization]]
- [[wiki/devops-infra/database-indexing|Database Indexing]]
