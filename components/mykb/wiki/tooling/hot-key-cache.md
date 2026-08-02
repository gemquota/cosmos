---
type: "concept"
title: "Hot Key Cache"
description: "Special handling for cache keys that receive disproportionate traffic"
tags: ["cache", "hot-keys", "performance", "reliability"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Hot Key Cache

## Summary
Hot keys are cache entries that absorb a disproportionate share of traffic — a celebrity profile, a viral article — straining a single cache node. Hot-key handling replicates or shards those entries so no one node melts.

## Details
- Replicate hot keys to multiple nodes and read from any copy; shard by random suffixes.
- Detect hot keys via per-key hit counters or proxy-level traffic analytics.
- Hot keys also stress origins on miss — protect both cache and origin paths.
- mykb relevance: the wiki's most-linked article becomes a replicated hot-key entry.

## Related
- [[wiki/tooling/distributed-cache|Distributed Cache]]
- [[wiki/tooling/cache-stampede|Cache Stampede]]
- [[wiki/tooling/local-cache|Local Cache]]
- [[wiki/software-engineering/performance-engineering|Performance Engineering]]
- [[wiki/tooling/caching-layers|Caching Layers]]
