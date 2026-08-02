---
type: "concept"
title: "tar & Archiving"
description: "Archive creation, extraction, and stream semantics"
tags: ["tar", "archive", "backup", "gzip"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://man7.org/linux/man-pages/man1/tar.1.html"]
---

# tar & Archiving

## Summary
tar bundles files and directories into a single stream, preserving permissions, ownership, and timestamps. It is the standard transport format for source trees and backups, usually compressed with gzip, xz, or zstd.

## Details
- Core modes: -c create, -x extract, -t list, with -f FILE naming the archive; -v lists names as processed.
- Compression flags: -z gzip, -J xz, --zstd, -j bzip2; modern tar detects compression on read, so tar -xf file.tar.gz just works.
- tar cf - dir | ssh host 'tar xf -' streams a tree over the network without a temp file — the classic remote copy idiom.
- --exclude patterns, --exclude-from file, and -C DIR (change directory) control what lands in the archive.
- Incremental backups use --listed-incremental with a snapshot file; --diff or -d compares an archive against the filesystem.
- Extraction safety: --no-same-owner for untrusted archives, and --one-top-level to avoid dumping files into cwd.
- GNU tar keeps hard links and xattrs; --acls/--xattrs preserve ACLs, and --sparse keeps sparse files sparse.

## Related
- [[wiki/os-shell/compression-tools|Compression Tools]] — the codecs tar pipes through
- [[wiki/os-shell/rsync-synchronization|rsync]] — the streaming alternative for syncing
- [[wiki/os-shell/checksums-and-hashing-tools|Checksums & Hashing]] — verifying archives after transfer
- [[wiki/os-shell/ssh-and-remote-access|SSH & Remote Access]] — tar-over-ssh pipelines
- [[wiki/devops-infra/backups|Backups]] — archive strategy at scale
