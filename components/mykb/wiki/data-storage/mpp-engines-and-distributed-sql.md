---
type: "concept"
title: "MPP Engines and Distributed SQL"
description: "Massively parallel processing for warehouse-scale analytics"
tags: ["mpp", "distributed-sql", "warehouse", "olap"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/Massively_parallel_processing", "https://clickhouse.com/docs/"]
---

# MPP Engines and Distributed SQL

## Summary

MPP engines split queries across many nodes that work in parallel.
Distributed SQL adds OLTP semantics to scale-out architecture.
They power cloud warehouses and large-scale analytics.
MPP and distributed SQL share the same idea: split the work, merge the results.

## Details

- MPP: shared-nothing nodes, columnar storage, parallel scans.
- Distributed SQL: sharded storage with ACID transactions (Spanner, CockroachDB).
- Query coordinator merges per-node results.
- Elastic scaling separates storage from compute.
- Choices: Redshift, Snowflake, BigQuery, ClickHouse, TiDB.
- Elastic compute changes capacity planning from sizing to budgets.
- Distributed SQL adds transactional semantics at scale.
- Scale-out compute is the reason cloud warehouses can query petabytes interactively.

## Related

- [[wiki/data-storage/distributed-query-engines|Distributed Query Engines]] — query engines
- [[wiki/data-storage/presto-and-trino|Presto And Trino]] — federated SQL
- [[wiki/data-storage/clickhouse-and-columnar-oltp|ClickHouse and Columnar OLTP]] — columnar MPP
- [[wiki/data-storage/massively-parallel-processing|Massively Parallel Processing]] — existing note
- [[wiki/infrastructure/cockroachdb-and-yugabytedb|Cockroachdb And Yugabytedb]] — distributed SQL
- [[wiki/data-storage/data-quality-dimensions|Data Quality Dimensions]] — quality dimensions
- [[wiki/data-storage/data-observability-and-monitoring|Data Observability and Monitoring]] — observability
- [[wiki/data-storage/data-testing-frameworks|Data Testing Frameworks]] — testing
- [[wiki/data-storage/feature-stores-and-ml-features|Feature Stores and ML Features]] — ML features
- [[wiki/data-storage/data-contracts-and-agreements|Data Contracts and Agreements]] — data contracts
- [[wiki/data-storage/incremental-loading-strategies|Incremental Loading Strategies]] — incremental loading
- [[wiki/data-storage/schema-evolution-in-streams|Schema Evolution In Streams]] — schema evolution
- [[wiki/data-storage/data-warehouse|Data Warehouse]] — warehouse reference

