---
type: "concept"
title: "Materialized Views"
description: "Precomputed query results with refresh strategies"
tags: ["materialized-views", "query-performance", "olap", "refresh"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://www.postgresql.org/docs/current/sql-creatematerializedview.html", "https://docs.snowflake.com/en/user-guide/views-materialized"]
---

# Materialized Views

## Summary
A materialized view stores the results of a query as a physical table, so reads avoid recomputing expensive aggregations and joins. The cost is freshness: the stored result must be refreshed periodically or incrementally, trading data staleness for dramatically faster queries.

## Details
- **Views vs materialized views** — a regular view is a saved query expanded at read time; a materialized view persists its output, trading storage and maintenance for query speed. Postgres materialized views and Snowflake, BigQuery, and Redshift materialized views follow the same idea with different refresh mechanics.
- **Refresh strategies** — full refresh recomputes the entire view (simple but expensive); incremental or auto refresh applies only changed rows, keeping the view near-current; Snowflake's auto-refresh, BigQuery's automatic refresh, and Postgres `REFRESH MATERIALIZED VIEW CONCURRENTLY` illustrate the spectrum.
- **Why they help** — aggregations over millions of rows (daily totals, rollups, denormalized joins) collapse to a small table; dashboards and reporting queries hit the view instead of the base tables, cutting latency by orders of magnitude.
- **Costs** — storage duplication, refresh windows of staleness, and refresh-time load spikes; incremental refresh reduces cost but requires the engine to track deltas, which some systems support only for restricted query shapes.
- **Alternatives** — query rewriting to precomputed tables, summary tables updated by ETL, indexed views (SQL Server), and OLAP cubes cover similar ground; which fits depends on refresh latency needs and query flexibility.
- **Best practice** — keep the defining query simple and stable, schedule refresh to avoid peak load, and monitor refresh failures since a stale view silently serves outdated answers.

## Related
- [[wiki/data-storage/query-tuning|Query Tuning]] — the performance lever views replace
- [[wiki/data-storage/data-warehouse|Data Warehouse]] — where precomputation is endemic
- [[wiki/data-storage/incremental-loading|Incremental Loading]] — delta-based refresh
- [[wiki/data-storage/olap-vs-oltp|OLAP vs OLTP]] — read-heavy workloads that benefit
- [[wiki/data-storage/denormalization|Denormalization]] — a related redundancy trade
