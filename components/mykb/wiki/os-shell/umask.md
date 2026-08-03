---
type: "concept"
title: "Umask"
description: "The default permission mask applied to every new file and directory"
tags: ["umask", "permissions", "defaults", "security"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
---

# Umask

## Summary
umask is the default permission mask the shell (and the process creating a file) applies to every new file and directory: `umask 022` means new files get 644 (rw-r--r--) and directories get 755 (rwxr-xr-x), because the mask *removes* those bits from the creator's requested mode. It is how a system enforces a baseline of privacy and shareability without remembering to `chmod` every file.

## Details
- Mechanism: when a program creates a file, it requests a mode (typically 0666 for files, 0777 for directories); the kernel ANDs that with the complement of the process's umask: `requested & ~umask`. So with umask 022, `0666 & ~022 = 0644`; with umask 077, the result is 0600 — owner-only. The umask is a process attribute inherited through fork/exec, set by the shell (often in `/etc/profile`, `~/.bashrc`, or PAM) and changeable with the `umask` builtin (`umask` prints it, `umask 077` sets it; symbolic forms like `umask u=rwx,g=,o=` work too). Every child inherits the shell's umask, which is why a restrictive login shell produces restrictive files everywhere.
- Concrete examples: a shared server sets `umask 022` so team files are group-readable; a workstation with private notes uses `umask 077`; a script that writes session tokens to a temp file does `(umask 077; echo "$token" > /tmp/token)` — the subshell tightens the mask just for that write; `install -m 600` and `mktemp` (which creates with 0600 by default) are the umask-aware tools; daemons often set umask 022 or 027 so their runtime files are not world-writable.
- Failure modes: the classic failure is a permissive umask on a system with sensitive data — files created with 666 default become world-writable unless the mask is tightened (a 022 mask on a single-user laptop is common and usually fine, but on a shared host it leaks secrets). The opposite failure is a too-strict umask (077) breaking collaboration or services: a web app that cannot read a colleague's files, or a daemon whose 0600 log files are unreadable by the log collector. The subtle failure is per-process variance: a service started by systemd with a different umask than your shell creates files with modes you did not expect.
- Operational tradeoffs: umask is the cheapest least-privilege control on the system — one number per process, applied universally — and the tradeoff is that it is a default, not a per-file decision: security-sensitive files should still be created with explicit modes (`chmod`, `install -m`, `mktemp`) rather than relying on the mask. The practice rules: set a deliberate umask in profile (022 for shared systems, 077 for personal/secret-heavy ones), tighten it locally around sensitive writes, and verify service umasks when debugging unexpected file modes.
- RSIS3/mykb relevance: wiki files created by agents inherit the harness umask; the corpus should be world-readable (0644) while keys and daemon config stay 0600 — encoding that split in the harness's umask and explicit modes prevents accidental credential exposure in the knowledge store.

## Related
- [[wiki/os-shell/permissions-model|Permissions Model]] — umask is the default of that model
- [[wiki/os-shell/users-and-groups|Users and Groups]] — umask interacts with ownership
- [[wiki/security/secrets-management|Secrets Management]] — private files need restrictive umasks
- [[wiki/os-shell/exit-codes|Exit Codes]] — script hygiene includes umask discipline
- [[wiki/os-shell/filesystem-hierarchy|Filesystem Hierarchy]] — default permissions apply across the hierarchy
- [[wiki/devops-infra/backups|Backups]] — default modes affect backup privacy
