---
type: "concept"
title: "Refresh Tokens"
description: "Refresh token lifecycle, rotation, and reuse detection"
tags: ["oauth2", "refresh-tokens", "tokens", "security", "session-lifecycle"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://www.rfc-editor.org/rfc/rfc6749#section-6", "https://auth0.com/docs/secure/tokens/refresh-tokens"]
---

# Refresh Tokens

## Summary
Refresh tokens are long-lived credentials that mint new access tokens without forcing the user to re-authenticate. Because access tokens are short-lived, refresh tokens extend sessions — and their lifecycle policies (rotation, expiry, revocation, reuse detection) determine whether a leaked token becomes a breach or a blip.

## Details
- Why they exist: short access tokens limit the damage of token theft; the refresh token lives server-side or in secure storage and buys new access tokens.
- Rotation: every refresh returns a NEW refresh token and invalidates the old one — a stolen, already-used token fails on reuse.
- Reuse detection: if an old rotated token is presented again, the IdP treats it as theft: revoke the whole refresh token family and force re-login.
- Lifetime: absolute expiry (days to months), sliding expiry (extend on activity), and per-client policies; combine with idle timeouts.
- Revocation: logout and admin actions must revoke refresh tokens (and their families) server-side, not just clear the browser.
- Storage: SPAs must keep refresh tokens out of JavaScript reach — httpOnly cookies or the BFF pattern — or XSS becomes token exfiltration.
- Binding: tie refresh tokens to clients (audience, client_id) and optionally to device/BIOS fingerprints for high-risk flows.

## Related
- [[wiki/api-protocols/oauth2|OAuth 2.0]] — the framework that defines refresh tokens
- [[wiki/api-protocols/oauth2-authorization-code|Authorization Code Flow]] — the flow that issues them
- [[wiki/api-protocols/oauth2-pkce|PKCE]] — protecting public-client sessions
- [[wiki/api-protocols/json-web-tokens|JWT]] — what access tokens often look like
- [[wiki/api-protocols/backend-for-frontend|Backend for Frontend]] — BFF keeps refresh tokens out of browsers
