---
type: "concept"
title: "Cache Eviction Policies"
description: "LRU, LFU, TTL, and capacity management"
tags: ["caching", "eviction", "lru", "redis"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://redis.io/docs/latest/operate/oss_and_stack/management/memory/", "https://docs.memcached.org/"]
---

# Cache Eviction Policies

## Summary
Eviction policies decide which entries to drop when a cache reaches capacity. Because caches are finite, the policy shapes hit rate: it should evict the entries least likely to be requested again while keeping popular data resident.

## Details
- **LRU (least recently used)** — evicts the entry whose last access is oldest; excellent for skewed access patterns and cheap to approximate with clock or segmented lists. Redis's `allkeys-lru` and Memcached's LRU are the common examples.
- **LFU (least frequently used)** — evicts entries with the lowest access frequency, protecting items that are hot but accessed in bursts; Redis `allkeys-lfu` maintains a counter per key with a decay so old popularity fades.
- **TTL and expiry** — entries removed after a configured lifetime; expiration requires lazy checks (on access) plus active cycles (Redis's `activeExpireCycle`) so expired keys do not accumulate.
- **No-eviction mode** — Redis's default `noeviction` refuses writes that would exceed `maxmemory`, returning errors instead of silently dropping data; good when the cache is a source of truth.
- **Random and FIFO** — cheap options with unpredictable hit rates; `allkeys-random` is useful when access is uniform.
- **Operational concerns** — evictions and expirations are the key telemetry; the Redis `evicted_keys` metric and Memcached `evictions` counter reveal whether capacity or TTLs are misconfigured.

## Related
- [[wiki/data-storage/caching-strategies|Caching Strategies]] — where eviction policies apply
- [[wiki/data-storage/key-value-stores|Key-Value Stores]] — Redis and Memcached as cache engines
- [[wiki/data-storage/buffer-pool-management|Buffer Pool Management]] — page-level replacement in databases
- [[wiki/data-storage/database-performance-monitoring|Database Performance Monitoring]] — cache hit-ratio metrics
- [[wiki/data-storage/backpressure|Backpressure]] — protecting caches from overload
