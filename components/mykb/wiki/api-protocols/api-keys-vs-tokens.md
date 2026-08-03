---
type: "concept"
title: "API Keys vs Tokens"
description: "Comparing static API keys with short-lived access tokens for API auth"
tags: ["api", "auth", "security", "design"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# API Keys vs Tokens

## Summary
API keys are opaque static identifiers for the caller; access tokens are short-lived, scoped, and introspectable credentials issued by an authorization server. The distinction drives revocation, rotation, and audit.

## Details
An API key is a long random string (often sk_live_... or a UUID) that identifies a client to a service. It is static: it stays valid until rotated or revoked, carries no expiry or scope of its own, and is typically the only credential the service checks. An access token, by contrast, is issued by an authorization server with a lifetime (often minutes), a scope, an audience, and optionally a JWT structure that the resource server can verify without a callback.

The mechanism: with keys, every request carries the same secret and the service looks it up in a key table with owner, quota, and permissions. With tokens, the client first exchanges credentials (client id and secret, refresh token, device authorization) for a short-lived token, then presents it; the resource server validates signature, expiry, and scope or calls introspection. Revocation of a key is immediate and total; revocation of a token is either quick (introspection or blacklist) or delayed until expiry.

Concrete example: a CI pipeline uses a long-lived deploy key so it can push artifacts without human login — a classic API key. A mobile app uses OAuth2 access tokens (short-lived, scoped, refreshed) so a leaked token expires in minutes and never grants access to other services. A leaked API key, in contrast, grants everything it grants until someone notices and rotates it.

Failure modes: static keys leak into git history, logs, and client bundles, and because they have no expiry, leaked keys are exploitable indefinitely; keys with overly broad permissions magnify any leak; and services that treat keys as user identity make it impossible to tell which human did what. Tokens fail differently: no refresh-token rotation, unvalidated scope or audience, or clock-skew tolerance beyond limits can extend or misdirect their validity.

Operational tradeoffs: keys are simplest to implement and debug — one header, no token dance — and fit scripts and machine-to-machine calls; tokens are more complex but give expiry, scope, revocation, and delegation. Many platforms converge on: keys for low-value automation, OAuth2 client credentials for service-to-service, and OIDC for humans. Key rotation policies (90 days, or immediately on suspicion) and hashing keys at rest are non-negotiable hygiene.

RSIS3/mykb relevance: RSIS3 loops that call the wiki daemon or external LLM APIs should standardize on short-lived tokens where possible and treat static keys as flagged credentials in check-practices runs.

## Related
- [[wiki/api-protocols/auth-flows-web|Auth Flows on the Web]] — related coverage in the same cluster
- [[wiki/api-protocols/api-basic-auth|API Basic Auth]] — related coverage in the same cluster
- [[wiki/api-protocols/api-digest-auth|API Digest Auth]] — related coverage in the same cluster
- [[wiki/api-protocols/bearer-tokens|Bearer Tokens]] — related coverage in the same cluster
- [[wiki/api-protocols/api-authentication-methods|API Authentication Methods]] — related coverage in the same cluster
- [[wiki/api-protocols/api-keys|API Keys]] — related coverage in the same cluster
- [[wiki/api-protocols/basic-authentication|Basic Authentication]] — related coverage in the same cluster
