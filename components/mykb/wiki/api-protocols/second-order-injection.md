---
type: "concept"
title: "Second-Order Injection"
description: "Payloads stored safely at write time but executed later at a different sink"
tags: ["security", "injection", "attacks", "data"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---
# Second-Order Injection

## Summary
Payloads stored safely at write time but executed later at a different sink. A stub in the mykb wiki that frames the concept and the questions to expand into a full article.

## Details
- Payloads stored innocently at write time execute at a later, different sink
- Escaping at every sink, not just at the first one, is the defense
- Open question — how do pipelines track taint across storage boundaries?

## Related
- [[wiki/api-protocols/web-security-owasp|Web Security (OWASP)]] — related coverage in the same cluster
- [[wiki/api-protocols/blind-injection|Blind Injection]] — related coverage in the same cluster
- [[wiki/api-protocols/header-injection|Header Injection]] — related coverage in the same cluster
- [[wiki/api-protocols/crlf-injection|CRLF Injection]] — related coverage in the same cluster
- [[wiki/security-auth/sql-injection-prevention|SQL Injection Prevention]] — related coverage in the same cluster
- [[wiki/security-auth/command-injection|Command Injection]] — related coverage in the same cluster
- [[wiki/security-auth/ldap-injection|LDAP Injection]] — related coverage in the same cluster
