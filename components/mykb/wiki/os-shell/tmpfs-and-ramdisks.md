---
type: "concept"
title: "tmpfs & RAM Disks"
description: "Memory-backed filesystems and their use cases"
tags: ["tmpfs", "ramdisk", "memory", "filesystem"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://docs.kernel.org/filesystems/tmpfs.html", "https://man7.org/linux/man-pages/man5/tmpfs.5.html"]
---

# tmpfs & RAM Disks

## Summary
tmpfs is a memory-backed filesystem: its files live in page cache and can spill to swap, giving RAM speed for transient data. RAM disks (ramfs, brd) are the cruder ancestor. Linux uses tmpfs for /dev/shm, /run, and often /tmp.

## Details
- tmpfs pages are backed by the kernel's page cache and swap, so data survives pressure by being paged out rather than lost.
- Unlike ramfs, tmpfs enforces a size limit (default half of RAM) and refuses writes past it, which prevents runaway memory consumption.
- Everything in tmpfs is lost on reboot; use it only for ephemeral data such as sockets, pidfiles, locks, and build artifacts.
- /dev/shm hosts POSIX shared memory objects and is sized via mount options; /run holds runtime state like pidfiles and sockets.
- tmpfs supports most filesystem operations, including hard links and per-mount modes, but no journaling or persistence.
- Kernel tmpfs also backs anonymous shared memory (shmem) used by SysV shm and the memfd_create(2) seals mechanism.
- Modern builds (ninja ccache directories, Docker container layers in memory) use tmpfs to cut I/O latency.

## Related
- [[wiki/os-shell/shared-memory|Shared Memory]] — /dev/shm is tmpfs
- [[wiki/os-shell/filesystem-mounts|Filesystem Mounts]] — how tmpfs is attached
- [[wiki/os-shell/virtual-memory|Virtual Memory]] — the memory backing tmpfs pages
- [[wiki/os-shell/swap-space|Swap Space]] — where tmpfs pages overflow
- [[wiki/os-shell/filesystem-hierarchy|Filesystem Hierarchy]] — the standard /run and /dev/shm locations
