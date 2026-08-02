---
type: "concept"
title: "Shared Memory"
description: "POSIX/SysV shm, mmap-based sharing, and synchronization needs"
tags: ["shared-memory", "ipc", "mmap", "shm", "synchronization"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://man7.org/linux/man-pages/man7/shm_overview.7.html", "https://man7.org/linux/man-pages/man2/shmget.2.html"]
---

# Shared Memory

## Summary
Shared memory is the fastest IPC: multiple processes map the same physical pages into their address spaces and read or write them directly, with no kernel copy. POSIX shared memory (shm_open + mmap) and System V shm (shmget/shmat) are the two classic Linux flavors.

## Details
- POSIX objects live in /dev/shm (a tmpfs), are opened by name, sized with ftruncate, and mapped with mmap; shm_unlink removes the name.
- SysV segments use keys, shmget for allocation, shmat/shmat for attachment, and shmctl IPC_RMID for removal; they survive until explicitly deleted.
- Because writes are unsynchronized by the kernel, processes must coordinate with semaphores, mutexes, or atomic operations to avoid races.
- The page cache deduplicates: several mappers of one object share frames, so multi-process databases and brokers get cheap communication.
- Anonymous shared mappings created before fork are inherited by children, a common pattern for worker pools.
- sysctl limits (kernel.shmmax, kernel.shmall) bound SysV segment sizes; /proc/sysvipc/shm lists live segments.
- Security note: shared memory bypasses file permissions after mapping, so access control happens at open time.

## Related
- [[wiki/os-shell/memory-mapped-files|Memory-Mapped Files]] — the mmap basis of POSIX shm
- [[wiki/os-shell/semaphores|Semaphores]] — the synchronization shared memory requires
- [[wiki/os-shell/tmpfs-and-ramdisks|tmpfs & RAM Disks]] — /dev/shm is tmpfs
- [[wiki/os-shell/message-queues|Message Queues]] — the copying alternative to shared memory
- [[wiki/os-shell/threads-and-concurrency|Threads & Concurrency]] — the same coordination problems in-process
