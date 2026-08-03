---
type: "concept"
title: "Authorization Code Flow"
description: "OAuth grant exchanging an authorization code for tokens at a confidential client"
tags: ["oauth2", "auth", "security", "web"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Authorization Code Flow

## Summary
The authorization code flow is OAuth2's primary flow for confidential and public clients: the user authorizes at the authorization server, the client exchanges a short-lived code for tokens, and tokens never travel through the browser.

## Details
In the authorization code flow, the client redirects the user to the authorization server's /authorize endpoint with client_id, redirect_uri, scope, state, and (for public clients) PKCE parameters. The user authenticates and consents; the server redirects back to the client's redirect_uri with a one-time authorization code plus the echoed state. The client then POSTs the code to /token with its client secret (confidential) or code_verifier (public), and receives access and refresh tokens.

The mechanism that makes it safe: the code is short-lived, single-use, bound to the redirect_uri and client_id, and exchanged over a direct back-channel that browser scripts cannot observe. state prevents login CSRF — the attacker's callback cannot inject a code into the victim's session — and PKCE (RFC 7636) binds the code to a code_challenge so a code intercepted by a rogue app on the device cannot be redeemed by it.

Concrete example: a wiki web app logs in with OIDC. It redirects to the IdP, the user signs in, the IdP returns ?code=abc&state=xyz to the app's callback; the app verifies state, POSTs code plus client_secret to the token endpoint, gets an id_token and access_token, and stores them outside the URL. Refresh tokens let the app keep the session alive without re-prompting.

Failure modes: missing state validation enables login CSRF; PKCE-less public clients are vulnerable to code interception; redirect_uri validation that accepts prefixes enables open redirects and code theft; storing tokens in localStorage exposes them to XSS; and refresh tokens without rotation or reuse detection allow long-lived session theft.

Operational tradeoffs: the flow has more moving parts than implicit or client credentials, but it keeps tokens out of the browser URL and supports refresh, revocation, and consent. For SPAs, pairing the code flow with PKCE and a secure token store (or a backend-for-frontend pattern) is the current baseline; the implicit flow's token-in-URL approach is deprecated for exactly the leakage reasons the code flow avoids.

RSIS3/mykb relevance: if the hub dashboard adds OIDC login, the code flow plus PKCE plus state validation pattern is the standing rule to encode, so RSIS3-generated security reviews check the callback handler's state check.

## Related
- [[wiki/api-protocols/auth-flows-web|Auth Flows on the Web]]
- [[wiki/api-protocols/device-flow|Device Authorization Flow]]
- [[wiki/api-protocols/client-credentials-flow|Client Credentials Flow]]
- [[wiki/api-protocols/oauth2|OAuth 2.0]]
- [[wiki/api-protocols/oauth2-client-credentials|Client Credentials]]
- [[wiki/api-protocols/oauth2-authorization-code|Authorization Code Flow]]
