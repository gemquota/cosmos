---
type: "concept"
title: "EXPLAIN ANALYZE"
description: "Running a query while showing the actual plan and execution times"
tags: ["explain-analyze", "databases", "performance", "diagnostics"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# EXPLAIN ANALYZE

## Summary
EXPLAIN ANALYZE executes a query and reports the plan with actual row counts, timings, and buffers — the ground truth for performance debugging. The difference between estimated and actual rows is where optimization starts.

## Details
- Compare estimates to actuals: big gaps signal stale statistics or bad cost models.
- Read bottom-up: the expensive node is where time concentrates; that is what to fix.
- Beware side effects: wrap in a transaction and roll back, or use ANALYZE with caution.
- mykb relevance: wiki sync slowness is triaged with EXPLAIN ANALYZE on the hot query.

## Related
- [[wiki/compositions/query-plans|Query Plans]]
- [[wiki/compositions/slow-query-triage|Slow Query Triage]]
- [[wiki/compositions/query-optimization|Query Optimization]]
- [[wiki/compositions/index-selection|Index Selection]]
- [[wiki/devops-infra/database-indexing|Database Indexing]]
