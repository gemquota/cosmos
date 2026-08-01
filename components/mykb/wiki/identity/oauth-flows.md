---
type: "concept"
title: "OAuth Flows"
description: "The OAuth 2.0 grant types that obtain tokens in different client contexts"
tags: ["oauth2", "flows", "grants", "tokens"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
source: ["https://oauth.net/2/"]
---

# OAuth Flows

- OAuth 2.0 defines grant types: authorization code (with PKCE), client credentials, refresh token, device, and resource-owner password (deprecated).
- Choosing the right flow depends on the client: confidential server apps use code flow, SPAs and mobile use code flow with PKCE, daemons use client credentials.
- Each flow has distinct token-handling and security properties, and mis-selecting a flow is a common source of token leakage.
- For mykb: the flow registry should document which client type each integration uses and why.

## Related

- [[wiki/identity/oidc-clients|OIDC Clients]] — client types drive flow choice
- [[wiki/identity/refresh-tokens|Refresh Tokens]] — the grant that renews access
- [[wiki/security/oauth2|OAuth 2.0]] — existing article on OAuth 2.0
- [[wiki/security-auth/token-authentication|Token Authentication]] — tokens produced by flows
