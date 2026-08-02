---
type: "concept"
title: "File Locking"
description: "flock vs fcntl locks, advisory locking, and lock files"
tags: ["file-locking", "flock", "fcntl", "locks", "advisory"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://man7.org/linux/man-pages/man2/fcntl.2.html", "https://man7.org/linux/man-pages/man2/flock.2.html"]
---

# File Locking

## Summary
File locking coordinates concurrent access to shared files. Linux offers two main families: flock(2), the BSD-style whole-file lock, and fcntl(2) record locks, which are POSIX-style, per-process, and can target byte ranges.

## Details
- Both are advisory by default: cooperating processes must take the lock; only mandatory locks (largely unsupported on Linux) force kernel enforcement.
- flock locks are attached to the open file description, so dup'd descriptors and fork share the lock, and any close of the description releases it.
- POSIX fcntl locks are per-process and per-range; closing any fd for the file releases all of that process's locks, which surprises programmers.
- Open-file-description (OFD) locks, Linux-specific via F_OFD_SETLK, fix the close and fork semantics of classic POSIX locks.
- Lock files are the shell-friendly alternative: create with O_CREAT|O_EXCL or use mkdir; stale locks need explicit pid handling and staleness checks.
- flock(1) gives shell scripts a lock primitive, and daemons commonly flock a pidfile to guarantee single-instance behavior.
- NFS lock semantics differ (NLM/NSM or NFSv4 state), so cross-host locking requires care; distributed systems usually prefer leases in a database.

## Related
- [[wiki/os-shell/file-descriptors|File Descriptors]] — locks bind to descriptions and inodes
- [[wiki/os-shell/daemon-processes|Daemon Processes]] — single-instance pidfile locking
- [[wiki/os-shell/process-supervision|Process Supervision]] — restart loops need lock discipline
- [[wiki/os-shell/here-documents|Here Documents]] — shell redirection interacts with lock files
- [[wiki/data-storage/deduplication|Deduplication]] — concurrent writers need the same locking rigor
