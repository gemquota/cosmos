---
type: "entity"
title: "XFS & ext4"
description: "The two battle-tested Linux filesystems and when to pick each"
tags: ["xfs", "ext4", "filesystem", "linux"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# XFS & ext4

## Summary
ext4 and XFS are the two battle-tested Linux filesystems for general-purpose storage, and the choice between them is mostly about workload shape. ext4 is the conservative default — mature, ubiquitous, resizable both ways — while XFS excels at large files, high parallelism, and big filesystems, at the cost of not being shrinkable. For most workloads either works; for large or highly parallel storage, XFS pulls ahead.

## Details
- Mechanism: ext4 is the evolution of ext3/ext2 — a journaled, extent-based filesystem with delayed allocation, online resize (grow and shrink), and 32-bit-or-64-bit addressing (up to 1 EiB, though 16 TiB is the common practical per-filesystem ceiling without 64-bit features). XFS is a high-performance 64-bit filesystem designed for parallelism: allocation groups (AGs) partition the filesystem into independent regions so multiple writers allocate concurrently without fighting over one bitmap; its extent-based B+tree allocation and delayed allocation handle large files and heavy concurrency well, and it supports online grow (but *not* shrink). Both support journaling, though ext4 is famous for its many mount options (data=ordered, noatime, discard) and XFS for its robustness track record on large servers.
- Concrete examples: a desktop Linux install uses ext4 as the default; a big media or backup volume (many TB of large files) uses XFS; a high-IOPs database or file server with many concurrent writers picks XFS for its AG-based parallelism; a VM image store that must shrink periodically stays with ext4 (or a thin-provisioned layer); `mkfs.xfs`/`mkfs.ext4` create them, `xfs_growfs`/`resize2fs` grow them, and `xfs_repair`/`e2fsck` repair them — always unmounted or read-only.
- Failure modes: the classic failures are assuming shrinkability (XFS cannot be shrunk, period — mis-sizing a volume is a painful migration), power-loss exposure differences (both journal metadata, but ext4's delayed allocation can lose recently written file data on crash unless `data=ordered` + fsync discipline is followed — the same is true of XFS), and feature mismatches: enabling ext4's 64-bit or bigalloc features changes compatibility, and XFS's realtime subvolumes are a niche with their own failure modes. Online-resize mistakes and running without `noatime` on busy filesystems add avoidable I/O.
- Operational tradeoffs: both are stable and supported by every Linux distribution; ext4's advantages are flexibility (shrink, ubiquitous tooling, battle-tested defaults) while XFS's are scalability (large filesystems, high concurrency, large files). The tradeoff is largely operational: choose ext4 when you may need to shrink or want maximum familiarity, XFS when size or parallelism dominates. The practice rules: size volumes with headroom (grow is easy, shrink is not), use `noatime` for hot filesystems, back up with tools that preserve xattrs and structure, and match the filesystem to the workload's file-size and concurrency profile rather than to fashion.
- RSIS3/mykb relevance: the wiki corpus is many small files (a workflow that suits either, slightly favoring ext4's metadata handling) while snapshot archives are large sequential files (XFS territory); matching the filesystem to the data shape is the same sizing discipline RSIS3 applies to registry and checkpoint storage.

## Related
- [[wiki/os-shell/kernel-architecture|Kernel Architecture]]
- [[wiki/os-shell/memory-management-paging|Memory Management & Paging]]
