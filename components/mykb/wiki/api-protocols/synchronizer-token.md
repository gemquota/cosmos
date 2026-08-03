---
type: "concept"
title: "Synchronizer Token Pattern"
description: "Server-stored CSRF tokens validated against session state"
tags: ["csrf", "security", "web", "forms"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Synchronizer Token Pattern

## Summary
The synchronizer token pattern is the classic CSRF defense: the server generates a random token per session, embeds it in forms, and rejects any state-changing request whose token does not match the one stored server-side. Because an attacker's cross-site form cannot read the token, the request is rejected before it reaches application logic.

## Details
- Mechanism: at session creation the server generates a cryptographically random value and stores it server-side (in the session record); every form includes it as a hidden field, and every mutating request must carry it back. On submission the server compares the submitted token against the stored one and rejects mismatches. The essential property is secrecy and session binding: the token is unpredictable, and it is meaningless without the matching session, so a request that carries a valid token must have been made by code that could read the page — which cross-site attackers cannot.
- Concrete examples: a login form renders `<input type="hidden" name="csrf" value="…">` where the value comes from the session; a JSON API requires the same token in an `X-CSRF-Token` header; a SPA fetches the token from a cookie or endpoint on boot and attaches it to every fetch. What makes it a synchronizer pattern rather than a double-submit is that the server state is the source of truth, so a leaked cookie value alone cannot be replayed without the server's matching record.
- Failure modes: the pattern breaks when comparison uses ordinary string equality (timing attacks can recover the token), when tokens are not bound to the session and any session's token is accepted, when the token is reusable and predictable (sequential IDs, timestamps), or when CORS misconfiguration lets a cross-site script actually read the response that contains the token. Frameworks that rotate the token per request must accept either the old or new value during a race, or legitimate double-submits get logged out.
- Operational tradeoffs: server-stored tokens are the most robust CSRF defense because validation cannot be bypassed by manipulating cookies, but they add session store lookups, require per-request token generation, and complicate stateless backends (which is why double-submit and SameSite exist as lighter alternatives). For high-traffic APIs, synchronizer tokens are usually reserved for browser form endpoints while SameSite plus fetch-metadata checks cover the rest.
- RSIS3/mykb relevance: the pattern is a template for any write-path validation that must prove the requester could read the source of truth: RSIS3's registry writes can require a token derived from the session state it is writing to, preventing blind cross-loop mutation.

## Related
- [[wiki/api-protocols/secure-cookies|Secure Cookies]] — related coverage in the same cluster
- [[wiki/api-protocols/sec-fetch-headers|Sec-Fetch Headers]] — related coverage in the same cluster
- [[wiki/api-protocols/csrf-tokens|CSRF Tokens]] — related coverage in the same cluster
- [[wiki/api-protocols/double-submit-cookie|Double-Submit Cookie]] — related coverage in the same cluster
- [[wiki/api-protocols/csrf|CSRF]] — related coverage in the same cluster
- [[wiki/security-auth/csrf-protection|CSRF Protection]] — related coverage in the same cluster
- [[wiki/api-protocols/http-headers|HTTP Headers]] — related coverage in the same cluster
