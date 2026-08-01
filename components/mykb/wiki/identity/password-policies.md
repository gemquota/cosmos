---
type: "concept"
title: "Password Policies"
description: "Rules governing password length, composition, age, and reuse at the organizational level"
tags: ["passwords", "policies", "authentication", "nist"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
source: ["https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html"]
---

# Password Policies

- Modern guidance (NIST SP 800-63B, OWASP) favors length over composition: 8+ characters, no forced complexity, and blocking known-breached passwords.
- Arbitrary expiry and composition rules push users toward weaker, reused passwords; screen against breach lists instead.
- Password managers plus MFA make policy enforcement more effective than password gymnastics.
- For mykb: the same policy should apply to human logins and any legacy service credentials that still rely on passwords.

## Related

- [[wiki/identity/password-managers|Password Managers]] — making long unique passwords practical
- [[wiki/identity/credential-stuffing|Credential Stuffing]] — breach-list screening counters reuse
- [[wiki/identity/authentication-factors|Authentication Factors]] — passwords are one factor among several
- [[wiki/security/password-hashing|Password Hashing]] — storing passwords correctly
