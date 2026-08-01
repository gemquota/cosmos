---
type: "concept"
title: "API Versioning"
description: "Managing incompatible API changes over time with URL, header, or query-string version identifiers"
tags: ["api", "versioning", "semver", "contracts", "backward-compatibility"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
source: ["https://learn.microsoft.com/en-us/azure/architecture/best-practices/api-design"]
---

# API Versioning

## Summary
API versioning is the practice of making breaking changes without breaking existing consumers. Version identifiers travel in the URL path, a custom header, the `Accept` header, or a query parameter. Good versioning policy, combined with deprecation timelines and documentation, keeps multi-client ecosystems like dashboards, agents, and mobile apps stable.

## Details
- Common styles: path (`/v1/pages`), header (`X-API-Version: 2`), query (`?api-version=2`), and media type (`Accept: application/vnd.my+json; version=2`).
- Path versioning is simplest and most visible; header/media-type versioning keeps URLs clean but hides the version in tooling.
- Prefer additive, backward-compatible evolution first: new fields, new endpoints, and `deprecated` flags delay the need for a major version.
- Semantic Versioning (SemVer) applies to API releases: MAJOR for breaking, MINOR for additive, PATCH for fixes; document the mapping in your spec.
- Deprecation policy: announce removal, keep the old version serving during a sunset window, and log usage so the cutover is data-driven.
- Worked example: if the mykb daemon's `/search` response changes shape, bumping to `/v2/search` lets RSIS3 upgrade on its own schedule.
- OpenAPI `deprecated: true` plus changelog entries make version diffs reviewable in CI.

## Related
- [[wiki/api-protocols/rest-apis|REST APIs]] — versioned resources are REST resources
- [[wiki/api-protocols/openapi|OpenAPI]] — spec diffs reveal breaking changes
- [[wiki/api-protocols/webhooks|Webhooks]] — payload versioning applies to callbacks too
- [[wiki/api-protocols/grpc|gRPC]] — versioning via package and field numbers
- [[wiki/devops-infra/github-actions|GitHub Actions]] — CI enforces spec-compat checks
- [[wiki/concepts/mykb-implementation-report|Mykb Implementation Report]] — version alignment across projects
- [[wiki/api-protocols/protobuf|Protocol Buffers]] — field-number evolution parallels versioning
- [[wiki/concepts/triad-architecture|Triad Architecture]] — version alignment across the three projects
