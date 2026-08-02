---
type: "concept"
title: "Block Devices & Partitions"
description: "Disk devices, MBR/GPT partition tables, and device nodes"
tags: ["block-devices", "partitions", "gpt", "mbr", "devices"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://man7.org/linux/man-pages/man4/sd.4.html", "https://man7.org/linux/man-pages/man8/fdisk.8.html"]
---

# Block Devices & Partitions

## Summary
Block devices are the kernel's interface to storage that transfers data in fixed-size blocks — hard drives, SSDs, NVMe, and USB sticks. Partition tables divide a disk into regions, and device nodes under /dev give user space a path to each.

## Details
- The sd driver names SATA/USB/SAS disks /dev/sda, /dev/sdb; NVMe uses /dev/nvme0n1, and partitions append numbers like /dev/sda1.
- Device nodes carry a major number (driver) and minor number (unit/partition); udev creates them dynamically from sysfs events.
- MBR (DOS) partition tables allow four primary partitions or three plus an extended partition with logicals, and cap disk addressing at 2 TiB.
- GPT is the modern standard: up to 128 partitions by default, a backup table at the end of disk, CRC protection, and GUIDs for partition types.
- Partition tools include fdisk, gdisk, parted, and sgdisk; changes need a kernel re-read (partprobe) and mounted partitions must be resized offline.
- The block layer adds queues, I/O schedulers, and integrity checks; bcache, LVM, and dm-crypt stack virtual block devices on top.
- lsblk, blkid, and /proc/partitions give a compact view of devices, UUIDs, and filesystem labels.

## Related
- [[wiki/os-shell/filesystem-mounts|Filesystem Mounts]] — mounting a filesystem from a partition
- [[wiki/os-shell/filesystem-types|Filesystem Types]] — what mkfs writes inside a partition
- [[wiki/os-shell/device-drivers|Device Drivers]] — how block majors/minors map to drivers
- [[wiki/os-shell/procfs-and-sysfs|procfs & sysfs]] — where device state is exposed
- [[wiki/os-shell/swap-space|Swap Space]] — swap partitions are block devices too
