---
type: "concept"
title: "Write-Behind Cache"
description: "Caches that absorb writes and flush them to the source asynchronously"
tags: ["write-behind", "cache", "async", "design"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Write-Behind Cache

## Summary
Write-behind caches accept writes into the cache and flush them to the source in the background, trading durability for latency and batching. A crash before flush loses acknowledged writes — the classic risk.

## Details
- Write-behind gives low latency and write coalescing, but a window of data loss.
- Use durable queues or WALs to shrink the loss window; flush policies bound it.
- Not for money; great for counters, analytics, and derived data.
- mykb relevance: article view counters flush write-behind from cache to the analytics store.

## Related
- [[wiki/tooling/write-through-cache|Write-Through Cache]]
- [[wiki/tooling/cache-aside|Cache-Aside]]
- [[wiki/software-engineering/at-most-once|At-Most-Once]]
- [[wiki/compositions/write-ahead-log|Write-Ahead Log]]
- [[wiki/compositions/dual-writes|Dual Writes]]
