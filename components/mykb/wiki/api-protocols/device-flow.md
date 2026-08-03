---
type: "concept"
title: "Device Authorization Flow"
description: "OAuth grant for input-constrained devices that cannot run a browser"
tags: ["oauth2", "auth", "devices", "security"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Device Authorization Flow

## Summary
The device authorization flow (RFC 8628) lets input-constrained devices — smart TVs, CLIs, printers — authenticate by displaying a code the user enters on a separate device. It solves the "no browser, no keyboard" problem without embedding credentials in the device.

## Details
The device flow works in two phases. First, the device POSTs to the authorization server's device_authorization_endpoint with its client_id and receives a device_code, user_code, and verification_uri. The device displays "Go to https://example.com/device and enter code ABCD-EFGH." Meanwhile the user, on any browser-capable device, visits the URL, enters the code, and authorizes. The device then polls the token endpoint with grant_type=urn:ietf:params:oauth:grant-type:device_code until the user authorizes, and receives tokens.

The mechanism: the device_code is bound to the user_code and the client, expires quickly (the flow is designed to be short), and the polling uses a server-specified interval with exponential backoff — polling too fast yields slow_down errors. The user_code is designed to be human-friendly and unguessable enough for short-lived use. Because the device never handles the user's password, a compromised TV cannot harvest credentials; it can only abuse its own token.

Concrete example: a smart TV signs into a streaming service. The TV shows a code and URL; the user authorizes from their phone; the TV polls, receives an access token plus refresh token, and starts streaming. A CLI tool can use the same flow: it prints a URL and code, the user authorizes in a browser, and the CLI completes — avoiding the need to paste credentials into a terminal.

Failure modes: user codes that are too short are guessable and enable authorization hijacking (an attacker who reaches the authorization page first); polling without honoring the interval and slow_down error hammers the server; and device codes stored or logged on the device become reusable until expiry. Devices that never finish the flow leave polling connections open; the server should enforce the expiry regardless of client behavior.

Operational tradeoffs: the flow trades setup complexity for security — no password on the device, no browser required — and is the right choice for any device with constrained input. It adds a polling loop and a user-facing code UX that must be documented. Pair it with per-device client registrations and token scope limiting so a stolen device token is bounded.

RSIS3/mykb relevance: headless RSIS3 automation that needs user-context tokens (for example accessing a user's data) can use the device flow from a terminal; documenting the polling contract keeps the loop from violating slow_down rules.

## Related
- [[wiki/api-protocols/auth-flows-web|Auth Flows on the Web]]
- [[wiki/api-protocols/client-credentials-flow|Client Credentials Flow]]
- [[wiki/api-protocols/authorization-code-flow|Authorization Code Flow]]
- [[wiki/api-protocols/oauth2|OAuth 2.0]]
- [[wiki/api-protocols/oauth2-client-credentials|Client Credentials]]
- [[wiki/api-protocols/oauth2-authorization-code|Authorization Code Flow]]
