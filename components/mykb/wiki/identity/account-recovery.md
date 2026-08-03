---
type: "concept"
title: "Account Recovery"
description: "Flows that restore access to an account after lost credentials or device loss"
tags: ["recovery", "authentication", "identity", "backup"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://pages.nist.gov/800-63-3/sp800-63b.html"]
---

# Account Recovery

## Summary
Account recovery re-establishes access when the user loses their factor — a password, device, or security key. Because recovery is the back door to every identity, it must be designed with the same rigor as authentication itself: NIST SP 800-63B treats recovery as an authentication event that must not be weaker than the original login, or attackers will simply target recovery instead of the front door.

## Details
- NIST SP 800-63B treats recovery as an authentication event: it must not be weaker than the original login, or attackers will target it. That means a recovery flow that accepts only an email link for an account protected by a security key is not a convenience — it is a downgrade attack waiting to be used.
- Patterns: recovery codes, backup devices, delegated recovery (trusted contacts), and identity proofing for high-value accounts. Recovery codes are pre-generated single-use secrets printed at enrollment; backup devices are additional enrolled factors; delegated recovery lets trusted contacts vouch for the user; identity proofing (documents, biometrics) is reserved for high-value accounts where the cost of proof is justified.
- Concrete example: a user loses their hardware key. A well-designed flow offers their recovery codes or a pre-enrolled backup key as the path back, requires a new key to be enrolled before the old one is fully retired, and sends a notification to the account's other channels so the user notices a hijacked recovery attempt.
- Failure modes: recovery channels that are weaker than the primary factor; recovery codes stored insecurely (in email, screenshots, notes apps) or never invalidated after use; recovery flows that bypass MFA; and the "security question" pattern, which is knowledge an attacker can harvest from social media.
- The design tension is usability versus security: self-service recovery is convenient but is a classic takeover vector, while slow, high-assurance recovery protects the account at the cost of frustrating legitimate users. The resolution is tiered recovery matched to account value and risk signals.
- Operational practice: require re-authentication with a remaining factor before issuing recovery material, expire recovery codes after a single use, bind recovery events to notifications, log all recovery attempts as security events, and test the flow end to end — including the attacker path.
- For mykb: recovery of an RSIS3 identity should require at least the same assurance level as the original enrollment, and recovery events should be recorded in the security log like any authentication event.

## Related
- [[wiki/identity/mfa-patterns|MFA Patterns]] — factor enrollment and backup design
- [[wiki/identity/account-takeover|Account Takeover]] — recovery is a prime ATO vector
- [[wiki/identity/hardware-security-keys|Hardware Security Keys]] — device loss is the common trigger
- [[wiki/security/mfa|Multi-Factor Authentication]] — recovery must not bypass MFA
