---
type: "concept"
title: "OAuth Scopes"
description: "Scope design and consent granularity"
tags: ["oauth2", "scopes", "authorization", "permissions", "api-design"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://oauth.net/2/scope/", "https://www.rfc-editor.org/rfc/rfc6749#section-3.3"]
---

# OAuth Scopes

## Summary
OAuth scopes are strings that bound what a token may do: scope=read:orders write:orders. They turn blanket access into granular, consentable permissions — the resource server must enforce them, the authorization server must present them for consent, and the client should request the least it needs.

## Details
- Format conventions: namespaced verbs over nouns (read:orders, write:orders) or resource:action pairs; match the API's resources.
- Consent: the authorization server shows the user exactly which scopes are requested; unknown or excessive scopes are the classic over-request anti-pattern.
- Enforcement: resource servers validate the token's scope claim per endpoint — scope checking is server-side, never assumed from the token type.
- Least privilege: request only what the current screen needs, and split APIs by scope families so clients can compose.
- Granularity trade-offs: too fine (read:order.status) is unmanageable; too coarse (api.all) defeats consent; aim for resource-level actions.
- Custom vs standardized: many providers define custom scopes; OIDC standardizes openid, profile, email, and offline_access.
- Evolution: adding scopes is backward-compatible; changing semantics or removing scopes breaks existing tokens and clients.

## Related
- [[wiki/api-protocols/oauth2|OAuth 2.0]] — scopes are the authorization payload
- [[wiki/api-protocols/oauth2-authorization-code|Authorization Code Flow]] — consent happens in the authorize step
- [[wiki/api-protocols/api-authentication-methods|API Authentication Methods]] — scope granularity vs API keys
- [[wiki/security-auth/least-privilege|Least Privilege]] — scopes implement least privilege
- [[wiki/api-protocols/openid-connect|OpenID Connect]] — OIDC scopes add identity claims
