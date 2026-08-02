---
type: "concept"
title: "Dirty Reads"
description: "Reading data that another transaction has written but not committed"
tags: ["dirty-reads", "isolation", "transactions", "anomalies"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Dirty Reads

## Summary
A dirty read observes uncommitted data that may later roll back, meaning the reader saw values that never existed in any committed state. Read committed and stronger isolation levels prevent it.

## Details
- Rollback after a dirty read leaves the reader acting on phantom facts.
- Read uncommitted permits dirty reads; read committed is the standard cure.
- Dirty reads are sometimes acceptable for analytics — usually not for decisions.
- mykb relevance: wiki content reads must never see an article still mid-save.

## Related
- [[wiki/compositions/read-uncommitted|Read Uncommitted]]
- [[wiki/compositions/read-committed|Read Committed]]
- [[wiki/compositions/transaction-isolation-practice|Transaction Isolation Practice]]
- [[wiki/compositions/phantom-reads|Phantom Reads]]
- [[wiki/compositions/repeatable-read|Repeatable Read]]
