---
type: "concept"
title: "TTL Caches"
description: "Caches that expire entries after a fixed time-to-live"
tags: ["ttl", "cache", "expiry", "design"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# TTL Caches

## Summary
TTL caches drop entries after a fixed lifetime, bounding staleness without any invalidation machinery. They are the simplest correct cache when slightly stale data is acceptable.

## Details
- The TTL is a staleness contract: choose it from how fresh data must be.
- Shorter TTLs mean more origin load; longer TTLs mean staler reads — tune per entry type.
- Expiry storms happen when many entries die at once — add jitter to TTLs.
- mykb relevance: the wiki tag-cloud caches with a five-minute TTL and jitter.

## Related
- [[wiki/tooling/cache-invalidation|Cache Invalidation]]
- [[wiki/tooling/cache-aside|Cache-Aside]]
- [[wiki/tooling/cache-stampede|Cache Stampede]]
- [[wiki/dev-tools/graceful-degradation|Graceful Degradation]]
- [[wiki/tooling/caching-layers|Caching Layers]]
