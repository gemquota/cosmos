---
type: "concept"
title: "Zip Slip"
description: "Path traversal via archive entries that escape the extraction directory"
tags: ["security", "file-upload", "attacks", "paths"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---
# Zip Slip

## Summary
Path traversal via archive entries that escape the extraction directory. A stub in the mykb wiki that frames the concept and the questions to expand into a full article.

## Details
- Archive entry names with ../ escape the extraction root
- Canonicalizing and validating entry paths before write prevents traversal
- Open question — how do extraction libraries default on unsafe entries?

## Related
- [[wiki/api-protocols/web-security-owasp|Web Security (OWASP)]] — related coverage in the same cluster
- [[wiki/api-protocols/cache-poisoning|Cache Poisoning]] — related coverage in the same cluster
- [[wiki/api-protocols/request-smuggling|Request Smuggling]] — related coverage in the same cluster
- [[wiki/api-protocols/ssrf-practice|SSRF Attacks]] — related coverage in the same cluster
- [[wiki/security-auth/ssrf-prevention|SSRF Prevention]] — related coverage in the same cluster
- [[wiki/security-auth/deserialization-attacks|Deserialization Attacks]] — related coverage in the same cluster
- [[wiki/security-auth/privilege-escalation|Privilege Escalation]] — related coverage in the same cluster
