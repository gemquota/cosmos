---
type: "concept"
title: "BigQuery Architecture"
description: "Serverless columnar warehouse with disaggregated storage and a petabit-scale query fabric"
tags: ["bigquery", "gcp", "serverless", "warehouse"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# BigQuery Architecture

## Summary

BigQuery is Google Cloud's serverless, columnar data warehouse, built on a disaggregated architecture: storage lives in Colossus (Google's distributed file system), compute runs on Dremel workers scheduled by Borg, and the two scale independently. Because storage and compute are separated, you pay for stored bytes and for query execution separately, and queries can burst to thousands of workers without provisioning anything.

## Details

- BigQuery separates storage (Colossus) from compute (Dremel/Borg) and charges per query or flat-rate slots. In on-demand mode you pay per byte scanned; in flat-rate mode you buy a pool of slots (units of query compute) and pay a fixed price, trading predictable cost for a concurrency ceiling. The slot model is the operational heart: a flat-rate pool with more concurrent queries than slots queues the excess, and a single expensive query can consume the whole pool — which is why slot monitoring is a first-class operational practice.
- Columnar Capacitor format and tree-shaped shuffle give high scan throughput on petabyte tables. Capacitor stores data column-by-column with compression and block-level metadata, so a query scanning one column of a huge table reads only that column's bytes. The Dremel query engine fans out to thousands of workers (the tree), each scanning its slice in parallel, then shuffles intermediate results up the tree — a massively parallel execution model that turns a petabyte scan into a parallel read rather than a bottleneck.
- Partitioning, clustering, and materialized views control cost; slots bound concurrency in flat-rate mode. Partitioning prunes whole partitions by a column's value (a date column means queries on one day read one partition's files). Clustering orders rows within partitions so that filters on the clustering column skip blocks — zone-map style pruning at the file level. Materialized views precompute aggregations and are incrementally maintained, trading storage for query speed. Together they are the cost-control triad: partition by the common filter, cluster by the second filter, materialize the hot aggregations.
- BI Engine and BigLake extend it toward interactive and lakehouse workloads. BI Engine is an in-memory acceleration layer that makes dashboards sub-second against BigQuery tables; BigLake lets the warehouse query data sitting in GCS (and other clouds) without copying, with row-level security and metadata managed centrally.
- For mykb: the node anchors the GCP warehouse branch and connects MPP, serverless cost models, and partition-pruning concepts to a concrete implementation.


## Related
- [[wiki/data-storage/data-warehouse|Data Warehouse]] — warehouse fundamentals
- [[wiki/data-storage/massively-parallel-processing|Massively Parallel Processing]] — MPP roots of Dremel
- [[wiki/infrastructure/serverless-data-platforms|Serverless Data Platforms]] — serverless cost model
- [[wiki/data-storage/partition-pruning-and-zone-maps|Partition Pruning And Zone Maps]] — cost control via pruning
- [[wiki/data-storage/data-engineering-fundamentals|Data Engineering Fundamentals]] — core data engineering concepts
