---
type: "concept"
title: "REST API Design"
description: "Resource-oriented HTTP API design: nouns, methods, status codes, and consistent conventions"
tags: ["rest", "api", "http", "design", "json"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://developer.mozilla.org/en-US/docs/Glossary/REST", "https://learn.microsoft.com/en-us/azure/architecture/best-practices/api-design"]
---
# REST API Design

## Summary
REST organizes APIs around resources identified by URLs and manipulated with standard HTTP methods. Good REST design makes endpoints predictable: collections and items, explicit status codes, and consistent query and error conventions. It remains the default for public APIs because it is simple, cacheable, and universally tooled.

## Details
- **Resources, not actions** — URLs name nouns (`/users/42`), methods express verbs. Non-CRUD actions are modeled as sub-resources or controller endpoints with explicit semantics.
- **Status codes carry meaning** — 2xx for success, 3xx for redirection, 4xx for client errors, 5xx for server faults. 201 Created, 204 No Content, 400/422 for validation, and 429 for rate limits are the workhorses.
- **Consistency conventions** — filtering, sorting, pagination, and sparse fieldsets use documented query parameters; errors use a stable envelope with machine-readable codes.
- **Versioning** — path, header, or media-type versioning lets the API evolve without breaking consumers.
- **Worked example** — the mykb FastAPI service exposes REST resources with automatic OpenAPI docs; wiki notes on error contracts and pagination make the conventions explicit.
- **Trade-offs** — REST over-fetches for client-driven queries (GraphQL) and lacks typed wire contracts (gRPC); hybrid designs pick per-concern.

## Related
- [[wiki/api-protocols/quota-headers|Quota Headers]] — adjacent concept in this wiki
- [[wiki/api-protocols/retry-after-web|Retry-After]] — adjacent concept in this wiki
- [[wiki/api-protocols/429-handling|Handling 429]] — adjacent concept in this wiki
- [[wiki/api-protocols/503-handling|Handling 503]] — adjacent concept in this wiki
- [[wiki/api-protocols/http-status-codes|HTTP Status Codes]] — existing coverage
- [[wiki/api-protocols/retry-backoff|Retry & Backoff]] — existing coverage
- [[wiki/api-protocols/error-contract-design|Error Contract Design]] — existing coverage
