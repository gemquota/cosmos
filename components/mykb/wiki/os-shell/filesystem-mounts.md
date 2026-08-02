---
type: "concept"
title: "Filesystem Mounts"
description: "mount/umount, mount points, fstab, and bind mounts"
tags: ["mount", "filesystem", "fstab", "bind-mounts", "namespaces"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://man7.org/linux/man-pages/man8/mount.8.html", "https://man7.org/linux/man-pages/man5/fstab.5.html"]
---

# Filesystem Mounts

## Summary
Mounting attaches a filesystem's root at a directory in an existing tree, making its contents reachable at that path. The mount table is the kernel's record of these attachments, and mount namespaces let different processes see different trees.

## Details
- mount(8) is the userspace front end to the mount(2) syscall; umount detaches, and the kernel refuses to unmount busy filesystems.
- /etc/fstab lists automatic mounts with six fields: device, mount point, type, options, dump flag, and fsck order.
- Common options include ro, noexec, nosuid, nodev, noatime, and bind; relatime is the modern default atime behavior.
- Bind mounts re-expose an existing directory at another path with the same inode tree — the tool behind chroot setups and container rootfs mounts.
- Overlay mounts combine lower and upper layers into one view, the basis of container images and live system recovery.
- Mount propagation flags (shared, slave, private, unbindable) control whether mounts replicate across namespaces.
- /proc/mounts and findmnt(8) show the live table; systemd mounts via .mount units with proper dependency ordering.

## Related
- [[wiki/os-shell/filesystem-types|Filesystem Types]] — what gets mounted where
- [[wiki/os-shell/linux-namespaces|Linux Namespaces]] — mount namespaces isolate trees per process
- [[wiki/os-shell/filesystem-hierarchy|Filesystem Hierarchy]] — where mount points conventionally live
- [[wiki/os-shell/block-devices-and-partitions|Block Devices & Partitions]] — the devices fstab refers to
- [[wiki/os-shell/containers-vs-vms|Containers vs VMs]] — mount and overlay tricks at the core of containers
