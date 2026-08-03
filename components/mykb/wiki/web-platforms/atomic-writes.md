---
type: "concept"
title: "Atomic Writes"
description: "Replacing files via temp file and rename to avoid partial states"
tags: ["filesystem", "reliability", "data", "practice"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Atomic Writes

## Summary

Atomic writes make a file's new content visible all at once or not at all: write to a temp file, fsync, then rename over the target. Readers never observe a half-written state, which is the foundation of durable, crash-safe storage.

## Details
- Mechanism: write temp file in the same directory, fsync it, rename over the destination, then fsync the directory. Rename is atomic on POSIX filesystems, so any reader sees either the old or new content, never a mix; fsync ordering is what survives a power loss.
- Concrete example: a wiki engine saving a note writes components/mykb/wiki/note.md.tmp, flushes it, renames to note.md, and fsyncs the directory. A crash at any point leaves either the previous note or the complete new one — never a truncated file.
- Failure modes: skipping the temp-file step and writing in place can truncate on crash; renaming across filesystems is not atomic (use same-directory temps); forgetting the directory fsync can lose the rename itself on some filesystems; and atomicity does not extend to multi-file operations — a two-file update needs a journal or versioned directory.
- Operational tradeoffs: atomic writes cost an extra copy and fsync, so hot paths batch or accept the durability tax; they do not give you atomic read-modify-write — two writers still need a lock or compare-and-swap to avoid clobbering each other.
- RSIS3/mykb relevance: the wiki daemon and snapshot scripts write via temp-and-rename so concurrent readers (dashboard fetches, graph builds) never see partial notes; the same pattern protects state files in the rack during loop checkpoints.
- Cross-process note: atomic rename also coordinates writers — a last-writer-wins overwrite is atomic but not conflict-free; pair with locks or version checks where both writers must survive.
- Temp-file hygiene: write temp files in the destination directory and clean them on failure; cross-directory renames are not atomic.

## Related
- [[wiki/api-protocols/web-security-owasp|Web Security (OWASP)]]
- [[wiki/web-platforms/file-locks|File Locking]]
- [[wiki/web-platforms/race-conditions-web|Race Conditions on the Web]]
- [[wiki/web-platforms/toctou|TOCTOU Vulnerabilities]]
- [[wiki/api-protocols/idempotency|Idempotency]]
- [[wiki/api-protocols/optimistic-concurrency|Optimistic Concurrency]]
- [[wiki/web-platforms/web-apis|Web APIs]]
