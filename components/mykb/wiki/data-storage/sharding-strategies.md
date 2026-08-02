---
type: "concept"
title: "Sharding Strategies"
description: "Horizontal splits by key, hash, or range across nodes"
tags: ["sharding", "scaling", "distributed-databases", "partitioning"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://www.mongodb.com/docs/manual/sharding/", "https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/bp-partition-key-design.html"]
---

# Sharding Strategies

## Summary
Sharding splits a dataset horizontally across multiple nodes, with each shard owning a disjoint subset of rows or keys, so capacity and throughput grow with node count. The strategy — how keys map to shards — determines balance, locality, and how well queries scale.

## Details
- **Hash sharding** — a hash of the shard key determines the shard (MongoDB hashed shard keys, consistent hashing rings); writes distribute evenly and hot keys spread out, but range scans lose locality and must fan out to every shard.
- **Range sharding** — rows are assigned by key ranges, so queries over contiguous ranges hit one shard; the risk is hotspots: a monotonically increasing key (timestamps, auto-increment IDs) concentrates writes on the newest range.
- **Directory-based sharding** — a lookup table maps keys to shards (e.g., tenant to shard); flexible and tunable, but the mapping service is a dependency and a potential bottleneck.
- **Choosing a shard key** — the key must distribute writes evenly, match the common query pattern, and be immutable: DynamoDB's partition-key design guidance (high-cardinality keys, no hot partitions), MongoDB's shard-key rules, and Postgres/Citus distribution columns all encode the same lesson.
- **Fan-out and cross-shard work** — scatter-gather queries touch many shards; joins and transactions across shards are expensive, so data that must be colocated (tenant data, related entities) should share a shard or use composite keys.
- **Operations** — rebalancing, resharding, and hotspot mitigation are ongoing: MongoDB balancer and chunk splits, DynamoDB's automatic splitting, and virtual nodes in Cassandra ease the pain; monitoring per-shard load is mandatory.

## Related
- [[wiki/data-storage/consistent-hashing|Consistent Hashing]] — the hash-ring distribution scheme
- [[wiki/data-storage/table-partitioning|Table Partitioning]] — the single-node cousin
- [[wiki/data-storage/partition-pruning|Partition Pruning]] — skipping irrelevant shards/partitions
- [[wiki/data-storage/key-value-stores|Key-Value Stores]] — the scaling patterns originate here
- [[wiki/data-storage/replication-strategies|Replication Strategies]] — replicas per shard
- [[wiki/data-storage/wide-column-stores|Wide-Column Stores]] — shard-first NoSQL systems
