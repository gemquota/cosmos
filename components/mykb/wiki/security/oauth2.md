---
type: "concept"
title: "OAuth 2.0"
description: "Authorization framework granting scoped, delegated access to protected resources via tokens"
tags: ["oauth2", "authn", "authz", "security", "tokens"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
source: ["https://www.rfc-editor.org/rfc/rfc6749"]
---

# OAuth 2.0

## Summary
OAuth 2.0 (RFC 6749) is an authorization framework that lets applications obtain limited, scoped access to a user's resources without sharing passwords. The resource owner authorizes a client, which exchanges an authorization grant for an access token from an authorization server. It is the industry standard behind "Sign in with Google/GitHub" and most modern API security.

## Details
- Roles: resource owner, client (app), authorization server, and resource server; tokens are presented to the resource server, never the user's password.
- Grant types: authorization code (with PKCE for public clients), client credentials (machine-to-machine), refresh token, and device flow.
- Scopes constrain what a token may do (`read:notes`, `write:notes`), and the authorization server issues only approved scopes.
- Tokens are opaque or JWT-encoded; short-lived access tokens plus refresh tokens reduce blast radius if one leaks.
- OpenID Connect (OIDC) layers identity on top: the `id_token` and `userinfo` endpoint answer "who is the user" while OAuth answers "what may the app do".
- Worked example: mykb could act as an OAuth resource server protecting `/api/notes`, with RSIS3 authenticating via client-credentials flow and scoped tokens.
- Relationship: OAuth pairs with [[wiki/security/jwt|JWT]] for self-contained tokens and [[wiki/security/sso|Single Sign-On]] for cross-app identity.

## Related
- [[wiki/security/jwt|JWT]] — common access-token format
- [[wiki/security/sso|Single Sign-On]] — OAuth/OIDC as the SSO backbone
- [[wiki/security/passkeys|Passkeys]] — passwordless authentication feeding identity providers
- [[wiki/api-protocols/rest-apis|REST APIs]] — token-protected resource servers
- [[wiki/api-protocols/rate-limiting|Rate Limiting]] — per-principal limits via token identity
- [[wiki/security/zero-trust|Zero Trust Architecture]] — continuous verification of token holders
- [[wiki/concepts/triad-architecture|Triad Architecture]] — engine-to-memory bridge authentication
- [[wiki/ops/gap-report|Gap Analysis Report]] — auth coverage gaps tracked
