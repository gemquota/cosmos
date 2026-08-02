---
type: "concept"
title: "Filesystem Permissions & umask"
description: "Mode bits, ownership, and default permission masks"
tags: ["permissions", "umask", "filesystem", "security"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: [
  "https://man7.org/linux/man-pages/man7/inode.7.html",
  "https://www.gnu.org/software/coreutils/manual/html_node/File-permissions.html",
]
---

# Filesystem Permissions & umask

## Summary
Filesystem permissions control who can read, write, and execute files through mode bits, ownership, and ACLs. umask sets the default permissions for new files. Getting permissions right is fundamental to multiuser security and shared systems administration.

## Details
- Mode bits encode read/write/execute for owner, group, and others, plus setuid/setgid and sticky bits.
- The inode man page documents how permissions are stored and checked.
- umask filters permission bits for newly created files and directories.
- The GNU coreutils manual explains chmod semantics, symbolic and octal, precisely.
- The GNU coreutils manual explains chmod semantics precisely.
- In mykb, permissions connect to users/groups, capabilities, and SELinux.
- Setuid and sticky bits add special semantics that require careful auditing.
- ACL tools like setfacl manage per-user exceptions beyond the three classic classes.
- Kernel and userspace behavior meet here; the related process, memory, and filesystem articles provide the implementation detail.
- Tuning this behavior in production relies on the system monitoring and resource utilization articles of this cluster.

## Related
- [[wiki/os-shell/namespace-networking|Namespace Networking]]
- [[wiki/os-shell/kernel-modules-and-loading|Kernel Modules & Loading]]
- [[wiki/os-shell/filesystem-hierarchy|Filesystem Hierarchy]]
- [[wiki/os-shell/filesystem-mounts|Filesystem Mounts]]
