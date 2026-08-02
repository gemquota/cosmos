---
type: "concept"
title: "Caching Layers"
description: "Positioning caches at each tier from browser to CDN to app to database"
tags: ["caching", "architecture", "performance", "layers"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Caching Layers

## Summary
Caching layers place fast storage at every level of the stack — browser, CDN, reverse proxy, application, database — so repeated reads rarely reach the origin. Each layer has its own invalidation rules and consistency contract.

## Details
- Layer order: browser → CDN → edge cache → app cache → DB cache; each layer shrinks traffic below.
- Each layer needs its own TTL and invalidation strategy; mismatched layers serve stale data.
- Cache hits hide problems: measure miss rates per layer, not just overall hit ratio.
- mykb relevance: the wiki serves from a multi-layer cache so article reads never hit disk.

## Related
- [[wiki/tooling/cache-invalidation|Cache Invalidation]]
- [[wiki/tooling/ttl-caches|TTL Caches]]
- [[wiki/tooling/distributed-cache|Distributed Cache]]
- [[wiki/tooling/local-cache|Local Cache]]
- [[wiki/tooling/cdn-practice|CDN Practice]]
