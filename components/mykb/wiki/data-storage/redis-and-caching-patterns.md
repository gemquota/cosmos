---
type: "concept"
title: "Redis and Caching Patterns"
description: "In-memory data structures for speed"
tags: ["redis", "caching", "in-memory", "performance"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://redis.io/docs/latest/", "https://en.wikipedia.org/wiki/Redis"]
---

# Redis and Caching Patterns

## Summary

Redis is an in-memory data structure store used for caching and real-time state.
Its data structures (strings, hashes, lists, sets, streams) serve many patterns.
Caching is the most common but not the only use.
Redis earns its place when latency matters and state is small enough to fit in memory.

## Details

- Cache patterns: cache-aside, read-through, write-through.
- TTLs bound staleness; eviction policies manage capacity.
- Redis Streams provide lightweight event logs.
- Persistence options (RDB, AOF) trade durability for speed.
- Cluster and Sentinel provide scale and availability.
- Design for eviction: cache misses should be cheap.
- Use Redis Streams for lightweight event needs without Kafka.
- Redis is a toolbox, not just a cache; its structures map to many real-time problems.

## Related

- [[wiki/data-storage/cache-aside-and-write-through|Cache-Aside and Write-Through]] — patterns
- [[wiki/data-storage/memcached-vs-redis|Memcached vs Redis]] — comparison
- [[wiki/infrastructure/redis-cluster-and-sentinel|Redis Cluster And Sentinel]] — HA
- [[wiki/data-storage/caching-strategies|Caching Strategies]] — existing note
- [[wiki/data-storage/cache-eviction-policies|Cache Eviction Policies]] — eviction
- [[wiki/data-storage/data-quality-dimensions|Data Quality Dimensions]] — quality dimensions
- [[wiki/data-storage/data-observability-and-monitoring|Data Observability and Monitoring]] — observability
- [[wiki/data-storage/data-testing-frameworks|Data Testing Frameworks]] — testing
- [[wiki/data-storage/feature-stores-and-ml-features|Feature Stores and ML Features]] — ML features
- [[wiki/data-storage/data-contracts-and-agreements|Data Contracts and Agreements]] — data contracts
- [[wiki/data-storage/incremental-loading-strategies|Incremental Loading Strategies]] — incremental loading
- [[wiki/data-storage/schema-evolution-in-streams|Schema Evolution In Streams]] — schema evolution

