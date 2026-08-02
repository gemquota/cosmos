---
type: "concept"
title: "Special File Bits"
description: "setuid/setgid/sticky bits and their security effects"
tags: ["setuid", "setgid", "sticky", "permissions", "security"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://man7.org/linux/man-pages/man7/inode.7.html"]
---

# Special File Bits

## Summary
Beyond read/write/execute, the mode word carries three special bits: setuid, setgid, and the sticky bit. Setuid lets a program run with the owner's identity, setgid fixes group inheritance on directories, and the sticky bit restricts deletion in shared directories.

## Details
- chmod 4755 sets setuid: when executed, the process gains the file owner's effective UID — how passwd and sudo work as non-root users.
- chmod 2755 sets setgid: files get the group of the directory that contains them, and on executables the process runs with the file's group.
- The sticky bit (chmod 1777) on /tmp lets anyone create files but only the owner, root, or a directory owner delete or rename them.
- ls -l shows these as s/S and t/T in the execute positions; lowercase means the execute bit is also set.
- Setuid binaries are prime attack surface: a bug gives attackers elevated privileges, so they should be minimal, own their files, and avoid writable paths.
- Linux largely replaces setuid with capabilities (cap_net_bind_service, CAP_SYS_ADMIN) granted per binary via setcap.
- Setgid directories combined with default ACLs are how shared team directories keep new files in the right group.

## Related
- [[wiki/os-shell/permissions-model|Permissions Model]] — the mode bits these flags extend
- [[wiki/os-shell/sudo-and-privilege-escalation|sudo & Privilege Escalation]] — a prominent setuid-root binary
- [[wiki/security-auth/privilege-escalation|Privilege Escalation]] — the attacks setuid enables
- [[wiki/os-shell/access-control-lists|Access Control Lists]] — setgid directories pair with default ACLs
- [[wiki/os-shell/users-and-groups|Users & Groups]] — the identities setuid/setgid switch to
