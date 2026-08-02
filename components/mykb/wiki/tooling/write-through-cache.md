---
type: "concept"
title: "Write-Through Cache"
description: "Caches that are updated synchronously on every write"
tags: ["write-through", "cache", "consistency", "design"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Write-Through Cache

## Summary
Write-through caches update the cache in the same operation as the source write, so reads never see stale cache for data just written. It keeps cache and source consistent at the cost of write-path latency.

## Details
- The cache stays warm and consistent, but every write pays the cache update cost.
- Writes that fail after cache update need compensation or the cache diverges.
- Best for hot data with high read/write ratios on the same records.
- mykb relevance: article saves update the index cache write-through for immediate consistency.

## Related
- [[wiki/tooling/cache-aside|Cache-Aside]]
- [[wiki/tooling/write-behind-cache|Write-Behind Cache]]
- [[wiki/tooling/cache-invalidation|Cache Invalidation]]
- [[wiki/tooling/caching-layers|Caching Layers]]
- [[wiki/compositions/dual-writes|Dual Writes]]
