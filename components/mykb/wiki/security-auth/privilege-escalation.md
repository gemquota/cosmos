---
type: "concept"
title: "Privilege Escalation"
description: "Gaining permissions beyond those originally granted"
tags: ["privilege-escalation", "attacks", "mitre", "defense"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
source: ["https://attack.mitre.org/techniques/T1068/"]
---

# Privilege Escalation

- Privilege escalation moves an attacker from limited access to higher permissions — root, admin, or service accounts.
- ATT&CK T1068 covers exploitation for escalation: kernel flaws, misconfigured sudo, service misconfigurations, and token abuse.
- Defenses: least privilege, patching, capability reduction, and monitoring for unexpected privilege changes.
- For mykb: agent runtimes should run unprivileged and escalate only through audited, scoped mechanisms.

## Related

- [[wiki/security-auth/least-privilege|Least Privilege]] — the principle escalation violates
- [[wiki/security-auth/mitre-attack-framework|MITRE ATT&CK Framework]] — T1068 within the framework
- [[wiki/security-auth/patch-management|Patch Management]] — patching escalation flaws
- [[wiki/security-auth/security-incident-monitoring|Security Incident Monitoring]] — detecting privilege jumps
