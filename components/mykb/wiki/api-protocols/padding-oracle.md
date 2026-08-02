---
type: "concept"
title: "Padding Oracle"
description: "CBC decryption oracle that reveals plaintext via padding-error responses"
tags: ["security", "crypto", "attacks", "padding"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---
# Padding Oracle

## Summary
CBC decryption oracle that reveals plaintext via padding-error responses. A stub in the mykb wiki that frames the concept and the questions to expand into a full article.

## Details
- CBC padding errors act as a decryption oracle
- Authenticated encryption (AEAD) eliminates padding oracles
- Open question — which legacy CBC cipher suites still linger in services?

## Related
- [[wiki/api-protocols/web-security-owasp|Web Security (OWASP)]] — related coverage in the same cluster
- [[wiki/api-protocols/hash-collision-dos|Hash Collision DoS]] — related coverage in the same cluster
- [[wiki/api-protocols/regex-dos|ReDoS Attacks]] — related coverage in the same cluster
- [[wiki/api-protocols/decompression-bombs|Decompression Bombs]] — related coverage in the same cluster
- [[wiki/security-auth/cve-disclosures|CVE Disclosures]] — related coverage in the same cluster
- [[wiki/api-protocols/rate-limiting|Rate Limiting]] — related coverage in the same cluster
- [[wiki/api-protocols/backpressure|Backpressure]] — related coverage in the same cluster
