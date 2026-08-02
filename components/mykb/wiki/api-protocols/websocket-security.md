---
type: "concept"
title: "WebSocket Security"
description: "Origin checks, wss, and token authentication"
tags: ["websockets", "security", "authentication", "origin", "tls"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://owasp.org/www-community/attacks/WebSocket_Hijacking", "https://portswigger.net/web-security/websockets"]
---

# WebSocket Security

## Summary
WebSocket security inherits HTTP's threats and adds a few of its own: cross-site WebSocket hijacking, origin spoofing, and token leakage in URLs. The checklist — wss://, Origin validation, token-based auth during the handshake, and message-level authorization — closes most of the surface.

## Details
- Transport: always wss:// (TLS); plain ws:// lets attackers sniff and inject frames — same rationale as HTTPS.
- Cross-site hijacking: a malicious page opens a WebSocket to your API; the browser sends cookies, so the server must validate the Origin header against an allowlist.
- Authentication: authenticate during the handshake — cookies, or better, an Authorization header or a short-lived ticket in a subprotocol or query param (avoid permanent tokens in URLs, which leak in logs).
- Authorization per message: connection auth is not enough; check that the sender may publish/subscribe to each topic (room membership checks server-side).
- CSRF-style defenses: because the handshake is an HTTP request, SameSite cookies and token-based auth both apply; never rely on the Sec-WebSocket-Key for auth.
- Input validation: frames are untrusted input — validate JSON, cap message sizes, and treat WebSocket data like any other request body.
- Reconnect tokens: use short-lived reconnection credentials so a leaked token cannot mint unlimited sessions.

## Related
- [[wiki/api-protocols/websocket-handshake|WebSocket Handshake]] — auth and origin checks happen at upgrade time
- [[wiki/api-protocols/csrf|CSRF]] — cross-site hijacking is a CSRF variant
- [[wiki/security-auth/token-authentication|Token Authentication]] — handshake tokens vs cookie sessions
- [[wiki/api-protocols/websocket-frames|WebSocket Frames]] — frame-level input validation
- [[wiki/api-protocols/cors|CORS]] — CORS rules do not govern WebSockets — Origin checks do
