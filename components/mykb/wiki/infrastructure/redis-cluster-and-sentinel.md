---
type: "concept"
title: "Redis Cluster and Sentinel"
description: "Scaling and high availability for Redis via sharding and monitoring"
tags: ["redis", "cluster", "sentinel", "high-availability"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Redis Cluster and Sentinel

## Summary

Redis Cluster and Sentinel are the two ways to make Redis survive beyond a single node: Sentinel provides high availability (monitoring and automatic failover) for a primary-replica deployment, while Redis Cluster provides both high availability and horizontal scaling by sharding keys across nodes. The choice is an architecture decision: Sentinel keeps Redis's simple model and adds a failover brain; Cluster changes the data model (sharding) to gain capacity.

## Details

- Redis Cluster shards keys across 16384 hash slots with replica nodes for failover. Every key hashes to one of 16384 slots; each cluster node owns a contiguous range of slots; clients (with cluster support) compute the slot for a key and talk directly to the owning node, which may redirect (MOVED) if the client is stale. Each slot has a primary and can have replicas; if a primary fails, its replica is promoted (with a quorum of masters agreeing). The scaling is horizontal — add nodes, rebalance slots — and the availability is automatic, with the tradeoff being that Cluster changes Redis's semantics: multi-key commands work only if all keys hash to the same slot, and the client library must be cluster-aware.
- Sentinel monitors masters/replicas and promotes replicas on failure for non-cluster deployments. Sentinel is a separate process (usually three of them, for quorum) that watches the Redis instances, agrees on master failures (quorum-based), promotes a replica, and reconfigures the clients (via pub/sub notifications) to follow the new master. The model stays classic Redis — one master, replicas, all keys everywhere — so the client sees a single endpoint and the failover is transparent, with the caveat that failover takes seconds (during which writes fail or queue) and the promotion can lose the last writes (async replication).
- Cluster mode changes client behavior: cross-slot commands fail and keys must stay in one slot. This is the design consequence that surprises most teams: you cannot run a multi-key operation across slots, so data that is accessed together must be co-located by key design (hash tags — `{user:42}:cart` forces all tagged keys into one slot). The migration is the other shock: moving from single-node Redis to Cluster is a data-modeling project, not a config change.
- Use sentinel for small HA setups, cluster for multi-node scale; both change ops complexity. Sentinel is right when the dataset fits one node and the requirement is availability; Cluster is right when capacity or write throughput exceeds one node. Both add operational surface: Sentinel adds the sentinel processes themselves (a second system to operate), Cluster adds slot management, rebalancing, and the client-version coordination.
- For mykb: the node anchors the Redis branch of the data-storage cluster — caching strategies, replication, and consistent hashing all connect here.

## Related

- [[wiki/data-storage/caching-strategies|Caching Strategies]] — Redis's main job
- [[wiki/data-storage/consistent-hashing|Consistent Hashing]] — slot-based hashing
- [[wiki/data-storage/replication-strategies|Replication Strategies]] — replication behind failover
- [[wiki/data-storage/redis-and-caching-patterns|Redis And Caching Patterns]] — cache patterns on Redis
- [[wiki/data-storage/valkey-and-keydb|Valkey And Keydb]] — drop-in Redis forks
