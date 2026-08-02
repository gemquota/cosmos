---
type: "concept"
title: "In-Memory Databases"
description: "Main-memory engines and their durability trade-offs"
tags: ["in-memory", "main-memory-databases", "durability", "redis"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://redis.io/docs/latest/operate/oss_and_stack/management/persistence/", "https://www.sqlite.org/inmemorydb.html"]
---

# In-Memory Databases

## Summary
In-memory databases keep the primary dataset in RAM, trading durable storage for latency. They suit caching, session state, leaderboards, and hot analytical paths; durability becomes an explicit design question answered by snapshots, append logs, or replication.

## Details
- **Why they are fast** — page reads hit memory instead of disk, and engines can skip buffer-pool management entirely; the whole table lives in a contiguous address space, enabling cache-friendly scans and simplified concurrency.
- **Durability options** — Redis offers RDB snapshots and AOF (append-only file) with configurable fsync policies; Memcached is purely volatile by design; hybrid systems like VoltDB rely on synchronous replication and logging for durability.
- **Hybrid approaches** — SAP HANA and Oracle TimesTen keep hot data in memory with disk overflow; DuckDB and SQLite offer in-memory modes for analytics and testing; columnar in-memory engines power many real-time OLAP products.
- **Costs** — RAM is expensive relative to disk, so capacity planning and eviction matter; process restarts lose data unless snapshots or replicas exist, and memory bandwidth becomes the new bottleneck.
- **When to choose** — point lookups, sub-millisecond writes, and workloads with skewed read patterns benefit most; large analytical scans may still be cheaper on compressed columnar disk storage.

## Related
- [[wiki/data-storage/caching-strategies|Caching Strategies]] — cache-aside and write-through over durable stores
- [[wiki/data-storage/cache-eviction-policies|Cache Eviction Policies]] — managing bounded memory
- [[wiki/data-storage/key-value-stores|Key-Value Stores]] — the shape most in-memory engines take
- [[wiki/data-storage/backup-strategies|Backup Strategies]] — persistence beyond RAM
- [[wiki/data-storage/columnar-storage|Columnar Storage]] — compression that changes the memory/disk calculus
