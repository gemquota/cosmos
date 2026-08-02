---
type: "concept"
title: "ReDoS Attacks"
description: "Catastrophic backtracking in regular expressions causing CPU exhaustion"
tags: ["security", "regex", "dos", "attacks"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---
# ReDoS Attacks

## Summary
Catastrophic backtracking in regular expressions causing CPU exhaustion. A stub in the mykb wiki that frames the concept and the questions to expand into a full article.

## Details
- Catastrophic backtracking blows up on crafted input
- Linear-time matching engines and input length caps prevent ReDoS
- Open question — should regex engines default to linear-time algorithms?

## Related
- [[wiki/api-protocols/web-security-owasp|Web Security (OWASP)]] — related coverage in the same cluster
- [[wiki/api-protocols/decompression-bombs|Decompression Bombs]] — related coverage in the same cluster
- [[wiki/api-protocols/billion-laughs|Billion Laughs]] — related coverage in the same cluster
- [[wiki/api-protocols/entity-expansion|Entity Expansion]] — related coverage in the same cluster
- [[wiki/security-auth/cve-disclosures|CVE Disclosures]] — related coverage in the same cluster
- [[wiki/api-protocols/rate-limiting|Rate Limiting]] — related coverage in the same cluster
- [[wiki/api-protocols/backpressure|Backpressure]] — related coverage in the same cluster
