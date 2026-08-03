---
type: "concept"
title: "API Digest Auth"
description: "Challenge-response HTTP authentication with hashed credentials"
tags: ["http", "auth", "api", "security"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# API Digest Auth

## Summary
Digest authentication avoids sending the password in the clear by proving knowledge of it through a challenge-response hash, but it is still weak against modern attackers and rarely used for APIs.

## Details
Digest auth (RFC 7616) has the server issue a challenge with a nonce and realm; the client responds with a hash computed over username, realm, password, nonce, method, and URI. The password never crosses the wire. Its design goal was protecting passwords from passive sniffing without TLS — a pre-TLS-era concern that TLS largely made obsolete.

The mechanism: the server sends 401 with WWW-Authenticate: Digest realm=..., nonce=..., qop="auth". The client computes something like MD5(MD5(user:realm:pass) : nonce : nc : cnonce : qop : MD5(method:uri)) and sends Authorization: Digest username=..., response=..., nc=..., cnonce=..., uri=.... The server recomputes and compares. The qop=auth-int variant also hashes the body, which is what makes it meaningfully better than basic auth on that axis.

Concrete example: a legacy embedded device with no TLS stack authenticates to a firmware server using digest auth, because the device cannot do TLS at all. The hash binds method and URI, so a captured response cannot be replayed verbatim for a different request — though it can be replayed for the same request, which is why the nonce must be single-use and expire quickly.

Failure modes: MD5 is the default hash and is broken; a man-in-the-middle can still downgrade or offline-brute-force the response hash with a dictionary attack; replay within the nonce window is possible; and the scheme is vulnerable to chosen-plaintext attacks when the attacker can pick the server nonce. Browser support has historically been uneven, especially with qop variations, which kills it for web UIs.

Operational tradeoffs: digest avoids storing cleartext passwords at the server (it can store the HA1 hash), but every client library must implement the challenge dance, and debugging is harder because each request has two round trips and opaque hashes. For APIs, the pragmatic stance is: use TLS plus bearer tokens or client certificates; reserve digest for constrained devices that literally cannot do TLS.

RSIS3/mykb relevance: the wiki's API guidance should list digest auth as legacy-only so automation loops do not accidentally standardize on it when the goal is long-term credential hygiene.

## Related
- [[wiki/api-protocols/auth-flows-web|Auth Flows on the Web]]
- [[wiki/api-protocols/bearer-tokens|Bearer Tokens]]
- [[wiki/api-protocols/m2m-tokens|Machine-to-Machine Tokens]]
- [[wiki/api-protocols/api-keys-vs-tokens|API Keys vs Tokens]]
- [[wiki/api-protocols/api-authentication-methods|API Authentication Methods]]
- [[wiki/api-protocols/api-keys|API Keys]]
- [[wiki/api-protocols/basic-authentication|Basic Authentication]]
