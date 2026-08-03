---
type: "concept"
title: "Refresh Token Rotation"
description: "Issuing a new refresh token on every use so stolen tokens die fast"
tags: ["oauth2", "tokens", "security", "api"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Refresh Token Rotation

## Summary
Refresh token rotation issues a new refresh token each time the old one is used, so a stolen refresh token becomes a one-time credential: replaying it fails and signals theft. It is the strongest practical defense against refresh-token theft.

## Details
A refresh token is long-lived, so its theft is equivalent to permanent session compromise unless something invalidates it. Rotation solves this: every successful refresh consumes the presented token and returns a new one (and a new access token). The old token is dead after use. If an attacker and the legitimate client both hold the same token, only one can use it — and the replay by the other is a detectable theft signal.

The mechanism: the authorization server marks a refresh token as used on redemption and issues a replacement bound to the same session. Detection logic: if a used (rotated) token is presented again, the server assumes theft and can revoke the entire token family — the legitimate client's new token included — forcing re-authentication. RFC 9700 (the OAuth 2.0 security BCP) recommends rotation with reuse detection as the default for refresh tokens.

Concrete example: a mobile app refreshes with token R1 and receives R2. An attacker who stole R1 tries to use it; the server sees a replay of a rotated token, revokes R2 as well, and flags the account. The user is logged out and must re-authenticate — annoying but safe. Without rotation, the attacker's R1 and the app's R1 both work indefinitely, and nothing alerts anyone.

Failure modes: rotation without reuse detection is just token churn — the server must actually detect the replay of a consumed token; refresh tokens stored where the client can lose them (localStorage) defeat the scheme when both copies leak; and rotation that silently fails (network errors during the token exchange) can leave the client with a dead token and no path to re-auth. The server should also bound token family lifetimes so sessions can't renew forever.

Operational tradeoffs: rotation adds a write per refresh and requires the client to handle the "this token was already used" error by re-authenticating; the payoff is the elimination of long-lived stolen credentials. Pair rotation with short access-token lifetimes, jti-based denylists, and family revocation on reuse. The baseline for any OAuth2 deployment: rotate on every refresh, detect reuse, revoke the family, and document the client behavior on rotation failure.

RSIS3/mykb relevance: RSIS3's own refresh handling should implement rotation; documenting the contract (rotate, reuse-detect, revoke family) keeps loop sessions from going stale or staying stolen.

## Related
- [[wiki/api-protocols/token-refresh-strategies|Token Refresh Strategies]] — related coverage in the same cluster
- [[wiki/api-protocols/refresh-token-rotation|Refresh Token Rotation]] — related coverage in the same cluster
- [[wiki/api-protocols/refresh-token-rotation|Refresh Token Rotation]] — related coverage in the same cluster
- [[wiki/api-protocols/refresh-token-rotation|Refresh Token Rotation]] — related coverage in the same cluster
- [[wiki/api-protocols/oauth2-refresh-tokens|Refresh Tokens]] — related coverage in the same cluster
- [[wiki/api-protocols/oauth2|OAuth 2.0]] — related coverage in the same cluster
- [[wiki/identity/refresh-tokens|Refresh Tokens]] — related coverage in the same cluster
