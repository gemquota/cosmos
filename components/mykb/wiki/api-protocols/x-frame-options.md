---
type: "concept"
title: "X-Frame-Options"
description: "Legacy header that prevents a page from being embedded in frames"
tags: ["security", "http", "headers", "clickjacking"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---
# X-Frame-Options

## Summary
Legacy header that prevents a page from being embedded in frames. A stub in the mykb wiki that frames the concept and the questions to expand into a full article.

## Details
- DENY and SAMEORIGIN block framing in legacy browsers
- frame-ancestors in CSP is the modern replacement
- Open question — is X-Frame-Options still worth sending for compatibility?

## Related
- [[wiki/api-protocols/web-security-owasp|Web Security (OWASP)]] — related coverage in the same cluster
- [[wiki/api-protocols/mime-sniffing|MIME Sniffing]] — related coverage in the same cluster
- [[wiki/api-protocols/nosniff-header|X-Content-Type-Options nosniff]] — related coverage in the same cluster
- [[wiki/api-protocols/hsts-practice|HSTS in Practice]] — related coverage in the same cluster
- [[wiki/security-auth/security-headers|Security Headers]] — related coverage in the same cluster
- [[wiki/security-auth/content-security-policy|Content Security Policy]] — related coverage in the same cluster
- [[wiki/security-auth/same-origin-policy|Same-Origin Policy]] — related coverage in the same cluster
