---
type: "concept"
title: "Authentication Patterns"
description: "The ways systems verify who is asking — sessions, tokens, and federated login"
tags: ["authentication", "patterns", "security", "identity"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/Authentication", "https://en.wikipedia.org/wiki/OAuth"]
---

# Authentication Patterns

## Summary
Authentication patterns verify identity: password plus MFA, session cookies, bearer tokens, API keys, and federated flows like OAuth 2.0 and OpenID Connect. Each pattern balances security, usability, and delegation; modern practice centers on short-lived tokens and MFA.

## Details
- Password auth needs MFA and secure hashing (argon2/bcrypt) — never roll your own crypto.
- Sessions (server-side, cookie-bound) suit browser apps; tokens (JWT, opaque) suit APIs and mobile.
- OAuth 2.0 delegates authorization with scoped, expiring access tokens; OIDC adds an identity layer.
- Machine identities use API keys or mTLS with rotation and scopes, like human identities.
- Threats to handle: phishing (phishable secrets), replay (short lifetimes), and credential stuffing (MFA, rate limits).
- For the mykb bundle, the API uses short-lived bearer tokens with MFA at the gate and scoped keys for agents.
- Worked example — a curator logs in with SSO plus MFA, gets a 15-minute access token and a refresh token; the agent integration uses scoped API keys that rotate monthly.

Worked example — a curator logs in with SSO plus MFA, gets a 15-minute access token and a refresh token; the agent integration uses scoped API keys that rotate monthly.

## Related
- [[wiki/compositions/identity-management|Identity Management]]
- [[wiki/compositions/authorization-models|Authorization Models]]
- [[wiki/security/oauth2|OAuth 2.0]]
- [[wiki/security/mfa|MFA]]
- [[wiki/security-auth/token-authentication|Token Authentication]]
- [[wiki/compositions/zero-trust-architecture|Zero-Trust Architecture]]
- [[wiki/compositions/fencing-tokens|Fencing Tokens]]
- [[wiki/software-engineering/retry-after|Retry-After]]
