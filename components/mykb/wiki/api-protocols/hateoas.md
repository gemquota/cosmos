---
type: "concept"
title: "HATEOAS"
description: "Hypermedia links that drive application state"
tags: ["hateoas", "hypermedia", "rest", "api-design", "discoverability"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://restfulapi.net/hateoas/", "https://en.wikipedia.org/wiki/HATEOAS"]
---

# HATEOAS

## Summary
HATEOAS (Hypermedia As The Engine Of Application State) makes responses self-describing: each representation carries links describing the transitions the client may take next. Instead of hard-coding URLs, the client follows rel-tagged links, so the API can evolve its address space without breaking consumers.

## Details
- Core mechanics: a response embeds a links object (self, next, cancel, approve) with rel labels and hrefs; the client navigates by relation name, not by remembered paths.
- Formats: HAL (application/hal+json) with _links and _embedded, JSON:API's links objects, and RFC 8288 Link headers for non-JSON resources.
- Discoverability is the payoff: new capabilities appear as links without a client release, and the root resource advertises entry points.
- Costs: extra fields bloat every payload, clients must implement link traversal, and automated testing must assert link presence and rel semantics.
- The Web Linking standard (RFC 8288) defines rel registrations; IANA maintains well-known relation types such as next, edit, and alternate.
- Adoption is selective: many teams apply HATEOAS to workflow-heavy domains (payments, approvals) while leaving read-heavy CRUD APIs plain.

## Related
- [[wiki/api-protocols/rest-maturity-model|REST Maturity Model]] — level 3 is defined by hypermedia
- [[wiki/api-protocols/json-api-spec|JSON:API]] — links objects are built into the spec
- [[wiki/api-protocols/rest-resource-design|REST Resource Design]] — stable resources make links meaningful
- [[wiki/api-protocols/api-backward-compatibility|API Backward Compatibility]] — links let URLs evolve without breaking clients
- [[wiki/api-protocols/openapi|OpenAPI]] — documenting links and examples in the contract
