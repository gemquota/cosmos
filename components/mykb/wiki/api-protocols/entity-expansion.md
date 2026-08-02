---
type: "concept"
title: "Entity Expansion"
description: "XML and HTML entities abused to amplify payload size during parsing"
tags: ["security", "xml", "dos", "attacks"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---
# Entity Expansion

## Summary
XML and HTML entities abused to amplify payload size during parsing. A stub in the mykb wiki that frames the concept and the questions to expand into a full article.

## Details
- Entity expansion amplifies small input into large parsed trees
- Billion-laughs is the extreme; even modest expansion taxes parsers
- Open question — do JSON parsers have an analogous amplification vector?

## Related
- [[wiki/api-protocols/web-security-owasp|Web Security (OWASP)]] — related coverage in the same cluster
- [[wiki/api-protocols/timing-attacks|Timing Attacks]] — related coverage in the same cluster
- [[wiki/api-protocols/padding-oracle|Padding Oracle]] — related coverage in the same cluster
- [[wiki/api-protocols/hash-collision-dos|Hash Collision DoS]] — related coverage in the same cluster
- [[wiki/security-auth/cve-disclosures|CVE Disclosures]] — related coverage in the same cluster
- [[wiki/api-protocols/rate-limiting|Rate Limiting]] — related coverage in the same cluster
- [[wiki/api-protocols/backpressure|Backpressure]] — related coverage in the same cluster
