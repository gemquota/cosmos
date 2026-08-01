---
type: "concept"
title: "Permissions Model"
description: "The Unix read/write/execute model for files and directories, plus ownership"
tags: ["permissions", "unix", "security", "files"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
---

# Permissions Model

## Summary
Unix permissions grant read, write, and execute to three classes — owner, group, others — stored as mode bits (`rwxr-xr--`). Directories interpret the bits differently: execute means traverse.

## Details
- `chmod`, `chown`, and `chgrp` manage modes and ownership; octal notation (755) is the shorthand.
- The model also includes setuid/setgid, sticky bits, and ACLs as extensions.
- RSIS3 relevance: file permissions protect the wiki and its secrets from misreads.

## Related
- [[wiki/os-shell/users-and-groups|Users and Groups]] — permissions are granted to users and groups
- [[wiki/os-shell/umask|Umask]] — the default mode applied at file creation
- [[wiki/os-shell/filesystem-hierarchy|Filesystem Hierarchy]] — each hierarchy node has permissions
- [[wiki/security/rbac|RBAC]] — the larger authorization framework
- [[wiki/security/secrets-management|Secrets Management]] — permissions protect secrets at rest
