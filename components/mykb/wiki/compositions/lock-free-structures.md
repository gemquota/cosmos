---
type: "concept"
title: "Lock-Free Structures"
description: "Concurrent data structures that make progress without locks"
tags: ["lock-free", "concurrency", "data-structures", "performance"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Lock-Free Structures

## Summary
Lock-free data structures guarantee system-wide progress without mutexes, using atomic operations like CAS. They avoid deadlock and priority inversion but demand care: ABA problems, memory reclamation, and subtle ordering bugs.

## Details
- Building blocks: compare-and-swap loops, atomic reference counting, hazard pointers.
- Lock-free guarantees progress for the system; wait-free guarantees per-thread progress.
- Hard to verify — prefer well-tested libraries over hand-rolled versions.
- mykb relevance: lock-free queues could handle agent task dispatch without contention.

## Related
- [[wiki/compositions/compare-and-swap|Compare-and-Swap]]
- [[wiki/compositions/pessimistic-locking|Pessimistic Locking]]
- [[wiki/software-engineering/concurrency-models|Concurrency Models]]
- [[wiki/software-engineering/thread-pools|Thread Pools]]
- [[wiki/software-engineering/performance-engineering|Performance Engineering]]
