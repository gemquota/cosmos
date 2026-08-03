---
type: "concept"
title: "Conditional PUT"
description: "Using If-Match and ETags to prevent lost updates on writes"
tags: ["http", "api", "concurrency", "design"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Conditional PUT

## Summary
A conditional PUT uses If-Match or If-None-Match with ETags to make writes safe against concurrent modification: the server applies the write only if the precondition holds, turning lost updates into clean conflicts.

## Details
A conditional PUT attaches a precondition — If-Match: "abc" (apply only if the current ETag matches) or If-None-Match: * (apply only if the resource does not exist) — so the server can detect concurrent modification before overwriting. The client reads the resource, edits it locally, and writes back with the ETag it read; if someone else changed the resource in between, the server responds 412 Precondition Failed instead of silently clobbering the other edit.

The mechanism: the server computes an ETag (usually a hash of the representation or a version counter) and returns it on GET and HEAD and on writes. On PUT with If-Match, the server compares the tag; a mismatch means the resource changed since the client read it, and the server rejects with 412 — no body, no state change. If-None-Match: * is the create-or-fail primitive, which fixes the classic create race where two clients both PUT the same new URL and the second overwrites the first.

Concrete example: two editors load the same wiki page (ETag "v7"), both edit, and both PUT. The first PUT with If-Match: "v7" succeeds and bumps the tag to "v8"; the second PUT with If-Match: "v7" gets 412. The client then re-reads, diffs, and merges — an optimistic concurrency loop that never loses a write silently. Payment and order APIs use the same pattern to reject stale amount updates.

Failure modes: generating weak or non-changing ETags defeats the mechanism — a tag that never changes never conflicts; ignoring the 412 and force-PUTting recreates the lost update; retrying the whole write on 412 without a fresh read can loop forever; and conditional writes without a server-side transaction between check and apply can still race on backends where the check is not atomic with the write.

Operational tradeoffs: conditional PUTs add one round trip (read before write) and require the server to implement ETags and atomic check-and-set, but they eliminate the worst distributed-systems bug — silent overwrites — at the API level. Where the backend is a document store, the ETag should map to a real revision or version field so the check is atomic at the storage layer.

RSIS3/mykb relevance: concurrent RSIS3 loops editing the same wiki page are exactly this race; the standing rule is "read, edit, conditional PUT with ETag, merge on 412" — a pattern already natural to the wiki's revision model.

## Related
- [[wiki/api-protocols/rest-api-design|REST API Design]]
- [[wiki/api-protocols/error-codes-api|Error Codes in APIs]]
- [[wiki/api-protocols/error-contract-design|Error Contract Design]]
- [[wiki/api-protocols/problem-details|Problem Details]]
- [[wiki/api-protocols/http-conditional-requests|HTTP Conditional Requests]]
