---
type: "concept"
title: "CORS Wildcards"
description: "Access-Control-Allow-Origin: * and when it is safe to use"
tags: ["cors", "security", "http", "web"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# CORS Wildcards

## Summary
The CORS wildcard (Access-Control-Allow-Origin: *) says any origin may read the response. It is safe only for fully public data and breaks the moment credentials, cookies, or per-user content enter the response.

## Details
Access-Control-Allow-Origin: * tells browsers that any origin may read the response. It is the simplest CORS policy and the correct one for genuinely public endpoints — logos, public API data, static assets, open documentation. Because the wildcard means "every origin," it must never be combined with Access-Control-Allow-Credentials: true; browsers reject that combination, and any implementation that tries to serve credentialed wildcard responses is misconfigured by construction.

The mechanism: the browser compares the response's Access-Control-Allow-Origin against the requesting origin. With *, every origin matches. The response is then readable by any site, and the browser sends the request from any site. The subtlety: * also applies to the preflight, so a wildcard server answers allow-methods and allow-headers to everyone. If the server instead reflects the request's Origin header (Access-Control-Allow-Origin: <echo>), it looks like a wildcard but is actually per-request — and if that echo also allows credentials, it is equivalent to an open CORS policy.

Concrete example: a public weather API serves GET /v1/forecast with no auth and returns Allow-Origin: * — correct, because the data is the same for every caller and nothing sensitive is exposed. The same API adding an authenticated /v1/account endpoint with Allow-Origin: * would be a vulnerability: any website could read a logged-in user's account data if the app also sent credentials.

Failure modes: wildcard on authenticated endpoints leaks per-user data to any site; wildcard plus Allow-Credentials is invalid and confusingly breaks legitimate clients; and wildcard on responses that are currently public but will become authenticated (or will start varying by user) silently turns into a data-exfiltration channel when the change ships without updating CORS.

Operational tradeoffs: the wildcard is zero-maintenance and cache-friendly, which is why it is right for public assets; an explicit allowlist costs maintenance but is the only correct choice for anything credential-bearing. The default posture should be: deny by default, wildcard only for public read-only endpoints, explicit allowlist everywhere else, and Vary: Origin on any response whose CORS headers can change per request.

RSIS3/mykb relevance: the dashboard's public snapshots can use the wildcard; its authenticated APIs must not. Documenting which endpoints are public versus credentialed keeps the CORS policy auditable in check-practices runs.

## Related
- [[wiki/api-protocols/web-security-owasp|Web Security (OWASP)]] — related coverage in the same cluster
- [[wiki/api-protocols/cross-origin-isolation|Cross-Origin Isolation]] — related coverage in the same cluster
- [[wiki/api-protocols/cors-preflight|CORS Preflight]] — related coverage in the same cluster
- [[wiki/api-protocols/cors-credentials|CORS with Credentials]] — related coverage in the same cluster
- [[wiki/api-protocols/cors|CORS]] — related coverage in the same cluster
- [[wiki/security-auth/cors-policy|CORS Policy]] — related coverage in the same cluster
- [[wiki/security-auth/same-origin-policy|Same-Origin Policy]] — related coverage in the same cluster
