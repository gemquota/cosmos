---
type: "concept"
title: "DuckDB"
description: "In-process analytical database engine, 'SQLite for analytics', optimized for OLAP queries"
tags: ["duckdb", "olap", "analytics", "embedded", "database"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# DuckDB

## Summary
DuckDB is an embedded, columnar analytical engine — often called "SQLite for analytics." It runs fast SQL over Parquet, CSV, and JSON without a server.

## Details
- Great for local data science and batch analysis of wiki stats or pulse data.
- Reads Parquet directly, supports window functions and rich aggregations.
- Pairs with Python notebooks and the mykb graph engine's analysis passes.

## Related
- [[wiki/devops-infra/clickhouse|ClickHouse]] — server-based OLAP alternative
- [[wiki/devops-infra/sqlite|SQLite]] — embedded OLTP counterpart
- [[wiki/devops-infra/query-planning|Query Planning]] — analytical optimizations
- [[wiki/concepts/mykb-analysis|Mykb Analysis]] — local analytics workflows
- [[wiki/devops-infra/observability|Observability]] — local analytics over exported telemetry
