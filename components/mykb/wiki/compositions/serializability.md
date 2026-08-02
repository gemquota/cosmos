---
type: "concept"
title: "Serializability"
description: "Making concurrent transactions behave as if they ran one after another"
tags: ["serializability", "transactions", "isolation", "models"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Serializability

## Summary
Serializability guarantees the result of concurrent transactions equals some serial order, so no transaction sees another's intermediate state. It is the strongest isolation level; linearizability is about single operations, serializability about transaction groups.

## Details
- Serializable execution avoids all anomalies: dirty reads, lost updates, write skew.
- Implementations: strict two-phase locking, serializable snapshot isolation, optimistic concurrency.
- Cost is contention and aborts; many workloads accept weaker levels deliberately.
- mykb relevance: multi-article transactions (rename + relink) should be serializable.

## Related
- [[wiki/compositions/snapshot-isolation|Snapshot Isolation]]
- [[wiki/compositions/linearizability|Linearizability]]
- [[wiki/compositions/transaction-isolation-practice|Transaction Isolation Practice]]
- [[wiki/compositions/write-skew|Write Skew]]
- [[wiki/tooling/distributed-consistency|Distributed Consistency]]
