---
type: "concept"
title: "ZFS Features & Snapshots"
description: "Copy-on-write pools, checksums, snapshots, and scrubs"
tags: ["zfs", "filesystem", "snapshots", "storage"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# ZFS Features & Snapshots

## Summary
ZFS is a copy-on-write (CoW) filesystem and volume manager in one: it pools disks, checksums every block, snapshots instantly, scrubs for silent corruption, and offers RAID-Z (its own parity scheme). Originally from Solaris, it now runs on Linux (OpenZFS) and FreeBSD, and its snapshot + send/receive model is widely considered the best-in-class backup primitive in the storage world.

## Details
- Mechanism: ZFS is a transactional CoW filesystem: writes go to new blocks, metadata updates are batched into transactions that are atomically committed, so the filesystem is always consistent (no fsck) and a snapshot is just a read-only reference to a previous transaction group — nearly free to create. Every block has a checksum (fletcher4 or sha256 by default), and ZFS verifies it on read, returning the *known-bad* data with an error rather than silently corrupt data; on redundant vdevs (mirror, RAID-Z), a read error triggers an automatic rebuild of the bad block from the healthy copy. `zfs snapshot pool/fs@snap`, `zfs list -t snapshot`, and `zfs rollback` manage point-in-time state; `zfs send`/`zfs receive` stream snapshots (and incremental diffs) to another pool or host; `zfs scrub` walks the pool verifying all checksums.
- Concrete examples: a home NAS creates `zfs snapshot tank/data@$(date +%F)` nightly and `zfs send -i` incrementals to an external disk; a virtualization host uses ZFS for VM disk images with snapshots before every upgrade; `zpool scrub` finds and repairs silent bit rot on aging disks; `zfs set compression=lz4 tank/data` shrinks data with near-zero CPU cost; `zpool status` shows health and `zpool import` recovers a pool after a host change.
- Failure modes: the classic failures are RAM hunger (ZFS uses a large ARC cache; on hosts with little RAM, default `zfs_arc_max` can starve applications), RAID-Z write amplification and the inability to grow a RAID-Z vdev by adding one disk (you add whole vdevs, not disks — a planning trap), and snapshot accumulation: snapshots share blocks, but a changing dataset grows them, and an overflowing pool where snapshots hold the space hostage until they are pruned. Send/receive stream mismatches (feature-flag differences between versions) and pool import confusion after disk reordering round out the operational risks.
- Operational tradeoffs: ZFS trades RAM, CPU (checksums/compression), and operational vocabulary (vdevs, pools, datasets, snapshots, scrubs) for data integrity, instant snapshots, and flexible volumes that no traditional filesystem matches. The tradeoff is real: on small or underpowered hosts, ext4/XFS plus a backup tool may serve better; on storage-centric machines where data integrity and snapshots matter, ZFS is hard to beat. The practice rules: size RAM deliberately (1GB ARC per TB is a rough heuristic, tunable), plan vdev growth ahead, prune snapshots automatically, scrub on a schedule, and test `zfs send` recovery before you need it.
- RSIS3/mykb relevance: ZFS snapshots are the storage mirror of MyKB's snapshot discipline — cheap point-in-time states with incremental transfer and verified integrity; the scrub concept (proactively validate every block) is exactly what the wiki's snapshot verification scripts do for the corpus.

## Related
- [[wiki/os-shell/btrfs-features-and-limitations|Btrfs Features & Limitations]] — related coverage in the same cluster
- [[wiki/os-shell/kernel-architecture|Kernel Architecture]] — related coverage in the same cluster
- [[wiki/os-shell/memory-management-paging|Memory Management & Paging]] — related coverage in the same cluster
- [[wiki/syntheses/knowledge-acquisition-workflow|Knowledge Acquisition Workflow]] — how stubs grow into full articles in mykb
- [[wiki/syntheses/mykb-acquisition-curation-and-practices|Acquisition, Curation & Practices]] — the curation loop this stub belongs to
