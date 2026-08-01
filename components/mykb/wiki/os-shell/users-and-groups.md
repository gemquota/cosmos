---
type: "concept"
title: "Users and Groups"
description: "The identity system of the OS: accounts with UIDs/GIDs that own processes and files"
tags: ["users", "groups", "identity", "unix"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
---

# Users and Groups

## Summary
Unix identifies accounts by user IDs (UID) and group IDs (GID); every process runs as some user, and every file belongs to a user and group. This identity is the substrate of the permissions model.

## Details
- `whoami`, `id`, and `groups` inspect identity; `sudo` and `su` switch it.
- System users (daemons like nginx) run services with minimal privileges.
- RSIS3 relevance: the agent runs as a specific user; ownership mistakes break the wiki pipeline.

## Related
- [[wiki/os-shell/permissions-model|Permissions Model]] — permissions are attached to users and groups
- [[wiki/os-shell/process-management|Process Management]] — processes carry identity
- [[wiki/security/rbac|RBAC]] — authorization builds on OS identity
- [[wiki/os-shell/environment-variables|Environment Variables]] — identity and env define the process context
- [[wiki/devops-infra/backups|Backups]] — ownership drives backup access
