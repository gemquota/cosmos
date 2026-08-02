---
type: "concept"
title: "Write-Ahead Log"
description: "Persisting intent before applying changes so recovery is possible"
tags: ["write-ahead-log", "durability", "databases", "recovery"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Write-Ahead Log

## Summary
The write-ahead log (WAL) records every intended change durably before the data pages change, so a crash can replay the log to a consistent state. It is how PostgreSQL, MySQL/InnoDB, and most durable systems guarantee atomicity and durability.

## Details
- Order matters: log the change, fsync the log, then apply to pages — replay fills any gap.
- WAL doubles as replication stream (PostgreSQL streaming replication reads it).
- Checkpointing bounds replay; the log itself needs rotation and archiving.
- mykb relevance: the wiki sync journal is a WAL that replays after a crash.

## Related
- [[wiki/compositions/idempotent-writes|Idempotent Writes]]
- [[wiki/compositions/backup-and-restore|Backup and Restore]]
- [[wiki/concepts/checkpoint-rollback|Checkpoint Rollback]]
- [[wiki/tooling/write-behind-cache|Write-Behind Cache]]
- [[wiki/tooling/consensus-algorithms|Consensus Algorithms]]
