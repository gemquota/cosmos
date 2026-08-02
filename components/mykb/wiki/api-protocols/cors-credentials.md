---
type: "concept"
title: "CORS with Credentials"
description: "Cross-origin requests that carry cookies, TLS client certs, or HTTP auth"
tags: ["cors", "http", "security", "cookies"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---
# CORS with Credentials

## Summary
Cross-origin requests that carry cookies, TLS client certs, or HTTP auth. A stub in the mykb wiki that frames the concept and the questions to expand into a full article.

## Details
- Credentials mode allows cookies, client certs, and HTTP auth cross-origin
- Access-Control-Allow-Credentials: true is required and forbids wildcard origins
- Open question — when is sharing credentials cross-origin justified?

## Related
- [[wiki/api-protocols/web-security-owasp|Web Security (OWASP)]] — related coverage in the same cluster
- [[wiki/api-protocols/cors-wildcard|CORS Wildcards]] — related coverage in the same cluster
- [[wiki/api-protocols/cross-origin-isolation|Cross-Origin Isolation]] — related coverage in the same cluster
- [[wiki/api-protocols/cors-preflight|CORS Preflight]] — related coverage in the same cluster
- [[wiki/api-protocols/cors|CORS]] — related coverage in the same cluster
- [[wiki/security-auth/cors-policy|CORS Policy]] — related coverage in the same cluster
- [[wiki/security-auth/same-origin-policy|Same-Origin Policy]] — related coverage in the same cluster
