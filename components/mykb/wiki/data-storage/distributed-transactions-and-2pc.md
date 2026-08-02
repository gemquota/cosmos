---
type: "concept"
title: "Distributed Transactions and 2PC"
description: "Atomicity across multiple nodes and the two-phase commit protocol"
tags: ["2pc", "distributed-transactions", "atomicity", "consensus"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Distributed Transactions and 2PC

## Summary

A stub to be expanded into a full article; frames the concept and open questions.

## Details

- 2PC coordinates participants through prepare and commit phases for atomic commit.
- Blocking on coordinator failure is the classic 2PC weakness; 3PC and Paxos commit reduce it.
- Modern databases (Spanner, CockroachDB) use consensus-based commit variants.
- Consider sagas or outbox patterns when distributed transactions are too costly.

## Related

- [[wiki/data-storage/two-phase-commit|Two-Phase Commit]] — 2PC note
- [[wiki/data-storage/distributed-transactions|Distributed Transactions]] — transactions
- [[wiki/data-storage/saga-transactions-and-compensations|Saga Transactions And Compensations]] — alternative
- [[wiki/data-storage/outbox-pattern-for-transactions|Outbox Pattern For Transactions]] — alternative
- [[wiki/data-storage/data-engineering-fundamentals|Data Engineering Fundamentals]] — core data engineering concepts
