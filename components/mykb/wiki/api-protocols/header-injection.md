---
type: "concept"
title: "Header Injection"
description: "Injecting CRLF or other delimiters to forge HTTP response headers"
tags: ["security", "http", "injection", "attacks"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---
# Header Injection

## Summary
Injecting CRLF or other delimiters to forge HTTP response headers. A stub in the mykb wiki that frames the concept and the questions to expand into a full article.

## Details
- CRLF and delimiter injection forges or splits response headers
- Encoding and validating all header values at the sink blocks the class
- Open question — which header values still accept raw newlines in frameworks?

## Related
- [[wiki/api-protocols/web-security-owasp|Web Security (OWASP)]] — related coverage in the same cluster
- [[wiki/api-protocols/crlf-injection|CRLF Injection]] — related coverage in the same cluster
- [[wiki/api-protocols/response-splitting|Response Splitting]] — related coverage in the same cluster
- [[wiki/api-protocols/content-sniffing|Content Sniffing Attacks]] — related coverage in the same cluster
- [[wiki/security-auth/sql-injection-prevention|SQL Injection Prevention]] — related coverage in the same cluster
- [[wiki/security-auth/command-injection|Command Injection]] — related coverage in the same cluster
- [[wiki/security-auth/ldap-injection|LDAP Injection]] — related coverage in the same cluster
