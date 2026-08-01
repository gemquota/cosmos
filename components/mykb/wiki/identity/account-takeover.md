---
type: "concept"
title: "Account Takeover"
description: "Gaining unauthorized control of a user account through stolen or guessed credentials"
tags: ["account-takeover", "attacks", "identity", "ato"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
source: ["https://attack.mitre.org/tactics/TA0006/"]
---

# Account Takeover

- Account takeover (ATO) is the end state of credential theft: an attacker gains control of an account, often changing credentials and exfiltrating data before the user notices.
- Common paths: credential stuffing, phishing, session hijacking, SIM swapping, and reused passwords on breached services.
- Detection signals: unusual geolocation, new devices, password resets, and abnormal access patterns.
- Mitigations: MFA, session binding, breach monitoring, and rapid account-recovery flows that require proof.
- For RSIS3: ATO of an agent or admin identity is the worst case, so detection rules should target it explicitly.

## Related

- [[wiki/identity/credential-stuffing|Credential Stuffing]] — a primary ATO vector
- [[wiki/identity/account-recovery|Account Recovery]] — recovery flows are both fix and attack surface
- [[wiki/identity/session-hijacking|Session Hijacking]] — stealing live sessions to take over accounts
- [[wiki/security-auth/security-incident-monitoring|Security Incident Monitoring]] — detecting takeover attempts
