---
type: "concept"
title: "TOTP"
description: "Time-based one-time passwords generated from a shared secret and the current time"
tags: ["totp", "otp", "mfa", "rfc6238"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
source: ["https://www.rfc-editor.org/rfc/rfc6238"]
---

# TOTP

- TOTP (RFC 6238) derives a short-lived code from a shared secret and the current time window, typically 30 seconds, using HMAC.
- It is the standard behind authenticator apps (Google Authenticator, Authy, 1Password) and needs no network connection at verification time.
- The shared secret must be provisioned securely (QR code), stored encrypted, and backed up deliberately.
- TOTP resists password replay but not real-time phishing relay, and secrets are recoverable only from the seed.
- For mykb: TOTP is a reasonable default second factor for human accounts below AAL3.

## Related

- [[wiki/identity/otp-codes|OTP Codes]] — TOTP is the time-based OTP family
- [[wiki/identity/mfa-patterns|MFA Patterns]] — TOTP as a standard MFA pattern
- [[wiki/identity/key-rotation|Key Rotation]] — TOTP seeds are long-lived keys
- [[wiki/security/mfa|Multi-Factor Authentication]] — existing MFA article
