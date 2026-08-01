---
type: "concept"
title: "Lateral Movement"
description: "Moving between systems within a network after initial compromise"
tags: ["lateral-movement", "attacks", "mitre", "defense"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
source: ["https://attack.mitre.org/tactics/TA0008/"]
---

# Lateral Movement

- Lateral movement (ATT&CK TA0008) describes how attackers hop between hosts using stolen credentials, remote services, or shared tooling.
- Segmentation, least privilege, and per-service authentication make each hop harder and more visible.
- Detection: anomalous remote logins, credential use from new hosts, and unusual service-to-service traffic.
- For mykb: audit logs of service-to-service calls are the raw material for spotting movement.

## Related

- [[wiki/security-auth/network-segmentation|Network Segmentation]] — limiting movement surface
- [[wiki/security-auth/mitre-attack-framework|MITRE ATT&CK Framework]] — TA0008 in context
- [[wiki/security-auth/privilege-escalation|Privilege Escalation]] — movement often follows escalation
- [[wiki/security-auth/audit-logging|Audit Logging]] — the telemetry that reveals movement
