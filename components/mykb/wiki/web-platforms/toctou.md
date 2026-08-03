---
type: "concept"
title: "TOCTOU Vulnerabilities"
description: "Time-of-check to time-of-use gaps in authorization and files"
tags: ["concurrency", "security", "filesystem", "attacks"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# TOCTOU Vulnerabilities

## Summary

Time-of-check to time-of-use (TOCTOU) is a race where a resource's state changes between a security check and the operation that relied on it — a file swapped after validation, a lock released between check and write. It undermines check-then-act code.

## Details
- Mechanism: code checks a condition (file is a regular file, path is inside root, lock is held, size is under limit) and later uses the resource, but another actor can change it in between; the window between check and use is the race. Classic targets: file uploads, symlink checks, quota enforcement, and authz checks followed by data access.
- Concrete example: an upload endpoint checks the destination path is inside /uploads, then another request replaces the path with a symlink before the write — the file lands outside; a backup tool checks disk space then writes, and concurrent writers exceed the limit. Fixes use atomic operations (rename, O_NOFOLLOW, open-then-fstat) instead of separate checks.
- Failure modes: checking and using different handles (path vs fd) so the object can change identity; caches keyed by checked values that are never re-validated; and locks acquired after the check instead of before, so the protected section still races.
- Operational tradeoffs: eliminating TOCTOU means designing operations to be atomic or handle-based rather than check-then-act; where unavoidable, re-verify after the operation and make failures loud. Document which invariants rely on atomicity so refactors cannot split them.
- RSIS3/mykb relevance: the wiki daemon's file operations open-then-verify and use atomic renames; this note records the invariants the loop must preserve in storage code.
- Audit pattern: look for check-then-use pairs in code review (stat, open, validate, write); each pair is a candidate TOCTOU and a design conversation about making the operation atomic.
- Filesystem note: prefer open-then-fstat over stat-then-open; the file descriptor is the object you will actually use.

## Related
- [[wiki/api-protocols/web-security-owasp|Web Security (OWASP)]]
- [[wiki/web-platforms/atomic-writes|Atomic Writes]]
- [[wiki/web-platforms/file-locks|File Locking]]
- [[wiki/web-platforms/race-conditions-web|Race Conditions on the Web]]
- [[wiki/api-protocols/idempotency|Idempotency]]
- [[wiki/api-protocols/optimistic-concurrency|Optimistic Concurrency]]
- [[wiki/web-platforms/web-apis|Web APIs]]
