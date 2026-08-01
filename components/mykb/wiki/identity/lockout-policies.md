---
type: "concept"
title: "Lockout Policies"
description: "Rules that temporarily or permanently disable access after repeated failed attempts"
tags: ["lockout", "policies", "authentication", "abuse"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
source: ["https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html"]
---

# Lockout Policies

- Lockout policies disable an account or session after a threshold of failed attempts to slow guessing.
- Permanent lockouts invite denial-of-service and account-recovery abuse; exponential backoff and temporary lockout are safer.
- Widely-used correct-password detection (Google's approach) only penalizes clients whose guesses are all wrong, avoiding legitimate-user lockouts.
- Recovery flows must not silently bypass lockout state, or attackers will pivot there.
- For mykb: lockout decisions should be logged and feed the incident-monitoring pipeline.

## Related

- [[wiki/identity/brute-force-protection|Brute-Force Protection]] — lockout is a throttling mechanism
- [[wiki/identity/account-takeover|Account Takeover]] — lockout abuse as a DOS vector
- [[wiki/identity/account-recovery|Account Recovery]] — recovery must respect lockout state
- [[wiki/security-auth/audit-logging|Audit Logging]] — lockout events as security signals
