---
type: "concept"
title: "API Backward Compatibility"
description: "Additive changes and compatibility rules"
tags: ["api-design", "backward-compatibility", "versioning", "contracts", "evolution"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://learn.microsoft.com/en-us/azure/architecture/best-practices/api-design#versioning-a-restful-web-api", "https://www.mnot.net/blog/2011/10/25/web_api_versioning_smackdown"]
---

# API Backward Compatibility

## Summary
Backward compatibility means old clients keep working against new server versions. The practical rule is additive evolution: add fields, endpoints, and media types; never remove or reinterpret what already shipped. Compatibility is defined at the wire contract level — request acceptance and response shape — not in the source code.

## Details
- Additive changes are safe: new optional fields, new endpoints, new enum values (if clients tolerate unknowns), and new media type parameters.
- Breaking changes: deleting fields, changing types, making optional fields required, reordering arrays with positional meaning, and changing error semantics.
- Response tolerance: clients must ignore unknown fields, and servers should never reorder or repurpose them — this is why JSON objects beat positional arrays.
- Enum and value evolution: adding enum values breaks strict parsers; use extensible enums, or document that unknown values pass through.
- Semantics are part of the contract: a 200->202 change, a status-code class change, or new failure modes on an existing call are breaking even if the schema is unchanged.
- Backward-compatible versioning is cheaper than versioning: many APIs ship years of additive changes before a breaking major is justified.
- CI enforcement: diff the OpenAPI/protobuf contract in CI and fail merges that break compatibility (tools like openapi-diff, buf breaking).

## Related
- [[wiki/api-protocols/semver-for-apis|SemVer for APIs]] — version numbers encode compatibility
- [[wiki/api-protocols/api-deprecation|API Deprecation]] — phasing out superseded behavior
- [[wiki/api-protocols/media-type-versioning|Media Type Versioning]] — media types as compatibility boundaries
- [[wiki/api-protocols/contract-testing|Contract Testing]] — contracts prove compatibility continuously
- [[wiki/api-protocols/api-design-first|Design-First APIs]] — spec review gates prevent breaks
