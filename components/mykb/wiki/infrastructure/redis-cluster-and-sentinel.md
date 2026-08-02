---
type: "concept"
title: "Redis Cluster and Sentinel"
description: "Scaling and high availability for Redis via sharding and monitoring"
tags: ["redis", "cluster", "sentinel", "high-availability"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Redis Cluster and Sentinel

## Summary

A stub to be expanded into a full article; frames the concept and open questions.

## Details

- Redis Cluster shards keys across 16384 hash slots with replica nodes for failover.
- Sentinel monitors masters/replicas and promotes replicas on failure for non-cluster deployments.
- Cluster mode changes client behavior: cross-slot commands fail and keys must stay in one slot.
- Use sentinel for small HA setups, cluster for multi-node scale; both change ops complexity.

## Related

- [[wiki/data-storage/caching-strategies|Caching Strategies]] — Redis's main job
- [[wiki/data-storage/consistent-hashing|Consistent Hashing]] — slot-based hashing
- [[wiki/data-storage/replication-strategies|Replication Strategies]] — replication behind failover
- [[wiki/data-storage/redis-and-caching-patterns|Redis And Caching Patterns]] — cache patterns on Redis
- [[wiki/data-storage/valkey-and-keydb|Valkey And Keydb]] — drop-in Redis forks
