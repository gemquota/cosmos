---
type: "concept"
title: "Passkeys"
description: "Passwordless sign-in using device-bound public-key credentials synced across platforms"
tags: ["passkeys", "webauthn", "authentication", "security", "fido2"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Passkeys

## Summary
Passkeys replace passwords with public-key credentials: the private key stays on the user's device (or synced via the OS), and sign-in uses a biometric/PIN gesture. They are the phishing-resistant evolution of WebAuthn.

## Details
- Backed by FIDO2/WebAuthn; platform vendors (Apple, Google, Microsoft) sync passkeys across devices.
- Phishing-resistant because credentials are bound to the relying-party origin.
- Adoption: most major platforms now support them; pair with MFA fallbacks during transition.

## Related
- [[wiki/security/webauthn|WebAuthn]] — the underlying standard
- [[wiki/security/mfa|Multi-Factor Authentication]] — passkeys as possession+biometric
- [[wiki/security/sso|Single Sign-On]] — passkey-backed identity providers
- [[wiki/security/password-hashing|Password Hashing]] — the problem passkeys remove
