---
type: "concept"
title: "CORS"
description: "Preflight, headers, and configuration"
tags: ["cors", "browser-security", "http", "web-platforms", "headers"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS", "https://www.rfc-editor.org/rfc/rfc6454"]
---

# CORS

## Summary
Cross-Origin Resource Sharing (CORS) is the browser mechanism that lets a web app from one origin call APIs on another. The server opts in by sending Access-Control-Allow-* headers; for requests that are not 'simple', the browser first sends a preflight OPTIONS request to check permissions before the real call.

## Details
- Origin model: the browser enforces the Same-Origin Policy; CORS relaxes it for specific origins via response headers.
- Simple requests: GET/POST/HEAD with basic content types and no custom headers skip preflight; anything else (Authorization, JSON, PUT/DELETE) triggers OPTIONS preflight.
- Key headers: Access-Control-Allow-Origin (echo the origin or *), Allow-Methods, Allow-Headers, Expose-Headers, Max-Age, and Allow-Credentials.
- Credentials: with credentials (cookies, TLS client certs), Allow-Origin must be an explicit origin (never *), and Allow-Credentials: true is required.
- Preflight caching: Access-Control-Max-Age lets browsers reuse preflight results, cutting request latency.
- Configuration hygiene: do not blindly allow * with credentials; scope origins to real domains and keep the allowlist explicit.
- CORS is not security: it stops browsers from reading responses, but non-browser clients ignore it entirely — real auth belongs in the API.

## Related
- [[wiki/api-protocols/csrf|CSRF]] — CORS complements CSRF defenses
- [[wiki/api-protocols/http-headers|HTTP Headers]] — the Access-Control-* field family
- [[wiki/security-auth/same-origin-policy|Same-Origin Policy]] — the policy CORS extends
- [[wiki/api-protocols/grpc-web|gRPC-Web]] — browser gRPC needs CORS at the proxy
- [[wiki/api-protocols/websocket-handshake|WebSocket Handshake]] — WebSockets use Origin checks, not CORS
