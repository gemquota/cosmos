---
type: "concept"
title: "Refresh Tokens"
description: "Long-lived credentials that obtain new access tokens without re-authentication"
tags: ["refresh-tokens", "tokens", "oauth2", "sessions"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://www.rfc-editor.org/rfc/rfc6749"]
---

# Refresh Tokens

## Summary
Refresh tokens (RFC 6749) let a client trade a long-lived credential for fresh short-lived access tokens, avoiding repeated logins. They exist because access tokens should be short-lived (minutes) to bound the damage of theft, yet forcing the user to re-authenticate every few minutes would be unusable — the refresh token carries the session between token renewals.

## Details
- Refresh tokens (RFC 6749) let a client trade a long-lived credential for fresh short-lived access tokens, avoiding repeated logins. The refresh token is issued at authorization, stored securely by the client, and exchanged for a new access token (and often a new refresh token) at the token endpoint whenever the access token is near expiry.
- They must be stored as securely as passwords, be bound to a client and scope, and support rotation and revocation. A stolen refresh token is a stolen session: it can mint access tokens until revoked, so it deserves password-grade protection, client binding (only the issuing client can use it), and scope binding (it cannot mint tokens beyond its granted scope).
- Refresh-token rotation (issuing a new token per use, invalidating the old) limits the damage of token theft. With rotation, a stolen token works once; the next legitimate use fails because the stolen token was already superseded, and the replay is visible.
- Reuse detection: when a rotated token is replayed, revoke the whole session and alert — a strong compromise signal. If the attacker used the stolen token and the legitimate client then uses its (now stale) token, the provider sees a replay and can revoke the entire token family, terminating the attacker's session and surfacing an incident.
- Concrete example: a mobile app holds a refresh token; every 15 minutes it exchanges it for a fresh access token, rotating the refresh token each time. An attacker who steals the current refresh token uses it once, but the app's next exchange trips reuse detection, the session is revoked, and the user must re-authenticate — the theft cost the attacker nothing but the session was saved.
- Failure modes: refresh tokens stored insecurely (localStorage, logs) or without client binding; rotation disabled, so stolen tokens work indefinitely; tokens that never expire; and revocation gaps, where a logged-out user's refresh token keeps minting access tokens.
- For mykb: refresh tokens are how agents keep working sessions without holding long-lived access tokens — the wiki should document the token lifecycle (issue, rotate, revoke) as the standard session policy for every integration.

## Related
- [[wiki/identity/token-revocation|Token Revocation]] — invalidating tokens including refresh tokens
- [[wiki/security-auth/token-authentication|Token Authentication]] — the access tokens they renew
- [[wiki/identity/session-management|Session Management]] — refresh lifecycle as session policy
- [[wiki/security/oauth2|OAuth 2.0]] — the framework that defines them
