---
type: "concept"
title: "Pessimistic Locking"
description: "Locking rows or resources before use to prevent concurrent conflicts"
tags: ["pessimistic-locking", "locks", "concurrency", "databases"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Pessimistic Locking

## Summary
Pessimistic locking acquires a lock before reading or writing, blocking other transactions until release. It guarantees serial access at the cost of contention and deadlock risk; optimistic approaches detect conflicts at commit instead.

## Details
- Row locks (SELECT ... FOR UPDATE) and application mutexes are the common forms.
- Hold locks briefly and in consistent order to minimize deadlocks.
- Long-held locks serialize the hot path — measure contention before choosing.
- mykb relevance: wiki slug allocation locks pessimistically to avoid duplicates.

## Related
- [[wiki/api-protocols/optimistic-concurrency|Optimistic Concurrency]]
- [[wiki/compositions/distributed-locks|Distributed Locks]]
- [[wiki/compositions/transaction-isolation-practice|Transaction Isolation Practice]]
- [[wiki/compositions/lock-free-structures|Lock-Free Structures]]
- [[wiki/software-engineering/concurrency-models|Concurrency Models]]
