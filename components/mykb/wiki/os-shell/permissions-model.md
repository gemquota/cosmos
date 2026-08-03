---
type: "concept"
title: "Permissions Model"
description: "The Unix read/write/execute model for files and directories, plus ownership"
tags: ["permissions", "unix", "security", "files"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
---

# Permissions Model

## Summary
Unix permissions grant read, write, and execute to three classes — owner, group, others — stored as mode bits (`rwxr-xr--`). Directories interpret the bits differently: read lists entries, write adds/removes entries, and execute means *traverse* (the ability to pass through into the directory to reach files inside). This small model, plus ownership, is the foundation of everything else in Unix security.

## Details
- Mechanism: every file and directory has an owner (uid) and group (gid), and three permission triplets — user, group, other. The mode is stored as bits (rwx = 421 octal), so 755 means owner rwx, group r-x, others r-x; 644 (files) and 755 (directories) are the defaults everyone knows. Access is determined by a single matching class: if you are the owner, only the owner bits apply; else if you are in the file's group, group bits; else other bits — there is no "most permissive wins". Directories need execute to be traversed, so a directory that is r-- but not --x cannot be entered at all, and write-without-execute means you can name files you cannot look up.
- Concrete examples: `chmod 600 ~/.ssh/id_ed25519` makes a private key owner-only (ssh refuses keys that are too permissive); `chmod 755 bin/` makes a directory searchable by all; `chown -R www-data:www-data /var/www` fixes a web root owned by root; a sticky bit on `/tmp` (1777) lets anyone create files but only owners delete them; setuid on `/usr/bin/passwd` runs with root privileges so it can write `/etc/shadow`; `umask 022` ensures new files default to 644.
- Failure modes: the classic failures are over-permissioning (`chmod 777` on a web directory allows anyone to overwrite served files — a defacement vector), the setuid footgun (a setuid binary with a bug becomes privilege escalation), and confusion between file and directory semantics (a directory that is 666 still cannot be listed without execute). Root bypasses everything, which makes "it works as root" tests misleading; ACLs and capabilities then extend the model in ways that break naive assumptions about what the mode bits mean.
- Operational tradeoffs: the model is simple and predictable, which is its strength, and coarse, which is its weakness — "group" is one class, there is no per-user or per-group-per-file granularity without ACLs (POSIX ACLs add named users/groups) and no fine-grained command-level control without capabilities or a framework like RBAC. The practice rules: least privilege by default (644/755, tighten private data to 600/700), set umask deliberately, audit with `find -perm` for world-writable files, and treat the execute bit on directories as the traversal permission it is.
- RSIS3/mykb relevance: file permissions protect the wiki and its secrets from misreads; the wiki corpus should be owner-writable and world-readable, while daemon config and keys stay 600 — the same least-privilege default RSIS3 applies to registry and checkpoint files.

## Related
- [[wiki/os-shell/users-and-groups|Users and Groups]] — permissions are granted to users and groups
- [[wiki/os-shell/umask|Umask]] — the default mode applied at file creation
- [[wiki/os-shell/filesystem-hierarchy|Filesystem Hierarchy]] — each hierarchy node has permissions
- [[wiki/security/rbac|RBAC]] — the larger authorization framework
- [[wiki/security/secrets-management|Secrets Management]] — permissions protect secrets at rest
