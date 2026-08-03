---
type: "concept"
title: "Users, Groups & ACLs"
description: "Local identity model of users and groups with discretionary ACLs on Linux files"
tags: ["users", "groups", "acl", "unix"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Users, Groups & ACLs

## Summary
The local identity model pairs users (numeric UIDs) and groups (GIDs) with discretionary access control: every file carries an owner, a group, and mode bits, and POSIX access control lists (ACLs) extend that model with per-user and per-group entries beyond the single owner/group. ACLs are how a shared filesystem gives *specific* people access without creating a new group per combination.

## Details
- Mechanism: the base model is owner/group/other mode bits; POSIX ACLs (`setfacl`/`getfacl`) add a list of entries: named users (`u:alice:rw-`), named groups (`g:devs:r-x`), a mask that caps the maximum permissions granted to named users/groups and the owning group, and the default ACL (inherited by new files in a directory). When an ACL is present, the kernel's permission check consults the ACL instead of just the mode bits: the mask is the ceiling, so `setfacl -m g:devs:rwx file` followed by `setfacl -m m::rx file` reduces what devs actually get. ACLs are stored in extended attributes (system.posix_acl_access), so filesystems must support xattrs.
- Concrete examples: a shared project directory where `alice` and `bob` each need different rights without a shared group: `setfacl -m u:alice:rwx,u:bob:r-x,default:u:alice:rwx dir`; a web root where the app user needs write access while the deploy user only reads; `getfacl`/`setfacl -x` to inspect and remove entries; `ls -l` shows a `+` marker on files with ACLs; `setfacl -b` removes all ACL entries and restores plain modes; NFSv4 ACLs are the richer, different standard used on NFS exports.
- Failure modes: the classic failures are the mask silently clipping permissions (you grant `rwx` to a group, the mask says `r-x`, and "why can't they write?" — the answer is the mask, which many admins forget exists), ACL bloat (hundreds of ad hoc entries replacing clean group design), and portability breaks (copying files with `cp -a`/`rsync -A` preserves ACLs, plain `cp` does not; filesystems without xattr support drop them). The `+` in `ls -l` hides that the mode bits no longer tell the full story, so ACLs make permissions harder to audit at a glance.
- Operational tradeoffs: ACLs buy fine-grained, per-user sharing without group proliferation, at the cost of complexity — the mask semantics, default-ACL inheritance, and tooling differences make them harder to reason about than plain modes. The practice rules: prefer groups for anything stable (they are simpler and visible in `ls -l`), use ACLs for the genuinely irregular exceptions, keep the mask in mind when debugging, and document or script ACL setup so it is reproducible rather than ad hoc.
- RSIS3/mykb relevance: the wiki's shared corpus is a classic ACL use case — many agents and humans with different roles (read-only editors, write-capable daemons); encoding that as groups plus a few ACL exceptions, and scripting it, mirrors RSIS3's principle that access policy should be declared and reproducible, not accumulated by hand.

## Related
- [[wiki/cloud-infra/cloud-security-groups|Cloud Security Groups]]
- [[wiki/os-shell/users-and-groups|Users and Groups]]
- [[wiki/os-shell/process-groups-and-sessions|Process Groups & Sessions]]
- [[wiki/os-shell/kernel-architecture|Kernel Architecture]]
- [[wiki/os-shell/memory-management-paging|Memory Management & Paging]]
- [[wiki/syntheses/knowledge-acquisition-workflow|Knowledge Acquisition Workflow]] — how stubs grow into full articles in mykb
- [[wiki/syntheses/mykb-acquisition-curation-and-practices|Acquisition, Curation & Practices]] — the curation loop this stub belongs to
