---
type: "concept"
title: "Argon2"
description: "Memory-hard password-hashing function, winner of the Password Hashing Competition"
tags: ["argon2", "passwords", "hashing", "security", "cryptography"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
---

# Argon2

## Summary
Argon2 won the Password Hashing Competition (2015) and is now the recommended password hash: memory-hard, with Argon2id balancing side-channel resistance and brute-force hardness.

## Details
- Parameters: memory cost, time cost, parallelism, salt, and tag length; tune to your hardware.
- Memory-hardness makes GPU/ASIC cracking far more expensive than bcrypt/scrypt.
- Supported by libsodium, Python's `argon2-cffi`, and modern frameworks.

## Parameter Selection

Argon2 exposes three tuning knobs: memory cost, time cost, and parallelism. Memory cost sets the amount of memory the function must fill, time cost sets the number of passes over that memory, and parallelism sets the number of lanes used. A common starting point is 64 MiB of memory, a time cost of 3, and parallelism of 4 for interactive logins; higher values protect better but cost more CPU and wall time. The salt should be unique per password and generated with a secure random source, and the tag length determines the output size.

Because parameters affect both security and user-perceived latency, they should be tuned against the fastest hardware you expect to serve. Store the parameters alongside the hash so verification can always reconstruct the exact computation; libsodium's `crypto_pwhash_str` and Python's `argon2-cffi` both encode parameters into the hash string, which removes the need for a separate config.

## Comparison Notes

Argon2's memory-hardness is its defining advantage. bcrypt and scrypt are also memory-hard or memory-sensitive, but Argon2's design allows a much larger memory footprint for a given time budget, which raises the cost of GPU and ASIC cracking far beyond what CPU-bound hashes achieve. Argon2id, the recommended variant, combines the side-channel resistance of Argon2i with the brute-force resistance of Argon2d, making it the safest default for password storage. Modern frameworks and password libraries increasingly ship Argon2id as the default algorithm.

## Related

- [[wiki/security/password-hashing|Password Hashing]] — the general requirement
- [[wiki/security/bcrypt|bcrypt]] — legacy alternative
- [[wiki/security/mfa|Multi-Factor Authentication]] — reduce password reliance
- [[wiki/security/secrets-management|Secrets Management]] — store hashes and params safely
