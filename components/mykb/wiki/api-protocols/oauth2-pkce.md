---
type: "concept"
title: "PKCE"
description: "Code verifier and challenge for public clients"
tags: ["oauth2", "pkce", "security", "spa", "authentication"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://www.rfc-editor.org/rfc/rfc7636", "https://oauth.net/2/pkce/"]
---

# PKCE

## Summary
PKCE (Proof Key for Code Exchange, RFC 7636) protects the authorization code flow for public clients — SPAs, mobile apps, and CLIs that cannot keep a client secret. The client generates a random code_verifier, sends only its hash as the code_challenge, and later proves possession of the verifier when exchanging the code.

## Details
- Mechanics: client creates a random verifier (43-128 chars), sends code_challenge (S256 hash or plain) with the authorize request, then sends the verifier with the token request; the server hashes and compares.
- Why it exists: without a client secret, a stolen code is enough to mint tokens — PKCE ties the code to the original client via the verifier.
- S256 vs plain: S256 (SHA-256) is the default and safe; plain is discouraged because the challenge equals the verifier.
- Now standard practice: even confidential clients use PKCE as defense-in-depth (OAuth 2.1 recommends it for all clients).
- Verifier handling: keep it out of logs; the verifier travels with the code exchange and is single-use per authorization.
- It does not replace state: PKCE protects code interception; the state parameter still guards login CSRF.
- Adoption: Auth0, Okta, and most IdPs support PKCE natively; OAuth 2.1 and the new RFC 9700 guidance make it baseline.

## Related
- [[wiki/api-protocols/oauth2-authorization-code|Authorization Code Flow]] — PKCE secures this grant
- [[wiki/api-protocols/oauth2|OAuth 2.0]] — the framework context
- [[wiki/api-protocols/csrf|CSRF]] — state complements PKCE
- [[wiki/api-protocols/oauth2-refresh-tokens|Refresh Tokens]] — public clients rotate refresh tokens
- [[wiki/security-auth/token-authentication|Token Authentication]] — validating the access tokens minted
