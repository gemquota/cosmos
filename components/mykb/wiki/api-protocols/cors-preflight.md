---
type: "concept"
title: "CORS Preflight"
description: "OPTIONS request browsers send before risky cross-origin requests"
tags: ["cors", "http", "security", "browsers"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---
# CORS Preflight

## Summary
OPTIONS request browsers send before risky cross-origin requests. A stub in the mykb wiki that frames the concept and the questions to expand into a full article.

## Details
- Preflights are OPTIONS requests with Access-Control-Request-Method and -Headers
- They gate non-simple methods, headers, and credentials
- Open question — how much latency do preflights add in practice?

## Related
- [[wiki/api-protocols/web-security-owasp|Web Security (OWASP)]] — related coverage in the same cluster
- [[wiki/api-protocols/cors-credentials|CORS with Credentials]] — related coverage in the same cluster
- [[wiki/api-protocols/cors-wildcard|CORS Wildcards]] — related coverage in the same cluster
- [[wiki/api-protocols/cross-origin-isolation|Cross-Origin Isolation]] — related coverage in the same cluster
- [[wiki/api-protocols/cors|CORS]] — related coverage in the same cluster
- [[wiki/security-auth/cors-policy|CORS Policy]] — related coverage in the same cluster
- [[wiki/security-auth/same-origin-policy|Same-Origin Policy]] — related coverage in the same cluster
