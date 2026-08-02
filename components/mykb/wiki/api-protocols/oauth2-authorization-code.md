---
type: "concept"
title: "Authorization Code Flow"
description: "The standard OAuth grant end to end"
tags: ["oauth2", "authorization-code", "oauth", "security", "authentication"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://www.rfc-editor.org/rfc/rfc6749#section-4.1", "https://oauth.net/2/grant-types/authorization-code/"]
---

# Authorization Code Flow

## Summary
The authorization code grant is OAuth 2.0's primary flow for user-facing apps: the user authorizes in the browser, the authorization server returns a short-lived code to the app, and the app exchanges that code for tokens at the token endpoint — keeping secrets and tokens off the browser's JavaScript context.

## Details
- Steps: redirect to /authorize -> user signs in and consents -> auth server redirects with ?code= -> app POSTs code + client credentials to /token -> receives access + refresh tokens.
- Why a code, not tokens: the browser sees only a one-time code; token exchange happens server-side, so tokens never live in browser storage.
- One-time and short-lived: codes expire in minutes and are single-use; replaying a code is an error (and a red flag).
- State parameter: the app sends a random state and verifies it on return, preventing login CSRF.
- PKCE: public clients (SPAs, mobile) add a code_verifier/code_challenge so a stolen code cannot be exchanged without the verifier.
- Redirect URIs: must be registered and matched exactly; wildcards and open redirectors are a leading account-takeover vector.
- Response modes: query, fragment (implicit-style), and form_post; the code flow uses query for the redirect.

## Related
- [[wiki/api-protocols/oauth2|OAuth 2.0]] — the framework this grant belongs to
- [[wiki/api-protocols/oauth2-pkce|PKCE]] — mandatory protection for public clients
- [[wiki/api-protocols/oauth2-refresh-tokens|Refresh Tokens]] — token renewal after the code exchange
- [[wiki/api-protocols/oauth2-scopes|OAuth Scopes]] — consented permissions
- [[wiki/api-protocols/csrf|CSRF]] — state parameter defends the redirect
