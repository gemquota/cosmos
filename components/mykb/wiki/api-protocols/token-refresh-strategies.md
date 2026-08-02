---
type: "concept"
title: "Token Refresh Strategies"
description: "Keeping sessions alive with refresh tokens: rotation, reuse detection, and silent renewal"
tags: ["tokens", "oauth2", "refresh", "auth", "sessions"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://www.rfc-editor.org/rfc/rfc6749", "https://auth0.com/docs/secure/tokens/refresh-tokens"]
---
# Token Refresh Strategies

## Summary
Access tokens are short-lived by design; refresh tokens let clients obtain new ones without re-authentication. Good refresh strategy balances security (rotation, reuse detection) with UX (silent renewal, offline tolerance). Refresh tokens are high-value secrets and need their own protection and lifecycle.

## Details
- **Rotation** — each refresh issues a new access token and a new refresh token while retiring the old one; replay of a rotated token signals theft.
- **Reuse detection** — if a rotated token is used again, revoke the whole family and alert; this bounds the damage of leaks.
- **Silent renewal** — SPAs refresh in the background before expiry; the storage and theft surface of tokens in browser storage is a known tension.
- **Expiry policy** — absolute session lifetimes, idle timeouts, and step-up re-auth define when refresh stops working.
- **Worked example** — the mykb dashboard refreshes five minutes before expiry with rotation, then logs out on reuse detection.
- **Relevance** — RSIS3's long-running agent sessions rely on the same refresh cadence so tools never die mid-task.

## Related
- [[wiki/api-protocols/refresh-token-rotation|Refresh Token Rotation]] — adjacent concept in this wiki
- [[wiki/api-protocols/jti-claims|JWT ID Claims]] — adjacent concept in this wiki
- [[wiki/api-protocols/audience-claims|Audience Claims]] — adjacent concept in this wiki
- [[wiki/api-protocols/scope-validation|Scope Validation]] — adjacent concept in this wiki
- [[wiki/api-protocols/oauth2-refresh-tokens|Refresh Tokens]] — existing coverage
- [[wiki/api-protocols/oauth2|OAuth 2.0]] — existing coverage
- [[wiki/identity/refresh-tokens|Refresh Tokens]] — existing coverage
