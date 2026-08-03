---
type: "concept"
title: "Request Smuggling"
description: "Desynchronizing frontend and backend request parsing to smuggle requests"
tags: ["security", "http", "attacks", "proxies"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Request Smuggling

## Summary
HTTP request smuggling exploits disagreements between a frontend (proxy, CDN, load balancer) and a backend about where one request ends and the next begins. The smuggled second request can bypass access controls, poison caches, or hijack other users' requests.

## Details
A proxy and origin both parse the request stream using Content-Length and Transfer-Encoding. When they disagree — one trusts Content-Length, the other Transfer-Encoding, or they parse the TE header differently (CL.TE, TE.CL, TE.TE) — an attacker crafts a request whose first part the frontend sees as one request and the backend sees as a request plus a smuggled prefix. The smuggled bytes are then prepended to the next legitimate request that arrives.

The mechanism: in CL.TE smuggling, the frontend uses Content-Length and forwards the body; the backend uses Transfer-Encoding: chunked and interprets part of the body as a complete chunked message, leaving the rest to be read as the start of the next request. The attacker's smuggled request sits in the connection, waiting for the next victim request to be concatenated after it. Consequences range from cache poisoning and WAF bypass to full request hijacking of other users' traffic.

Concrete example: an attacker sends a request that the CDN forwards whole, but the origin parses as two requests — the first a harmless GET, the second a smuggled GET /admin/delete?id=1 with the attacker's headers. The next request that shares the connection gets the smuggled request processed first, with the victim's connection state — a request hijack that can steal sessions or trigger admin actions.

Failure modes: frontend and backend using different parsers, or the same parser with different normalization (stripping whitespace, case, or duplicate headers differently); legacy servers that ignore Transfer-Encoding; and connection reuse amplifying the attack (each reused connection delivers the smuggled request to the next user). Smuggling is hard to detect because the smuggled request never appears in the frontend's logs.

Operational tradeoffs: the durable fix is protocol normalization: reject requests with conflicting Content-Length and Transfer-Encoding, strip or canonicalize both headers at the edge, and use HTTP/2 end-to-end where possible (its framing removes the ambiguity). Testing requires differential requests against the actual proxy-origin pair. This is a class where configuration and parser choice matter more than application code.

RSIS3/mykb relevance: any gateway the wiki deploys must normalize framing headers; documenting the CL/TE rule gives RSIS3's infra checks a concrete test.

## Related
- [[wiki/api-protocols/web-security-owasp|Web Security (OWASP)]] — related coverage in the same cluster
- [[wiki/api-protocols/ssrf-practice|SSRF Attacks]] — related coverage in the same cluster
- [[wiki/api-protocols/idor-web|IDOR on the Web]] — related coverage in the same cluster
- [[wiki/api-protocols/mass-assignment|Mass Assignment]] — related coverage in the same cluster
- [[wiki/security-auth/ssrf-prevention|SSRF Prevention]] — related coverage in the same cluster
- [[wiki/security-auth/deserialization-attacks|Deserialization Attacks]] — related coverage in the same cluster
- [[wiki/security-auth/privilege-escalation|Privilege Escalation]] — related coverage in the same cluster
