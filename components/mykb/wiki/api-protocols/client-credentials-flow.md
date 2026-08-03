---
type: "concept"
title: "Client Credentials Flow"
description: "OAuth grant for machine-to-machine authentication without a user"
tags: ["oauth2", "auth", "m2m", "security"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Client Credentials Flow

## Summary
The client credentials flow lets a service authenticate as itself — no user involved — and receive a token with its own scopes. It is the standard machine-to-machine grant and the one RSIS3-style automation should use.

## Details
In the client credentials grant (RFC 6749 section 4.4), the client POSTs its own credentials (client_id plus client_secret, or a signed JWT assertion) directly to the token endpoint with grant_type=client_credentials and receives an access token representing the client, not a user. There is no redirect, no consent screen, and no refresh-token dance in the classic form — the client can re-request tokens whenever it needs one.

The mechanism: the authorization server authenticates the client (secret, mTLS, or private_key_jwt), checks the requested scope against the client's registered grants, and mints a token whose subject is the client itself. The resource server authorizes based on the client's scopes and roles. Because there is no user, there is no user consent or MFA step; the security boundary is entirely the client's credential storage and the scopes granted.

Concrete example: a batch job that syncs the wiki's graph to a database uses client credentials: the job's config holds client_id and secret, requests scope=graph:write, and gets a 30-minute token. When the job restarts, it simply requests a new token. This is the right pattern for RSIS3 loops calling internal services — no human session, no stored password, scoped to exactly what the loop needs.

Failure modes: storing client secrets in source code or world-readable config turns the flow into a static-key system; granting broad scopes to long-lived client identities magnifies any leak; missing audience validation lets a client token minted for one API work on another; and some implementations skip refresh tokens entirely, which is fine until the token endpoint requires rotation, at which point automated re-auth must be in place.

Operational tradeoffs: client credentials are simple and auditable — the client is the actor — but they cannot express user intent, so any "acting on behalf of a user" requirement means the authorization code flow instead. Token caching matters: minting a token per request is wasteful, so clients should cache and refresh before expiry. Rotation of client secrets should be automated, and mTLS or JWT-based client auth raises the bar over shared secrets.

RSIS3/mykb relevance: this is the canonical grant for RSIS3's own service-to-service calls; the standing rule is scoped client credentials plus secret rotation plus token caching, all of which belong in the wiki's API synthesis notes.

## Related
- [[wiki/api-protocols/auth-flows-web|Auth Flows on the Web]]
- [[wiki/api-protocols/authorization-code-flow|Authorization Code Flow]]
- [[wiki/api-protocols/device-flow|Device Authorization Flow]]
- [[wiki/api-protocols/oauth2|OAuth 2.0]]
- [[wiki/api-protocols/oauth2-client-credentials|Client Credentials]]
- [[wiki/api-protocols/oauth2-authorization-code|Authorization Code Flow]]
