---
type: "concept"
title: "Query Plans"
description: "The execution strategy a database chooses for a query"
tags: ["query-plans", "databases", "performance", "optimization"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Query Plans

## Summary

A query plan is the database's chosen strategy — which indexes, join orders, and scan methods to run. Reading plans (EXPLAIN output) is how you find out why a query is slow instead of guessing.

## Details
- Mechanism: the planner turns SQL into an operator tree: scans (sequential vs index), joins (nested loop, hash, merge), aggregations, and filters, each with cost estimates (row counts, selectivity); EXPLAIN shows the plan, EXPLAIN ANALYZE runs it and reports actual times and rows; plan shape changes with statistics and data volume.
- Concrete example: a slow wiki search query shows a sequential scan on a 10M-row table because the planner's row estimate for the filter is wrong; updating statistics or adding the right index flips it to an index scan; a join that nested-loops millions of rows becomes a hash join once the planner estimates correctly.
- Failure modes: estimate drift — stale statistics produce plans for data that no longer exists; plan shape inversion with scale (fast at 1k rows, disastrous at 1M); parameterized queries with different plans per value (bind peeking surprises); and over-indexing as a reflex instead of reading the plan first.
- Operational tradeoffs: reading plans is the prerequisite for index selection and query rewriting; the trade is planner accuracy (ANALYZE cost) vs correctness; the discipline is EXPLAIN ANALYZE on production-shaped data, checking estimates against actuals, and re-checking plans after schema or data changes.
- RSIS3/mykb relevance: the wiki DB explains slow index queries before adding an index, so schema changes are driven by measured plans, not guesses.
- Plan reviews: capture EXPLAIN ANALYZE output in CI for hot queries so plan regressions (index silently unused) fail review instead of production.
- Workload realism: analyze against production-like data volumes and distributions; dev-sized data produces plans that mislead.

## Related
- [[wiki/compositions/explain-analyze|EXPLAIN ANALYZE]]
- [[wiki/compositions/index-selection|Index Selection]]
- [[wiki/compositions/slow-query-triage|Slow Query Triage]]
- [[wiki/compositions/query-optimization|Query Optimization]]
- [[wiki/devops-infra/database-indexing|Database Indexing]]
