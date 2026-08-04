---
type: "entity"
title: "Redshift Architecture"
description: "AWS's petabyte-scale MPP warehouse with leader and compute nodes"
tags: ["redshift", "aws", "mpp", "warehouse"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Redshift Architecture

## Summary

Redshift is AWS's petabyte-scale data warehouse built on a massively parallel processing (MPP) architecture: a cluster of compute nodes, each with its own CPU, memory, and local storage, coordinated by a leader node that plans and distributes queries. It delivers warehouse performance on large datasets by partitioning both the data (across slices) and the query work (across nodes), with the performance tuning living in the data layout — distribution, sort keys, and compression.

## Details

- Redshift clusters split tables across slices on compute nodes; the leader node plans and coordinates queries. Each compute node is divided into slices (one per CPU core), and each table's rows are distributed across all slices according to a distribution style. The leader node receives the query, builds the execution plan, sends per-slice fragments to the nodes, and merges the results. The MPP payoff: a scan of a 10TB table is split into hundreds of parallel scans, each reading its slice; the price is the coordination cost — a query that needs to shuffle data between nodes (joins on mismatched distribution keys, aggregations) pays network transfer, which is why distribution design decides performance.
- Columnar compression, zone maps, and sort/dist keys drive performance; spectrum extends queries to S3. Redshift stores data columnarly with per-column compression encoding (AZ64, ZSTD, etc.), so a query touching one column reads only that column's data. Zone maps are block-level min/max metadata — the skip layer: a query filtering on a column skips any block whose zone map cannot contain the filter's values. Sort keys order rows so zone maps are effective (a sorted column's zone maps prune; an unsorted one's maps are useless), and distribution keys decide where rows land (even = round-robin, key = hash by the join column, all = full copies on every node). The combination is the tuning triad: sort key for the common filter, distribution key for the common join, encoding per column.
- RA3 nodes offload managed storage, decoupling compute and storage for elastic resize. Classic Redshift nodes stored data on local disks — compute and storage were locked together, so scaling compute meant re-copying data. RA3 nodes separate the layers: data lives in managed S3-backed storage, and the node keeps a local SSD cache; compute can scale up/down (elastic resize) without moving data, and the cluster pays for storage and compute independently. The tradeoff: remote storage adds latency for uncached reads, so RA3 workloads depend on cache hit rates.
- Classic choices: distribution style (even/key/all), sort keys, and encoding per column. These are made at table creation and are expensive to change later (redistribution rewrites the table), which is why the tuning happens in the schema-design phase, not after deployment — the classic failure is the table created with default distribution that meets its first query pattern and then performs badly as the workload evolves.
- For mykb: the node anchors the AWS warehouse branch — MPP mechanics, zone maps, and warehouse optimization connect to this concrete implementation.


## Related
- [[wiki/data-storage/massively-parallel-processing|Massively Parallel Processing]] — MPP architecture basics
- [[wiki/data-storage/data-warehouse|Data Warehouse]] — warehouse fundamentals
- [[wiki/data-storage/partition-pruning-and-zone-maps|Partition Pruning And Zone Maps]] — zone maps as Redshift's skip layer
- [[wiki/data-storage/warehouse-optimization|Warehouse Optimization]] — tuning sort and dist keys
- [[wiki/data-storage/data-engineering-fundamentals|Data Engineering Fundamentals]] — core data engineering concepts
