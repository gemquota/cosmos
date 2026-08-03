---
type: "concept"
title: "FUSE & User-Space Filesystems"
description: "Filesystems implemented in userspace via the FUSE kernel module"
tags: ["fuse", "filesystem", "userspace", "linux"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# FUSE & User-Space Filesystems

## Summary
FUSE (Filesystem in Userspace) is a Linux kernel module that lets a normal userspace program implement a filesystem: the kernel forwards VFS operations — lookup, read, write, readdir — to a daemon over a device (`/dev/fuse`), and the daemon answers with data and metadata. This is how SSHFS, s3fs, gocryptfs, and virtually every "cloud drive" desktop app mount their stores as ordinary directories.

## Details
- Mechanism: a FUSE program mounts at a path with `fuse_main` or a binding (python-fuse, go-fuse), registering handlers for the core operations. When a process opens `/mnt/cloud/photo.jpg`, the kernel sends a FUSE request to the daemon, which performs its own I/O (an S3 GET, an SSH read, a decryption) and returns the result; the kernel caches the response per its caching settings. Mount options and `direct_io`, `allow_other`, and `auto_cache` shape the semantics; the daemon must implement `getattr`, `readdir`, and `open`/`read`/`write` at minimum for a useful read-write filesystem.
- Concrete examples: SSHFS mounts a remote directory over SSH with no server-side software; s3fs and rclone present object storage as a tree; gocryptfs and EncFS provide transparent encryption at the file level; AppImage and Flatpak use FUSE mounts to present application images as mounted filesystems; a wiki tool could expose a search index as a FUSE view where filenames are query results.
- Failure modes: the classic failures are performance — every operation crosses a kernel/userspace boundary, and naive implementations produce 10-100x slowdowns, especially for metadata-heavy workloads (small files, directory listings), which is why caching (`kernel_cache`, attribute timeout) and `readahead` matter — and reliability: if the daemon crashes or hangs, the mount becomes a black hole where `ls` blocks indefinitely (unmounting needs `fusermount -u` or `umount -l`). Cache coherence with the real source (another process writing the same S3 object) and security (the `allow_other` mount option exposes the filesystem to all users unless `user_allow_other` is carefully configured) are the other recurring traps.
- Operational tradeoffs: FUSE's value is turning arbitrary backends into POSIX-compatible interfaces with zero client changes; the cost is a performance ceiling and a daemon that must be supervised like a service. The practice rules: enable kernel-side caching aggressively for read-heavy workloads, monitor the daemon's health (a hung FUSE process is a hung mount), prefer `direct_io` only when coherence demands it, and never expose a FUSE mount with `allow_other` on shared systems without authentication. RSIS3/mykb relevance: mounting the wiki corpus or search index via FUSE would let existing shell tooling treat the knowledge base as files; the tradeoff — POSIX convenience versus daemon reliability — is the same one RSIS3 weighs when wrapping services behind familiar interfaces.

## Related
- [[wiki/os-shell/journaling-filesystems|Journaling Filesystems]]
- [[wiki/os-shell/copy-on-write-filesystems|Copy-on-Write Filesystems]]
- [[wiki/os-shell/disk-partitioning-and-filesystems|Disk Partitioning & Filesystems]]
- [[wiki/os-shell/immutable-filesystems|Immutable Filesystems]]
- [[wiki/syntheses/knowledge-acquisition-workflow|Knowledge Acquisition Workflow]] — how stubs grow into full articles in mykb
- [[wiki/syntheses/mykb-acquisition-curation-and-practices|Acquisition, Curation & Practices]] — the curation loop this stub belongs to
