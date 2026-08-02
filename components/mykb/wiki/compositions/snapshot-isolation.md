---
type: "concept"
title: "Snapshot Isolation"
description: "Reading from a consistent snapshot so transactions never see partial commits"
tags: ["snapshot-isolation", "transactions", "isolation", "databases"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Snapshot Isolation

## Summary
Snapshot isolation gives each transaction a consistent snapshot of committed state; readers never block writers and never see in-progress changes. It prevents dirty reads and most anomalies, but allows write skew and is not fully serializable.

## Details
- MVCC is the standard implementation: versions per row, snapshots per transaction.
- Write-write conflicts are detected on commit (first-writer-wins) to avoid lost updates.
- Write skew (two transactions read overlapping data and write conflictingly) is possible.
- mykb relevance: wiki reports run on snapshots so reads never stall the sync writer.

## Related
- [[wiki/compositions/read-committed|Read Committed]]
- [[wiki/compositions/serializability|Serializability]]
- [[wiki/compositions/write-skew|Write Skew]]
- [[wiki/compositions/transaction-isolation-practice|Transaction Isolation Practice]]
- [[wiki/compositions/phantom-reads|Phantom Reads]]
