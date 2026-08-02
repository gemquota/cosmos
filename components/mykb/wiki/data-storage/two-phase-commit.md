---
type: "concept"
title: "Two-Phase Commit"
description: "Prepare/commit coordinator protocol for distributed atomicity"
tags: ["two-phase-commit", "distributed-transactions", "atomicity", "protocols"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/Two-phase_commit_protocol", "https://dev.mysql.com/doc/refman/8.4/en/xa.html"]
---

# Two-Phase Commit

## Summary
Two-phase commit (2PC) is the protocol that lets multiple resource managers commit a single transaction atomically. A coordinator first asks every participant to prepare and vote, then broadcasts commit only if all votes are yes; otherwise it broadcasts rollback.

## Details
- **Phase one (prepare)** — the coordinator sends a prepare request; each participant flushes its redo log, becomes ready, and votes yes or no. A yes vote is a promise the participant can commit locally when told to.
- **Phase two (commit/abort)** — if all votes are yes, the coordinator logs a commit decision and tells participants to commit; a single no means every participant rolls back. Participants that miss the message recover by asking the coordinator.
- **Blocking problem** — if the coordinator crashes after prepares but before deciding, participants cannot resolve unilaterally and hold locks until it recovers; 3PC and Paxos commit variants reduce but do not eliminate the window.
- **XA integration** — JDBC and ODBC transaction managers drive 2PC across databases and queues; MySQL supports XA statements, and Postgres has long supported 2PC via `PREPARE TRANSACTION`, though it is rarely used directly.
- **When to use it** — strong atomicity across few, reliable participants; for many microservices, sagas and idempotent events usually beat 2PC's availability cost.
- **Monitoring** — stuck `PREPARED` transactions are a classic production incident; tooling must list and resolve in-doubt transactions.

## Related
- [[wiki/data-storage/distributed-transactions|Distributed Transactions]] — the problem 2PC solves
- [[wiki/data-storage/write-ahead-logging|Write-Ahead Logging]] — what a prepare vote persists
- [[wiki/data-storage/raft-consensus|Raft Consensus]] — leader-driven agreement alternative
- [[wiki/data-storage/crash-recovery|Crash Recovery]] — recovering in-doubt participants
- [[wiki/data-storage/deadlock-detection|Deadlock Detection]] — lock waits 2PC can cause
