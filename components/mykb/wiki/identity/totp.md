---
type: "concept"
title: "TOTP"
description: "Time-based one-time passwords generated from a shared secret and the current time"
tags: ["totp", "otp", "mfa", "rfc6238"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://www.rfc-editor.org/rfc/rfc6238"]
---

# TOTP

## Summary
TOTP (RFC 6238) derives a short-lived code from a shared secret and the current time window, typically 30 seconds, using HMAC. It is the standard behind authenticator apps (Google Authenticator, Authy, 1Password) and needs no network connection at verification time — the code is computed independently on both sides from the same seed and clock.

## Details
- TOTP (RFC 6238) derives a short-lived code from a shared secret and the current time window, typically 30 seconds, using HMAC. The algorithm is: `HMAC-SHA1(secret, counter)` where the counter is the current Unix time divided by the time step; the result is truncated to a 6-8 digit code. Both the authenticator and the server compute the same value from the same seed and window.
- It is the standard behind authenticator apps (Google Authenticator, Authy, 1Password) and needs no network connection at verification time. This offline property is its strength: verification does not depend on SMS delivery, email reachability, or a network path, so it works in constrained environments and is immune to interception of the delivery channel.
- The shared secret must be provisioned securely (QR code), stored encrypted, and backed up deliberately. Provisioning via QR means the seed crosses one screen at enrollment; after that it lives in the authenticator and the server. Backup matters: if the user loses the device holding the app, the seed is gone — which is why services offer recovery codes or re-enrollment alongside TOTP.
- TOTP resists password replay but not real-time phishing relay, and secrets are recoverable only from the seed. An attacker who phishes the user's password and current code relays both to the real site within the validity window and completes the login; a hardware security key does not have this weakness because its assertions are origin-bound.
- Concrete example: a user logs in, opens their authenticator app, and enters the six-digit code shown for the current 30-second window. The server verifies the code against the current and adjacent windows (to tolerate slight clock skew), marks it used, and rejects replays — the same code cannot authenticate twice.
- Failure modes: clock skew beyond the accepted window causing legitimate logins to fail; seeds stored without backup, so device loss locks the account; codes with no replay protection; and phishing-relay attacks that defeat the whole family.
- For mykb: TOTP is a reasonable default second factor for human accounts below AAL3, and the wiki should document the seed lifecycle (provision, backup, revoke) as part of identity operations.

## Related
- [[wiki/identity/otp-codes|OTP Codes]] — TOTP is the time-based OTP family
- [[wiki/identity/mfa-patterns|MFA Patterns]] — TOTP as a standard MFA pattern
- [[wiki/identity/key-rotation|Key Rotation]] — TOTP seeds are long-lived keys
- [[wiki/security/mfa|Multi-Factor Authentication]] — existing MFA article
