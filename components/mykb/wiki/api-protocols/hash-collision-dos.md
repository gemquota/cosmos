---
type: "concept"
title: "Hash Collision DoS"
description: "Forcing many same-bucket hashes to degrade map lookups to linear time"
tags: ["security", "dos", "hashing", "attacks"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---
# Hash Collision DoS

## Summary
Forcing many same-bucket hashes to degrade map lookups to linear time. A stub in the mykb wiki that frames the concept and the questions to expand into a full article.

## Details
- Attacker-chosen keys colliding into one bucket degrade map operations
- Randomized hashing and bounded bucket behavior blunt the attack
- Open question — how do language runtimes defend hash maps in 2026?

## Related
- [[wiki/api-protocols/web-security-owasp|Web Security (OWASP)]] — related coverage in the same cluster
- [[wiki/api-protocols/regex-dos|ReDoS Attacks]] — related coverage in the same cluster
- [[wiki/api-protocols/decompression-bombs|Decompression Bombs]] — related coverage in the same cluster
- [[wiki/api-protocols/billion-laughs|Billion Laughs]] — related coverage in the same cluster
- [[wiki/security-auth/cve-disclosures|CVE Disclosures]] — related coverage in the same cluster
- [[wiki/api-protocols/rate-limiting|Rate Limiting]] — related coverage in the same cluster
- [[wiki/api-protocols/backpressure|Backpressure]] — related coverage in the same cluster
