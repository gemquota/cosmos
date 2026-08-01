---
type: "concept"
title: "WebAuthn"
description: "W3C web standard for passwordless, phishing-resistant authentication using public-key cryptography"
tags: ["webauthn", "fido2", "authentication", "web", "security"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# WebAuthn

## Summary
WebAuthn is the W3C standard letting browsers authenticate users with public-key cryptography instead of passwords. Credentials are created by authenticators — hardware keys, platform biometrics — and bound to origins.

## Details
- Registration and assertion flows use attestation/challenge tokens; private keys never leave the authenticator.
- Resists phishing because the origin is part of the credential contract.
- Server libraries exist for most frameworks; combines with the CTAP2 authenticator layer (FIDO2).

## Related
- [[wiki/security/passkeys|Passkeys]] — productized WebAuthn
- [[wiki/security/mfa|Multi-Factor Authentication]] — phishing-resistant factor
- [[wiki/security/oauth2|OAuth 2.0]] — identity-provider integration
- [[wiki/security/zero-trust|Zero Trust Architecture]] — strong device-bound auth
- [[wiki/api-protocols/rest-apis|REST APIs]] — assertion endpoints
