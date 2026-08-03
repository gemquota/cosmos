---
type: "concept"
title: "Cross-Origin Isolation"
description: "COOP and COEP headers that enable powerful APIs and harden the origin boundary"
tags: ["security", "http", "headers", "web"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Cross-Origin Isolation

## Summary
Cross-origin isolation is a security state a site opts into with Cross-Origin-Opener-Policy (COOP) and Cross-Origin-Resource-Policy (CORP) plus Cross-Origin-Embedder-Policy (COEP). It blocks cross-origin attacks and unlocks APIs like SharedArrayBuffer.

## Details
A cross-origin isolated page can use high-performance APIs (SharedArrayBuffer, performance.measureUserAgentSpecificMemory) and is protected against a class of cross-origin attacks. The state requires three headers: COOP: same-origin (isolates the opener relationship), COEP: require-corp (every cross-origin resource must be loaded with CORP or CORS headers), and a secure context. The cost is real: any third-party resource that doesn't opt in with CORP breaks.

The mechanism: COOP ensures a window opened from your page (or opening it) is placed in a separate browsing context group, so cross-origin pages can't reference or script each other through window.opener. COEP forces every subresource (scripts, images, iframes, fonts) to declare itself via Cross-Origin-Resource-Policy or CORS; anything that doesn't is blocked from loading. Together they close side-channel and cross-origin leaks that spectre-class attacks exploit, which is why browsers gate SharedArrayBuffer on this state.

Concrete example: a data-heavy dashboard needs SharedArrayBuffer for a WebAssembly image pipeline. It adds COOP: same-origin and COEP: require-corp, then audits every third-party script and font to add CORP: same-site or serve them via CORS. A third-party analytics script loaded without CORP silently stops loading — the integration cost of isolation.

Failure modes: enabling COEP without auditing resources breaks the page (blank embeds, missing fonts) in confusing ways; COOP: same-origin breaks popup flows that rely on window.opener communication (OAuth popups, payment windows); and adding just one of the three headers gives no isolation while creating a false sense of security. Proxies and CDNs that strip or merge headers also silently disable the state.

Operational tradeoffs: isolation is the strongest client-side boundary available, but it requires controlling every resource your page loads — which is precisely why sites with heavy third-party content often stay non-isolated. The migration path is gradual: ship COOP first, use COEP: credentialless as a bridge, audit resources with Reporting API, then enforce require-corp.

RSIS3/mykb relevance: if the dashboard needs shared-memory features or wants maximal hardening, the COOP+COEP contract is the documented state to target; recording it lets RSIS3 check the headers on deployment.

## Related
- [[wiki/api-protocols/web-security-owasp|Web Security (OWASP)]] — related coverage in the same cluster
- [[wiki/api-protocols/cors-preflight|CORS Preflight]] — related coverage in the same cluster
- [[wiki/api-protocols/cors-credentials|CORS with Credentials]] — related coverage in the same cluster
- [[wiki/api-protocols/cors-wildcard|CORS Wildcards]] — related coverage in the same cluster
- [[wiki/api-protocols/cors|CORS]] — related coverage in the same cluster
- [[wiki/security-auth/cors-policy|CORS Policy]] — related coverage in the same cluster
- [[wiki/security-auth/same-origin-policy|Same-Origin Policy]] — related coverage in the same cluster
