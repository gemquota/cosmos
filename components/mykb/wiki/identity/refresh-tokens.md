---
type: "concept"
title: "Refresh Tokens"
description: "Long-lived credentials that obtain new access tokens without re-authentication"
tags: ["refresh-tokens", "tokens", "oauth2", "sessions"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
source: ["https://www.rfc-editor.org/rfc/rfc6749"]
---

# Refresh Tokens

- Refresh tokens (RFC 6749) let a client trade a long-lived credential for fresh short-lived access tokens, avoiding repeated logins.
- They must be stored as securely as passwords, be bound to a client and scope, and support rotation and revocation.
- Refresh-token rotation (issuing a new token per use, invalidating the old) limits the damage of token theft.
- Reuse detection: when a rotated token is replayed, revoke the whole session and alert — a strong compromise signal.
- For mykb: refresh tokens are how agents keep working sessions without holding long-lived access tokens.

## Related

- [[wiki/identity/token-revocation|Token Revocation]] — invalidating tokens including refresh tokens
- [[wiki/security-auth/token-authentication|Token Authentication]] — the access tokens they renew
- [[wiki/identity/session-management|Session Management]] — refresh lifecycle as session policy
- [[wiki/security/oauth2|OAuth 2.0]] — the framework that defines them
