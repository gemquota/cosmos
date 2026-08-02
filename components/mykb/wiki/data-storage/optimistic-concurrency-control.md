---
type: "concept"
title: "Optimistic Concurrency Control"
description: "Validating conflicts at commit instead of locking up front"
tags: ["optimistic-concurrency", "conflict-detection", "transactions", "concurrency-control"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/Optimistic_concurrency_control", "https://www.postgresql.org/docs/current/functions-admin.html"]
---

# Optimistic Concurrency Control

## Summary
Optimistic concurrency control (OCC) lets transactions run without locks and checks at commit time whether any read set or write set changed. If the version check fails, the transaction aborts and retries, trading wasted work for freedom from blocking.

## Details
- **Read phase** — transactions read data and track the versions of everything they touched; no locks are taken, so readers and writers never block one another.
- **Validation phase** — at commit, the engine compares read-set versions against the current state; if a concurrent transaction committed a conflicting write, validation fails and the transaction rolls back.
- **Write phase** — validated writes are installed atomically; the writer must ensure it applied changes to the versions it validated, often by re-reading or by writing through versioned rows.
- **Versioning strategies** — a monotonically increasing version number or updated-timestamp per row is the common scheme; application-level optimistic locking in ORMs (Rails, JPA, EF Core) uses the same idea.
- **When it wins** — workloads with low write contention get high throughput because there is no lock traffic; under heavy contention, aborts and retries dominate and pessimistic locking performs better.
- **Hybrids** — MVCC databases use optimistic validation at serializable isolation (Postgres SSI), while read-committed engines use short locks with version checks at the application layer.

## Related
- [[wiki/data-storage/multiversion-concurrency-control|Multiversion Concurrency Control]] — versioning that enables validation
- [[wiki/data-storage/two-phase-locking|Two-Phase Locking]] — the pessimistic alternative
- [[wiki/data-storage/transaction-isolation-levels|Transaction Isolation Levels]] — guarantees after validation
- [[wiki/data-storage/deadlock-detection|Deadlock Detection]] — the problem OCC avoids
- [[wiki/devops-infra/optimistic-locking|Optimistic Locking]] — application-level version checks
