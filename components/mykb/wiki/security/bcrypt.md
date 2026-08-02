---
type: "concept"
title: "bcrypt"
description: "Adaptive, salted password-hashing function based on the Blowfish cipher"
tags: ["bcrypt", "passwords", "hashing", "security", "cryptography"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
---

# bcrypt

## Summary
bcrypt is a widely used password-hashing function with built-in salts and an adaptive cost factor. It derives from the Blowfish cipher's key schedule, which is deliberately expensive to compute, and that expense is tunable. Its 72-byte input limit and aging design have prompted newer recommendations, but bcrypt remains the default in many frameworks and is still a reasonable choice when configured with an adequate cost factor.

## Details
- Cost factor (`10-12`) doubles work per increment; choose based on hardware.
- The 72-byte truncation issue requires pre-hashing only in controlled designs.
- Still a solid default in many frameworks; Argon2 is the newer recommendation.
- The salt is generated per password and stored inside the output string, so identical passwords never hash alike and rainbow tables are ineffective.
- The output format embeds version, cost, salt, and hash, which makes verification self-describing across libraries.
- Verify with a constant-time comparison and an equality API provided by the library, never with a naive string compare.
- Do not invent a pre-hashing step casually: it can introduce length-extension or encoding pitfalls; if needed, hash with a separate function and document it.
- Store no plaintext or reversible encryption of passwords anywhere; the hash is the only acceptable artifact.
- Combine with rate limiting on the login endpoint and account lockout policies to slow offline and online guessing.
- When migrating, use the newer algorithm for new hashes and rehash old credentials lazily on successful login.
- Never log hashes, salts, or password attempts; they are sensitive artifacts even in hashed form.
- Where hardware is weak, benchmark the cost factor and choose the highest that still keeps logins responsive.

## Related
- [[wiki/security/argon2|Argon2]] — successor algorithm
- [[wiki/security/password-hashing|Password Hashing]] — family context
- [[wiki/security/mfa|Multi-Factor Authentication]] — layered auth
- [[wiki/security/oauth2|OAuth 2.0]] — modern auth flows reduce password use
