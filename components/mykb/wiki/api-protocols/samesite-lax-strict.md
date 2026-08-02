---
type: "concept"
title: "SameSite Lax vs Strict"
description: "Cookie scoping that limits cross-site request sending"
tags: ["cookies", "http", "security", "csrf"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---
# SameSite Lax vs Strict

## Summary
Cookie scoping that limits cross-site request sending. A stub in the mykb wiki that frames the concept and the questions to expand into a full article.

## Details
- Lax allows top-level GET navigation; Strict blocks cross-site sends entirely
- Lax is the pragmatic default for most sessions
- Open question — how do SameSite rules affect embedded widgets?

## Related
- [[wiki/api-protocols/secure-cookies|Secure Cookies]] — related coverage in the same cluster
- [[wiki/api-protocols/cookie-prefixes|Cookie Prefixes]] — related coverage in the same cluster
- [[wiki/api-protocols/cookie-scoping|Cookie Scoping]] — related coverage in the same cluster
- [[wiki/api-protocols/domain-cookies|Domain Cookies]] — related coverage in the same cluster
- [[wiki/api-protocols/http-cookies|HTTP Cookies]] — related coverage in the same cluster
- [[wiki/api-protocols/csrf|CSRF]] — related coverage in the same cluster
- [[wiki/security-auth/same-origin-policy|Same-Origin Policy]] — related coverage in the same cluster
