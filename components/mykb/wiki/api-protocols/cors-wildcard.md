---
type: "concept"
title: "CORS Wildcards"
description: "Using * in Access-Control-Allow-* headers and its restrictions with credentials"
tags: ["cors", "http", "security", "headers"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---
# CORS Wildcards

## Summary
Using * in Access-Control-Allow-* headers and its restrictions with credentials. A stub in the mykb wiki that frames the concept and the questions to expand into a full article.

## Details
- * is allowed for origins and methods but not credentialed requests
- Wildcards still expose endpoints to any site
- Open question — do per-origin allowlists beat wildcard plus token auth?

## Related
- [[wiki/api-protocols/web-security-owasp|Web Security (OWASP)]] — related coverage in the same cluster
- [[wiki/api-protocols/cross-origin-isolation|Cross-Origin Isolation]] — related coverage in the same cluster
- [[wiki/api-protocols/cors-preflight|CORS Preflight]] — related coverage in the same cluster
- [[wiki/api-protocols/cors-credentials|CORS with Credentials]] — related coverage in the same cluster
- [[wiki/api-protocols/cors|CORS]] — related coverage in the same cluster
- [[wiki/security-auth/cors-policy|CORS Policy]] — related coverage in the same cluster
- [[wiki/security-auth/same-origin-policy|Same-Origin Policy]] — related coverage in the same cluster
