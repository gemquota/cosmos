---
type: "concept"
title: "Memcached vs Redis"
description: "Two in-memory caching systems compared"
tags: ["memcached", "redis", "caching", "comparison"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://github.com/memcached/memcached/wiki", "https://en.wikipedia.org/wiki/Memcached"]
---

# Memcached vs Redis

## Summary

Memcached is a simple, high-throughput key-value cache.
Redis adds data structures, persistence, and replication.
Choose by feature needs, not raw throughput alone.
The choice is feature depth versus minimalism; most teams outgrow memcached's feature set quickly.

## Details

- Memcached: multithreaded, minimal, volatile only.
- Redis: rich types, persistence, pub/sub, and Lua scripting.
- Both are fastest for hot-path caching.
- Operational differences: Redis needs more careful memory planning.
- Redis forks (Valkey, KeyDB) matter for licensing decisions.
- Benchmark with your own access patterns, not synthetic loads.
- Consider Valkey for Redis-compatible open-source licensing.
- The right cache choice is boring and measurable: pick what your workload and team can operate.

## Related

- [[wiki/data-storage/redis-and-caching-patterns|Redis And Caching Patterns]] — Redis
- [[wiki/data-storage/cache-aside-and-write-through|Cache-Aside and Write-Through]] — patterns
- [[wiki/data-storage/valkey-and-keydb|Valkey And Keydb]] — Redis forks
- [[wiki/data-storage/caching-strategies|Caching Strategies]] — caching
- [[wiki/data-storage/in-memory-databases|In-Memory Databases]] — in-memory
- [[wiki/data-storage/data-quality-dimensions|Data Quality Dimensions]] — quality dimensions
- [[wiki/data-storage/data-observability-and-monitoring|Data Observability and Monitoring]] — observability
- [[wiki/data-storage/data-testing-frameworks|Data Testing Frameworks]] — testing
- [[wiki/data-storage/feature-stores-and-ml-features|Feature Stores and ML Features]] — ML features
- [[wiki/data-storage/data-contracts-and-agreements|Data Contracts and Agreements]] — data contracts
- [[wiki/data-storage/incremental-loading-strategies|Incremental Loading Strategies]] — incremental loading
- [[wiki/data-storage/schema-evolution-in-streams|Schema Evolution In Streams]] — schema evolution

