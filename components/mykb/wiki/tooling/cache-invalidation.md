---
type: "concept"
title: "Cache Invalidation"
description: "Removing or refreshing cached entries when the source data changes"
tags: ["cache", "invalidation", "consistency", "design"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Cache Invalidation

## Summary
Cache invalidation is the hard half of caching: entries must disappear or refresh when truth changes. Strategies span TTLs, event-driven invalidation, versioned keys, and write-through updates.

## Details
- TTL-based invalidation is simple and bounded-stale; event-based invalidation is fresh but complex.
- Version keys (content hash in the key) make invalidation automatic and race-free.
- Stampede risk rises at invalidation moments — refresh early or serve stale briefly.
- mykb relevance: the wiki index invalidates only the entries a sync actually changed.

## Related
- [[wiki/tooling/cache-stampede|Cache Stampede]]
- [[wiki/tooling/ttl-caches|TTL Caches]]
- [[wiki/tooling/cache-aside|Cache-Aside]]
- [[wiki/tooling/etag-negotiation|ETag Negotiation]]
- [[wiki/tooling/caching-layers|Caching Layers]]
