---
type: "concept"
title: "Filesystem Types"
description: "ext4, XFS, Btrfs, ZFS, FAT features and tradeoffs"
tags: ["filesystems", "ext4", "xfs", "btrfs", "zfs"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://docs.kernel.org/filesystems/index.html"]
---

# Filesystem Types

## Summary
Linux supports a wide family of filesystems, each tuned for different tradeoffs between robustness, scalability, and features. The classic Linux choices are ext4 for general-purpose disks, XFS for large throughput, Btrfs and ZFS for snapshots and checksums, and FAT/exFAT for removable media compatibility.

## Details
- ext4 is the default for most distributions: journaled, extent-based, supports online defragmentation, and tolerates full disks reasonably well.
- XFS scales to very large filesystems with aggressive delayed allocation and parallel allocation groups, at the cost of some tail latency.
- Btrfs is a copy-on-write filesystem with subvolumes, snapshots, compression, and checksums; send/receive enables efficient backups.
- ZFS (OpenZFS) pools disks into zpools with raidz redundancy, checksums every block, and provides instant snapshots and clones.
- FAT32 and exFAT have no journal and no POSIX permissions, but are the compatibility lingua franca for cameras, USB sticks, and dual-boot setups.
- Flash-oriented choices include F2FS, which reduces write amplification for SSDs, and the overlayfs stack used by containers.
- Choosing involves durability (journal vs COW), feature needs (snapshots, dedup, encryption), and operational maturity; mkfs and mount flags tune the result.

## Related
- [[wiki/os-shell/journaling-filesystems|Journaling Filesystems]] — the crash-safety mechanism most of them use
- [[wiki/os-shell/filesystem-mounts|Filesystem Mounts]] — how any of these is attached to the tree
- [[wiki/os-shell/block-devices-and-partitions|Block Devices & Partitions]] — the storage beneath the fs
- [[wiki/os-shell/inodes-and-filesystem-metadata|Inodes & Filesystem Metadata]] — how metadata is stored per type
- [[wiki/os-shell/tmpfs-and-ramdisks|tmpfs & RAM Disks]] — the memory-backed exception
