---
type: "concept"
title: "Hash Indexes"
description: "Exact-match lookup structures for point queries and joins"
tags: ["hash-index", "indexing", "point-lookup", "join"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://dev.mysql.com/doc/refman/8.4/en/index-btree-hash.html", "https://www.postgresql.org/docs/current/hash-intro.html"]
---

# Hash Indexes

## Summary
Hash indexes map keys to buckets through a hash function, giving constant-time equality lookups without any ordering. They suit point queries and join probes, but cannot serve range scans or ordered output.

## Details
- **How they work** — the hash of the key selects a bucket; buckets chain entries or overflow pages when collisions occur; lookups hash once and walk a short chain.
- **Strengths** — O(1)-ish equality lookups can beat B-tree descent on huge keys (long strings), and they shine for primary-key-style point reads and hash-join probes.
- **Weaknesses** — no range queries, no prefix scans, no ordered iteration; MySQL's MEMORY engine and PostgreSQL's `hash` access method are the classic implementations.
- **PostgreSQL history** — hash indexes were historically non-WAL-logged and crash-prone; since PostgreSQL 10 they are fully logged and crash-safe, making them a viable choice again.
- **Dynamic hashing** — extendible and linear hashing grow the bucket count without full rehashes; in-memory engines use similar schemes for hash tables and grouping.
- **mykb relevance** — exact-match lookups such as `slug = 'raft-consensus'` or hash keys in content-addressable storage are ideal candidates; anything requiring `BETWEEN` or `ORDER BY` needs a B-tree instead.

## Related
- [[wiki/data-storage/b-tree-indexing|B-Tree Indexing]] — the ordered alternative for ranges
- [[wiki/data-storage/join-algorithms|Join Algorithms]] — hash joins build in-memory hash tables
- [[wiki/data-storage/consistent-hashing|Consistent Hashing]] — distributed key placement using hashing
- [[wiki/data-storage/in-memory-databases|In-Memory Databases]] — engines that lean on hash structures
- [[wiki/data-storage/content-addressable-storage|Content-Addressable Storage]] — lookups keyed by content hash
- [[wiki/data-storage/index-maintenance|Index Maintenance]] — keeping hash structures compact
