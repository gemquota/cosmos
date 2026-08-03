---
type: "concept"
title: "Account Takeover"
description: "Gaining unauthorized control of a user account through stolen or guessed credentials"
tags: ["account-takeover", "attacks", "identity", "ato"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://attack.mitre.org/tactics/TA0006/"]
---

# Account Takeover

## Summary
Account takeover (ATO) is the end state of credential theft: an attacker gains control of an account, often changing credentials and exfiltrating data before the user notices. It is the most damaging and most common identity attack, because a single hijacked account unlocks everything the account can reach — and once credentials are changed, the legitimate owner is locked out of their own identity.

## Details
- Common paths: credential stuffing, phishing, session hijacking, SIM swapping, and reused passwords on breached services. Credential stuffing feeds breach dumps against the service at scale; phishing harvests credentials and MFA codes in real time; session hijacking steals live authenticated sessions; SIM swapping redirects SMS-based recovery; and password reuse lets one breach compound into many accounts.
- Concrete example: an attacker takes breach credentials for a user, verifies the password works against the service, logs in from a residential proxy in a new region, disables notifications, changes the password and recovery email, and exfiltrates the user's saved data over the next days — the user discovers the takeover only when their login stops working.
- Detection signals: unusual geolocation, new devices, password resets, and abnormal access patterns. Each signal is weak alone — users travel and change devices — but the combination (new device, new location, immediate password change, notification suppression) is a strong takeover signature.
- Mitigations: MFA, session binding, breach monitoring, and rapid account-recovery flows that require proof. Phishing-resistant factors (hardware keys) close the real-time relay path; session binding ties tokens to device fingerprints; breach monitoring lets the service force password resets before attackers use leaked credentials; and recovery that requires proof prevents the attacker's "I forgot my password" shortcut.
- Failure modes: detection that only fires after the account is locked out; recovery flows that are easier than the original login; and the notification-suppression gap, where attackers disable alerts before the user can react.
- Operational practice: score login risk per request, challenge high-risk logins with step-up auth, monitor for the takeover signature (new device + reset + location change), and make recovery require proof that an attacker would not have.
- For RSIS3: ATO of an agent or admin identity is the worst case, so detection rules should target it explicitly — an agent identity that suddenly changes its own credentials is the same attack, and the response should be automatic session revocation plus human review.

## Related
- [[wiki/identity/credential-stuffing|Credential Stuffing]] — a primary ATO vector
- [[wiki/identity/account-recovery|Account Recovery]] — recovery flows are both fix and attack surface
- [[wiki/identity/session-hijacking|Session Hijacking]] — stealing live sessions to take over accounts
- [[wiki/security-auth/security-incident-monitoring|Security Incident Monitoring]] — detecting takeover attempts
