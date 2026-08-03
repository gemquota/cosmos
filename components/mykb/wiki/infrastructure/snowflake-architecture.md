---
type: "concept"
title: "Snowflake Architecture"
description: "Three-layer warehouse: storage, compute, and cloud services"
tags: ["snowflake", "warehouse", "cloud", "saas"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Snowflake Architecture

## Summary
Snowflake's architecture separates storage, compute, and cloud services into three independent layers: compressed columnar files in object storage, elastic virtual warehouses that execute queries, and a metadata-and-services layer that coordinates everything. This disaggregation is what lets warehouses scale up, down, and even suspend entirely while data stays available.

## Details
- Storage layer: tables are split into immutable micro-partitions (typically 50–500 MB) stored in S3-style object storage in an encrypted, compressed columnar format. Micro-partitions make pruning, clustering, and time travel practical because metadata tracks value ranges per partition.
- Compute layer: virtual warehouses are independent MPP clusters of EC2-style instances, each with its own cache; they can scale horizontally and be suspended to zero compute. Multiple warehouses can query the same tables concurrently without lock contention because storage is shared and stateless.
- Services layer: a central cloud service manages metadata, transactions, optimization (automatic clustering and micro-partition maintenance), security, and query planning. Because planning is centralized, even small warehouses can run queries against huge tables.
- Time travel and fail-safe: Snowflake retains snapshots of changed data for configurable periods, allowing point-in-time queries and undo; cloning a table is a metadata-only operation that costs nothing until data diverges.
- Failure modes and tradeoffs: warehouse startup latency after suspension, credit costs that spike with aggressive auto-scaling, query queueing under concurrency, data egress costs when moving data out, and SaaS lock-in for teams that need on-prem or multi-cloud portability.
- Operational practice: right-size warehouses by workload (ETL vs BI vs ad-hoc), use auto-suspend aggressively, cache heavy workloads on a dedicated warehouse, and use external stages and tables to avoid paying for ingestion of data that stays in object storage.
- RSIS3/mykb relevance: the storage/compute/services separation is a reference architecture for RSIS3's own persistence-versus-execution split, and this node makes the analogy retrievable when reasoning about scaling the knowledge store.

## Related
- [[wiki/data-storage/data-warehouse|Data Warehouse]] — warehouse fundamentals
- [[wiki/infrastructure/warehouse-clusters-and-virtual-warehouses|Warehouse Clusters And Virtual Warehouses]] — the virtual warehouse model
- [[wiki/data-storage/data-warehouse-benchmarks|Data Warehouse Benchmarks]] — how Snowflake performs in benchmarks
- [[wiki/data-storage/warehouse-optimization|Warehouse Optimization]] — tuning Snowflake workloads
- [[wiki/data-storage/data-engineering-fundamentals|Data Engineering Fundamentals]] — core data engineering concepts
