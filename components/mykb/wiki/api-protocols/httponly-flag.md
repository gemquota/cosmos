---
type: "concept"
title: "HttpOnly Cookie Flag"
description: "Blocking JavaScript access to cookies to blunt XSS theft"
tags: ["cookies", "http", "security", "xss"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---
# HttpOnly Cookie Flag

## Summary
Blocking JavaScript access to cookies to blunt XSS theft. A stub in the mykb wiki that frames the concept and the questions to expand into a full article.

## Details
- HttpOnly keeps cookies out of document.cookie and JS access
- It blunts XSS theft but not CSRF
- Open question — why do some libraries still read auth cookies from JS?

## Related
- [[wiki/api-protocols/secure-cookies|Secure Cookies]] — related coverage in the same cluster
- [[wiki/api-protocols/samesite-lax-strict|SameSite Lax vs Strict]] — related coverage in the same cluster
- [[wiki/api-protocols/cookie-prefixes|Cookie Prefixes]] — related coverage in the same cluster
- [[wiki/api-protocols/cookie-scoping|Cookie Scoping]] — related coverage in the same cluster
- [[wiki/api-protocols/http-cookies|HTTP Cookies]] — related coverage in the same cluster
- [[wiki/api-protocols/csrf|CSRF]] — related coverage in the same cluster
- [[wiki/security-auth/same-origin-policy|Same-Origin Policy]] — related coverage in the same cluster
