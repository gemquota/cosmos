---
type: "concept"
title: "Btrfs Features & Limitations"
description: "Subvolumes, snapshots, and RAID on the copy-on-write filesystem"
tags: ["btrfs", "filesystem", "snapshots", "linux"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Btrfs Features & Limitations

## Summary
Btrfs is a modern copy-on-write (CoW) filesystem for Linux that bundles subvolumes, snapshots, checksums, compression, and RAID into one tool. Its headline promise — instant snapshots and self-healing checksums on commodity hardware — made it the default on Fedora and openSUSE, while its RAID reliability history has made it a controversial choice for production arrays.

## Details
- Mechanism: because writes never overwrite existing blocks (copy-on-write), a snapshot is nearly free: it is just a new root that shares all existing blocks until they change, after which only the changed blocks are duplicated. Subvolumes are independently mountable trees with their own roots, which is how `@` and `@home` split a root filesystem. Every block carries a checksum (crc32c by default), so read errors and silent corruption are detected and, on RAID1-like profiles, repaired from the other copy.
- Concrete examples: `btrfs subvolume snapshot /mnt/btrfs/@ /mnt/btrfs/@snap-$(date +%F)` creates an instant backup; `snapper` automates hourly/daily snapshots that make system updates rollbackable; `btrfs send | btrfs receive` streams snapshot diffs to another disk for incremental backup; compress=zstd on a database directory shrinks data and often speeds reads; `btrfs balance` re-arranges extents after profile changes.
- Failure modes: the cautionary tales are RAID5/RAID6 parity mode — historically vulnerable to write-hole and RST (RAID stripe tree) bugs that could corrupt data on power loss, so it is not recommended for data you cannot lose — and full-disk exhaustion during CoW operations: snapshots share blocks, but heavy write workloads (databases, VMs) fragment extents and can run out of space unless `nodatacow` is set on those files. Unbalanced multi-device arrays need periodic `balance`, and a nearly-full btrfs filesystem degrades differently than ext4, with writes failing while space "exists" as shared extents.
- Operational tradeoffs: btrfs trades the simplicity and mature RAID of ext4/XFS for integrated snapshots, checksums, compression, and resizing that most other Linux filesystems lack; the costs are CPU overhead from checksums and CoW, the RAID5/6 caveats, and a larger operational vocabulary (subvolumes, balance, scrub, send/receive). The pragmatic posture: excellent for workstations and root filesystems with snapper-style snapshots; acceptable for single-disk or RAID1 servers; avoid parity RAID for production data unless you accept the risk and test power-loss behavior.
- RSIS3/mykb relevance: the snapshot-and-send model is the filesystem analog of MyKB's snapshot discipline — cheap, shareable point-in-time states with incremental transfer — and the same tradeoff (copy-on-write sharing vs. space accounting) appears in the knowledge graph's checkpoint design.

## Related
- [[wiki/os-shell/zfs-features-and-snapshots|ZFS Features & Snapshots]]
- [[wiki/os-shell/kernel-architecture|Kernel Architecture]]
- [[wiki/os-shell/memory-management-paging|Memory Management & Paging]]
- [[wiki/syntheses/knowledge-acquisition-workflow|Knowledge Acquisition Workflow]] — how stubs grow into full articles in mykb
- [[wiki/syntheses/mykb-acquisition-curation-and-practices|Acquisition, Curation & Practices]] — the curation loop this stub belongs to
