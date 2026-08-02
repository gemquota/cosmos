---
type: "concept"
title: "Cache-Aside"
description: "The pattern where the app checks cache, then loads and populates on miss"
tags: ["cache-aside", "pattern", "caching", "design"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Cache-Aside

## Summary
Cache-aside (lazy loading) reads the cache first, loads from the source on a miss, and writes the entry back with a TTL. It is simple and resilient — the cache can be cleared without breaking anything, at the cost of cold-start misses.

## Details
- The cache is not authoritative; the source of truth stays behind it.
- Populate-on-miss means the first read after invalidation is slow (and can stampede).
- Use this pattern unless you need write-path freshness — then consider write-through.
- mykb relevance: the wiki resolver cache-aside on article lookups with a bounded TTL.

## Related
- [[wiki/tooling/write-through-cache|Write-Through Cache]]
- [[wiki/tooling/write-behind-cache|Write-Behind Cache]]
- [[wiki/tooling/ttl-caches|TTL Caches]]
- [[wiki/tooling/cache-stampede|Cache Stampede]]
- [[wiki/tooling/caching-layers|Caching Layers]]
