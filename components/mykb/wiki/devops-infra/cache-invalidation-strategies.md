---
type: "concept"
title: "Cache Invalidation Strategies"
description: "Purge, versioned keys, and TTL design to keep caches correct"
tags: ["cache", "invalidation", "http", "cdn"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Cache Invalidation Strategies

## Summary
Cache invalidation decides when cached copies become stale and how they get refreshed: TTL-based expiry, explicit purges, and versioned keys are the three families. The goal is to serve most reads from cache while never serving data older than the business can tolerate.

## Details
- TTL: entries expire after a fixed time; cheap and self-healing, but a synchronized expiry causes a thundering herd at the cache edge unless TTLs are staggered, jittered, or refreshed in the background before expiry (stale-while-revalidate).
- Explicit purge: on write, the origin tells each cache to drop affected keys (CDN purge APIs, Redis DEL, HTTP invalidation requests); precise, but every writer must know every cache, and a failed purge leaves stale data with no recovery until the TTL expires.
- Versioned keys: content-addressed URLs (hash-named files, `?v=timestamp`) make stale data impossible because a key is never reused; the costs are unbounded growth unless old versions are garbage-collected, plus clients must resolve the current key.
- Concrete example: a CDN serving hash-named bundles never needs purging — a deploy changes the hash; a feed with `Cache-Control: max-age=300` plus a purge-on-publish needs both TTL and purge because readers should not wait five minutes for a correction.
- Failure modes: caching per-user data under a shared key leaks data between sessions; long TTLs on mutable content serve stale pricing or security state; purge storms choke the cache control plane; mass invalidation followed by cache warming spikes origin load.
- Tradeoffs: longer TTLs improve hit rate and cut origin cost but widen staleness; versioned keys buy correctness at the cost of storage and client complexity; choose per endpoint, not globally.
- RSIS3 relevance: the dashboard reads generated JSON snapshots — hash-named or versioned snapshot files avoid stale telemetry after regeneration, and TTLs on live queries prevent the dashboard from hammering the MyKB daemon.

## Related
- [[wiki/devops-infra/backup-strategies-3-2-1|Backup Strategies: 3-2-1]]
- [[wiki/devops-infra/progressive-sync-strategies|Progressive Sync Strategies]]
- [[wiki/cloud-infra/cloud-migration-strategies|Cloud Migration Strategies]]
- [[wiki/cloud-infra/snapshot-strategies|Snapshot Strategies]]
