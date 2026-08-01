---
type: "concept"
title: "OTP Codes"
description: "One-time passwords used as a second factor or for step-up verification"
tags: ["otp", "one-time-password", "mfa", "authentication"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
source: ["https://www.rfc-editor.org/rfc/rfc6238"]
---

# OTP Codes

- A one-time password (OTP) is a code valid for a single authentication event, derived from a shared secret (HOTP, RFC 4226) or from time plus secret (TOTP, RFC 6238).
- Delivered via authenticator apps, SMS, email, or hardware tokens, OTPs are the most common second factor.
- Limitations: codes are phishable in real time (AiTM relay) and SMS is vulnerable to interception and SIM swapping.
- NIST ranks OTP authenticators below phishing-resistant hardware-backed methods.
- For mykb: OTPs fit low- and mid-assurance flows; sensitive operations should demand stronger factors.

## Related

- [[wiki/identity/totp|TOTP]] — the time-based variant in authenticator apps
- [[wiki/identity/mfa-patterns|MFA Patterns]] — where OTPs sit in the factor matrix
- [[wiki/identity/hardware-security-keys|Hardware Security Keys]] — stronger possession alternative
- [[wiki/security/mfa|Multi-Factor Authentication]] — OTP as an MFA factor
