---
type: "concept"
title: "StarRocks and Doris"
description: "Open-source MPP engines for real-time and high-concurrency analytics"
tags: ["starrocks", "doris", "mpp", "olap"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# StarRocks and Doris

## Summary
Doris is an Apache-licensed MPP database for real-time analytics; StarRocks forked from it with added optimizations. Both use columnar storage, materialized views, and MySQL-protocol compatibility, targeting sub-second queries over large tables with high concurrency and low admin overhead.

## Details
- Mechanism: MPP query engines distribute scans and aggregations across nodes; columnar storage compresses and accelerates column reads; built-in materialized views pre-aggregate hot queries; MySQL protocol compatibility means existing SQL tooling connects without drivers; both support real-time ingestion via stream load.
- Concrete example: a dashboard querying billions of event rows returns aggregates in under a second; a materialized view pre-computes daily totals by tag so the hot query hits pre-aggregated data; stream load ingests events continuously; the cluster serves hundreds of concurrent dashboard queries.
- Failure modes: schema rigidity — MPP engines want declared schemas and penalize frequent changes; query patterns that defeat the optimizer (unbounded scans, poor join order); materialized view drift or refresh lag; node imbalance degrading the whole cluster; underestimating ingestion and compaction load.
- Tradeoffs: both engines trade the flexibility of general-purpose databases for analytics speed — they are specialized OLAP systems; the alternative, ClickHouse, is stronger for deep ad-hoc SQL, while Druid/Pinot specialize in serving; StarRocks/Doris sit between, strong on high-concurrency serving with MySQL familiarity.
- Operational notes: benchmark the real query mix, design materialized views for hot queries, and monitor compaction and node balance.
- RSIS3 relevance: wiki telemetry at scale (pulses, sync history) could land in StarRocks/Doris — the serving engine for fast, concurrent dashboard queries.

- Validate MySQL-protocol expectations early, since some tooling and driver behaviors differ from a real MySQL server.
## Related

- [[wiki/data-storage/massively-parallel-processing|Massively Parallel Processing]] — MPP query model
- [[wiki/data-storage/columnar-storage|Columnar Storage]] — columnar storage basis
- [[wiki/data-storage/real-time-dashboards-and-alerts|Real Time Dashboards And Alerts]] — serving workloads
- [[wiki/data-storage/materialized-views-and-incremental-refresh|Materialized Views And Incremental Refresh]] — built-in MV acceleration
- [[wiki/data-storage/data-engineering-fundamentals|Data Engineering Fundamentals]] — core data engineering concepts
