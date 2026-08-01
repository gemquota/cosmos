---
type: "concept"
title: "OIDC Clients"
description: "Applications registered with an OpenID provider to request authentication and tokens"
tags: ["oidc", "clients", "registration", "openid-connect"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
source: ["https://openid.net/specs/openid-connect-core-1_0.html"]
---

# OIDC Clients

- An OIDC client (relying party) registers with an OpenID provider, obtaining a client ID and secret (or public-client configuration) plus redirect URIs.
- Registration parameters — redirect URIs, response types, scopes, and token endpoint auth method — define the client's security posture.
- Public clients (SPAs, mobile) must use PKCE because they cannot protect a secret; confidential clients store secrets server-side.
- For mykb: each RSIS3 integration should be a registered client with locked-down redirect URIs and minimal scopes.

## Related

- [[wiki/identity/openid-connect|OpenID Connect]] — the protocol clients participate in
- [[wiki/identity/oauth-flows|OAuth Flows]] — flows depend on client type
- [[wiki/security/oauth2|OAuth 2.0]] — the underlying framework
- [[wiki/security-auth/least-privilege|Least Privilege]] — minimal scopes per client
