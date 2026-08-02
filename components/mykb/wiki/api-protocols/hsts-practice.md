---
type: "concept"
title: "HSTS in Practice"
description: "HTTP Strict Transport Security header forcing HTTPS-only browser connections"
tags: ["security", "http", "headers", "tls"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---
# HSTS in Practice

## Summary
HTTP Strict Transport Security header forcing HTTPS-only browser connections. A stub in the mykb wiki that frames the concept and the questions to expand into a full article.

## Details
- HSTS forces HTTPS and blocks scheme downgrades via the Strict-Transport-Security header
- Preload lists bootstrap HSTS for first visits
- Open question — how should subdomain and includeSubDomains policies be tuned?

## Related
- [[wiki/api-protocols/web-security-owasp|Web Security (OWASP)]] — related coverage in the same cluster
- [[wiki/api-protocols/csp-headers|CSP Headers]] — related coverage in the same cluster
- [[wiki/api-protocols/referrer-policy|Referrer Policy]] — related coverage in the same cluster
- [[wiki/api-protocols/x-frame-options|X-Frame-Options]] — related coverage in the same cluster
- [[wiki/security-auth/security-headers|Security Headers]] — related coverage in the same cluster
- [[wiki/security-auth/content-security-policy|Content Security Policy]] — related coverage in the same cluster
- [[wiki/security-auth/same-origin-policy|Same-Origin Policy]] — related coverage in the same cluster
