---
type: "concept"
title: "CORS with Credentials"
description: "Allowing cross-origin requests that carry cookies and credentials"
tags: ["cors", "security", "http", "web"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# CORS with Credentials

## Summary
CORS with credentials (Access-Control-Allow-Credentials: true) lets cross-origin requests carry cookies and Authorization-adjacent credentials. It must be paired with an explicit origin allowlist, never the wildcard.

## Details
By default, cross-origin fetch requests are sent without cookies and the browser refuses to expose their responses to the calling page. To allow credentialed cross-origin calls, the server must respond with Access-Control-Allow-Credentials: true and Access-Control-Allow-Origin: <exact origin> — the wildcard * is forbidden when credentials are allowed. The browser then includes the origin's cookies on the cross-origin request and lets the page read the response.

The mechanism: the browser's same-origin policy gates both sending and reading. For credentialed requests, the preflight (for non-simple requests) and the actual response must both pass the CORS checks: allow-origin must match the requesting origin exactly (not *), allow-credentials must be true, and allow-methods and allow-headers must cover the request. The Origin header can be forged by a malicious server, but browsers enforce the checks against the response the server actually sends, so the trust anchor is the server's allowlist.

Concrete example: a dashboard at dashboard.example calls api.example with credentials: 'include'. api.example must answer Access-Control-Allow-Origin: https://dashboard.example plus Access-Control-Allow-Credentials: true. If api.example returns Allow-Origin: * instead, the browser blocks the response from being read — good — but the request may still be sent, so CSRF-ish effects on simple requests (GET, form POSTs) remain possible if the API isn't CSRF-protected.

Failure modes: reflecting any Origin (Access-Control-Allow-Origin: <echo>) with credentials lets any website read authenticated responses — full cross-origin data exfiltration; allowing null origins (sandboxed iframes) with credentials enables token theft from file:// or sandbox contexts; and Allow-Credentials on an endpoint that also returns sensitive data with Allow-Origin * silently breaks (browser blocks) but confuses debugging.

Operational tradeoffs: credentialed CORS is required for SPAs that call APIs on another origin and use cookie sessions; the alternative is token-in-header auth (Authorization) with origin-restricted CORS, or a same-origin backend-for-frontend proxy that removes the CORS problem. The baseline: an explicit, maintained allowlist, no wildcard-with-credentials, Vary: Origin, and CSRF protection on top, because CORS never stops the request, only the read.

RSIS3/mykb relevance: if the hub dashboard calls an API cross-origin, the allowlist is infrastructure; documenting which origins are allowed and why keeps RSIS3-generated access reviews accurate.

## Related
- [[wiki/api-protocols/web-security-owasp|Web Security (OWASP)]] — related coverage in the same cluster
- [[wiki/api-protocols/cors-wildcard|CORS Wildcards]] — related coverage in the same cluster
- [[wiki/api-protocols/cross-origin-isolation|Cross-Origin Isolation]] — related coverage in the same cluster
- [[wiki/api-protocols/cors-preflight|CORS Preflight]] — related coverage in the same cluster
- [[wiki/api-protocols/cors|CORS]] — related coverage in the same cluster
- [[wiki/security-auth/cors-policy|CORS Policy]] — related coverage in the same cluster
- [[wiki/security-auth/same-origin-policy|Same-Origin Policy]] — related coverage in the same cluster
