---
type: "entity"
title: "ClickHouse"
description: "Columnar OLAP database for fast analytical queries over large event datasets"
tags: ["clickhouse", "olap", "columnar", "analytics", "database"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
---

# ClickHouse

## Summary
ClickHouse is a columnar, open-source OLAP database optimized for analytical queries over billions of rows. It excels at aggregations and time-series analytics.

## Details
- Columnar storage compresses well and scans fast; materialized views pre-aggregate.
- Natural fit for pulse telemetry, session logs, and event analytics at scale.
- Contrast with DuckDB: ClickHouse is a server, DuckDB is embedded analytical.

## Architecture

ClickHouse is built around merge-tree tables that store data in sorted, compressed parts. Inserts accumulate in memory and are periodically flushed to disk as new parts, while background merges combine parts to keep scans efficient. Because each column is stored separately, queries read only the columns they touch, which is what makes aggregation over billions of rows practical on modest hardware.

Replicated tables use ZooKeeper or ClickHouse Keeper to coordinate data distribution across shards, giving horizontal scale-out for event workloads. The engine trades per-row update flexibility for extremely high insert throughput and fast analytic scans, so it pairs naturally with a transactional OLTP store such as [[wiki/devops-infra/postgresql|PostgreSQL]].

## Query Patterns

The SQL dialect is analytic-first: GROUP BY, aggregation functions, window functions, and array operations are all optimized, while point lookups by primary key are supported but not the engine's strength. Materialized views attach to insert streams and maintain pre-aggregated targets automatically, so dashboards read tiny rolled-up tables instead of scanning raw events. Time-based partitioning and TTL policies keep old data pruned without manual jobs.

## Operational Notes

For pulse telemetry and session logs, the common pattern is to write raw events with a timestamp, keep a short retention in hot storage, and maintain materialized views for per-day, per-user, or per-tool summaries. Contrast with [[wiki/devops-infra/duckdb|DuckDB]], which is an embedded analytical engine ideal for single-node analysis of files, whereas ClickHouse is a server that many clients query concurrently. Capacity planning centers on insert rate, part count, and query memory, and observability of the cluster itself is typically stored alongside the data it serves.

## Related
- [[wiki/devops-infra/duckdb|DuckDB]] — embedded analytical alternative
- [[wiki/devops-infra/observability|Observability]] — telemetry storage
- [[wiki/devops-infra/postgresql|PostgreSQL]] — OLTP complement
- [[wiki/devops-infra/partitioning|Partitioning]] — time-based data layout
- [[wiki/concepts/mykb-analysis|Mykb Analysis]] — analytics over wiki activity
