---
type: "concept"
title: "SSRF Attacks"
description: "Server-Side Request Forgery: abusing server fetches to reach internal services"
tags: ["security", "ssrf", "api", "attacks"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# SSRF Attacks

## Summary
Server-Side Request Forgery (SSRF) is an attack where the attacker controls the destination of a server-side fetch — a webhook URL, an image proxy, a PDF renderer, a status check — and uses the server's network position to reach services that were never meant to be public: cloud metadata endpoints, internal dashboards, databases, and admin panels.

## Details
- Mechanism: the application accepts a URL and fetches it with the privileges of the server, which sits inside the network perimeter. An attacker submits `http://169.254.169.254/latest/meta-data/iam/security-credentials/` (the AWS metadata service) or `http://localhost:6379` (an internal Redis), and the server happily performs the request, returning internal data in the response or triggering internal actions. Redirects compound the problem: a public URL that 302s to an internal address bypasses simple checks on the submitted value.
- Concrete examples: an image-resize service that fetches user-supplied URLs and exposes the fetched content; a webhook tester that lets users send requests to arbitrary hosts and is used to scan the internal network; a PDF generator that renders a supplied URL, leaking intranet pages into the generated file; an agent or chatbot tool that fetches links on behalf of users, which is why tool-fetch features are a favorite SSRF target.
- Failure modes: deny-lists of `localhost`, `127.0.0.1`, and metadata IPs fail against DNS rebinding, decimal/hex IP encodings, IPv6 literals, redirects, and URL parsers that disagree with the actual fetch library (parser differentials). Even "safe" schemes can misfire: `file://`, `gopher://`, and `dict://` reach local files and arbitrary TCP ports. The second-order failure is an allow-list that is too broad, like permitting any `*.internal.example` name that includes attacker-influenced subdomains.
- Operational tradeoffs: allow-lists of hosts or domains are far stronger than deny-lists, but they break legitimate use cases like arbitrary webhook targets; the realistic middle is an SSRF-aware egress proxy that resolves DNS itself, blocks private ranges and metadata IPs at the network layer, disallows redirects to blocked destinations, and validates the scheme. Validate URLs with the same parser the fetch uses, pin DNS resolution, and never return raw response bodies of internal requests to the caller.
- RSIS3/mykb relevance: RSIS3 loop tools that fetch URLs or webhook targets must scope egress the same way: treat every tool-fetch as an attacker-influenced request and route it through the same allow-list and proxy discipline.

## Related
- [[wiki/api-protocols/web-security-owasp|Web Security (OWASP)]] — related coverage in the same cluster
- [[wiki/api-protocols/idor-web|IDOR on the Web]] — related coverage in the same cluster
- [[wiki/api-protocols/mass-assignment|Mass Assignment]] — related coverage in the same cluster
- [[wiki/api-protocols/insecure-deserialization|Insecure Deserialization]] — related coverage in the same cluster
- [[wiki/security-auth/ssrf-prevention|SSRF Prevention]] — related coverage in the same cluster
- [[wiki/security-auth/deserialization-attacks|Deserialization Attacks]] — related coverage in the same cluster
- [[wiki/security-auth/privilege-escalation|Privilege Escalation]] — related coverage in the same cluster
