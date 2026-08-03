---
type: "concept"
title: "URL Structure"
description: "Anatomy of a URL: scheme, authority, path, query, and fragment components"
tags: ["url", "http", "web-platforms", "standards"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# URL Structure

## Summary
A URL is a structured string with five components — scheme, authority, path, query, and fragment — each with its own grammar, encoding rules, and security implications. Parsing these components correctly and consistently is a prerequisite for routing, access control, and SSRF defenses, because libraries disagree on edge cases in surprising ways.

## Details
- Mechanism: RFC 3986 defines the generic syntax as `scheme://authority/path?query#fragment`. The scheme (`https`) selects the protocol; the authority holds optional userinfo, a host (DNS name or IP), and an optional port; the path identifies a resource hierarchically; the query carries non-hierarchical parameters; the fragment addresses a secondary part of the resource and, critically, is never sent to the server. Each component has different character rules, which is why the same URL is parsed differently depending on whether the parser is strict about the authority, percent-encoding, or Unicode normalization.
- Concrete examples: `https://user:pass@api.example.com:8443/v1/orders?status=open#summary` breaks down into scheme `https`, userinfo `user:pass`, host `api.example.com`, port 8443, path `/v1/orders`, query `status=open`, fragment `summary`. In REST design, the path is the resource hierarchy (`/v1/users/42/orders`), the query is the projection (`?fields=id&sort=-date`), and fragments are almost never used server-side. The same structural rules apply to relative URLs, which resolve against a base URL before any security decision is made.
- Failure modes: the highest-risk failure is parser divergence: one parser treats `https://example.com\@evil.com` as host `evil.com` (backslash handling), another as `example.com`; encoded dots and slashes (`%2e%2e`, `%2f`) bypass path normalization in some stacks; and userinfo in the authority is a classic credential-leak vector. If authorization is decided on a string match instead of parsed components, SSRF and open-redirect bugs follow. Redirects and URL rewriting multiply the surface because each hop re-parses.
- Operational tradeoffs: enforce a canonical URL parser in one place and reuse it everywhere — gateways, proxies, and application code should agree on what a URL means. Normalize before comparing (lowercase scheme and host, resolve dot segments, decode or reject ambiguous encodings), reject userinfo on server-bound URLs, and log the parsed components, not the raw string, when auditing access. The cost is a small abstraction; the payoff is that a single parser differential cannot become a security hole.
- RSIS3/mykb relevance: MyKB's lookup and graph tools operate on slugs and paths; treating them through one canonical URL parser keeps wikilink resolution, search, and the daemon's API consistent, and prevents encoded-path tricks from escaping the wiki's root namespace.

## Related
- [[wiki/api-protocols/http-fundamentals|HTTP Fundamentals]] — related coverage in the same cluster
- [[wiki/api-protocols/uri-vs-url|URI vs URL]] — related coverage in the same cluster
- [[wiki/api-protocols/percent-encoding|Percent-Encoding]] — related coverage in the same cluster
- [[wiki/api-protocols/punycode-domains|Punycode Domains]] — related coverage in the same cluster
- [[wiki/api-protocols/http-methods|HTTP Methods]] — related coverage in the same cluster
- [[wiki/api-protocols/http-headers|HTTP Headers]] — related coverage in the same cluster
- [[wiki/security-auth/same-origin-policy|Same-Origin Policy]] — related coverage in the same cluster
