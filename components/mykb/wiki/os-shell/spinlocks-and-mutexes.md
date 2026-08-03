---
type: "concept"
title: "Spinlocks & Mutexes"
description: "Locking primitives and when spinning beats sleeping"
tags: ["locking", "spinlock", "mutex", "kernel"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Spinlocks & Mutexes

## Summary
Spinlocks and mutexes are the two fundamental locking primitives: a spinlock busy-waits (spins) until the lock is free, while a mutex puts the waiter to sleep and reschedules it later. The choice is about hold time and context: spin when the critical section is tiny and the CPU would waste more time sleeping than spinning; use a mutex (or sleepable lock) when the holder might block, sleep, or hold for a long time.

## Details
- Mechanism: a spinlock is a tight atomic test-and-set loop (on x86, `lock cmpxchg`); it disables preemption on the local CPU (on SMP, it prevents migration and, in interrupt context, masks interrupts), and waiters burn CPU until the holder releases. It is only valid for short, non-sleeping critical sections — in the kernel, holding a spinlock forbids sleeping, and the scheduler/interrupts cannot run on the holding CPU. A mutex, by contrast, is a sleepable lock: a waiter sets a flag, sleeps on a wait queue, and the scheduler wakes it when the lock frees — costing a context switch but burning zero CPU while waiting. The kernel's `mutex`, `semaphore`, `rwsem`, and `rcu` (lock-free reads) form the rest of the toolkit; user space has pthread mutexes, which the glibc implementation optimizes with a short spin before sleeping.
- Concrete examples: a driver's interrupt handler protects a ring-buffer index with a spinlock (must not sleep); a filesystem protects its inode cache with mutexes (operations can sleep on I/O); user-space thread pools use pthread mutexes with adaptive spinning for short critical sections; a per-CPU variable needs no lock at all if it is only touched by its own CPU; `spin_lock_irqsave` guards state also touched by interrupt handlers.
- Failure modes: the classic failures are sleeping while holding a spinlock (kernel panic/oops), deadlock from lock ordering (A then B vs. B then A — the reason lockdep exists), priority inversion (a low-priority holder stalls high-priority waiters — solved by priority inheritance in rt mutexes), and over-contention where a single hot lock serializes all cores (the "livelock at scale" symptom: 100% CPU, no progress). Holding locks across user-space copies or I/O extends hold times and multiplies contention.
- Operational tradeoffs: spinlocks are fast when contention is rare and hold times are nanoseconds, but wasteful when many CPUs spin on a contended lock; mutexes cost a context switch per handoff but scale to long or contended sections. The practice rules: measure contention before optimizing (perf lock, lockstat), keep critical sections minimal, prefer RCU or per-CPU structures for read-mostly data, and let lockdep validate ordering in debug builds. RSIS3/mykb relevance: RSIS3's registry and checkpoint writes are a locking design problem: spinlock-style optimism for short updates, mutex-style serialization for long rebuilds, and the same deadlock/inversion discipline applies to loop coordination.

## Related
- [[wiki/os-shell/kernel-architecture|Kernel Architecture]]
- [[wiki/os-shell/memory-management-paging|Memory Management & Paging]]
- [[wiki/syntheses/knowledge-acquisition-workflow|Knowledge Acquisition Workflow]] — how stubs grow into full articles in mykb
- [[wiki/syntheses/mykb-acquisition-curation-and-practices|Acquisition, Curation & Practices]] — the curation loop this stub belongs to
