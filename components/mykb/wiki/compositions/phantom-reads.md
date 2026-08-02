---
type: "concept"
title: "Phantom Reads"
description: "Rows appearing or disappearing mid-transaction as other transactions commit"
tags: ["phantom-reads", "isolation", "transactions", "anomalies"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Phantom Reads

## Summary
Phantom reads happen when a transaction re-runs a range query and sees different rows because another transaction committed inserts or deletes. Snapshot isolation and serializable levels handle phantoms differently — snapshot isolation hides them within a snapshot.

## Details
- Phantoms are about row sets, not values: the same query returns a different set.
- Serializable levels use predicate locks or serialization checks to prevent them.
- Snapshot isolation avoids phantoms within a transaction's snapshot; conflicts surface at commit.
- mykb relevance: wiki report queries on a snapshot see a stable article set.

## Related
- [[wiki/compositions/snapshot-isolation|Snapshot Isolation]]
- [[wiki/compositions/repeatable-read|Repeatable Read]]
- [[wiki/compositions/dirty-reads|Dirty Reads]]
- [[wiki/compositions/transaction-isolation-practice|Transaction Isolation Practice]]
- [[wiki/compositions/serializability|Serializability]]
