---
type: "concept"
title: "Backup Tools: restic & Borg"
description: "Deduplicating encrypted backups with restic and Borg"
tags: ["restic", "borg", "backup", "encryption"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Backup Tools: restic & Borg

## Summary
restic and Borg are deduplicating, encrypted backup tools for filesystem trees. Both split data into chunks, store each chunk once, encrypt with a user key, and support retention-based pruning; restic targets heterogeneous remote backends (S3, B2, SFTP, local), while Borg is optimized for local or SSH destinations with its own append-only repo format.

## Details
- Mechanism: content-defined chunking splits files into variable-size blocks, so a small edit to a large file changes only the affected chunks; chunk indexes and snapshots let a restore reconstruct any point in time; encryption keys stay local, so the remote never sees plaintext names or contents.
- Concrete example: `restic backup ~/data --repo s3:...` followed by `restic forget --keep-daily 7 --keep-monthly 6 --prune`; Borg uses `borg create repo::host-{now} ~/data` and `borg prune`. Both are cron-friendly and support pre/post hooks for consistent database dumps.
- Failure modes: losing the repository password makes the backup unrecoverable — store the key in a secrets manager and test a restore from a cold environment; interrupted prunes or pruning bugs can waste space or corrupt the index, so run `restic check` or `borg check`; backing up a live database without a coherent snapshot captures torn state, so back up a consistent dump or snapshot first.
- Tradeoffs: dedup makes these tools cheap for versioned file trees but less useful for already-compressed media; encryption and chunking add CPU cost; both are single-writer, so concurrent backups to one repo need locking. Borg's dedup and compression are tighter for local repos; restic wins on backend variety and cloud object-storage friendliness.
- Operational notes: test restores from the actual remote, monitor repo growth, and set retention before the repo balloons past budget.
- RSIS3/mykb relevance: restic/Borg are the tooling layer for the wiki's 3-2-1 strategy — an encrypted, deduplicated snapshot of the markdown store gives RSIS3 a recoverable memory that survives machine loss.

## Related
- [[wiki/shell-environment/unix-text-processing-tools|Unix Text Processing Tools]] — related coverage in the same cluster
- [[wiki/devops-infra/backup-strategies-3-2-1|Backup Strategies: 3-2-1]] — related coverage in the same cluster
- [[wiki/os-shell/checksums-and-hashing-tools|Checksums & Hashing]] — related coverage in the same cluster
- [[wiki/devops-infra/fault-injection-tools|Fault Injection Tools]] — related coverage in the same cluster
- [[wiki/devops-infra/kubernetes-control-plane|Kubernetes Control Plane]] — related coverage in the same cluster
- [[wiki/devops-infra/observability-pillars|Observability Pillars]] — related coverage in the same cluster
- [[wiki/syntheses/knowledge-acquisition-workflow|Knowledge Acquisition Workflow]] — how stubs grow into full articles in mykb
- [[wiki/syntheses/mykb-acquisition-curation-and-practices|Acquisition, Curation & Practices]] — the curation loop this stub belongs to
