---
type: "concept"
title: "Third-Party Cookies"
description: "Cookies set by embedded origins and their tracking and deprecation story"
tags: ["cookies", "privacy", "web", "security"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Third-Party Cookies

## Summary
A third-party cookie is one set by an origin other than the site the user is visiting, usually through embedded content: ad networks, analytics, video players, and social widgets. They powered cross-site identity and advertising for two decades, and they are now being partitioned or blocked by every major browser, forcing a redesign of large parts of the web's tracking and federated-login machinery.

## Details
- Mechanism: when a page at `shop.example` embeds a script from `ads.net`, that script can read or set cookies scoped to `ads.net`; on the user's next visit to a different site embedding the same script, `ads.net`'s cookies come along, letting the network recognize the same browser across sites. That cross-site recognition is the tracking primitive. The SameSite attribute and third-party cookie blocking break the primitive: with blocking, the embedded origin gets a fresh, cookie-less context on each top-level site.
- Concrete examples: an ad exchange identifying a user across publisher sites; a video host remembering playback settings per viewer; an analytics suite stitching sessions across domains; federated login iframes (OAuth popups, "Sign in with X" widgets) that historically relied on third-party cookies to keep the user's session inside the iframe. Each of these is being re-architected with first-party-set cookies, partitioned storage, or redirect-based flows that hop through the identity provider's own origin.
- Failure modes: the deprecation failure modes are mostly silent: embedded widgets lose session state, users appear logged out inside iframes, A/B and analytics identity breaks, and teams rediscover the breakage through metric cliffs weeks later. The security failure mode is the opposite extreme — treating third-party cookies as fully dead and forgetting that `SameSite=None; Secure` cookies still exist and still carry cross-site identity when embedded contexts allow them.
- Operational tradeoffs: third-party cookies bought convenience for federated features at the price of pervasive cross-site tracking, and the ecosystem is trading that convenience for privacy. The migration path is to stop depending on them: use first-party storage for your own state, partition-aware APIs (Storage Partitioning, CHIPS) where a genuine embedded use case remains, redirect-based OAuth for logins, and fingerprint-resistant analytics. None of these are drop-in replacements; each changes a privacy or UX property, so the tradeoffs must be decided per feature.
- RSIS3/mykb relevance: the deprecation is a live example of external invariants changing under a system: like RSIS3 loops, web features that silently rely on ambient browser state need explicit re-validation when the platform shifts, and the memory layer should record such platform changes as durable lessons rather than incident trivia.

## Related
- [[wiki/api-protocols/secure-cookies|Secure Cookies]] — related coverage in the same cluster
- [[wiki/api-protocols/partitioned-cookies|Partitioned Cookies]] — related coverage in the same cluster
- [[wiki/api-protocols/cross-site-requests|Cross-Site Requests]] — related coverage in the same cluster
- [[wiki/api-protocols/cookie-flags|Cookie Flags]] — related coverage in the same cluster
- [[wiki/api-protocols/http-cookies|HTTP Cookies]] — related coverage in the same cluster
- [[wiki/api-protocols/csrf|CSRF]] — related coverage in the same cluster
- [[wiki/security-auth/same-origin-policy|Same-Origin Policy]] — related coverage in the same cluster
