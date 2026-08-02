---
type: "concept"
title: "Sharding and Partitioning Revisited"
description: "Splitting data across nodes and files for scale"
tags: ["sharding", "partitioning", "scaling", "databases"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/Shard_(database_architecture)", "https://www.mongodb.com/docs/manual/sharding/"]
---

# Sharding and Partitioning Revisited

## Summary

Sharding distributes rows across nodes by a shard key; partitioning splits tables within a node.
Both exist to keep data access localized and workloads parallel.
Shard key choice determines scalability and query efficiency.
The shard key is the schema decision with the longest half-life; changing it later is a migration project.

## Details

- Hash sharding balances load; range sharding supports range scans.
- Shard key alignment with query patterns avoids cross-shard scatter.
- Resharding and hot shards are the main operational headaches.
- Partitioning (by date, by tenant) enables pruning and independent maintenance.
- Distributed SQL systems automate much of this but constrain keys.
- Monitor hot shards and rebalance before they degrade queries.
- Partitioning also enables lifecycle management per partition.
- Partitioning and sharding are how databases grow past a single node or a single scan.

## Related

- [[wiki/data-storage/sharding-and-partitioning-revisited|Sharding and Partitioning Revisited]] — overview
- [[wiki/data-storage/consistent-hashing-and-ring-topology|Consistent Hashing And Ring Topology]] — distribution
- [[wiki/data-storage/partition-pruning-and-zone-maps|Partition Pruning And Zone Maps]] — pruning
- [[wiki/data-storage/sharding-strategies|Sharding Strategies]] — strategies
- [[wiki/data-storage/table-partitioning|Table Partitioning]] — partitioning

