---
type: "concept"
title: "Write Skew"
description: "Two transactions writing different rows based on overlapping reads, breaking an invariant"
tags: ["write-skew", "isolation", "transactions", "anomalies"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Write Skew

## Summary
Write skew happens when two transactions read the same rows, each writes a different row consistent with what it saw, and together the writes violate an invariant — neither transaction alone is wrong. Snapshot isolation allows it; serializable levels prevent it.

## Details
- Classic example: two doctors both see one of them on call and both go off call.
- Write skew requires overlapping reads and disjoint writes.
- Fix with serializable isolation, materialized conflict rows, or application-level locks.
- mykb relevance: wiki publish rules (one publisher per article) are write-skew-prone.

## Related
- [[wiki/compositions/snapshot-isolation|Snapshot Isolation]]
- [[wiki/compositions/serializability|Serializability]]
- [[wiki/compositions/transaction-isolation-practice|Transaction Isolation Practice]]
- [[wiki/compositions/lost-update-problem|Lost Update Problem]]
- [[wiki/compositions/distributed-locks|Distributed Locks]]
