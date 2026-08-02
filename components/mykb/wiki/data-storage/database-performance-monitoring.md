---
type: "concept"
title: "Database Performance Monitoring"
description: "Metrics, slow-query logs, and bottleneck detection"
tags: ["database-monitoring", "performance", "slow-queries", "observability"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://www.postgresql.org/docs/current/monitoring-stats.html", "https://dev.mysql.com/doc/refman/8.4/en/performance-schema.html"]
---

# Database Performance Monitoring

## Summary
Database performance monitoring collects metrics, query statistics, and system telemetry to detect slowdowns, find their root cause, and verify fixes. The goal is to connect user-visible latency to the underlying cause: a slow query, a lock, a saturated buffer pool, or a resource ceiling.

## Details
- **Metrics layers** — three levels matter together: OS/host (CPU, memory, disk I/O, network), database internals (buffer cache hit ratio, connections, replication lag, locks), and query-level (latency percentiles, rows scanned, execution plans).
- **Slow-query logs** — Postgres `log_min_duration_statement` and MySQL's slow query log capture statements over a threshold; paired with `EXPLAIN ANALYZE` they turn a symptom into a diagnosis. `pg_stat_statements` aggregates statement fingerprints across the workload.
- **Internal statistics** — Postgres `pg_stat_*` views expose seq scans, index scans, dead tuples, and cache hit ratios; MySQL's Performance Schema and `sys` schema expose wait events, statement summaries, and lock contention.
- **Bottleneck signatures** — high CPU with few rows returned suggests expensive plans or missing indexes; high disk I/O with low hit ratio points at undersized buffers; idle-in-transaction and lock-wait metrics point at concurrency problems.
- **Baselines and alerting** — percentiles (p95/p99) beat averages for spotting tail latency; alert on changes from a baseline rather than fixed thresholds, since every workload differs.
- **Golden signals** — saturation, errors, and latency apply to databases too: connection pool saturation, replication lag, and deadlock rates are early warning indicators.

## Related
- [[wiki/data-storage/query-tuning|Query Tuning]] — acting on monitoring findings
- [[wiki/data-storage/buffer-pool-management|Buffer Pool Management]] — hit-ratio telemetry
- [[wiki/data-storage/index-maintenance|Index Maintenance]] — index health as a metric
- [[wiki/data-storage/vacuuming-and-compaction|Vacuuming & Compaction]] — bloat as a slow-growth problem
- [[wiki/data-storage/backpressure|Backpressure]] — consumer lag as pipeline pressure
- [[wiki/devops-infra/observability|Observability]] — dashboards and alerting patterns
