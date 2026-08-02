---
type: "concept"
title: "File Descriptors"
description: "FD table, open file descriptions, and dup/close semantics"
tags: ["file-descriptors", "open-files", "dup", "io", "unix"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://man7.org/linux/man-pages/man2/open.2.html", "https://man7.org/linux/man-pages/man2/dup.2.html"]
---

# File Descriptors

## Summary
A file descriptor is an integer handle into a per-process table of open files. The descriptor is not the file itself: the kernel maintains a separate open file description holding the offset, status flags, and locks, so several descriptors can share one file position.

## Details
- The process fd table is indexed from 0; 0, 1, 2 conventionally mean stdin, stdout, and stderr, and new descriptors take the lowest free number.
- An open file description records the current file offset, access mode, and file status flags; dup(2) and dup2(2) create descriptors sharing the same description.
- fork(2) copies the fd table, so parent and child share offsets after fork — a classic source of interleaved-write bugs.
- The close-on-exec flag (FD_CLOEXEC, set with O_CLOEXEC) prevents accidental inheritance across execve, now the default in most programs.
- /proc/<pid>/fd symlinks reveal every open descriptor, and lsof(1) cross-references them to processes and paths.
- RLIMIT_NOFILE caps the table size; hitting "too many open files" means exhausting the limit, not the disk.
- Unix-domain sockets use descriptors to pass both data and other descriptors (SCM_RIGHTS) between processes.

## Related
- [[wiki/os-shell/stdin-stdout-stderr|Stdin, Stdout & Stderr]] — the three canonical descriptors
- [[wiki/os-shell/file-locking|File Locking]] — locks attach to descriptions and inodes
- [[wiki/os-shell/ulimit-and-resource-limits|Resource Limits]] — RLIMIT_NOFILE bounds the table
- [[wiki/os-shell/process-substitution|Process Substitution]] — shells create anonymous pipes as fds
- [[wiki/os-shell/unix-domain-sockets|Unix Domain Sockets]] — fd passing between processes
