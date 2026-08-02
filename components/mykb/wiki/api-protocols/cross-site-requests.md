---
type: "concept"
title: "Cross-Site Requests"
description: "How browsers attach credentials to requests across sites and origins"
tags: ["cookies", "cors", "security", "web"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---
# Cross-Site Requests

## Summary
How browsers attach credentials to requests across sites and origins. A stub in the mykb wiki that frames the concept and the questions to expand into a full article.

## Details
- Site, not origin, determines cross-site credential behavior
- SameSite and CORS jointly govern what browsers send and expose
- Open question — how do agents reason about site versus origin?

## Related
- [[wiki/api-protocols/secure-cookies|Secure Cookies]] — related coverage in the same cluster
- [[wiki/api-protocols/cookie-flags|Cookie Flags]] — related coverage in the same cluster
- [[wiki/api-protocols/secure-flag|Secure Cookie Flag]] — related coverage in the same cluster
- [[wiki/api-protocols/httponly-flag|HttpOnly Cookie Flag]] — related coverage in the same cluster
- [[wiki/api-protocols/http-cookies|HTTP Cookies]] — related coverage in the same cluster
- [[wiki/api-protocols/csrf|CSRF]] — related coverage in the same cluster
- [[wiki/security-auth/same-origin-policy|Same-Origin Policy]] — related coverage in the same cluster
