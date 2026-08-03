---
type: "concept"
title: "OTP Codes"
description: "One-time passwords used as a second factor or for step-up verification"
tags: ["otp", "one-time-password", "mfa", "authentication"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://www.rfc-editor.org/rfc/rfc6238"]
---

# OTP Codes

## Summary
A one-time password (OTP) is a code valid for a single authentication event, derived from a shared secret (HOTP, RFC 4226) or from time plus secret (TOTP, RFC 6238). OTPs are the most common second factor in the world — delivered by authenticator apps, SMS, email, or hardware tokens — and they are a solid mid-assurance control with a known weakness: real-time phishing can relay the code the moment it is entered.

## Details
- A one-time password (OTP) is a code valid for a single authentication event, derived from a shared secret (HOTP, RFC 4226) or from time plus secret (TOTP, RFC 6238). HOTP is a counter-based code that advances with each use; TOTP derives a code from the current time window (typically 30 seconds) and is what authenticator apps use.
- Delivered via authenticator apps, SMS, email, or hardware tokens, OTPs are the most common second factor. App-based TOTP needs no network at verification time; SMS and email trade that convenience for interception risk; hardware OTP tokens are a physical possession factor without smartphone dependency.
- Concrete example: a user logs in, enters their password, and is prompted for the six-digit code from their authenticator app. The code is generated from the app's shared seed and the current 30-second window, is valid for that window plus a small tolerance for clock skew, and is rejected once used — replaying the same code fails.
- Limitations: codes are phishable in real time (AiTM relay) and SMS is vulnerable to interception and SIM swapping. In an adversary-in-the-middle attack, the phishing site relays the user's code to the real site within the validity window, completing the login as the user; SMS adds interception and SIM-swap paths that app-based TOTP does not have.
- NIST ranks OTP authenticators below phishing-resistant hardware-backed methods. They are a genuine improvement over passwords alone but are not the strongest tier; for sensitive operations, the code must not be the last line of defense.
- Failure modes: seeds provisioned over insecure channels; clock skew breaking TOTP windows; codes with excessive time tolerance enabling reuse windows; and lockout interactions where failed OTP entries lock accounts and create denial-of-service.
- For mykb: OTPs fit low- and mid-assurance flows; sensitive operations should demand stronger factors — and the same relay weakness applies to any one-time code, so step-up decisions should not rest on OTP alone.

## Related
- [[wiki/identity/totp|TOTP]] — the time-based variant in authenticator apps
- [[wiki/identity/mfa-patterns|MFA Patterns]] — where OTPs sit in the factor matrix
- [[wiki/identity/hardware-security-keys|Hardware Security Keys]] — stronger possession alternative
- [[wiki/security/mfa|Multi-Factor Authentication]] — OTP as an MFA factor
