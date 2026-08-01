---
type: "concept"
title: "Password Hashing"
description: "One-way, salted, computationally expensive hashing of passwords for secure storage"
tags: ["passwords", "hashing", "security", "authentication", "cryptography"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Password Hashing

## Summary
Password hashing converts passwords into one-way digests using salted, slow algorithms (Argon2, bcrypt, scrypt, PBKDF2) so a database leak does not reveal credentials.

## Details
- Never use fast hashes (MD5/SHA-1) for passwords — they are brute-forceable in bulk.
- Per-user random salts defeat rainbow tables; work factors raise cost per guess.
- Verify with constant-time comparison and add rate limiting on login.

## Related
- [[wiki/security/argon2|Argon2]] — modern PHC winner
- [[wiki/security/bcrypt|bcrypt]] — widely deployed standard
- [[wiki/security/mfa|Multi-Factor Authentication]] — defense beyond passwords
- [[wiki/security/secrets-management|Secrets Management]] — protect hash salts/config
- [[wiki/api-protocols/rate-limiting|Rate Limiting]] — slow brute force
