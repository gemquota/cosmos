---
type: "concept"
title: "ClickHouse"
description: "Columnar OLAP database for fast analytical queries over large event datasets"
tags: ["clickhouse", "olap", "columnar", "analytics", "database"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# ClickHouse

## Summary
ClickHouse is a columnar, open-source OLAP database optimized for analytical queries over billions of rows. It excels at aggregations and time-series analytics.

## Details
- Columnar storage compresses well and scans fast; materialized views pre-aggregate.
- Natural fit for pulse telemetry, session logs, and event analytics at scale.
- Contrast with DuckDB: ClickHouse is a server, DuckDB is embedded analytical.

## Related
- [[wiki/devops-infra/duckdb|DuckDB]] — embedded analytical alternative
- [[wiki/devops-infra/observability|Observability]] — telemetry storage
- [[wiki/devops-infra/postgresql|PostgreSQL]] — OLTP complement
- [[wiki/devops-infra/partitioning|Partitioning]] — time-based data layout
- [[wiki/concepts/mykb-analysis|Mykb Analysis]] — analytics over wiki activity
