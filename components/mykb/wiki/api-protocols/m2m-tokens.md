---
type: "concept"
title: "Machine-to-Machine Tokens"
description: "Tokens that authenticate services to services without a human user"
tags: ["oauth2", "auth", "m2m", "security"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Machine-to-Machine Tokens

## Summary
Machine-to-machine (M2M) tokens authenticate a service to other services — no human session involved. They are typically issued via the client credentials grant, scoped to the calling service, and cached rather than minted per request.

## Details
M2M tokens represent the client itself as the actor: the subject is the service account, not a person. The client authenticates to the authorization server (client_id plus secret, mTLS, or a JWT assertion) and receives a token whose scopes express what the service may do — graph:write, jobs:run — not who a human is. This is the OAuth2 client credentials flow in its primary use.

The mechanism: because there is no user, there is no redirect, consent, or refresh-token dance; the client can re-request tokens whenever it needs one. Resource servers validate the token (signature or introspection) and authorize on the client's scopes and roles. Audit trails attribute actions to the service account, which is exactly right for automation: every action has a stable, inspectable identity.

Concrete example: RSIS3's consolidation loop calls the wiki API to write synthesis notes. It holds client credentials for service account wiki-writer, requests scope=notes:write, caches the 30-minute token, and reuses it until near expiry. A leaked token is short-lived and scoped — it cannot read user data or call other services. Compare with a static API key that grants everything until rotated.

Failure modes: storing client secrets in config files that ship with the repo; granting M2M clients overly broad scopes because "it's internal"; missing audience or issuer validation so a token for one API works on another; and minting a fresh token per request, which hammers the token endpoint and creates a burst of revocable-but-active credentials. Long-lived client identities without rotation become de facto static keys.

Operational tradeoffs: M2M tokens trade setup complexity for expiry, scoping, and auditability — the right trade for service-to-service traffic. Token caching with proactive refresh avoids per-request minting; scopes should be the minimum the service needs; and client secrets should rotate on a schedule with automated re-provisioning. Where possible, mTLS or private-key JWT client auth replaces the shared secret entirely.

RSIS3/mykb relevance: this is the standing pattern for RSIS3's own integrations; documenting the M2M token contract (grant, scopes, caching, rotation) keeps every loop consistent.

## Related
- [[wiki/api-protocols/auth-flows-web|Auth Flows on the Web]] — related coverage in the same cluster
- [[wiki/api-protocols/api-keys-vs-tokens|API Keys vs Tokens]] — related coverage in the same cluster
- [[wiki/api-protocols/api-basic-auth|API Basic Auth]] — related coverage in the same cluster
- [[wiki/api-protocols/api-digest-auth|API Digest Auth]] — related coverage in the same cluster
- [[wiki/api-protocols/api-authentication-methods|API Authentication Methods]] — related coverage in the same cluster
- [[wiki/api-protocols/api-keys|API Keys]] — related coverage in the same cluster
- [[wiki/api-protocols/basic-authentication|Basic Authentication]] — related coverage in the same cluster
