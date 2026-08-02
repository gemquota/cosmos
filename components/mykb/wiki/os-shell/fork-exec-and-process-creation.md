---
type: "concept"
title: "Fork, Exec & Process Creation"
description: "fork/exec semantics, PID handling, and process-creation paths"
tags: ["fork", "exec", "processes", "pid", "posix-spawn"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://man7.org/linux/man-pages/man2/fork.2.html", "https://man7.org/linux/man-pages/man3/posix_spawn.3.html"]
---

# Fork, Exec & Process Creation

## Summary
Unix creates processes in two steps: fork(2) clones the calling process, and execve(2) replaces the clone's image with a new program. The split gives the parent a chance to configure the child — redirecting file descriptors, setting environment, changing privileges — before the new program starts.

## Details
- fork returns 0 to the child and the child's PID to the parent; the child starts with a copy of the parent's memory, file-descriptor table, and signal dispositions.
- Memory copying is lazy: pages are shared copy-on-write, so fork is cheap until either side writes.
- execve discards the old image, loads the new executable, and preserves open fds, environment, and PID; on success it never returns.
- The kernel builds the new process around task_struct, sets up the stack and entry point, and uses a binary handler (ELF, script shebang, or interpreter).
- vfork shares the parent's address space for immediate exec; clone(2) is the general primitive behind both fork and pthread_create.
- Children must be reaped with wait/waitpid; otherwise they become zombies and leak PIDs, which are a finite kernel resource.
- posix_spawn(3) packages fork+exec for environments where fork is expensive or unavailable, and glibc optimizes it on Linux.

## Related
- [[wiki/os-shell/copy-on-write|Copy-on-Write]] — the mechanism that makes fork cheap
- [[wiki/os-shell/process-management|Process Management]] — the full lifecycle from fork to reaping
- [[wiki/os-shell/file-descriptors|File Descriptors]] — the inherited table children configure before exec
- [[wiki/os-shell/exit-codes|Exit Codes]] — what wait() reports when a child finishes
- [[wiki/os-shell/daemon-processes|Daemon Processes]] — double-fork is a creation idiom
