---
type: "concept"
title: "Mass Assignment"
description: "Over-binding client fields onto server objects when input is bound blindly"
tags: ["security", "api", "validation", "attacks"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---
# Mass Assignment

## Summary
Over-binding client fields onto server objects when input is bound blindly. A stub in the mykb wiki that frames the concept and the questions to expand into a full article.

## Details
- Binding request bodies straight onto models lets clients set protected fields
- Explicit allow-lists of bindable fields prevent role or status overwrites
- Open question — do typed DTO layers eliminate mass assignment in practice?

## Related
- [[wiki/api-protocols/web-security-owasp|Web Security (OWASP)]] — related coverage in the same cluster
- [[wiki/api-protocols/insecure-deserialization|Insecure Deserialization]] — related coverage in the same cluster
- [[wiki/api-protocols/file-upload-security|File Upload Security]] — related coverage in the same cluster
- [[wiki/api-protocols/zip-slip|Zip Slip]] — related coverage in the same cluster
- [[wiki/security-auth/ssrf-prevention|SSRF Prevention]] — related coverage in the same cluster
- [[wiki/security-auth/deserialization-attacks|Deserialization Attacks]] — related coverage in the same cluster
- [[wiki/security-auth/privilege-escalation|Privilege Escalation]] — related coverage in the same cluster
