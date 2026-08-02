---
type: "concept"
title: "Threads & Concurrency"
description: "Thread model, user vs kernel threads, and synchronization primitives"
tags: ["threads", "concurrency", "pthreads", "synchronization", "futex"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://man7.org/linux/man-pages/man7/pthreads.7.html", "https://docs.kernel.org/locking/index.html"]
---

# Threads & Concurrency

## Summary
A thread is a schedulable execution context that shares an address space, file descriptors, and signal handlers with other threads of the same process. Linux implements threads with the clone(2) syscall and the NPTL library, using a 1:1 user-thread-to-kernel-thread mapping.

## Details
- User-level threads multiplex onto kernel threads in userspace (green threads); kernel threads are the units the scheduler sees. NPTL gives each pthread a kernel thread.
- Threads share memory, open files, and working directory but keep private stacks, thread-local storage, and errno.
- Synchronization primitives include mutexes, condition variables, read-write locks, barriers, and spinlocks.
- Since POSIX 2008, pthread_mutex_t supports robust mutexes: if a thread dies while holding one, waiters get EOWNERDEAD instead of hanging forever.
- Futexes (fast user-space mutexes) are the kernel primitive under mutexes and semaphores: uncontended locks never enter the kernel.
- Data races are undefined behavior in C; tools like ThreadSanitizer detect them, and std::atomic or explicit locks are required for safe sharing.
- Forks in multithreaded programs are tricky: only the calling thread survives in the child, so mutexes may stay locked — atfork handlers help.

## Related
- [[wiki/os-shell/context-switching|Context Switching]] — thread switches are cheaper than process switches
- [[wiki/os-shell/semaphores|Semaphores]] — the counting primitive often paired with threads
- [[wiki/os-shell/process-scheduling|Process Scheduling]] — threads are the kernel's schedulable units
- [[wiki/os-shell/file-descriptors|File Descriptors]] — the shared table threads inherit
- [[wiki/concepts/working-memory|Working Memory]] — concurrency also matters for agent state machines
