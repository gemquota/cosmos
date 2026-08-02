---
type: "concept"
title: "Distributed Cache"
description: "A cache shared across many app instances, usually with key sharding"
tags: ["distributed-cache", "redis", "caching", "architecture"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Distributed Cache

## Summary
A distributed cache (Redis, Memcached, Hazelcast) sits outside app instances and serves any instance, so a cache hit works regardless of which node handled the request. Sharding spreads keys; replication adds availability.

## Details
- Central caches add a network hop — local caches are faster, distributed caches are shared.
- Key design and TTL policy dominate behavior; eviction policies (LRU, LFU) matter under pressure.
- Availability of the cache is now a dependency: handle cache-down gracefully.
- mykb relevance: the wiki link-index cache is a sharded Redis cluster.

## Related
- [[wiki/tooling/local-cache|Local Cache]]
- [[wiki/tooling/hot-key-cache|Hot Key Cache]]
- [[wiki/tooling/cache-aside|Cache-Aside]]
- [[wiki/tooling/ttl-caches|Redis]]
- [[wiki/software-engineering/performance-engineering|Performance Engineering]]
