---
type: "concept"
title: "Local Cache"
description: "An in-process cache that lives inside each application instance"
tags: ["local-cache", "caching", "performance", "in-process"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Local Cache

## Summary
A local cache stores data in each instance's own memory — no network hop, maximum speed — but every instance has its own copy that can diverge. It suits immutable data and per-instance state; it complicates invalidation.

## Details
- Local caches are fastest and free of network failure modes.
- Consistency is per-instance: invalidation must fan out or accept staleness windows.
- Memory is bounded per instance — size, evict, and monitor.
- mykb relevance: each wiki worker caches slug-to-path maps locally for build speed.

## Related
- [[wiki/tooling/distributed-cache|Distributed Cache]]
- [[wiki/tooling/cache-invalidation|Cache Invalidation]]
- [[wiki/tooling/cache-aside|Cache-Aside]]
- [[wiki/software-engineering/performance-engineering|Performance Engineering]]
- [[wiki/tooling/caching-layers|Caching Layers]]
