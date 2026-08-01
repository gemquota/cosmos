---
type: "concept"
title: "Multi-Factor Authentication"
description: "Requiring two or more independent evidence types to authenticate a user, reducing credential-theft risk"
tags: ["mfa", "2fa", "authentication", "security", "nist"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
source: ["https://pages.nist.gov/800-63-3/sp800-63b.html"]
---

# Multi-Factor Authentication

## Summary
Multi-factor authentication (MFA) requires two or more distinct authentication factors — something you know (password), something you have (phone, key), something you are (biometric) — so a stolen password alone cannot grant access. NIST SP 800-63B defines factor strength and recommends phishing-resistant methods. MFA is the single most effective control against account takeover.

## Details
- Factor classes: knowledge, possession, and inherence; combining two classes is true MFA, two of the same class is not.
- Common second factors: TOTP apps (RFC 6238), SMS codes (discouraged by NIST due to SIM-swap risk), hardware keys (FIDO2/WebAuthn), and passkeys.
- Phishing resistance: WebAuthn-bound credentials are tied to the origin, so a fake login page cannot replay them — unlike TOTP or SMS.
- Enrollment and recovery: force enrollment on first login, provide verified recovery codes, and rate-limit verification attempts.
- Step-up: treat sensitive operations (deleting the wiki, exporting memory) with an extra factor even when the session is already authenticated.
- Worked example: the mykb daemon's admin endpoints could require a TOTP challenge for destructive operations, with the secret stored in the secrets vault.
- Integration: MFA sits above [[wiki/security/sso|SSO]]; identity providers enforce it once for all downstream apps.

## Related
- [[wiki/security/webauthn|WebAuthn]] — phishing-resistant possession factor
- [[wiki/security/passkeys|Passkeys]] — passwordless evolution of hardware keys
- [[wiki/security/sso|Single Sign-On]] — central enforcement point for MFA
- [[wiki/security/password-hashing|Password Hashing]] — first factor must still be stored safely
- [[wiki/security/zero-trust|Zero Trust Architecture]] — continuous, step-up authentication
- [[wiki/concepts/mykb-research-report|Mykb Research Report]] — memory store access control
- [[wiki/ops/gap-report|Gap Analysis Report]] — access-control gaps noted
