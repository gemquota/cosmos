---
type: "concept"
title: "Optimistic Concurrency"
description: "Version/ETag-based conflict detection"
tags: ["concurrency", "etag", "optimistic-locking", "api-design", "http"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://www.rfc-editor.org/rfc/rfc9110#name-if-match", "https://www.martinfowler.com/eaaCatalog/optimisticOfflineLock.html"]
---

# Optimistic Concurrency

## Summary
Optimistic concurrency assumes conflicts are rare: the client reads a resource with its current version, makes changes, and submits them with a precondition asserting that version is still current. If someone else changed it first, the write is rejected with 412 Precondition Failed — no locks, no waiting.

## Details
- Version signals: an ETag header (strong) or a version field in the payload; both identify the exact state the client based its edit on.
- Write pattern: PUT or PATCH with If-Match: "<etag>" — the server compares, applies, and issues a new ETag; mismatch returns 412.
- Why optimistic: readers never block writers; contention cost is paid only when a conflict actually occurs, at the price of occasional rejected writes.
- Client handling: on 412, refetch the resource, merge or surface the conflict, and retry — the UI owns the reconciliation.
- Granularity: versions can be per-resource or per-field; document which one your API uses so clients know what a mismatch means.
- Beware weak ETags: W/ variants are fine for caching but must not guard writes; use strong validators for If-Match.
- Distributed caveats: read-modify-write races between proxy and database need atomic compare-and-set, not just an application-level check.

## Related
- [[wiki/api-protocols/http-conditional-requests|HTTP Conditional Requests]] — If-Match is the HTTP precondition
- [[wiki/api-protocols/rest-partial-updates|REST Partial Updates]] — PATCH plus validators prevents clobbering
- [[wiki/api-protocols/json-patch|JSON Patch]] — test operations add in-body preconditions
- [[wiki/devops-infra/optimistic-locking|Optimistic Locking]] — the database-side versioning pattern
- [[wiki/api-protocols/http-caching|HTTP Caching]] — ETags serve both caching and concurrency
