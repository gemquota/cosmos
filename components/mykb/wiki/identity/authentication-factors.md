---
type: "concept"
title: "Authentication Factors"
description: "Categories of evidence used to verify identity: knowledge, possession, and inherence"
tags: ["authentication", "factors", "identity", "nist", "mfa"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://pages.nist.gov/800-63-3/sp800-63b.html"]
---

# Authentication Factors

## Summary

An authentication factor is a category of evidence presented to prove a claim of identity. The classic three classes are knowledge (something you know, e.g. a password or PIN), possession (something you have, e.g. a phone or security key), and inherence (something you are, e.g. a fingerprint or face). Factors matter because the strength of an authentication event is only as good as the factors behind it: combining independent factors is multi-factor authentication (MFA), while reusing one factor type, such as two passwords, adds little. NIST SP 800-63B grades authenticators by these categories when assigning Authentication Assurance Levels (AAL), which is the vocabulary RSIS3 uses when reasoning about how strongly its own identities are established.

## Details

- Knowledge factors are cheap and universal but suffer from guessing, theft, and reuse; NIST now treats passwords as a single factor that must be paired with another category for AAL2+.
- Possession factors split into single-factor OTP devices (SMS, TOTP apps) and multi-factor cryptographic devices (hardware security keys, passkeys), with the latter being phishing-resistant because the key never leaves the device.
- Inherence factors (biometrics) are convenient but not secret: they cannot be rotated if compromised, which is why they are usually combined with possession via platform authenticators.
- The authentication-factor pyramid maps to NIST AALs: AAL1 is single-factor, AAL2 requires two different factor categories, AAL3 adds a hardware-based, phishing-resistant authenticator.
- For mykb, treating RSIS3's API credentials, agent sessions, and user logins as separate factor categories keeps a single compromised secret from granting full memory access.

## Related

- [[wiki/identity/mfa-patterns|MFA Patterns]] — combines factor categories into deployment patterns
- [[wiki/identity/passwordless-authentication|Passwordless Authentication]] — replaces knowledge factors with cryptographic possession
- [[wiki/identity/otp-codes|OTP Codes]] — possession-factor implementations
- [[wiki/identity/hardware-security-keys|Hardware Security Keys]] — device-based possession factors
- [[wiki/security/mfa|Multi-Factor Authentication]] — existing article on combining factors
- [[wiki/security/passkeys|Passkeys]] — phishing-resistant possession factor
- [[wiki/security/password-hashing|Password Hashing]] — protecting the knowledge factor at rest
- [[wiki/concepts/identity-system|RSIS3 Identity System]] — identity model that assigns factors to agent and user roles
