---
type: "concept"
title: "Partitioning"
description: "Dividing tables into smaller physical segments by key or range for manageability and performance"
tags: ["partitioning", "database", "performance", "postgresql", "data"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Partitioning

## Summary
Partitioning splits one logical table into physical partitions (e.g. by month), so queries scan only relevant segments and old data drops cheaply. It is a single-node technique, unlike sharding.

## Details
- Range, list, and hash partition strategies; partition pruning cuts scan cost.
- Common for time-series data: pulse telemetry by month, logs by day.
- Partition maintenance (attach/detach) must be scripted; constraints enforce routing.

## Related
- [[wiki/devops-infra/sharding|Sharding]] — cross-node scaling counterpart
- [[wiki/devops-infra/database-indexing|Database Indexing]] — indexes per partition
- [[wiki/devops-infra/clickhouse|ClickHouse]] — time-partitioned analytics
- [[wiki/devops-infra/backups|Backups]] — partition-level archival
- [[wiki/devops-infra/query-planning|Query Planning]] — pruning effects
- [[wiki/devops-infra/observability|Observability]] — partition growth and maintenance signals
