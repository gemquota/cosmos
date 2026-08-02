---
type: "concept"
title: "Cache-Aside and Write-Through"
description: "The core cache consistency patterns"
tags: ["caching", "cache-aside", "write-through", "consistency"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://learn.microsoft.com/en-us/azure/architecture/patterns/cache-aside", "https://redis.io/docs/latest/"]
---

# Cache-Aside and Write-Through

## Summary

Cache-aside loads data into cache on miss and lets the app manage invalidation.
Write-through updates the cache on every write, keeping it warm.
Pattern choice trades consistency complexity against hit rates.
Cache consistency is a correctness problem, not just a performance one.

## Details

- Cache-aside: read miss -> load from DB -> populate cache.
- Invalidation on writes prevents stale reads.
- Write-through adds write latency but keeps cache fresh.
- Write-behind batches writes but risks loss.
- TTLs are the safety net for all patterns.
- Plan invalidation paths before enabling caching.
- TTLs are the safety net; monitor hit rates to tune them.
- Cache consistency patterns are the difference between a fast system and a wrong one.

## Related

- [[wiki/data-storage/redis-and-caching-patterns|Redis And Caching Patterns]] — engine
- [[wiki/data-storage/read-replicas-and-scaling|Read Replicas And Scaling]] — scaling reads
- [[wiki/data-storage/eventual-consistency-and-conflict-resolution|Eventual Consistency And Conflict Resolution]] — staleness
- [[wiki/data-storage/caching-strategies|Caching Strategies]] — existing note
- [[wiki/data-storage/cache-eviction-policies|Cache Eviction Policies]] — eviction
- [[wiki/data-storage/data-quality-dimensions|Data Quality Dimensions]] — quality dimensions
- [[wiki/data-storage/data-observability-and-monitoring|Data Observability And Monitoring]] — observability
- [[wiki/data-storage/data-testing-frameworks|Data Testing Frameworks]] — testing
- [[wiki/data-storage/feature-stores-and-ml-features|Feature Stores And Ml Features]] — ML features
- [[wiki/data-storage/data-contracts-and-agreements|Data Contracts And Agreements]] — data contracts
- [[wiki/data-storage/incremental-loading-strategies|Incremental Loading Strategies]] — incremental loading
- [[wiki/data-storage/schema-evolution-in-streams|Schema Evolution In Streams]] — schema evolution

