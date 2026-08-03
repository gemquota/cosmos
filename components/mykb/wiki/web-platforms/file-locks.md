---
type: "concept"
title: "File Locking"
description: "Advisory locks coordinating concurrent file access"
tags: ["filesystem", "concurrency", "reliability", "practice"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# File Locking

## Summary

File locks coordinate access so concurrent processes do not interleave writes or read torn files. Advisory locking (flock) and OS-level atomic primitives each trade convenience for safety; the web world mostly needs atomic writes plus a lock file.

## Details
- Mechanism: flock locks a file descriptor with LOCK_SH/LOCK_EX/LOCK_NB — advisory: cooperating processes must opt in, and locks are released on close or process exit (no stale-lock problem). POSIX record locks (fcntl) are per-process and vanish on close of any fd, a notorious footgun.
- Concrete example: a build script takes an exclusive flock on build.lock before writing artifacts, so parallel CI jobs serialize; a wiki sync daemon locks its state file while rotating logs. Advisory locks fail open — a non-cooperating process ignores them, so critical paths add atomic rename as the real guarantee.
- Failure modes: lock files surviving crashes (mitigate with flock which dies with the fd, or O_EXCL creation with staleness checks); deadlocks from acquiring locks in different orders; blocking forever when a holder hangs (use LOCK_NB with timeout); and locking across NFS/network filesystems where semantics degrade.
- Operational tradeoffs: file locks are simple and local but do not scale to multi-host coordination — there you need a lease service or database lock. Prefer atomic temp-file-and-rename for content writes and reserve locks for exclusive sections (log rotation, migrations).
- RSIS3/mykb relevance: the wiki daemon uses flock around state-file updates and atomic renames for note writes, preventing torn reads during concurrent graph builds.
- Advisory semantics: remember flock is cooperative — it stops cooperating processes, not malicious or buggy ones; pair it with atomic writes so a non-cooperating writer cannot produce a torn file.
- Timeout policy: always acquire with LOCK_NB plus a retry/backoff instead of blocking forever; a hung holder otherwise stalls the whole pipeline with no way to time out.

## Related
- [[wiki/api-protocols/web-security-owasp|Web Security (OWASP)]]
- [[wiki/web-platforms/race-conditions-web|Race Conditions on the Web]]
- [[wiki/web-platforms/toctou|TOCTOU Vulnerabilities]]
- [[wiki/web-platforms/atomic-writes|Atomic Writes]]
- [[wiki/api-protocols/idempotency|Idempotency]]
- [[wiki/api-protocols/optimistic-concurrency|Optimistic Concurrency]]
- [[wiki/web-platforms/web-apis|Web APIs]]
