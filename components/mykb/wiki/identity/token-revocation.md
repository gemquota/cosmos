---
type: "concept"
title: "Token Revocation"
description: "Invalidating tokens before their natural expiry, per RFC 7009"
tags: ["token-revocation", "tokens", "oauth2", "rfc7009"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
source: ["https://www.rfc-editor.org/rfc/rfc7009"]
---

# Token Revocation

- RFC 7009 defines the OAuth 2.0 revocation endpoint, letting clients invalidate access or refresh tokens before expiry.
- Revocation is critical for logout, device loss, compromise response, and offboarding.
- Stateless JWT tokens cannot be revoked without server-side state (deny lists) or very short lifetimes.
- For mykb: revocation feeds should be shared across all resource servers so a revoked token dies everywhere at once.

## Related

- [[wiki/identity/refresh-tokens|Refresh Tokens]] — refresh tokens are revoked on logout
- [[wiki/security-auth/token-authentication|Token Authentication]] — token lifecycle management
- [[wiki/identity/session-management|Session Management]] — revocation is part of session termination
- [[wiki/security/oauth2|OAuth 2.0]] — the framework's revocation endpoint
