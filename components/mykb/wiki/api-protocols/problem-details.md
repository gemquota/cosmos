---
type: "concept"
title: "Problem Details"
description: "RFC 9457 error response format"
tags: ["problem-details", "errors", "rfc9457", "error-handling", "http"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://www.rfc-editor.org/rfc/rfc9457", "https://datatracker.ietf.org/doc/html/rfc9457"]
---

# Problem Details

## Summary
RFC 9457 (Problem Details for HTTP APIs) standardizes error responses as a JSON object with type, title, status, detail, and instance fields, served as application/problem+json. It replaces per-API error formats with one interoperable shape that clients can parse generically and extend with custom members.

## Details
- Core members: type (a URI identifying the problem class), title (short summary), status (HTTP status code), detail (human explanation), and instance (URI of the specific occurrence).
- Media type: application/problem+json (and +xml); the Content-Type lets clients detect the format without sniffing.
- Extensibility: custom members (errors array, retry_after, code) are allowed and become part of the problem class's schema.
- Compatibility: many APIs ship a Content-Type of application/json with problem-shaped bodies; strictly, the +json suffix should be used.
- Status duplication: the status member duplicates the HTTP code — keep them consistent; changing one without the other confuses clients.
- Documentation: publish the type URIs (often relative to your docs, e.g., /problems/rate-limited) with full descriptions.
- Adoption: used by GitHub, Microsoft, and the ASP.NET Core default error pipeline, making it the de facto REST error standard.

## Related
- [[wiki/api-protocols/error-contract-design|Error Contract Design]] — problem details are a concrete contract
- [[wiki/api-protocols/http-status-codes|HTTP Status Codes]] — status member mirrors the class
- [[wiki/api-protocols/response-envelopes|Response Envelopes]] — errors as a first-class envelope
- [[wiki/api-protocols/json-api-spec|JSON:API]] — JSON:API error objects follow the same philosophy
- [[wiki/api-protocols/rate-limit-headers|Rate Limit Headers]] — retry hints pair with 429 problems
