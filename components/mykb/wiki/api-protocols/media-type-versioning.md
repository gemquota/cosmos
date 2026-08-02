---
type: "concept"
title: "Media Type Versioning"
description: "Vendor media types for versioned representations"
tags: ["versioning", "media-types", "content-negotiation", "api-design", "rest"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://learn.microsoft.com/en-us/azure/architecture/best-practices/api-design#versioning-a-restful-web-api", "https://www.ietf.org/rfc/rfc6838.txt"]
---

# Media Type Versioning

## Summary
Media type versioning moves the version into the representation: clients request application/vnd.company.resource.v2+json instead of a versioned URL. The same resource URI stays stable across versions, and content negotiation selects the shape — a cleaner separation of resource identity from representation.

## Details
- Syntax (RFC 6838): vendor tree (vnd.), the company identifier, the resource type, an optional version, and +json/+xml suffix: application/vnd.api+json or application/vnd.github.v3+json.
- Request: the client sends Accept: application/vnd.company.widget.v2+json; the server answers with Content-Type set to the matched representation.
- Benefits: one URI per resource, versions chosen per client, and no URL churn; API clients upgrade by changing a header.
- Costs: caches must key on Vary: Accept; debuggers see opaque URLs; and some HTTP tooling does not handle custom media types gracefully.
- Hybrid practice: GitHub historically combined a version in the Accept header with path-based majors — evidence that both approaches coexist.
- Negotiation defaults: servers must define what a missing or wildcard Accept gets (usually the latest stable version).
- Registry discipline: register types in the IANA media type registry or document custom types; avoid inventing ad-hoc suffixes.

## Related
- [[wiki/api-protocols/content-negotiation|Content Negotiation]] — media types are negotiated via Accept
- [[wiki/api-protocols/semver-for-apis|SemVer for APIs]] — version numbers follow semver semantics
- [[wiki/api-protocols/api-backward-compatibility|API Backward Compatibility]] — media type versions create parallel contracts
- [[wiki/api-protocols/json-api-spec|JSON:API]] — a vendor media type in production use
- [[wiki/api-protocols/http-caching|HTTP Caching]] — Vary: Accept keeps versions cacheable
