---
type: "entity"
title: "rsync"
description: "Incremental sync, remote copies, and key flags"
tags: ["rsync", "sync", "backup", "remote"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://man7.org/linux/man-pages/man1/rsync.1.html"]
---

# rsync

## Summary
rsync synchronizes files between directories and hosts, transferring only what changed. Its delta algorithm compares file pieces and sends just the differences, making it the backbone of backups, mirrors, and deploys.

## Details
- Core flags: -a (archive: recurse, preserve perms/times/owner), -z compress, -v verbose, -h human sizes; combine as rsync -avz.
- --delete removes destination files absent from the source; --delete-excluded and --delete-delay refine the semantics for mirrors.
- --exclude/--include patterns prune trees; --exclude-from file scales for big configs; --dry-run (-n) previews without touching.
- Remote sync uses ssh by default: rsync -av src/ host:/dest/; the trailing slash on src copies contents, not the directory itself.
- --partial keeps incomplete files across interrupted transfers; --progress shows rate and percent; -P is both combined.
- Checksum mode (-c) compares content instead of size+mtime, catching changed files that kept timestamps; it costs I/O.
- Hard-link backups: --link-dest=prev makes --delete-style snapshots cheap by hard-linking unchanged files; --inplace avoids rename races.

## Related
- [[wiki/os-shell/ssh-and-remote-access|SSH & Remote Access]] — the transport rsync uses
- [[wiki/os-shell/hard-links|Hard Links]] — link-dest snapshot mechanics
- [[wiki/devops-infra/backups|Backups]] — rsync as a backup primitive
- [[wiki/os-shell/checksums-and-hashing-tools|Checksums & Hashing]] — -c content verification
- [[wiki/devops-infra/disaster-recovery|Disaster Recovery]] — restorable copies matter
