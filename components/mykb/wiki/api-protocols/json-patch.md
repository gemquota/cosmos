---
type: "concept"
title: "JSON Patch"
description: "RFC 6902 operation format for partial updates"
tags: ["json", "patch", "partial-updates", "rfc6902", "api-design"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://www.rfc-editor.org/rfc/rfc6902", "https://jsonpatch.com/"]
---

# JSON Patch

## Summary
JSON Patch (RFC 6902) describes modifications to a JSON document as an ordered list of operations: add, remove, replace, move, copy, and test. Applied against a target document via the application/json-patch+json media type, it gives fine-grained, atomic partial updates where whole-resource PUT would overwrite too much.

## Details
- Each operation is an object with op and path (a JSON Pointer, RFC 6901); add, replace, move, and copy also carry a value or from pointer.
- add inserts at an array index or object key; remove deletes it; replace is add plus remove in one step; move and copy reuse an existing value; test asserts a value before proceeding.
- Semantics: a failed test aborts the whole patch (atomicity), which is why clients combine test with If-Match-style preconditioning for optimistic concurrency.
- Media type application/json-patch+json; the server applies operations in order and returns 204 No Content or 200 with the updated document.
- Compared with merge-patch (RFC 7386), JSON Patch expresses deletions and array surgery explicitly, while merge-patch cannot remove array elements or null-valued keys without special conventions.
- Implementations exist in most languages; libraries validate pointer syntax, index bounds, and operation ordering before mutating.

## Related
- [[wiki/api-protocols/rest-partial-updates|REST Partial Updates]] — JSON Patch is one PATCH representation
- [[wiki/api-protocols/json-schema|JSON Schema]] — schema validation complements patch application
- [[wiki/api-protocols/optimistic-concurrency|Optimistic Concurrency]] — test operations guard concurrent edits
- [[wiki/api-protocols/http-methods|HTTP Methods]] — PATCH carries the patch document
- [[wiki/api-protocols/error-contract-design|Error Contract Design]] — invalid patches return structured errors
