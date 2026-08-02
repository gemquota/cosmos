---
type: "concept"
title: "Response Splitting"
description: "CRLF-based header injection that appends a second forged HTTP response"
tags: ["security", "http", "injection", "attacks"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---
# Response Splitting

## Summary
CRLF-based header injection that appends a second forged HTTP response. A stub in the mykb wiki that frames the concept and the questions to expand into a full article.

## Details
- Forcing a second response lets attackers poison caches and sessions
- Rejecting CRLF in header values is the primary fix
- Open question — is response splitting fully mitigated by modern frameworks?

## Related
- [[wiki/api-protocols/web-security-owasp|Web Security (OWASP)]] — related coverage in the same cluster
- [[wiki/api-protocols/content-sniffing|Content Sniffing Attacks]] — related coverage in the same cluster
- [[wiki/api-protocols/template-injection|Template Injection]] — related coverage in the same cluster
- [[wiki/api-protocols/sql-injection-practice|SQL Injection]] — related coverage in the same cluster
- [[wiki/security-auth/sql-injection-prevention|SQL Injection Prevention]] — related coverage in the same cluster
- [[wiki/security-auth/command-injection|Command Injection]] — related coverage in the same cluster
- [[wiki/security-auth/ldap-injection|LDAP Injection]] — related coverage in the same cluster
