---
type: "concept"
title: "Lost Update Problem"
description: "Two writes to the same value where one silently overwrites the other"
tags: ["lost-update", "concurrency", "transactions", "anomalies"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Lost Update Problem

## Summary
The lost update problem occurs when two transactions read a value, modify it, and write back — the second write clobbers the first's change. It is the classic read-modify-write race, prevented by locking, CAS, or version checks.

## Details
- Classic example: two counters increment from 0 to 1 instead of 0 to 2.
- Fix with SELECT FOR UPDATE, optimistic version checks, or atomic increments.
- Read-committed databases do not prevent lost updates — you must add the mechanism.
- mykb relevance: wiki edit counters and cache-aside writes are lost-update-prone.

## Related
- [[wiki/compositions/compare-and-swap|Compare-and-Swap]]
- [[wiki/api-protocols/optimistic-concurrency|Optimistic Concurrency]]
- [[wiki/compositions/pessimistic-locking|Pessimistic Locking]]
- [[wiki/compositions/transaction-isolation-practice|Transaction Isolation Practice]]
- [[wiki/compositions/dirty-reads|Dirty Reads]]
