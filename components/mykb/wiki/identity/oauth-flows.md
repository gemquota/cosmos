---
type: "concept"
title: "OAuth Flows"
description: "The OAuth 2.0 grant types that obtain tokens in different client contexts"
tags: ["oauth2", "flows", "grants", "tokens"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://oauth.net/2/"]
---

# OAuth Flows

## Summary
OAuth 2.0 flows (grant types) are the different ways a client obtains tokens, each designed for a specific client context — a confidential server app, a browser SPA, a mobile app, a daemon, or a device. Choosing the right flow matters because each has distinct token-handling and security properties, and mis-selecting a flow is a common source of token leakage.

## Details
- OAuth 2.0 defines grant types: authorization code (with PKCE), client credentials, refresh token, device, and resource-owner password (deprecated). The authorization-code grant is the workhorse for user-facing apps; PKCE (Proof Key for Code Exchange) protects it for public clients; client credentials serve machine-to-machine; the refresh grant renews access without re-login; the device grant handles TVs and CLI tools; and the password grant is deprecated because it hands credentials to the client.
- Choosing the right flow depends on the client: confidential server apps use code flow, SPAs and mobile use code flow with PKCE, daemons use client credentials. Confidential clients can hold a client secret; public clients (SPAs, mobile) cannot, so PKCE binds the authorization code to the original request and defeats code interception.
- Concrete example: a mobile app logs a user in. It opens the browser, the user authenticates at the provider, the provider returns an authorization code to the app's redirect URI, the app exchanges the code for tokens with PKCE verification — and the app never sees the user's password, only tokens scoped to what the app needs.
- Each flow has distinct token-handling and security properties, and mis-selecting a flow is a common source of token leakage. Storing tokens in an SPA where a public client cannot keep a secret, using the password grant and sending credentials to a compromised client, or using client credentials where user consent is required all leak tokens or over-scope access.
- Failure modes: redirect URI validation gaps, where an attacker's URI receives the code; PKCE omitted on public clients, leaving code interception open; tokens stored in places exposed to XSS; and flows used for the wrong client type, which either leak secrets or fail at runtime.
- Operational practice: use code flow with PKCE for anything that is not a confidential server, keep client secrets out of frontend code, bind refresh tokens to clients, and log which flow each integration uses so misconfigurations are visible.
- For mykb: the flow registry should document which client type each integration uses and why — a one-line rationale per integration prevents the "works in dev, leaks in prod" class of token-handling bugs.

## Related
- [[wiki/identity/oidc-clients|OIDC Clients]] — client types drive flow choice
- [[wiki/identity/refresh-tokens|Refresh Tokens]] — the grant that renews access
- [[wiki/security/oauth2|OAuth 2.0]] — existing article on OAuth 2.0
- [[wiki/security-auth/token-authentication|Token Authentication]] — tokens produced by flows
