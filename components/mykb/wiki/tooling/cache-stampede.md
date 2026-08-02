---
type: "concept"
title: "Cache Stampede"
description: "The thundering herd that hits the origin when a hot cache entry expires"
tags: ["cache-stampede", "caching", "concurrency", "reliability"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Cache Stampede

## Summary
A cache stampede happens when a hot entry expires and many requests miss at once, all fetching from the origin simultaneously. Without protection, the origin collapses under the herd; the cache was meant to protect it.

## Details
- Mitigations: request coalescing (single-flight), early refresh, jittered TTLs, and lock-based population.
- Single-flight per key keeps one in-flight fetch and shares its result.
- Stampedes are worse for expensive recomputations — which is exactly where caches matter.
- mykb relevance: the wiki search index refresh uses single-flight to avoid rebuild stampedes.

## Related
- [[wiki/tooling/ttl-caches|TTL Caches]]
- [[wiki/tooling/cache-invalidation|Cache Invalidation]]
- [[wiki/tooling/cache-aside|Cache-Aside]]
- [[wiki/tooling/hot-key-cache|Hot Key Cache]]
- [[wiki/software-engineering/jitter-practice|Jitter Practice]]
