---
type: "concept"
title: "Billion Laughs"
description: "XML entity-expansion attack that grows output exponentially"
tags: ["security", "xml", "dos", "attacks"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---
# Billion Laughs

## Summary
XML entity-expansion attack that grows output exponentially. A stub in the mykb wiki that frames the concept and the questions to expand into a full article.

## Details
- Nested entity references expand exponentially during XML parsing
- Disabling DTDs and capping entity depth kills the amplification
- Open question — which formats still resolve entities by default?

## Related
- [[wiki/api-protocols/web-security-owasp|Web Security (OWASP)]] — related coverage in the same cluster
- [[wiki/api-protocols/entity-expansion|Entity Expansion]] — related coverage in the same cluster
- [[wiki/api-protocols/timing-attacks|Timing Attacks]] — related coverage in the same cluster
- [[wiki/api-protocols/padding-oracle|Padding Oracle]] — related coverage in the same cluster
- [[wiki/security-auth/cve-disclosures|CVE Disclosures]] — related coverage in the same cluster
- [[wiki/api-protocols/rate-limiting|Rate Limiting]] — related coverage in the same cluster
- [[wiki/api-protocols/backpressure|Backpressure]] — related coverage in the same cluster
