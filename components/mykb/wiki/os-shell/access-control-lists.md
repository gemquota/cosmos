---
type: "concept"
title: "Access Control Lists"
description: "POSIX ACLs beyond mode bits via getfacl/setfacl"
tags: ["acl", "permissions", "getfacl", "setfacl", "access-control"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://man7.org/linux/man-pages/man5/acl.5.html", "https://man7.org/linux/man-pages/man1/setfacl.1.html"]
---

# Access Control Lists

## Summary
POSIX access control lists extend the classic owner/group/other mode bits so a file can grant different permissions to multiple named users and groups. They are managed with getfacl(1) and setfacl(1) and remain the standard mechanism on Linux filesystems such as ext4 and XFS.

## Details
- An access ACL contains entries of class user, group, mask, and other; the mask entry caps the effective rights of named users and named groups.
- The owning user and "other" entries always exist; the group entry becomes the ACL mask when extra entries are added.
- Default ACLs on a directory are inherited by new files and subdirectories, which is how shared project directories grant uniform access.
- The mode bits shown by ls -l are a projection of the ACL; setfacl -m updates entries, and -x removes them.
- Permission checks become: owner entries, then named users, then owning group, named groups, then other, honoring the mask.
- Modern POSIX ACLs are limited to these simple rules; NFSv4 and SMB ACLs support richer inheritance and deny entries.
- ACLs travel over NFS with nfs4acl and appear in tar archives if you use --acls; plain cp -p may not preserve them.

## Related
- [[wiki/os-shell/permissions-model|Permissions Model]] — the base mode bits ACLs extend
- [[wiki/os-shell/users-and-groups|Users & Groups]] — the principals ACL entries name
- [[wiki/os-shell/umask|Umask]] — the default-mask logic ACLs interact with
- [[wiki/os-shell/special-file-bits|Special File Bits]] — setgid directories combine with default ACLs
- [[wiki/security-auth/role-based-access-control|Role-Based Access Control]] — the application-level model ACLs support
