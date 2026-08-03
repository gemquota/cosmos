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
- Detection is the hard part: per-key hit counters or proxy traffic analytics identify the entries whose request share is disproportionate, and the threshold should be derived from measured load, not intuition.
- Replication spreads the load: copy the hot key to several nodes and read from any of them, so no single node absorbs the full request rate.
- Sharding by random suffix breaks the single-key bottleneck when replication alone is not enough, trading memory for even distribution.
- The origin path needs protection too: hot keys stress origins on miss, so a miss should fall back to a shared cache or a coalesced origin request rather than a thundering herd.
- Stale-while-revalidate is a useful complement: serve the last known value while refreshing in the background, bounding the miss cost for entries that change rarely.
- Capacity planning should budget for the hottest key: estimate its request rate at peak and size the node group so the tail of the distribution, not the median, fits in memory.
- Monitoring hot-key health means tracking eviction and miss rates per key, because a replicated entry that gets evicted on every node is worse than no replication at all.
- mykb relevance: under the standing policy, the wiki's most-linked article would become a replicated hot-key entry, and any entry crossing the detection threshold would receive the same treatment.

## Related
- [[wiki/tooling/distributed-cache|Distributed Cache]]
- [[wiki/tooling/cache-stampede|Cache Stampede]]
- [[wiki/tooling/local-cache|Local Cache]]
- [[wiki/software-engineering/performance-engineering|Performance Engineering]]
- [[wiki/tooling/caching-layers|Caching Layers]]
