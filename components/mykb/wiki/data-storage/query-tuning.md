---
type: "concept"
title: "Query Tuning"
description: "Index selection, hinting, and rewriting slow queries"
tags: ["query-tuning", "performance", "explain", "indexing"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://www.postgresql.org/docs/current/performance-tips.html", "https://dev.mysql.com/doc/refman/8.4/en/optimization.html"]
---

# Query Tuning

## Summary
Query tuning improves slow queries by changing what the database executes — better indexes, rewritten SQL, updated statistics, or configuration — after understanding why the current plan is slow. The process is driven by execution plans, not intuition: measure, explain, change, re-measure.

## Details
- **Start with the plan** — `EXPLAIN (ANALYZE, BUFFERS)` in Postgres and `EXPLAIN ANALYZE` in MySQL show scan types, join order, row estimates, and actual timings; the largest discrepancies between estimated and actual rows point at the root cause.
- **Index selection** — missing indexes show up as sequential scans and high filter ratios; composite and covering indexes serve multi-column and projection-heavy queries, while partial indexes shrink index size; indexes that are never used should be dropped.
- **Statistics and estimates** — planners rely on `ANALYZE`-collected histograms; stale statistics cause bad join orders, and small sample sizes or skewed distributions need extended statistics or adjusted `default_statistics_target`.
- **Rewriting queries** — remove functions on indexed columns, avoid `SELECT *` in hot paths, replace OR with `UNION ALL` where appropriate, rewrite correlated subqueries as joins, and push filters and aggregations as early as possible.
- **Hints and knobs** — Postgres rarely needs hints (enable/disable node types, `random_page_cost`, work_mem); MySQL supports index hints and optimizer switches; hints should document a proven issue, not a guess.
- **Environment factors** — buffer pool/cache size, effective cache size, `work_mem` for sorts and hash joins, and connection pool size all shape whether a good plan is fast; parameter tuning complements, never replaces, plan fixes.
- **Verify after change** — re-run with realistic data and concurrency; an index that helps one query may slow writes, so measure end to end.

## Related
- [[wiki/data-storage/database-performance-monitoring|Database Performance Monitoring]] — finding the slow queries
- [[wiki/data-storage/index-maintenance|Index Maintenance]] — keeping indexes healthy
- [[wiki/data-storage/composite-indexes|Composite Indexes]] — multi-column index design
- [[wiki/data-storage/covering-indexes|Covering Indexes]] — index-only scans
- [[wiki/data-storage/cost-based-query-optimization|Cost-Based Query Optimization]] — how plans are chosen
- [[wiki/data-storage/partition-pruning|Partition Pruning]] — skipping data at plan time
