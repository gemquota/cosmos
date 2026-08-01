---
type: "concept"
title: "ACID"
description: "Atomicity, Consistency, Isolation, Durability — the guarantees of reliable transactions"
tags: ["acid", "transactions", "database", "consistency", "sql"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# ACID

## Summary
ACID describes transaction guarantees: Atomicity (all-or-nothing), Consistency (valid state to valid state), Isolation (concurrent transactions don't interfere), and Durability (committed data survives crashes).

## Details
- Databases trade some ACID for performance via isolation levels and replication lag.
- NoSQL systems often relax ACID (BASE) for availability; choose by consistency needs.
- mykb's note writes want strong atomicity — one note, one commit.

## Related
- [[wiki/devops-infra/transactions|Transactions]] — ACID in practice
- [[wiki/devops-infra/isolation-levels|Isolation Levels]] — the I in ACID
- [[wiki/devops-infra/replication|Replication]] — durability and availability tension
- [[wiki/devops-infra/postgresql|PostgreSQL]] — full ACID database
- [[wiki/api-protocols/idempotency|Idempotency]] — application-level dedup builds on atomic commits
