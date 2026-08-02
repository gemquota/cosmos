---
type: "concept"
title: "Basic Authentication"
description: "HTTP Basic auth mechanics and risks"
tags: ["basic-auth", "authentication", "http", "security", "legacy"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://www.rfc-editor.org/rfc/rfc7617", "https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Authorization"]
---

# Basic Authentication

## Summary
HTTP Basic authentication (RFC 7617) sends username:password base64-encoded in the Authorization header: Authorization: Basic dXNlcjpwYXNz. It is trivially simple and universally supported — and just as trivially dangerous without TLS, since the credential is one decode away from plaintext.

## Details
- Mechanics: the client sends credentials on every request; the server responds 401 with WWW-Authenticate: Basic realm="..." when they are missing or wrong.
- Encoding, not encryption: base64 is reversible, so Basic auth must never travel without TLS; over HTTP it is plaintext on the wire.
- No logout or expiry: credentials are replayed forever until changed — no token revocation, no session lifecycle.
- Browser UX: browsers show a native prompt and cache credentials per realm, which encourages password reuse behavior.
- Legitimate niches: initial device/API bootstrap, internal tools, and legacy systems; many services accept it only as a migration path to tokens.
- Brute force: no rate limiting by design, so servers must add throttling and lockout themselves; consider constant-time comparisons.
- Password storage: the server must still store passwords securely (hashed) — Basic auth only changes the transport, not the vault.

## Related
- [[wiki/api-protocols/api-authentication-methods|API Authentication Methods]] — where Basic sits in the taxonomy
- [[wiki/api-protocols/oauth2|OAuth 2.0]] — the modern replacement for user credentials
- [[wiki/api-protocols/api-keys|API Keys]] — key-based alternative for machine clients
- [[wiki/security-auth/least-privilege|Least Privilege]] — credential scoping mitigates Basic's bluntness
- [[wiki/api-protocols/tls-handshake|TLS Handshake]] — TLS is the non-negotiable companion
