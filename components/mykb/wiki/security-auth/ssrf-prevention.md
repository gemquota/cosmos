---
type: "concept"
title: "SSRF Prevention"
description: "Preventing server-side requests to internal or unintended targets"
tags: ["ssrf", "server-side", "defense", "network"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://cheatsheetseries.owasp.org/cheatsheets/Server_Side_Request_Forgery_Prevention_Cheat_Sheet.html"]
---

# SSRF Prevention

## Summary
Server-side request forgery (SSRF) lets an attacker make the server fetch URLs of the attacker's choosing — cloud metadata, internal services, or localhost. Prevention combines allowlisting, canonicalization, and network segmentation; any URL-fetching tool must implement SSRF guardrails.

## Details
- Mechanism: the server-side request path validates each URL before fetching: protocol allowlisting (http/https only), host allowlisting or denylisting of internal ranges, canonicalization (normalize redirects, encodings, and DNS), resolution checks (resolve the hostname and verify the IP is not internal), and denial of cloud metadata endpoints (169.254.169.254 and equivalents).
- Concrete example: a link-preview feature fetches arbitrary URLs; the guardrail resolves the hostname, rejects loopback and private ranges, forbids redirects to internal hosts, and blocks the metadata endpoint; a webhook handler validates callback URLs the same way; a scraper runs in a segmented network so even a bypass reaches nothing sensitive.
- Failure modes: redirects that bypass the initial check (the final URL differs from the validated one); DNS rebinding where resolution changes between validation and fetch; IPv6 and encoding tricks that slip past naive checks; cloud metadata reachable from the fetching host; missing checks in one of several fetch paths.
- Tradeoffs: strict allowlisting limits what can be fetched at the cost of functionality; network segmentation is the strongest control but needs infrastructure; the mature pattern is defense in depth — validate URLs, restrict protocols, block internal ranges, forbid redirects, and isolate fetching hosts.
- Operational notes: centralize URL fetching behind one validated library, test bypass techniques, and keep metadata endpoints unreachable from fetch hosts.
- RSIS3 relevance: any URL-fetching tool (link previews, scrapers, webhooks) in the wiki must implement SSRF guardrails — outbound requests are a trust boundary like any other.


## Related
- [[wiki/security-auth/xml-external-entities|XML External Entities]] — XXE can trigger SSRF
- [[wiki/security-auth/network-segmentation|Network Segmentation]] — limiting internal reachability
- [[wiki/api-protocols/webhooks|Webhooks]] — inbound URL-driven requests need validation
- [[wiki/api-services/cloud-security-posture|Cloud Security Posture]] — metadata endpoints as targets
- [[wiki/security-auth/least-privilege|Least Privilege]] — SSRF guardrails are outbound least privilege
