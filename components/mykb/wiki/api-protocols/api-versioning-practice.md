---
type: "concept"
title: "API Versioning Practice"
description: "Strategies for evolving APIs without breaking consumers: path, header, and media-type versioning"
tags: ["api", "versioning", "semver", "compatibility", "design"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://learn.microsoft.com/en-us/azure/architecture/best-practices/api-design#versioning-a-restful-web-api", "https://stripe.com/blog/api-versioning"]
---
# API Versioning Practice

## Summary
API versioning lets services change contracts while old clients keep working. The common strategies are URL path versions (`/v1/`), custom headers, and media-type versions. Each trades visibility, cache-friendliness, and operational complexity differently.

## Details
- **Path versioning** — `/v1/users` is visible and simple but pollutes URLs and is hard to cache-change; the most common default.
- **Header versioning** — `Accept-Version` or custom headers keep URLs clean but hide versions from logs and caches.
- **Media-type versioning** — `application/vnd.api+json;version=2` is the most semantic but least discoverable.
- **Compatibility discipline** — additive changes (new fields, new endpoints) avoid new versions; breaking changes warrant one; deprecation windows with sunset headers give clients time.
- **Worked example** — the mykb API keeps `/v1` stable and uses additive fields plus a documented deprecation schedule for breaking changes.
- **Relevance** — RSIS3's evolving tool contracts version their schemas the same way, keeping old pulse formats readable.

## Related
- [[wiki/api-protocols/404-vs-410|404 vs 410]] — adjacent concept in this wiki
- [[wiki/api-protocols/301-vs-302|301 vs 302]] — adjacent concept in this wiki
- [[wiki/api-protocols/error-codes-api|Error Codes in APIs]] — adjacent concept in this wiki
- [[wiki/api-protocols/api-docs-generators|API Docs Generators]] — adjacent concept in this wiki
- [[wiki/api-protocols/api-versioning|API Versioning]] — existing coverage
- [[wiki/api-protocols/api-backward-compatibility|API Backward Compatibility]] — existing coverage
- [[wiki/api-protocols/semver-for-apis|SemVer for APIs]] — existing coverage
