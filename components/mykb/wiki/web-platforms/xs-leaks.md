---
type: "concept"
title: "XS-Leaks"
description: "Cross-site information leaks through browser side channels"
tags: ["security", "privacy", "attacks", "browsers"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# XS-Leaks

## Summary

Cross-site leaks (XS-Leaks) infer cross-origin information from subtle differences in browser behavior — timing, redirects, error events, window properties — without reading the other origin. They are a class of side-channel attacks that privacy features like cross-origin isolation address.

## Details
- Mechanism: an attacker page embeds or probes a victim resource and measures observable differences: whether a script loads (error event), how long a fetch takes (timing), whether a window property exists, or how many frames are allocated; these correlate with the victim's state (logged in, resource exists, user in group).
- Concrete example: measuring load time of a cross-origin script to test if a user is logged into a service (the response is bigger/faster when authenticated); window.length differences when embedding pages that redirect; and the classic <img onerror> probing for the existence of private resources.
- Failure modes: assuming the same-origin policy fully isolates data — SOP blocks reading but not inference; forgetting that error events, timing, and redirect behavior are observable; and relying on referrer/policy alone, which does not stop timing side channels.
- Operational tradeoffs: defenses include SameSite cookies and cross-origin resource policy (CORP) to block embedding, Cross-Origin-Opener-Policy/Embedder-Policy (COOP/COEP) for cross-origin isolation, and cache-partitioning that browsers now ship; the trade is compatibility with legitimate embeds and third-party integrations.
- RSIS3/mykb relevance: the wiki's iframe-embedded viewers set CORP and COOP headers, and this node documents the header policy the loop applies to new embedded surfaces.
- Testing: browser timing side channels are environment-sensitive; test across network conditions and engines, and treat any new cross-origin embed as a potential leak surface.
- Header ordering: CORP/COOP/COEP must be set on responses for both document and subresources; a missing subresource header silently keeps the leak open.
- Embed review: treat every new cross-origin embed as a potential leak surface; COOP/COEP headers and SameSite cookies are the standing mitigation to keep applied.

## Related
- [[wiki/api-protocols/web-security-owasp|Web Security (OWASP)]]
- [[wiki/web-platforms/dom-clobbering|DOM Clobbering]]
- [[wiki/web-platforms/prototype-pollution-web|Prototype Pollution on the Web]]
- [[wiki/web-platforms/xs-leaks|XS-Leaks]]
- [[wiki/web-platforms/web-apis|Web APIs]]
- [[wiki/web-platforms/dom-manipulation|DOM Manipulation]]
- [[wiki/web-platforms/javascript-runtimes|JavaScript Runtimes]]
