---
type: "concept"
title: "Account Recovery"
description: "Flows that restore access to an account after lost credentials or device loss"
tags: ["recovery", "authentication", "identity", "backup"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
source: ["https://pages.nist.gov/800-63-3/sp800-63b.html"]
---

# Account Recovery

- Account recovery re-establishes access when the user loses their factor — a password, device, or security key.
- NIST SP 800-63B treats recovery as an authentication event: it must not be weaker than the original login, or attackers will target it.
- Patterns: recovery codes, backup devices, delegated recovery (trusted contacts), and identity proofing for high-value accounts.
- The design tension is usability versus security: self-service recovery is convenient but is a classic takeover vector.
- For mykb: recovery of an RSIS3 identity should require at least the same assurance level as the original enrollment.

## Related

- [[wiki/identity/mfa-patterns|MFA Patterns]] — factor enrollment and backup design
- [[wiki/identity/account-takeover|Account Takeover]] — recovery is a prime ATO vector
- [[wiki/identity/hardware-security-keys|Hardware Security Keys]] — device loss is the common trigger
- [[wiki/security/mfa|Multi-Factor Authentication]] — recovery must not bypass MFA
