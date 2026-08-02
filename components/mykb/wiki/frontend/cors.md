---
type: "concept"
title: "CORS"
description: "Cross-origin request rules and headers"
tags: [security", "cors", "http", "browser", "web-platform"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS", "https://fetch.spec.whatwg.org/#http-cors-protocol"]
---

# CORS

## Summary
Cross-Origin Resource Sharing defines how browsers allow scripts to make cross-origin requests. The server opts in with Access-Control-Allow-Origin and related headers; without them the browser blocks reading the response. CORS complements the same-origin policy by making cross-origin access explicit rather than impossible.

## Details
- Simple requests: GET and POST with basic headers may skip preflight; anything else triggers an OPTIONS preflight first.
- Response headers: Access-Control-Allow-Origin, -Methods, -Headers, and -Credentials permit specific origins, methods, and credentials.
- Credentials: Allow-Credentials: true plus an explicit origin (not *) lets cookies and auth headers cross origins.
- Client effects: preflight failures surface as network errors in fetch, even though the server may have handled the request.
- Server responsibility: CORS is enforced by the browser, not the server — curl bypasses it entirely.
- Workarounds: development proxies, edge rewrites, and API gateways configure CORS centrally instead of per client.

## Related
- [[wiki/security-auth/cors-policy|CORS Policy]] — the security-area deep dive
- [[wiki/security-auth/same-origin-policy|Same-Origin Policy]] — the baseline CORS relaxes
- [[wiki/frontend/fetch-api|Fetch API]] — the client enforcing CORS
- [[wiki/api-protocols/rest-apis|REST APIs]] — typical CORS-protected targets
- [[wiki/frontend/content-security-policy|Content Security Policy]] — the other cross-origin control
- [[wiki/devops-infra/nginx|Nginx]] — configuring CORS at the proxy
