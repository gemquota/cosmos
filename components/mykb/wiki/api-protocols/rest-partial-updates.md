---
type: "concept"
title: "REST Partial Updates"
description: "PATCH semantics and the merge-patch media type"
tags: ["rest", "patch", "partial-updates", "merge-patch", "api-design"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://www.rfc-editor.org/rfc/rfc7386", "https://www.rfc-editor.org/rfc/rfc5789"]
---

# REST Partial Updates

## Summary
PATCH (RFC 5789) applies a partial modification to a resource, and application/merge-patch+json (RFC 7386) is the simplest standard representation: a JSON object whose present keys are merged into the target and whose null values delete keys. PATCH sits between PUT's full replacement and field-by-field POSTs.

## Details
- PATCH is not idempotent by default: the effect depends on the current state, so clients should pair it with If-Match and an ETag for safe retries.
- Merge-patch semantics: an empty object is a no-op, a null value removes the key, and nested objects merge recursively rather than replacing wholesale.
- PUT vs PATCH: PUT replaces the whole representation (idempotent), PATCH describes a delta; many APIs still accept full documents on PATCH for convenience.
- The JSON Patch (RFC 6902) alternative expresses arrays and moves; merge-patch is simpler but cannot delete array elements (replace the whole array instead).
- Server behavior: apply the delta, return 200 with the updated representation or 204; 422 Unprocessable Content for structurally invalid patches.
- Preconditions: document that a 412 Precondition Failed can result from a stale If-Match, and make retry behavior explicit in the API contract.

## Related
- [[wiki/api-protocols/json-patch|JSON Patch]] — the precise, array-aware alternative to merge-patch
- [[wiki/api-protocols/http-methods|HTTP Methods]] — PATCH is the method for deltas
- [[wiki/api-protocols/optimistic-concurrency|Optimistic Concurrency]] — If-Match makes PATCH safe under concurrency
- [[wiki/api-protocols/http-conditional-requests|HTTP Conditional Requests]] — validators gate partial writes
- [[wiki/api-protocols/json-schema|JSON Schema]] — validating patch bodies before apply
