---
type: "concept"
title: "OAuth 2.0"
description: "Roles, grant types, and endpoints overview"
tags: ["oauth2", "authentication", "authorization", "tokens", "security"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://oauth.net/2/", "https://www.rfc-editor.org/rfc/rfc6749"]
---

# OAuth 2.0

## Summary
OAuth 2.0 (RFC 6749) is the authorization framework that lets users grant third-party apps limited access to their resources without sharing passwords. Four roles — resource owner, client, authorization server, and resource server — interact through grant types that fit different client types, issuing access tokens with scopes.

## Details
- Roles: the resource owner (user) delegates to the client (app), which calls the resource server (API) using tokens issued by the authorization server (IdP).
- Grants: authorization code (with PKCE) for user-facing apps, client credentials for machine-to-machine, device code for TVs/CLIs, and refresh tokens for renewals.
- Tokens: access tokens (short-lived, bearer) authorize API calls; refresh tokens (longer-lived) mint new access tokens without re-login.
- Endpoints: /authorize (user consent), /token (token exchange), and /revoke; discovery (RFC 8414) publishes them at /.well-known/oauth-authorization-server.
- Scopes: fine-grained permissions (read:orders, write:orders) consented to by the user and enforced by the resource server.
- Not authentication: OAuth 2.0 alone does not identify the user — OpenID Connect adds the ID token for identity.
- Security baseline: PKCE for public clients, short-lived access tokens, TLS everywhere, and client secrets never in browsers.

## Related
- [[wiki/api-protocols/oauth2-authorization-code|Authorization Code Flow]] — the standard interactive grant
- [[wiki/api-protocols/oauth2-client-credentials|Client Credentials]] — the machine-to-machine grant
- [[wiki/api-protocols/oauth2-scopes|OAuth Scopes]] — permission granularity
- [[wiki/api-protocols/openid-connect|OpenID Connect]] — identity on top of OAuth 2.0
- [[wiki/security-auth/token-authentication|Token Authentication]] — bearer token validation at APIs
