---
type: "concept"
title: "Decompression Bombs"
description: "Small compressed payloads that expand to enormous output, exhausting memory"
tags: ["security", "dos", "compression", "attacks"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---
# Decompression Bombs

## Summary
Small compressed payloads that expand to enormous output, exhausting memory. A stub in the mykb wiki that frames the concept and the questions to expand into a full article.

## Details
- Zip bombs and gzip bombs expand far beyond their wire size
- Ratio limits, uncompressed-size caps, and streaming checks bound damage
- Open question — how do HTTP decompression middleboxes enforce limits?

## Related
- [[wiki/api-protocols/web-security-owasp|Web Security (OWASP)]] — related coverage in the same cluster
- [[wiki/api-protocols/billion-laughs|Billion Laughs]] — related coverage in the same cluster
- [[wiki/api-protocols/entity-expansion|Entity Expansion]] — related coverage in the same cluster
- [[wiki/api-protocols/timing-attacks|Timing Attacks]] — related coverage in the same cluster
- [[wiki/security-auth/cve-disclosures|CVE Disclosures]] — related coverage in the same cluster
- [[wiki/api-protocols/rate-limiting|Rate Limiting]] — related coverage in the same cluster
- [[wiki/api-protocols/backpressure|Backpressure]] — related coverage in the same cluster
