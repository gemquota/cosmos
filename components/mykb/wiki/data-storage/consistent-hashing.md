---
type: "concept"
title: "Consistent Hashing"
description: "Minimal-reshuffle key distribution for sharded systems"
tags: ["consistent-hashing", "sharding", "distributed-systems", "hash-ring"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://cassandra.apache.org/doc/latest/cassandra/architecture/dynamo.html", "https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.Partitions.html"]
---

# Consistent Hashing

## Summary
Consistent hashing distributes keys across a ring of nodes so that adding or removing a node moves only a small fraction of keys, instead of rehashing everything. It is the load-balancing backbone of Dynamo-style and Cassandra-style distributed stores and many caching tiers.

## Details
- **The ring** — both keys and nodes hash to positions on a circular hash space; each key is owned by the first node clockwise from its position. A node owns the arc between itself and its predecessor.
- **Minimal reshuffling** — when a node joins or leaves, only keys in that node's arc move to the successor, so roughly `1/N` of keys shift instead of all of them. This makes elastic scale-out cheap.
- **Virtual nodes** — each physical node occupies multiple positions (vnodes) on the ring, which smooths load imbalance when few keys are present and lets heterogeneous machines own more vnodes. Cassandra's `num_tokens` configures this.
- **Replication placement** — the ring also determines replicas: the next N clockwise nodes hold copies, enabling hinted handoff and read repair. Cassandra and Riak place each key's replicas this way.
- **Comparisons** — range-based sharding preserves scan locality but skews under hot keys; classic modulo hashing balances well but reshuffles nearly everything on node count changes; consistent hashing balances the two.
- **Practical tuning** — hot keys still concentrate on single vnodes; strategies include splitting hot keys with suffixes or using Redis Cluster's 16384-slot design, which is a fixed-slot variant of the same idea.

## Related
- [[wiki/data-storage/sharding-strategies|Sharding Strategies]] — where consistent hashing fits
- [[wiki/data-storage/leaderless-replication|Leaderless Replication]] — ring-based replica placement
- [[wiki/data-storage/partition-pruning|Partition Pruning]] — deterministic routing by key
- [[wiki/data-storage/cache-eviction-policies|Cache Eviction Policies]] — distributed cache membership
- [[wiki/data-storage/table-partitioning|Table Partitioning]] — single-node partitioning contrasts
