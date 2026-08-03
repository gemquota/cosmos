---
type: "concept"
title: "Bearer Tokens"
description: "Authorization header tokens whose possession proves identity"
tags: ["http", "auth", "tokens", "security"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Bearer Tokens

## Summary
A bearer token is any string whose possession alone grants access: Authorization: Bearer <token>. Its simplicity is also its risk — anyone holding it can use it, so transport security, short lifetimes, and scopes are load-bearing.

## Details
Bearer tokens (RFC 6750) are presented as Authorization: Bearer <token>. The server trusts the token's mere presence: no additional proof of identity is required at request time. OAuth2 access tokens and most API session tokens are bearer by default. The token is usually opaque (a random ID the server looks up) or structured (a JWT the server verifies), but the wire format is the same.

The mechanism: the resource server extracts the header, validates the token (lookup, or signature plus expiry plus scope plus audience), and maps it to a principal and permissions. Because there is no per-request cryptographic proof of possession, a token copied out of logs, memory, or a client bundle works from anywhere — which is why bearer tokens demand TLS everywhere, short lifetimes, scoped grants, and careful storage.

Concrete example: a mobile app gets a five-minute access token from the IdP and sends it on every API call. If it leaks into a proxy log, the window of abuse is minutes, and the refresh token — kept in secure storage, never sent to resource servers — lets the legitimate client recover. Contrast with a long-lived API key sent in a URL or stored in plaintext config: leak and forget.

Failure modes: sending bearer tokens in URLs (query params) leaks them to logs, referrers, and browser history; tokens without expiry or scope become permanent, universal keys; validating only signature and forgetting audience or issuer lets tokens flow across services; and XSS or overly permissive CORS can exfiltrate tokens from localStorage or cookies.

Operational tradeoffs: bearer tokens are trivially simple for every client and library, at the cost of making token theft equivalent to account takeover; proof-of-possession schemes (DPoP, mTLS-bound tokens) raise the bar but add complexity and break naive clients. The pragmatic baseline: TLS, short access-token lifetime, refresh rotation, scoped tokens, and token storage out of reach of XSS.

RSIS3/mykb relevance: RSIS3's check-practices can flag any credential that is bearer-style without expiry; documenting the token lifecycle contract here gives the loop a concrete checklist.

## Related
- [[wiki/api-protocols/auth-flows-web|Auth Flows on the Web]] — related coverage in the same cluster
- [[wiki/api-protocols/m2m-tokens|Machine-to-Machine Tokens]] — related coverage in the same cluster
- [[wiki/api-protocols/api-keys-vs-tokens|API Keys vs Tokens]] — related coverage in the same cluster
- [[wiki/api-protocols/api-basic-auth|API Basic Auth]] — related coverage in the same cluster
- [[wiki/api-protocols/api-authentication-methods|API Authentication Methods]] — related coverage in the same cluster
- [[wiki/api-protocols/api-keys|API Keys]] — related coverage in the same cluster
- [[wiki/api-protocols/basic-authentication|Basic Authentication]] — related coverage in the same cluster
