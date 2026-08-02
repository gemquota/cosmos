---
type: "concept"
title: "Caching Strategies"
description: "Cache-aside, write-through, and write-back patterns"
tags: ["caching", "cache-aside", "write-through", "write-back"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://docs.aws.amazon.com/whitepapers/latest/database-caching-strategies-using-redis/caching-strategies.html", "https://redis.io/docs/latest/develop/use/cache/"]
---

# Caching Strategies

## Summary
Caching strategies describe how an application keeps a fast store (Redis, Memcached) consistent with a source of truth such as a database. The main patterns — cache-aside, read-through, write-through, and write-back — trade write latency, read latency, and consistency.

## Details
- **Cache-aside (lazy loading)** — the application checks the cache, and on a miss loads from the database and populates the cache; the cache holds only what was actually read. Simple and resilient, but misses cost extra latency and entries can go stale.
- **Read-through** — the cache itself loads from the database on a miss, centralizing load logic; the pattern hides the backing store behind the cache interface.
- **Write-through** — writes update the cache and the database in the same transaction; reads are always fresh, but every write pays both latencies, and writes to data never read are wasted effort.
- **Write-back (write-behind)** — writes go to the cache and are flushed to the database asynchronously; dramatically lower write latency but risks data loss if the cache dies before flushing, so it needs durable queuing and replay.
- **Refresh-ahead** — proactively refresh hot entries before they expire, smoothing latency spikes; requires predicting demand.
- **Failure handling** — caches must degrade safely: treat a cache outage as a miss, use short TTLs to bound staleness, and avoid stampedes with single-flight or locking on refill.
- **Trade-off summary** — cache-aside is the default; write-through suits consistency-sensitive reads; write-back suits write-heavy workloads that can tolerate eventual persistence.

## Related
- [[wiki/data-storage/cache-eviction-policies|Cache Eviction Policies]] — managing what stays resident
- [[wiki/data-storage/key-value-stores|Key-Value Stores]] — Redis/Memcached as cache engines
- [[wiki/data-storage/consistency-models|Consistency Models]] — staleness bounds in read/write paths
- [[wiki/data-storage/data-observability|Data Observability]] — hit-rate and staleness monitoring
- [[wiki/data-storage/database-performance-monitoring|Database Performance Monitoring]] — measuring cache effectiveness
