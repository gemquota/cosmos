---
type: "concept"
title: "Transactions and ACID Revisited"
description: "Atomicity, consistency, isolation, and durability in modern databases"
tags: ["acid", "transactions", "consistency", "databases"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://www.postgresql.org/docs/current/transactions.html", "https://en.wikipedia.org/wiki/ACID"]
---

# Transactions and ACID Revisited

## Summary

ACID transactions bundle operations so they succeed or fail as one unit.
The guarantees matter for correctness in operational systems.
Distributed systems relax or re-engineer ACID to scale, which is why semantics matter.
ACID is about trust: applications rely on atomic commits even when the network and disks fail.

## Details

- Atomicity via undo/redo logs; durability via WAL.
- Consistency is a property of the application plus constraints, not just the engine.
- Isolation is tunable; serializable is strongest but costliest.
- Distributed transactions (2PC, consensus-based commit) extend ACID across nodes.
- Event-driven systems often trade ACID for eventual consistency plus outbox patterns.
- Distributed transactions scale costs quickly; design for fewer cross-node commits.
- Sagas and outbox patterns relax ACID deliberately, with compensation.
- ACID remains the correctness baseline for operational systems; relax it only with explicit, reviewed tradeoffs.

## Related

- [[wiki/data-storage/wal-and-consistency|Wal And Consistency]] — durability
- [[wiki/data-storage/mvcc-and-isolation-levels|MVCC and Isolation Levels]] — isolation
- [[wiki/data-storage/distributed-transactions-and-2pc|Distributed Transactions And 2Pc]] — distributed ACID
- [[wiki/data-storage/acid-transactions|ACID Transactions]] — existing note
- [[wiki/data-storage/transaction-isolation-levels|Transaction Isolation Levels]] — levels
- [[wiki/data-storage/data-quality-dimensions|Data Quality Dimensions]] — quality dimensions
- [[wiki/data-storage/data-observability-and-monitoring|Data Observability and Monitoring]] — observability
- [[wiki/data-storage/data-testing-frameworks|Data Testing Frameworks]] — testing
- [[wiki/data-storage/feature-stores-and-ml-features|Feature Stores and ML Features]] — ML features
- [[wiki/data-storage/data-contracts-and-agreements|Data Contracts and Agreements]] — data contracts
- [[wiki/data-storage/incremental-loading-strategies|Incremental Loading Strategies]] — incremental loading
- [[wiki/data-storage/schema-evolution-in-streams|Schema Evolution In Streams]] — schema evolution

