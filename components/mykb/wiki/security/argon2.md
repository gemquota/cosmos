---
type: "concept"
title: "Argon2"
description: "Memory-hard password-hashing function, winner of the Password Hashing Competition"
tags: ["argon2", "passwords", "hashing", "security", "cryptography"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Argon2

## Summary
Argon2 won the Password Hashing Competition (2015) and is now the recommended password hash: memory-hard, with Argon2id balancing side-channel resistance and brute-force hardness.

## Details
- Parameters: memory cost, time cost, parallelism, salt, and tag length; tune to your hardware.
- Memory-hardness makes GPU/ASIC cracking far more expensive than bcrypt/scrypt.
- Supported by libsodium, Python's `argon2-cffi`, and modern frameworks.

## Related
- [[wiki/security/password-hashing|Password Hashing]] — the general requirement
- [[wiki/security/bcrypt|bcrypt]] — legacy alternative
- [[wiki/security/mfa|Multi-Factor Authentication]] — reduce password reliance
- [[wiki/security/secrets-management|Secrets Management]] — store hashes and params safely
