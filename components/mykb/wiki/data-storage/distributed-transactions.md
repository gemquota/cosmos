---
type: "concept"
title: "Distributed Transactions"
description: "Coordinating atomicity across multiple databases and systems"
tags: ["distributed-transactions", "atomicity", "two-phase-commit", "distributed-systems"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://www.postgresql.org/docs/current/ddl-foreign-data.html", "https://en.wikipedia.org/wiki/Distributed_transaction"]
---

# Distributed Transactions

## Summary
A distributed transaction spans multiple databases, services, or partitions and must commit atomically across all of them. Coordinating atomicity over a network is hard because participants can fail independently, which is why distributed transactions are either carefully protocol-driven or replaced with sagas and idempotent messaging.

## Details
- **Why they are hard** — any participant may commit while another crashes before committing, so the coordinator cannot know a global outcome; messages between participants add latency and failure modes that local engines never face.
- **Two-phase commit** — the classic protocol: a coordinator asks all participants to prepare (durably), then sends commit or rollback based on unanimous votes; a prepare-phase crash leaves participants blocked until the coordinator recovers.
- **XA standard** — the X/Open XA interface lets application servers coordinate heterogeneous resources (databases, queues) through a transaction manager; MySQL, PostgreSQL (via `pg_xact`-era mechanisms and ODBC/JDBC), and Oracle support XA.
- **Alternatives** — sagas split the transaction into local steps with compensating actions; outbox patterns write intent and events in one local transaction so consumers apply changes idempotently; both trade atomicity for availability.
- **Newer approaches** — consensus-based commit (e.g., Spanner's Paxos groups) removes the blocking coordinator failure mode; CockroachDB and TiDB use similar replicated-log designs for linearizable cross-partition transactions.

## Related
- [[wiki/data-storage/two-phase-commit|Two-Phase Commit]] — the foundational protocol
- [[wiki/data-storage/raft-consensus|Raft Consensus]] — replication that underlies modern commit
- [[wiki/data-storage/idempotent-ingestion|Idempotent Ingestion]] — retry-safe local transactions
- [[wiki/data-storage/acid-transactions|ACID Transactions]] — the guarantees being extended
- [[wiki/data-storage/event-streaming-platforms|Event Streaming Platforms]] — messaging-based coordination
