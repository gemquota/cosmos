---
type: "concept"
title: "Disk Partitioning & Filesystems"
description: "GPT and MBR layouts and how filesystems sit on partitions"
tags: ["partition", "filesystem", "gpt", "disk"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Disk Partitioning & Filesystems

## Summary
Disk partitioning divides a physical disk into addressable regions described by a partition table — the legacy MBR (master boot record) or the modern GPT (GUID partition table) — and each partition then hosts a filesystem. The partition table is the disk's top-level map; the filesystem is the structure inside a partition that stores files, directories, and metadata.

## Details
- Mechanism: MBR, from the 1980s, stores four primary partition entries in the first 512-byte sector, limits disks to 2 TiB, and has no checksums or backup copy — a corrupted MBR loses the whole map. GPT, part of the UEFI spec, uses 64-bit LBA addressing (supports disks far beyond 2 TiB), allows 128+ partitions, stores a protective MBR plus primary and backup GPT headers with CRC32 checksums, and requires UEFI boot on most systems (though BIOS can still boot GPT disks with special bootloaders). A filesystem (ext4, XFS, btrfs, NTFS) is then created inside a partition with `mkfs`, labeled and identified by UUID so mounts survive device reordering.
- Concrete examples: a modern Linux install uses GPT with an EFI System Partition (`vfat`), a root partition (ext4 or btrfs), and optionally swap; `lsblk` shows the layout (`sda1`, `sda2`); `/etc/fstab` mounts by `UUID=` so `/dev/sda` renaming does not break boot; `parted` or `gdisk` manipulate tables, and `growpart` + `resize2fs` extend a partition online after a cloud disk resize.
- Failure modes: the classic failures are mixing boot modes (a BIOS-installed system on GPT or UEFI-only firmware on MBR) causing "no bootable device", forgetting the ESP's required flags and FAT filesystem type, and misaligned partitions (starting at sector 63 in old tools) that cripple SSD performance — modern tools align to 1 MiB boundaries automatically. Resizing mistakes, deleting the wrong partition by `/dev/sdX` name, and losing the backup GPT header on a disk that had one partition removed are the data-loss classics; mounting by device name instead of UUID breaks after reordering.
- Operational tradeoffs: GPT is the right default for any modern disk — more partitions, larger disks, checksums, backup headers — with the only real cost being legacy BIOS boot compatibility; MBR survives only for ancient hardware and firmware. Inside partitions, the filesystem choice (journaling ext4/XFS, CoW btrfs/ZFS) trades features against operational complexity. The practice rules: GPT + UUID-based fstab + 1 MiB alignment, verify with `lsblk -f` before touching anything, and keep partition tables backed up with `sgdisk --backup`.
- RSIS3/mykb relevance: partitioning is the disk's registry — a structured map that must stay consistent or the whole system is unreadable; MyKB's wiki index plays the same role for articles, which is why index corruption and snapshot drift are treated as first-class failures.

## Related
- [[wiki/os-shell/journaling-filesystems|Journaling Filesystems]] — related coverage in the same cluster
- [[wiki/os-shell/copy-on-write-filesystems|Copy-on-Write Filesystems]] — related coverage in the same cluster
- [[wiki/os-shell/fuse-and-user-space-filesystems|FUSE & User-Space Filesystems]] — related coverage in the same cluster
- [[wiki/os-shell/immutable-filesystems|Immutable Filesystems]] — related coverage in the same cluster
- [[wiki/syntheses/knowledge-acquisition-workflow|Knowledge Acquisition Workflow]] — how stubs grow into full articles in mykb
- [[wiki/syntheses/mykb-acquisition-curation-and-practices|Acquisition, Curation & Practices]] — the curation loop this stub belongs to
