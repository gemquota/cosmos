---
type: "concept"
title: "CORS Preflight"
description: "The OPTIONS request browsers send before non-simple cross-origin calls"
tags: ["cors", "security", "http", "web"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# CORS Preflight

## Summary
The CORS preflight is an OPTIONS request the browser sends before non-simple cross-origin requests, asking the server which methods, headers, and origins are allowed. It exists to stop cross-origin writes the server never intended.

## Details
Before a cross-origin request that is not "simple" — a non-standard method (PUT, DELETE, PATCH), custom headers (Authorization, X-Requested-With), or certain Content-Types (application/json) — the browser sends a preflight OPTIONS request with Access-Control-Request-Method and Access-Control-Request-Headers. The server answers with Access-Control-Allow-Methods, Access-Control-Allow-Headers, Access-Control-Allow-Origin, and optionally Access-Control-Max-Age. Only if the preflight passes does the browser send the actual request.

The mechanism: the preflight is the browser's way of asking "if I send this request with these headers, will the server accept it?" It exists because the server historically couldn't distinguish a cross-origin POST (harmless form) from a cross-origin JSON POST with a bearer token (potentially destructive). By gating on an explicit server response, the browser prevents the request from even being attempted when the server hasn't opted in. Simple requests (GET, HEAD, POST with form content types) skip preflight, which is why CSRF defenses must still cover them.

Concrete example: a dashboard calls DELETE https://api.example/items/1 with an Authorization header. The browser preflights; api.example must return Access-Control-Allow-Methods: DELETE and Access-Control-Allow-Headers: Authorization. If the server only allows GET, the browser blocks the DELETE before it's sent — the server never sees it. If the preflight reflects methods or headers from the request instead of an allowlist, an attacker page can get its own headers allowed.

Failure modes: reflecting Access-Control-Request-Headers into allow-headers turns the allowlist into a pass-through; preflight responses cached too long (Max-Age) with a stale allowlist lock out legitimate clients after a config change; and 405s or 401s on OPTIONS break preflight — OPTIONS must be handled before auth middleware, since it carries no credentials. Wildcard allow-methods or allow-headers with credentials is also invalid and blocks the actual request.

Operational tradeoffs: preflights add a round trip per new cross-origin call, which matters on mobile networks; Access-Control-Max-Age caches the preflight to amortize the cost, at the price of slower propagation of allowlist changes. The robust pattern: explicit origin, method, and header allowlists, Vary: Origin, OPTIONS handled at the gateway, and no credential-carrying CORS without a specific reason.

RSIS3/mykb relevance: the dashboard's cross-origin API calls depend on a correct preflight contract; documenting the allowed methods and headers lets RSIS3 verify the gateway config against the actual client usage.

## Related
- [[wiki/api-protocols/web-security-owasp|Web Security (OWASP)]]
- [[wiki/api-protocols/cors-credentials|CORS with Credentials]]
- [[wiki/api-protocols/cors-wildcard|CORS Wildcards]]
- [[wiki/api-protocols/cross-origin-isolation|Cross-Origin Isolation]]
- [[wiki/api-protocols/cors|CORS]]
- [[wiki/security-auth/cors-policy|CORS Policy]]
- [[wiki/security-auth/same-origin-policy|Same-Origin Policy]]
