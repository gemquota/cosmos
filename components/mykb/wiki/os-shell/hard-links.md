---
type: "concept"
title: "Hard Links"
description: "Link counts, same-inode aliases, and limitations"
tags: ["hard-links", "inodes", "filesystem", "ln"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://man7.org/linux/man-pages/man2/link.2.html", "https://man7.org/linux/man-pages/man1/ln.1.html"]
---

# Hard Links

## Summary
A hard link is an additional directory entry pointing at the same inode as another name. Both names refer to the identical file — same data, same permissions, same timestamps — and the file is only deleted when the last link is removed.

## Details
- ln old new creates a hard link; after that, ls -l shows a link count of 2 for the inode, visible via stat st_nlink.
- All hard links share the inode, so editing through any name changes what every name shows; there is no "original."
- Hard links cannot cross filesystems, because the inode number is only meaningful within one filesystem, and cannot link directories.
- unlink(2) removes a name and decrements the count; the inode and data survive until the count reaches zero and all open handles close.
- A file with open handles can be unlinked entirely — the space is freed on close, a classic trick for temp files.
- find -samefile and ls -i reveal sharing; backup tools deduplicate by inode when preserving hard links.
- Hard links differ from symlinks, which are separate small files storing a path, can cross filesystems, and dangle when the target is removed.

## Related
- [[wiki/os-shell/inodes-and-filesystem-metadata|Inodes & Filesystem Metadata]] — link counts live in the inode
- [[wiki/os-shell/symlinks|Symlinks]] — the path-based alternative with different semantics
- [[wiki/os-shell/filesystem-mounts|Filesystem Mounts]] — why links cannot cross device boundaries
- [[wiki/os-shell/rsync-synchronization|rsync]] — preserving hard links during backup
- [[wiki/os-shell/file-descriptors|File Descriptors]] — open handles keep unlinked files alive
