---
type: "concept"
title: "Insecure Deserialization"
description: "Untrusted serialized data that triggers code execution or logic corruption"
tags: ["security", "serialization", "attacks", "api"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---
# Insecure Deserialization

## Summary
Untrusted serialized data that triggers code execution or logic corruption. A stub in the mykb wiki that frames the concept and the questions to expand into a full article.

## Details
- Untrusted bytes fed to deserializers can execute code or corrupt state
- Type allow-lists, signatures, and safe formats like JSON reduce exposure
- Open question — which serializers remain dangerous in 2026?

## Related
- [[wiki/api-protocols/web-security-owasp|Web Security (OWASP)]] — related coverage in the same cluster
- [[wiki/api-protocols/file-upload-security|File Upload Security]] — related coverage in the same cluster
- [[wiki/api-protocols/zip-slip|Zip Slip]] — related coverage in the same cluster
- [[wiki/api-protocols/cache-poisoning|Cache Poisoning]] — related coverage in the same cluster
- [[wiki/security-auth/ssrf-prevention|SSRF Prevention]] — related coverage in the same cluster
- [[wiki/security-auth/deserialization-attacks|Deserialization Attacks]] — related coverage in the same cluster
- [[wiki/security-auth/privilege-escalation|Privilege Escalation]] — related coverage in the same cluster
