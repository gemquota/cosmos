---
type: "concept"
title: "SSRF Attacks"
description: "Server-Side Request Forgery: abusing server fetches to reach internal services"
tags: ["security", "ssrf", "api", "attacks"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---
# SSRF Attacks

## Summary
Server-Side Request Forgery: abusing server fetches to reach internal services. A stub in the mykb wiki that frames the concept and the questions to expand into a full article.

## Details
- SSRF turns server-side fetches into probes of internal networks
- Deny-lists of localhost and metadata IPs are insufficient; allow-lists and SSRF-aware proxies help
- Open question — how do agent tool-fetch features scope SSRF risk?

## Related
- [[wiki/api-protocols/web-security-owasp|Web Security (OWASP)]] — related coverage in the same cluster
- [[wiki/api-protocols/idor-web|IDOR on the Web]] — related coverage in the same cluster
- [[wiki/api-protocols/mass-assignment|Mass Assignment]] — related coverage in the same cluster
- [[wiki/api-protocols/insecure-deserialization|Insecure Deserialization]] — related coverage in the same cluster
- [[wiki/security-auth/ssrf-prevention|SSRF Prevention]] — related coverage in the same cluster
- [[wiki/security-auth/deserialization-attacks|Deserialization Attacks]] — related coverage in the same cluster
- [[wiki/security-auth/privilege-escalation|Privilege Escalation]] — related coverage in the same cluster
