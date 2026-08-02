---
type: "concept"
title: "Read Committed"
description: "The isolation level where reads see only committed data"
tags: ["read-committed", "isolation", "transactions", "databases"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Read Committed

## Summary
Read committed is the default isolation in most databases: statements see only committed rows, preventing dirty reads. Within one transaction, different statements may see different snapshots, allowing non-repeatable reads.

## Details
- Each statement gets its own snapshot (or locks released on read), so values can change mid-transaction.
- Prevents dirty reads; allows non-repeatable reads and phantoms.
- It is the pragmatic default: good concurrency with a documented compromise.
- mykb relevance: wiki queries run at read committed and tolerate per-statement freshness.

## Related
- [[wiki/compositions/read-uncommitted|Read Uncommitted]]
- [[wiki/compositions/repeatable-read|Repeatable Read]]
- [[wiki/compositions/dirty-reads|Dirty Reads]]
- [[wiki/compositions/transaction-isolation-practice|Transaction Isolation Practice]]
- [[wiki/compositions/snapshot-isolation|Snapshot Isolation]]
