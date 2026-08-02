---
type: "concept"
title: "Repeatable Read"
description: "The isolation level where repeated reads in a transaction see the same snapshot"
tags: ["repeatable-read", "isolation", "transactions", "databases"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Repeatable Read

## Summary
Repeatable read gives each transaction a stable snapshot for the whole transaction, so the same query returns the same rows every time. It prevents dirty and non-repeatable reads; phantoms may still slip through depending on the engine.

## Details
- MySQL's default; PostgreSQL's default (read committed) is weaker per statement.
- Prevents non-repeatable reads; phantom rows from other commits can still appear (or not, with locks).
- Concurrency drops as snapshots and locks hold — tune for workload.
- mykb relevance: a long wiki migration script uses repeatable read for consistent view.

## Related
- [[wiki/compositions/read-committed|Read Committed]]
- [[wiki/compositions/snapshot-isolation|Snapshot Isolation]]
- [[wiki/compositions/phantom-reads|Phantom Reads]]
- [[wiki/compositions/transaction-isolation-practice|Transaction Isolation Practice]]
- [[wiki/compositions/serializability|Serializability]]
