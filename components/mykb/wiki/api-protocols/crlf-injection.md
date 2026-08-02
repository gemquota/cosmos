---
type: "concept"
title: "CRLF Injection"
description: "Carriage-return line-feed injection that splits headers or logs"
tags: ["security", "http", "injection", "attacks"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---
# CRLF Injection

## Summary
Carriage-return line-feed injection that splits headers or logs. A stub in the mykb wiki that frames the concept and the questions to expand into a full article.

## Details
- Carriage-return line-feed sequences terminate headers early
- Log forgery and cache poisoning are common downstream effects
- Open question — how consistently do servers reject CRLF in values?

## Related
- [[wiki/api-protocols/web-security-owasp|Web Security (OWASP)]] — related coverage in the same cluster
- [[wiki/api-protocols/response-splitting|Response Splitting]] — related coverage in the same cluster
- [[wiki/api-protocols/content-sniffing|Content Sniffing Attacks]] — related coverage in the same cluster
- [[wiki/api-protocols/template-injection|Template Injection]] — related coverage in the same cluster
- [[wiki/security-auth/sql-injection-prevention|SQL Injection Prevention]] — related coverage in the same cluster
- [[wiki/security-auth/command-injection|Command Injection]] — related coverage in the same cluster
- [[wiki/security-auth/ldap-injection|LDAP Injection]] — related coverage in the same cluster
