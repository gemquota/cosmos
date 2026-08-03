---
type: "concept"
title: "URI vs URL"
description: "Distinguishing uniform resource identifiers from locators in web standards"
tags: ["url", "uri", "http", "standards"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# URI vs URL

## Summary
URI (Uniform Resource Identifier) is the umbrella term: a string that identifies a resource. URL (Uniform Resource Locator) is the common subset that not only identifies but also locates a resource by describing how to access it — the scheme plus authority plus path that a client can use to fetch it. Every URL is a URI; not every URI is a URL.

## Details
- Mechanism: RFC 3986 defines a URI's generic syntax as `scheme://authority/path?query#fragment`, and the distinction is functional rather than syntactic. A URL includes access information: `https://example.com/docs/api` says where the resource lives and how to retrieve it. A URN (Uniform Resource Name) identifies without locating: `urn:isbn:0451450523` names a book by ISBN but carries no access method. Since the WHATWG URL standard collapsed the practical distinction and most developer tooling treats URL and URI as synonyms, the difference matters mainly when designing identifier systems rather than when parsing web addresses.
- Concrete examples: `https://mykb.local/wiki/syntheses/loop-notes.md` is a URL; `urn:uuid:9a7e...` is a URN; `mailto:dev@example.com` and `tel:+15551234` are URIs that identify a resource and imply an access scheme, blurring the line. In REST design, resource identifiers in URLs are routinely expected to be opaque (`/orders/42`), which is a URI discipline: the identifier should not encode mutable semantics, only the locator structure.
- Failure modes: the practical failures come from assuming URI features that URLs do not provide: treating a URL as a stable name breaks when the resource moves (hence the need for 301 redirects or content-addressable storage); building identifiers out of URLs leaks location into identity, so a rehosted wiki page silently changes meaning; and parsing differences between URI, URL, and IRI (internationalized) implementations cause validation bugs, especially with percent-encoding, punycode, and Unicode domains.
- Operational tradeoffs: for most web systems, using the URL as the identifier is fine because the locator is the contract; systems that need durable identity independent of location (documents, knowledge objects, artifacts) should mint separate IDs (UUIDs, content hashes) and treat the URL as one access path among several. The cost of URN-style identifiers is a resolution layer you must build and maintain; the benefit is that renames and moves stop breaking references.
- RSIS3/mykb relevance: MyKB's wikilinks are URI-style references to articles; keeping the slug stable and treating the filesystem path as a locator means the knowledge graph stays valid across reorgs — exactly the identifier-versus-locator discipline this distinction teaches.

## Related
- [[wiki/api-protocols/http-fundamentals|HTTP Fundamentals]]
- [[wiki/api-protocols/percent-encoding|Percent-Encoding]]
- [[wiki/api-protocols/punycode-domains|Punycode Domains]]
- [[wiki/api-protocols/url-structure|URL Structure]]
- [[wiki/api-protocols/http-methods|HTTP Methods]]
- [[wiki/api-protocols/http-headers|HTTP Headers]]
- [[wiki/security-auth/same-origin-policy|Same-Origin Policy]]
