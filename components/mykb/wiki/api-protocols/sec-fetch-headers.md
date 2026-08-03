---
type: "concept"
title: "Sec-Fetch Headers"
description: "Fetch metadata headers that reveal request destination and mode"
tags: ["security", "http", "headers", "web"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Sec-Fetch Headers

## Summary
Sec-Fetch-* headers, collectively called Fetch Metadata, let servers see the context of every request: which site initiated it, whether it is a navigation or a subresource load, and what the client intends to do with the response. Because browsers attach these headers automatically and forbid JavaScript from forging them, servers can use them as a cheap signal to reject cross-site anomalies before a request touches application code.

## Details
- Mechanism: the four main headers are `Sec-Fetch-Site` (cross-site, same-site, same-origin, none), `Sec-Fetch-Mode` (navigate, cors, no-cors, websocket, etc.), `Sec-Fetch-Dest` (document, script, image, empty), and `Sec-Fetch-User` (?1 for user-activated navigations). They are set by the browser based on the request's actual context, and user agents strip any attempt by page scripts to spoof them, which is what makes them a trust signal rather than just metadata.
- Concrete examples: a defense-in-depth rule rejects any state-changing API request whose `Sec-Fetch-Site` is `cross-site`, which would stop most CSRF attempts even if token checks regress; an image endpoint can reject requests whose `Sec-Fetch-Dest` is not `image`, cutting hotlinking and script-driven abuse; a login page can require `Sec-Fetch-Site: same-origin` for POSTs so a bookmarklet or external form cannot submit credentials programmatically.
- Failure modes: Fetch Metadata is a defense-in-depth signal, not a hard boundary: it is absent in older browsers, non-browser clients (curl, mobile SDKs, server-to-server calls) do not send it at all, and it says nothing about authentication or authorization. Enforcing it strictly will break legitimate API clients and health checks, so treat "missing headers" as an allow case for first-party tooling and use the headers to flag anomalies for review or rate limiting rather than blanket-rejecting everything.
- Operational tradeoffs: the cost is near zero (four small headers per request), and the benefit is a strong early-warning layer that complements CSRF tokens and CORS. The tradeoff is operational complexity: you must maintain an allowlist of legitimate contexts per route, keep it in sync as the site adds embedded widgets or partner integrations, and decide how to handle the growing set of contexts (speculative loads, prerenders, service workers) without breaking features.
- RSIS3/mykb relevance: the pattern — use ambient request context as a cheap pre-check before costly validation — mirrors RSIS3 loop hygiene where telemetry headers annotate pulse data, letting the dashboard reject malformed or cross-loop writes before they reach the knowledge graph.

## Related
- [[wiki/api-protocols/secure-cookies|Secure Cookies]] — related coverage in the same cluster
- [[wiki/api-protocols/csrf-tokens|CSRF Tokens]] — related coverage in the same cluster
- [[wiki/api-protocols/double-submit-cookie|Double-Submit Cookie]] — related coverage in the same cluster
- [[wiki/api-protocols/synchronizer-token|Synchronizer Token Pattern]] — related coverage in the same cluster
- [[wiki/api-protocols/csrf|CSRF]] — related coverage in the same cluster
- [[wiki/security-auth/csrf-protection|CSRF Protection]] — related coverage in the same cluster
- [[wiki/api-protocols/http-headers|HTTP Headers]] — related coverage in the same cluster
