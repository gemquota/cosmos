---
type: "concept"
title: "bcrypt"
description: "Adaptive, salted password-hashing function based on the Blowfish cipher"
tags: ["bcrypt", "passwords", "hashing", "security", "cryptography"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# bcrypt

## Summary
bcrypt is a widely used password-hashing function with built-in salts and an adaptive cost factor. Its 72-byte input limit and aging design have prompted newer recommendations.

## Details
- Cost factor (`10-12`) doubles work per increment; choose based on hardware.
- The 72-byte truncation issue requires pre-hashing only in controlled designs.
- Still a solid default in many frameworks; Argon2 is the newer recommendation.

## Related
- [[wiki/security/argon2|Argon2]] — successor algorithm
- [[wiki/security/password-hashing|Password Hashing]] — family context
- [[wiki/security/mfa|Multi-Factor Authentication]] — layered auth
- [[wiki/security/oauth2|OAuth 2.0]] — modern auth flows reduce password use
