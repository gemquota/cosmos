---
type: "concept"
title: "Timing Attacks"
description: "Side-channel leaks of secrets through measurable processing-time differences"
tags: ["security", "timing", "crypto", "attacks"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Timing Attacks

## Summary
Timing attacks are side-channel attacks that recover secrets by measuring how long operations take. If a comparison exits early on the first mismatched byte, an attacker who can time many guesses can infer the secret one byte at a time; similar channels exist in padding validation, cache behavior, and modular exponentiation. The defense is to make the critical paths run in constant time.

## Details
- Mechanism: the canonical example is password or MAC comparison implemented as `memcmp` or a loop that returns at the first mismatch. A guess that matches the first byte takes slightly longer than one that does not, and over thousands of samples a local or even remote attacker can recover the full value byte by byte. Cryptography adds richer channels: RSA and ECC implementations leak key bits through multiplication and squaring time, AES leaks through cache access patterns on lookup tables, and padding-oracle attacks exploit the timing difference between valid and invalid padding.
- Concrete examples: the Lucky13 attack on TLS uses padding-validation timing to recover plaintext; the Cache-timing attacks (like those on AES-NI lookup tables) use shared CPU caches to extract keys; on web servers, username enumeration and token validation loops can be timed to test guesses remotely. Even a login endpoint whose response body is identical but whose processing time differs by a few microseconds can be exploited with enough samples.
- Failure modes: the classic failure is a well-intentioned "constant-time" function that is not constant in practice — branches on secret data, data-dependent table indexing, or compiler optimizations that transform the code after review. Language-level equality operators on strings (`==` in Python, `equals` in Java) short-circuit on mismatch and are the most common accidental leak. Network jitter used to make remote timing seem impractical, but HTTP/2 multiplexing and statistical averaging have made remote attacks practical.
- Operational tradeoffs: use library-provided constant-time comparison (`hmac.compare_digest` in Python, `MessageDigest.isEqual` in Java) for secrets, keep cryptographic operations in audited libraries with constant-time guarantees, and avoid branching on secret-dependent values at the application layer. Where absolute constant time is impossible, add noise or bounds: rate-limit attempts, pad responses to a fixed time, and reject large batches of requests. The tradeoff is measurable performance cost in crypto paths, which is why blinding and fixed-window exponentiation exist.
- RSIS3/mykb relevance: any secret comparison in the RSIS3 stack — API tokens, registry checksums, webhook signature verification — should use constant-time primitives, and loop hygiene should treat hand-rolled equality as a review flag, since a leak in the memory layer's auth path compromises everything downstream.

## Related
- [[wiki/api-protocols/web-security-owasp|Web Security (OWASP)]] — related coverage in the same cluster
- [[wiki/api-protocols/padding-oracle|Padding Oracle]] — related coverage in the same cluster
- [[wiki/api-protocols/hash-collision-dos|Hash Collision DoS]] — related coverage in the same cluster
- [[wiki/api-protocols/regex-dos|ReDoS Attacks]] — related coverage in the same cluster
- [[wiki/security-auth/cve-disclosures|CVE Disclosures]] — related coverage in the same cluster
- [[wiki/api-protocols/rate-limiting|Rate Limiting]] — related coverage in the same cluster
- [[wiki/api-protocols/backpressure|Backpressure]] — related coverage in the same cluster
