---
type: "concept"
title: "mdadm & LVM2"
description: "Linux software RAID and logical volume management tools"
tags: ["mdadm", "lvm", "raid", "linux"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# mdadm & LVM2

## Summary
mdadm and LVM2 are the two classic Linux storage layers that sit between raw disks and filesystems. mdadm implements software RAID (combining disks into arrays with redundancy and striping), and LVM2 provides logical volumes (pooling physical disks into volume groups and carving flexible logical volumes with snapshots and resizing). They compose naturally — RAID for redundancy, LVM for flexibility — and both are command-line arts that reward careful practice.

## Details
- Mechanism: mdadm assembles arrays from block devices: RAID0 stripes for speed, RAID1 mirrors for redundancy, RAID5/6 stripe with parity, RAID10 mirrors of stripes, and linear/RAID0 concats. An array is identified by its UUID and assembled with `mdadm --assemble --scan` (driven by `/etc/mdadm.conf`), and a superblock on each member records the array's identity. LVM layers on top: `pvcreate` marks disks as physical volumes, `vgcreate` pools them into a volume group, `lvcreate` carves logical volumes, and `lvextend`/`lvreduce`/`lvresize` resize them; `lvs`/`vgs`/`pvs` report the hierarchy. LVM snapshots are CoW (space grows as changed blocks are copied), which makes them cheap for backups but not free.
- Concrete examples: a home server mirrors two disks with `mdadm --create /dev/md0 --level=1 --raid-devices=2 /dev/sdb /dev/sdc`; a database host uses RAID10 for metadata-heavy IOPS; a virtualization host pools disks into a VG and hands thin-provisioned LVs to VMs; `lvconvert --type raid1` converts a mirrored LV to use the kernel RAID layer; after a disk fails, `mdadm --remove`/`--add` rebuilds the mirror while the system runs; `vgreduce`/`pvextend` repair a degraded VG after disk replacement.
- Failure modes: the classic failures are forgetting the metadata: a fresh `mdadm --create` on disks that were array members destroys the array (always check with `mdadm --examine` first); losing a RAID5/6 array to two simultaneous failures; LVM metadata corruption or a missing PV that makes the VG "not found" at boot (`vgscan`/`vgchange -ay`); thin-pool exhaustion which freezes all thin volumes; and snapshots that fill up and go invalid. Ordering at boot (LVM on top of mdadm) is another classic — the initramfs must assemble both.
- Operational tradeoffs: software RAID plus LVM is cheap, flexible, and entirely supported by the kernel — ideal for home servers, lab storage, and small deployments — at the cost of CPU overhead (parity computation on RAID5/6) and a steeper operational vocabulary than a hardware RAID controller or ZFS. The practice rules: record `mdadm.conf` and LVM metadata backups (`vgcfgbackup`), monitor array state (`/proc/mdstat`, `mdadm --monitor`) and send alerts, test boot-from-array in a VM before trusting it, and prefer ZFS/btrfs when you want integrated checksums and snapshots instead of layering.
- RSIS3/mykb relevance: layered storage with explicit metadata mirrors MyKB's layering — raw files, index, snapshots — where each layer's metadata must be backed up and reconstructable, and the failure discipline (detect, alert, rebuild) is exactly what the wiki's snapshot verification scripts encode.

## Related
- [[wiki/os-shell/kernel-architecture|Kernel Architecture]] — related coverage in the same cluster
- [[wiki/os-shell/memory-management-paging|Memory Management & Paging]] — related coverage in the same cluster
- [[wiki/syntheses/knowledge-acquisition-workflow|Knowledge Acquisition Workflow]] — how stubs grow into full articles in mykb
- [[wiki/syntheses/mykb-acquisition-curation-and-practices|Acquisition, Curation & Practices]] — the curation loop this stub belongs to
