---
type: "concept"
title: "PKCE Flow"
description: "Proof Key for Code Exchange: protecting the authorization code grant on public clients"
tags: ["oauth2", "pkce", "auth", "security", "public-clients"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://www.rfc-editor.org/rfc/rfc7636", "https://oauth.net/2/pkce/"]
---
# PKCE Flow

## Summary
PKCE (Proof Key for Code Exchange) binds the authorization code exchange to the client that started it. The client generates a code verifier, sends its hash as the challenge, and proves possession when exchanging the code. It was designed for mobile and SPA public clients and is now recommended for all clients.

## Details
- **Verifier and challenge** — a high-entropy random verifier is hashed (S256) into the challenge sent with the authorization request; the verifier itself is sent only at the token exchange.
- **Interception defense** — a stolen code is useless without the verifier, which an attacker cannot read from the redirect.
- **Refresh tokens** — public clients typically get rotating refresh tokens; PKCE applies to refresh requests too in the latest guidance.
- **Worked example** — the mykb dashboard generates a verifier per login attempt, stores it in memory, and exchanges with S256; the wiki documents the flow so it is auditable.
- **Relevance** — RSIS3's browser-based UIs and CLI tools are public clients that must use PKCE rather than client secrets.

## Related
- [[wiki/api-protocols/device-flow|Device Authorization Flow]] — adjacent concept in this wiki
- [[wiki/api-protocols/authorization-code-flow|Authorization Code Flow]] — adjacent concept in this wiki
- [[wiki/api-protocols/refresh-token-rotation|Refresh Token Rotation]] — adjacent concept in this wiki
- [[wiki/api-protocols/scope-validation|Scope Validation]] — adjacent concept in this wiki
- [[wiki/api-protocols/oauth2-pkce|PKCE]] — existing coverage
- [[wiki/api-protocols/oauth2-authorization-code|Authorization Code Flow]] — existing coverage
- [[wiki/api-protocols/oauth2-scopes|OAuth Scopes]] — existing coverage
