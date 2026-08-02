---
type: "concept"
title: "Massively Parallel Processing"
description: "Shared-nothing engines that parallelize queries across nodes"
tags: ["mpp", "shared-nothing", "parallel-query", "distributed-databases"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://docs.aws.amazon.com/redshift/latest/dg/c_intro_high_level.html", "https://clickhouse.com/docs/en/architecture/introduction"]
---

# Massively Parallel Processing

## Summary
Massively parallel processing (MPP) databases split data and computation across many nodes that each work on their slice, then exchange partial results. The shared-nothing design trades setup complexity for near-linear scale-out on analytical workloads.

## Details
- **Shared-nothing model** — each node owns its CPU, memory, and disk; nodes communicate only via network messages, which removes shared-disk contention but makes data placement critical.
- **Data distribution** — tables are hash- or range-distributed across nodes so that joins and aggregations can run locally; a poorly chosen distribution key forces expensive reshuffles.
- **Exchange operators** — the query plan inserts exchange nodes (gather, redistribute, broadcast) that repartition intermediate results; these are the dominant cost in distributed execution.
- **Scale-out vs scale-up** — adding nodes grows aggregate throughput, but only up to the skew and shuffle limits; a hot key or skewed join makes one node the bottleneck.
- **Representative systems** — Amazon Redshift, Snowflake, Google BigQuery, Greenplum, and ClickHouse all follow MPP designs, with Snowflake and BigQuery decoupling storage from compute.
- **mykb relevance** — corpus-wide vector similarity and TF-IDF scoring are embarrassingly parallel, making MPP the natural scale path if the wiki ever outgrows a single DuckDB file.

## Related
- [[wiki/data-storage/sharding-strategies|Sharding Strategies]] — how data gets split across nodes
- [[wiki/data-storage/consistent-hashing|Consistent Hashing]] — key distribution that survives node changes
- [[wiki/data-storage/vectorized-query-execution|Vectorized Query Execution]] — per-node execution speed
- [[wiki/data-storage/olap-vs-oltp|OLAP vs OLTP]] — the workloads MPP targets
- [[wiki/data-storage/data-warehouse|Data Warehouse]] — where MPP engines usually live
- [[wiki/cloud-infra/autoscaling|Autoscaling]] — scaling MPP worker pools with demand
