---
type: "concept"
title: "Cost-Based Query Optimization"
description: "How planners estimate cardinality and choose join orders and scan paths"
tags: ["query-optimization", "cardinality-estimation", "planner", "sql"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://www.postgresql.org/docs/current/planner-optimizer.html", "https://www.sqlite.org/optoverview.html"]
---

# Cost-Based Query Optimization

## Summary
Cost-based optimizers (CBOs) enumerate candidate execution plans, estimate each one's cost, and pick the cheapest. Estimates come from table statistics and cardinality models, and they degrade gracefully when statistics are stale or missing.

## Details
- **Cost model** — each plan node accrues CPU and I/O cost: sequential scans cost per-page, index scans add descent plus random reads, and joins cost by input cardinality; PostgreSQL's constants are visible in `EXPLAIN` output.
- **Cardinality estimation** — histograms, most-common-values lists, and null fractions estimate how many rows a predicate returns; multi-column correlation is the classic weakness, causing underestimates on correlated filters.
- **Join-order search** — dynamic programming over join subsets (PostgreSQL up to a `geqo_threshold` of 12 relations) versus greedy heuristics for larger FROM clauses; the chosen order can change query time by orders of magnitude.
- **Access path selection** — bitmap heap scans, index-only scans, and sequential scans are compared per relation before joins are ordered.
- **Statistics hygiene** — `ANALYZE`/`VACUUM ANALYZE` refresh stats; extended statistics on correlated columns and expression indexes fix specific estimate failures.
- **mykb relevance** — when a wiki query plan looks wrong, first check row estimates against `EXPLAIN ANALYZE` actuals, then refresh statistics before blaming the SQL.

## Related
- [[wiki/data-storage/sql-engines|SQL Engine Architecture]] — where the optimizer sits
- [[wiki/data-storage/join-algorithms|Join Algorithms]] — the operators being costed
- [[wiki/data-storage/b-tree-indexing|B-Tree Indexing]] — the index access paths the CBO chooses between
- [[wiki/data-storage/query-tuning|Query Tuning]] — acting on optimizer output
- [[wiki/devops-infra/query-planning|Query Planning]] — practical plan reading
- [[wiki/data-storage/index-maintenance|Index Maintenance]] — keeping statistics and indexes healthy
