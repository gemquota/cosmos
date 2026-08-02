---
type: "concept"
title: "Request Smuggling"
description: "Exploiting parser discrepancies between proxies and backends to smuggle requests"
tags: ["security", "http", "proxies", "attacks"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---
# Request Smuggling

## Summary
Exploiting parser discrepancies between proxies and backends to smuggle requests. A stub in the mykb wiki that frames the concept and the questions to expand into a full article.

## Details
- Front-end and back-end disagree on Content-Length vs Transfer-Encoding
- Smuggled requests poison connections shared by other users
- Open question — how do modern proxies normalize desync safely?

## Related
- [[wiki/api-protocols/web-security-owasp|Web Security (OWASP)]] — related coverage in the same cluster
- [[wiki/api-protocols/ssrf-practice|SSRF Attacks]] — related coverage in the same cluster
- [[wiki/api-protocols/idor-web|IDOR on the Web]] — related coverage in the same cluster
- [[wiki/api-protocols/mass-assignment|Mass Assignment]] — related coverage in the same cluster
- [[wiki/security-auth/ssrf-prevention|SSRF Prevention]] — related coverage in the same cluster
- [[wiki/security-auth/deserialization-attacks|Deserialization Attacks]] — related coverage in the same cluster
- [[wiki/security-auth/privilege-escalation|Privilege Escalation]] — related coverage in the same cluster
