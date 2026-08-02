---
type: "concept"
title: "Cache Poisoning"
description: "Injecting malicious content into shared caches so victims receive attacker-served responses"
tags: ["security", "caching", "http", "attacks"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---
# Cache Poisoning

## Summary
Injecting malicious content into shared caches so victims receive attacker-served responses. A stub in the mykb wiki that frames the concept and the questions to expand into a full article.

## Details
- Attackers seed caches with responses that serve malicious content to later visitors
- Keying on host, path, and method alone makes poisoning easy
- Open question — how should caches key on Vary and request parameters?

## Related
- [[wiki/api-protocols/web-security-owasp|Web Security (OWASP)]] — related coverage in the same cluster
- [[wiki/api-protocols/request-smuggling|Request Smuggling]] — related coverage in the same cluster
- [[wiki/api-protocols/ssrf-practice|SSRF Attacks]] — related coverage in the same cluster
- [[wiki/api-protocols/idor-web|IDOR on the Web]] — related coverage in the same cluster
- [[wiki/security-auth/ssrf-prevention|SSRF Prevention]] — related coverage in the same cluster
- [[wiki/security-auth/deserialization-attacks|Deserialization Attacks]] — related coverage in the same cluster
- [[wiki/security-auth/privilege-escalation|Privilege Escalation]] — related coverage in the same cluster
