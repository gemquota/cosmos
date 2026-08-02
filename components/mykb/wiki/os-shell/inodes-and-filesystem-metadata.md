---
type: "concept"
title: "Inodes & Filesystem Metadata"
description: "Inode contents, allocation, and stat data"
tags: ["inodes", "filesystem", "metadata", "stat"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://man7.org/linux/man-pages/man7/inode.7.html", "https://man7.org/linux/man-pages/man2/stat.2.html"]
---

# Inodes & Filesystem Metadata

## Summary
An inode is the on-disk record describing a file's identity and layout: its type, permissions, owner, timestamps, size, link count, and the blocks that hold its data. Directory entries are just names pointing at inodes, which is why hard links can create many names for one file.

## Details
- The inode stores mode (type and permissions), uid/gid, atime/mtime/ctime, size, block count, and pointers to data blocks or extents.
- stat(2) exposes these fields, and stat(1), ls -l, and find -printf read the same data; ctime changes on any metadata update, not just content edits.
- On ext4, inodes live in fixed-size inode tables per block group, created at mkfs time; the number caps total files, visible with df -i.
- Modern filesystems use extents (contiguous block runs) and may allocate data structures differently, but the POSIX stat contract stays the same.
- Deleting a file unlinks its name and decrements the link count; the inode and data are freed only when the count reaches zero and no process holds the file open.
- Special inodes exist for directories, symlinks (the target stored in the inode when short), device nodes, and sockets/FIFOs.
- btime (birth time) is available on ext4/btrfs via statx(2), extending the classic three timestamps.

## Related
- [[wiki/os-shell/hard-links|Hard Links]] — multiple names, one inode
- [[wiki/os-shell/filesystem-types|Filesystem Types]] — how each fs lays out inodes
- [[wiki/os-shell/permissions-model|Permissions Model]] — the mode bits stored in the inode
- [[wiki/os-shell/symlinks|Symlinks]] — the inode-based alternative to hard links
- [[wiki/os-shell/filesystem-mounts|Filesystem Mounts]] — mounting exposes inode trees at a path
