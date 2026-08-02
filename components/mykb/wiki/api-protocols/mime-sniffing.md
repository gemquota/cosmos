---
type: "concept"
title: "MIME Sniffing"
description: "Browser behavior that guesses a resource type when Content-Type is absent or wrong"
tags: ["security", "http", "mime", "browsers"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---
# MIME Sniffing

## Summary
Browser behavior that guesses a resource type when Content-Type is absent or wrong. A stub in the mykb wiki that frames the concept and the questions to expand into a full article.

## Details
- Browsers guess types when headers are absent or ambiguous
- Sniffing enables drive-by execution of attacker-chosen formats
- Open question — how does modern Chrome reconcile sniffing with security?

## Related
- [[wiki/api-protocols/web-security-owasp|Web Security (OWASP)]] — related coverage in the same cluster
- [[wiki/api-protocols/nosniff-header|X-Content-Type-Options nosniff]] — related coverage in the same cluster
- [[wiki/api-protocols/hsts-practice|HSTS in Practice]] — related coverage in the same cluster
- [[wiki/api-protocols/csp-headers|CSP Headers]] — related coverage in the same cluster
- [[wiki/security-auth/security-headers|Security Headers]] — related coverage in the same cluster
- [[wiki/security-auth/content-security-policy|Content Security Policy]] — related coverage in the same cluster
- [[wiki/security-auth/same-origin-policy|Same-Origin Policy]] — related coverage in the same cluster
