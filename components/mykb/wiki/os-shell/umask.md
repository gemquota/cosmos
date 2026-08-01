---
type: "concept"
title: "Umask"
description: "The default permission mask applied to every new file and directory"
tags: ["umask", "permissions", "defaults", "security"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
---

# Umask

## Summary
umask sets which permission bits are removed by default when files are created: `umask 022` yields 644 files and 755 directories. It is how a system enforces a baseline of privacy and shareability.

## Details
- The mask is subtracted from the creator's requested mode; `umask` shows or sets it.
- Security-sensitive scripts may tighten umask before writing temp files.
- RSIS3 relevance: wiki files created by agents inherit the harness umask.

## Related
- [[wiki/os-shell/permissions-model|Permissions Model]] — umask is the default of that model
- [[wiki/os-shell/users-and-groups|Users and Groups]] — umask interacts with ownership
- [[wiki/security/secrets-management|Secrets Management]] — private files need restrictive umasks
- [[wiki/os-shell/exit-codes|Exit Codes]] — script hygiene includes umask discipline
- [[wiki/os-shell/filesystem-hierarchy|Filesystem Hierarchy]] — default permissions apply across the hierarchy
- [[wiki/devops-infra/backups|Backups]] — default modes affect backup privacy
