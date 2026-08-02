---
type: "concept"
title: "Table Partitioning"
description: "Dividing tables into partitions for pruning and management"
tags: ["partitioning", "postgresql", "mysql", "database-design"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://www.postgresql.org/docs/current/ddl-partitioning.html", "https://dev.mysql.com/doc/refman/8.4/en/partitioning.html"]
---

# Table Partitioning

## Summary
Table partitioning splits one logical table into multiple physical segments — partitions — based on a partition key. Queries transparently read only the partitions the predicates require (pruning), and maintenance operations like archival and dropping old data become cheap metadata actions instead of large deletes.

## Details
- **Partition methods** — range partitioning assigns rows to contiguous key ranges (dates, IDs); list partitioning matches discrete values (region, tenant); hash partitioning distributes rows by hash for load spreading; composite/subpartitioning layers methods.
- **Mechanics** — Postgres declarative partitioning creates a parent table plus child partitions; MySQL supports `PARTITION BY RANGE/LIST/HASH/KEY`; both route rows automatically and enforce partition-key constraints so the planner can prune.
- **Why partition** — three drivers: query performance via pruning (skip months of history), manageability (drop or archive an entire month as one operation, `pg_attach_partition`/`pg_detach_partition` for swaps), and vacuum/analyze granularity so maintenance touches only relevant segments.
- **Costs** — many small partitions add planner overhead and connection/catalog churn; partition keys must match query filters or partitioning buys little; unique constraints must include the partition key, and foreign keys need care.
- **Partition vs shard** — partitioning divides within one database server; sharding divides across servers. They combine: shard a table, then partition each shard by time for tiered analytics.
- **Operational patterns** — time-based rolling windows (create future partitions ahead, drop old ones on schedule), partition-aware vacuum in Postgres, and MySQL's automatic partition maintenance; automated tooling (pg_partman) manages the lifecycle.

## Related
- [[wiki/data-storage/partition-pruning|Partition Pruning]] — the query benefit of partitioning
- [[wiki/data-storage/sharding-strategies|Sharding Strategies]] — the distributed cousin
- [[wiki/data-storage/data-lifecycle-management|Data Lifecycle Management]] — partition-based archival
- [[wiki/data-storage/time-series-databases|Time-Series Databases]] — the canonical partitioned workload
- [[wiki/data-storage/storage-tiering|Storage Tiering]] — per-partition media placement
