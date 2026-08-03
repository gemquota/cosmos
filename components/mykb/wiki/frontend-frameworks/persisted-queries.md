---
type: "concept"
title: "Persisted GraphQL Queries"
description: "Sending query hashes instead of full documents"
tags: ["graphql", "caching", "security", "api"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Persisted GraphQL Queries

## Summary
Persisted queries let clients send a stable hash instead of a full GraphQL document: the client ships the query text once (or the server knows it from a manifest), and thereafter every request is `{ hash, variables }`, with the server resolving the hash to the stored document. The wins are smaller payloads, a locked query surface, and cacheable GET requests.

## Details
- Mechanism: there are two flavors. Automatic persisted queries (APQ) work on a cache-first handshake: the client sends the hash, the server returns `PersistedQueryNotFound`, the client then sends the full document once to register it, and later requests use the hash alone. Trusted persisted queries invert this: the server holds an approved manifest (hashes to documents, generated at build time from the client codebase or an allowlist), and the server never accepts arbitrary documents — a request whose hash is not in the manifest is rejected. Because the document is fixed, the request URL/body is stable, so it becomes a GET request that CDNs can cache.
- Concrete examples: a mobile app ships a generated query manifest, so every fetch is `?hash=abc123&variables=...` — smaller than any document and immune to payload tampering; a public API enables APQ so bandwidth-conscious clients save the document bytes on every call after the first; an internal gateway combines persisted queries with depth and cost limits so the only operations that can run are the ones the frontend team reviewed and registered.
- Failure modes: the classic failure is manifest drift — a client built against an older manifest sends a hash the server no longer knows after a schema or build change, producing hard-to-debug `PersistedQueryNotFound` storms. APQ has a race: a stale cache on the client can bounce between hash-miss and document-send on every request. Persisted queries also interact with schema evolution: renaming a field invalidates every persisted document that referenced it, so the manifest must be regenerated and deployed in lockstep with the schema.
- Operational tradeoffs: the security win is significant — the query surface is reduced to a finite allowlist, killing arbitrary-query DoS vectors (depth, cost, batching attacks) at the door, and variables remain the only input. The tradeoff is process: a build-time manifest means every query change requires a deploy, which slows iteration unless the pipeline is fast; and APQ without an allowlist gains bandwidth but not security. The pairing with cost analysis is complementary: persisted queries shrink the attack surface, cost limits bound the remaining variance from variables.
- RSIS3/mykb relevance: the manifest discipline — an approved, versioned set of operations — is exactly how RSIS3 treats loop configuration: changes are reviewed, versioned, and deployed together, so the runtime only ever executes known-good operations.

## Related
- [[wiki/api-protocols/graphql-basics|GraphQL Basics]] — related coverage in the same cluster
- [[wiki/frontend-frameworks/query-depth-limit|Query Depth Limits]] — related coverage in the same cluster
- [[wiki/frontend-frameworks/graphql-aliases|GraphQL Aliases]] — related coverage in the same cluster
- [[wiki/frontend-frameworks/graphql-variables|GraphQL Variables]] — related coverage in the same cluster
- [[wiki/api-protocols/graphql|GraphQL]] — related coverage in the same cluster
- [[wiki/api-protocols/graphql-schema-design|GraphQL Schema Design]] — related coverage in the same cluster
- [[wiki/api-protocols/graphql-security|GraphQL Security]] — related coverage in the same cluster
