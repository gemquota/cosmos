---
type: "concept"
title: "Caching Layers"
description: "Positioning caches at each tier from browser to CDN to app to database"
tags: ["caching", "architecture", "performance", "layers"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Caching Layers

## Summary
Caching layers place fast storage at every level of the stack — browser, CDN, reverse proxy, application, database — so repeated reads rarely reach the origin. Each layer has its own invalidation rules and consistency contract, and the art is choosing where a given read should be satisfied: close enough to be fast, far enough from the data that staleness is acceptable.

## Details
- Layer order: browser → CDN → edge cache → app cache → DB cache; each layer shrinks traffic below. A browser cache serves the same user's repeats; a CDN serves regional repeats; an edge or reverse-proxy cache serves shared responses; the application cache serves computed data; the database cache serves query results. The further up, the cheaper and faster the hit — and the more stale it may be.
- Each layer needs its own TTL and invalidation strategy; mismatched layers serve stale data. A CDN caching a page for an hour while the application cache refreshes every minute produces two different versions of the same resource depending on which layer answered; the layers' lifetimes must be coordinated so staleness is bounded at the outer layers.
- Concrete example: a wiki article is read ten thousand times a day. The browser cache serves repeat visitors instantly, the CDN absorbs the regional read storms, the edge cache shields the application, and the application cache protects the database — when the article changes, invalidation (purge from CDN and edge, bump the app-cache key) propagates so no layer serves the old version after the update.
- Cache hits hide problems: measure miss rates per layer, not just overall hit ratio. A high aggregate hit ratio can mask a specific layer's miss storm — if the application cache misses on every request because the key includes a random value, the database takes the load while the headline ratio looks healthy.
- Failure modes: cache stampede, where a key expires and thousands of requests hit the origin simultaneously (mitigated by request coalescing and jittered TTLs); thundering-herd invalidation, where a purge empties a layer at once; stale reads after writes, when invalidation is missed; and unbounded caches that evict hot data for cold data.
- Tradeoffs: each cache layer adds complexity, memory cost, and a consistency contract, but it also removes a network hop and an origin request per hit; the right number of layers is the minimum that keeps origin load and latency within budget — more layers than that is complexity without benefit.
- mykb relevance: the wiki would serve from a multi-layer cache so article reads never hit disk; the same layering would apply to the knowledge graph and index, with the lesson that invalidation on write is what keeps the layers honest.

## Related
- [[wiki/tooling/cache-invalidation|Cache Invalidation]]
- [[wiki/tooling/ttl-caches|TTL Caches]]
- [[wiki/tooling/distributed-cache|Distributed Cache]]
- [[wiki/tooling/local-cache|Local Cache]]
- [[wiki/tooling/cdn-practice|CDN Practice]]
