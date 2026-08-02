---
type: "concept"
title: "Buffer Pool Management"
description: "Page caching, eviction, and dirty-page flushing inside a database"
tags: ["buffer-pool", "page-cache", "eviction", "database-internals"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://dev.mysql.com/doc/refman/8.4/en/innodb-buffer-pool.html", "https://www.postgresql.org/docs/current/runtime-config-resource.html"]
---

# Buffer Pool Management

## Summary
The buffer pool is the database's in-memory cache of disk pages. Reads and writes go through it, so hit rate determines whether a workload runs at memory or disk speed; eviction and dirty-page flushing keep it coherent with storage.

## Details
- **Pool anatomy** — pages are read from disk into the pool in fixed-size frames; every access must pin the page so it is not evicted mid-operation. InnoDB's pool is a single large memory region; Postgres's shared buffers serve the same role.
- **Eviction** — when the pool is full, a replacement policy picks a victim. Most engines approximate LRU; InnoDB maintains a midpoint-insertion LRU so one-off scans do not flush the hot set, while Postgres uses a clock-sweep algorithm.
- **Dirty pages** — modified pages are marked dirty and later written back by background flushers; InnoDB uses a doublewrite buffer to survive partial page writes, and both engines bound flushing to smooth I/O.
- **Coherence** — the pool must stay consistent with the write-ahead log: redo is forced before dirty pages are written so recovery can reconstruct lost updates.
- **Tuning** — sizing the pool is the single biggest lever; too small causes churn, too large starves the OS cache. Monitoring hit ratio and dirty-page age separates cache problems from query problems.

## Related
- [[wiki/data-storage/write-ahead-logging|Write-Ahead Logging]] — what makes evicted dirty pages safe
- [[wiki/data-storage/cache-eviction-policies|Cache Eviction Policies]] — LRU, LFU, and clock variants
- [[wiki/data-storage/crash-recovery|Crash Recovery]] — replaying the log after a restart
- [[wiki/data-storage/database-performance-monitoring|Database Performance Monitoring]] — observing pool health
- [[wiki/devops-infra/postgresql|PostgreSQL]] — shared_buffers tuning in practice
