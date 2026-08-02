---
type: "concept"
title: "Copy-on-Write Filesystems"
description: "Cheap snapshots and checksums via write-time copying"
tags: ["cow", "snapshots", "btrfs", "zfs"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: [
  "https://openzfs.org/wiki/Main_Page",
  "https://btrfs.wiki.kernel.org/index.php/Main_Page",
]
---

# Copy-on-Write Filesystems

## Summary
Copy-on-write filesystems never overwrite live data: updates go to new blocks, making snapshots cheap and integrity verifiable. ZFS and Btrfs are the flagship implementations. CoW is the design pattern behind modern storage features.

## Details
- On write, the filesystem copies the affected blocks, updates them, and atomically points metadata at the new version.
- Snapshots are just read-only references to old block trees, so they cost almost nothing until the underlying data actually changes.
- Checksums stored per block detect silent corruption, and scrub processes verify data over time.
- OpenZFS documents the feature set, from snapshots and clones to compression and deduplication.
- Btrfs offers subvolumes, send/receive replication, and integrated RAID.
- CoW affects performance: write amplification exists, but benefits like instant snapshots usually win for infrastructure.
- Kernel and userspace behavior meet here; the related process, memory, and filesystem articles provide the implementation detail.
- Tuning this behavior in production relies on the system monitoring and resource utilization articles of this cluster.

## Related
- [[wiki/os-shell/disk-partitioning-and-filesystems|Disk Partitioning & Filesystems]]
- [[wiki/os-shell/fuse-and-user-space-filesystems|FUSE & User-Space Filesystems]]
- [[wiki/os-shell/copy-on-write|Copy-on-Write]]
- [[wiki/os-shell/access-control-lists|Access Control Lists]]
