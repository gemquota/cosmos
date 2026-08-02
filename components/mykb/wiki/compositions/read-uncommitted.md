---
type: "concept"
title: "Read Uncommitted"
description: "The weakest isolation level, allowing reads of uncommitted data"
tags: ["read-uncommitted", "isolation", "transactions", "databases"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Read Uncommitted

## Summary
Read uncommitted lets statements read data from transactions that have not committed — dirty reads included. It is the fastest, least-safe isolation, used only where approximate reads are fine.

## Details
- Dirty reads can observe values that later roll back — data that never existed.
- Suitable for rough counts, caching decisions, and non-critical analytics.
- Most databases default elsewhere; choose it explicitly and document why.
- mykb relevance: wiki view-count estimates tolerate read-uncommitted; article content does not.

## Related
- [[wiki/compositions/dirty-reads|Dirty Reads]]
- [[wiki/compositions/read-committed|Read Committed]]
- [[wiki/compositions/transaction-isolation-practice|Transaction Isolation Practice]]
- [[wiki/compositions/lost-update-problem|Lost Update Problem]]
- [[wiki/tooling/distributed-consistency|Distributed Consistency]]
