---
type: "concept"
title: "Users and Groups"
description: "The identity system of the OS: accounts with UIDs/GIDs that own processes and files"
tags: ["users", "groups", "identity", "unix"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
---

# Users and Groups

## Summary
Unix identifies every account by a numeric user ID (UID) and group ID (GID): every process runs as some user, every file belongs to a user and a group, and every permission check is an identity check. `whoami`, `id`, and `groups` inspect identity, `sudo`/`su` switch it, and the whole permissions model hangs off this substrate.

## Details
- Mechanism: accounts are entries in `/etc/passwd` (username, UID, GID, home, shell) and groups in `/etc/group` (name, GID, member list); NSS (Name Service Switch) can back these with LDAP/SSSD in larger environments. A process's credentials are its real/effective/saved UIDs and its supplementary group list — the *effective* UID decides permission checks, which is why setuid binaries can escalate. `id` shows all of it: `uid=1000(alice) gid=1000(alice) groups=1000(alice),4(adm),27(sudo)`. Switching identity: `su` changes user in a new shell, `sudo` runs one command with another user's privileges (with a configurable policy in `/etc/sudoers`), and setuid/setgid bits elevate a binary's effective identity at exec time.
- Concrete examples: a daemon (nginx, postgres) runs as a dedicated system user with minimal privileges so a compromise of the service does not mean root; `sudo -u www-data php artisan ...` runs a command as the web user; `useradd -m -s /bin/bash alice` and `usermod -aG docker alice` manage accounts; files show `user:group` in `ls -l`, and `chown`/`chgrp` change ownership; `groups alice` lists membership; UID 0 is root and UID 65534 is typically `nobody`.
- Failure modes: the classic failures are ownership mistakes — files created by root are uneditable by the app user (`chown` fixes it; the opposite, a web directory owned by the web user but writable by all, is a defacement vector), and services that refuse to start because they cannot read their own config after a restore. UID reuse after account deletion re-owns old files to the new account. Group membership changes that do not propagate (a user must log out/in for new groups to apply to new processes), and running everything as root out of convenience — the single most common privilege mistake in systems administration.
- Operational tradeoffs: OS identity is coarse (whole-process, file-level) and cheap; fine-grained authorization (who may call which operation) is the job of RBAC and application layers, which build on OS identity for their user records and process boundaries. The practice rules: one service per system user with minimal privileges, never run daemons as root without a documented reason, use `sudo` with a tight sudoers policy instead of shared root passwords, and audit ownership (`find / -nouser`) after user deletions.
- RSIS3/mykb relevance: the agent runs as a specific user; ownership mistakes break the wiki pipeline — a daemon that cannot write its own snapshot, or a harness that creates root-owned articles the editor cannot modify. Treating identity as part of the deployment contract (explicit users, explicit ownership, least privilege) mirrors RSIS3's registry discipline for every component.

## Related
- [[wiki/os-shell/permissions-model|Permissions Model]] — permissions are attached to users and groups
- [[wiki/os-shell/process-management|Process Management]] — processes carry identity
- [[wiki/security/rbac|RBAC]] — authorization builds on OS identity
- [[wiki/os-shell/environment-variables|Environment Variables]] — identity and env define the process context
- [[wiki/devops-infra/backups|Backups]] — ownership drives backup access
