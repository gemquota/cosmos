---
type: "concept"
title: "Journaling Filesystems"
description: "Write-ahead journaling, ext4 modes, and crash recovery"
tags: ["journaling", "ext4", "filesystem", "crash-recovery", "xfs"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://docs.kernel.org/filesystems/ext4/index.html"]
---

# Journaling Filesystems

## Summary
A journal is a write-ahead log of filesystem changes: metadata updates are first recorded in the journal, then applied to the main structures. After a crash, the filesystem replays or discards journal entries, restoring consistency without a full filesystem scan.

## Details
- The journal is a reserved region on disk; a transaction is committed only after its journal records are durable, guaranteeing atomicity across crashes.
- ext4 supports three data modes: ordered (default, data blocks written before metadata commit), writeback (only metadata ordered), and journal (full data journaling, slowest but safest).
- ext3/ext4 write a commit block to signal transaction completion; replay after reboot applies or rolls back partial transactions.
- XFS uses a similar log with delayed allocation; Btrfs and ZFS take a different route with copy-on-write trees, so a journal is less central.
- Journaling trades write amplification for recovery speed: a dirty filesystem recovers in seconds instead of running a full fsck.
- Checksums protect journal entries against torn writes on disks that lie about flush completion.
- Unmounting cleanly stops the need for replay; forced mounts (errors=remount-ro) avoid compounding damage.

## Related
- [[wiki/os-shell/filesystem-types|Filesystem Types]] — which filesystems journal and how
- [[wiki/os-shell/block-devices-and-partitions|Block Devices & Partitions]] — the storage the journal lives on
- [[wiki/os-shell/filesystem-mounts|Filesystem Mounts]] — mount options that select journal mode
- [[wiki/os-shell/inodes-and-filesystem-metadata|Inodes & Filesystem Metadata]] — what journaling protects
- [[wiki/os-shell/checksums-and-hashing-tools|Checksums & Hashing]] — the integrity checks protecting journals
