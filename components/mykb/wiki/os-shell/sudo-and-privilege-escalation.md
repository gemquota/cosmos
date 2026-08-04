---
type: "entity"
title: "sudo & Privilege Escalation"
description: "sudoers, privilege separation, and alternatives"
tags: ["sudo", "privilege", "security", "sudoers"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://www.sudo.ws/docs/man/sudoers.man.html", "https://man7.org/linux/man-pages/man8/sudo.8.html"]
---

# sudo & Privilege Escalation

## Summary
sudo lets authorized users run commands with another identity, usually root, while logging what was done. It is a setuid-root program whose entire security model lives in the sudoers policy file: who may run what, where, and how.

## Details
- sudoers syntax: user host=(runas:groups) commands, with aliases (User_Alias, Cmnd_Alias) for groups of users and commands.
- Ordering matters: the last matching rule wins, so defaults like !authenticate and NOPASSWD must be placed carefully.
- env_reset strips dangerous variables; secure_path fixes PATH; requiretty gates sudo to terminal sessions by policy.
- sudo validates by password by default, then caches with a timestamp file (tty_tickets isolates per terminal); sudo -k clears it.
- Every invocation logs to syslog and often /var/log/sudoers; audit logging is the main reason to route admin access through sudo.
- Privilege separation: daemons drop privileges after binding ports; sudo is one escalation point, doas and polkit are lighter alternatives.
- Misconfiguration is dangerous: a writable command in a NOPASSWD alias is root-equivalent, so least privilege and explicit commands are the rule.

## Related
- [[wiki/os-shell/special-file-bits|Special File Bits]] — sudo is a setuid-root binary
- [[wiki/security-auth/privilege-escalation|Privilege Escalation]] — the attacks sudo must resist
- [[wiki/security-auth/least-privilege|Least Privilege]] — the policy principle sudo encodes
- [[wiki/os-shell/users-and-groups|Users & Groups]] — the identities sudo switches between
- [[wiki/security-auth/audit-logging|Audit Logging]] — the record every sudo run leaves
