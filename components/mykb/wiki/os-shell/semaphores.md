---
type: "concept"
title: "Semaphores"
description: "Counting and binary semaphores, mutex vs semaphore roles"
tags: ["semaphores", "synchronization", "ipc", "mutex"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://man7.org/linux/man-pages/man7/sem_overview.7.html", "https://man7.org/linux/man-pages/man2/semget.2.html"]
---

# Semaphores

## Summary
A semaphore is a kernel- or library-maintained counter with two atomic operations: wait (decrement, blocking at zero) and post (increment, waking waiters). Counting semaphores manage pools of resources; binary semaphores behave like mutexes.

## Details
- POSIX unnamed semaphores (sem_init/sem_wait/sem_post) live in shared memory and work across threads or processes; named ones (sem_open) persist under /dev/shm.
- SysV semaphores (semget/semop) support sets of semaphores and atomic multi-operations; semctl(IPC_RMID) cleans them up.
- A mutex has ownership: only the locker may unlock. A binary semaphore can be posted by any process, which is why semaphores suit signaling.
- Classic pattern: a counting semaphore guards N resources; producers post, consumers wait, and the counter encodes availability.
- Implementation on Linux is futex-based, so uncontended wait/post never enter the kernel.
- Deadlock risk is real: lock ordering discipline and timeout variants (sem_timedwait) mitigate it.
- Kernel semaphores also exist internally (struct semaphore) for driver code, but userspace should prefer POSIX primitives.

## Related
- [[wiki/os-shell/threads-and-concurrency|Threads & Concurrency]] — where semaphores live in the sync toolbox
- [[wiki/os-shell/shared-memory|Shared Memory]] — the data semaphores protect
- [[wiki/os-shell/message-queues|Message Queues]] — producer/consumer coordination
- [[wiki/os-shell/file-locking|File Locking]] — file-level mutual exclusion
- [[wiki/software-engineering/type-systems|Type Systems]] — compile-time checks reduce runtime race risk
