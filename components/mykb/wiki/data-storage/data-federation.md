---
type: "concept"
title: "Data Federation"
description: "Querying multiple sources without copying data"
tags: ["data-federation", "virtualization", "federated-queries", "analytics"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://dev.mysql.com/doc/refman/8.4/en/federated-storage-engine.html", "https://trino.io/docs/current/overview.html"]
---

# Data Federation

## Summary
Data federation answers queries across multiple data sources in place — one SQL statement joining a Postgres table, an S3 lake, and a warehouse — without copying the data. Engines like Trino, Presto, and DuckDB push down what they can and stitch the rest, trading freshness and simplicity for latency.

## Details
- **How it works** — a federated engine exposes each source through a connector; query planning splits the statement into pushdown fragments (filters, projections, aggregations) executed remotely and a residual plan executed locally.
- **Why it helps** — no replication lag, no storage duplication, and one query surface over operational and analytical systems; it is the cheapest way to answer cross-system questions.
- **Costs** — network round trips and limited pushdown make federated queries slower than local ones; cross-source joins force pulling data into the engine, and source load is unbounded unless pushdown is aggressive.
- **Common engines** — Trino/Presto connectors (JDBC, Iceberg, Hive, Elasticsearch), MySQL FEDERATED tables, and DuckDB's httpfs/postgres extensions; lakehouse catalogs double as federated layers.
- **Operational notes** — connector configs, credentials, and statistics matter; missing source statistics produce terrible plans, so most engines support per-connector stats or hints.
- **When to use** — occasional cross-source analysis, metadata lookups, and migration-free integration; high-frequency joins are better served by copying or caching the hot data.

## Related
- [[wiki/data-storage/etl-vs-elt|ETL vs ELT]] — copying data as the alternative
- [[wiki/data-storage/query-tuning|Query Tuning]] — pushdown-aware planning
- [[wiki/data-storage/data-lake|Data Lake]] — a common federated target
- [[wiki/data-storage/object-storage|Object Storage]] — lake files behind connectors
- [[wiki/data-storage/data-warehouse|Data Warehouse]] — the integrated alternative
