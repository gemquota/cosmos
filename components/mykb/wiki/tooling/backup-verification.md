---
type: "concept"
title: "Backup Verification"
description: "Proving that backups can actually be restored"
tags: ["backups", "verification", "disaster-recovery", "testing"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Backup Verification

## Summary
Backup verification restores a backup into a scratch environment and checks the data — the only way to know a backup is real. Unverified backups are the classic discovery of disaster-recovery stories.

## Details
- Restore to a separate environment and compare checksums, row counts, or sampled data.
- Automate verification on a schedule; restore drills are verification with humans.
- Verify integrity (hashes, test reads) even for backups you do not fully restore.
- mykb relevance: the wiki archive restores to a scratch dir and diffs the tree quarterly.

## Related
- [[wiki/tooling/restore-drills|Restore Drills]]
- [[wiki/tooling/backup-types|Backup Types]]
- [[wiki/compositions/backup-and-restore|Backup and Restore]]
- [[wiki/communities/checksums|Checksums]]
- [[wiki/tooling/immutability-backups|Immutability Backups]]
