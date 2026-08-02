---
type: "concept"
title: "X-Content-Type-Options nosniff"
description: "Header that disables MIME sniffing so declared content types are honored"
tags: ["security", "http", "headers", "mime"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---
# X-Content-Type-Options nosniff

## Summary
Header that disables MIME sniffing so declared content types are honored. A stub in the mykb wiki that frames the concept and the questions to expand into a full article.

## Details
- X-Content-Type-Options: nosniff forces declared types to be honored
- It blocks MIME-confusion attacks like script served as image
- Open question — which legacy clients still ignore it?

## Related
- [[wiki/api-protocols/web-security-owasp|Web Security (OWASP)]] — related coverage in the same cluster
- [[wiki/api-protocols/hsts-practice|HSTS in Practice]] — related coverage in the same cluster
- [[wiki/api-protocols/csp-headers|CSP Headers]] — related coverage in the same cluster
- [[wiki/api-protocols/referrer-policy|Referrer Policy]] — related coverage in the same cluster
- [[wiki/security-auth/security-headers|Security Headers]] — related coverage in the same cluster
- [[wiki/security-auth/content-security-policy|Content Security Policy]] — related coverage in the same cluster
- [[wiki/security-auth/same-origin-policy|Same-Origin Policy]] — related coverage in the same cluster
