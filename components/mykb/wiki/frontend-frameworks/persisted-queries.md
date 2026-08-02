---
type: "concept"
title: "Persisted GraphQL Queries"
description: "Sending query hashes instead of full documents"
tags: ["graphql", "caching", "security", "api"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---
# Persisted GraphQL Queries

## Summary
Sending query hashes instead of full documents. A stub in the mykb wiki that frames the concept and the questions to expand into a full article.

## Details
- Clients send hashes; servers look up stored documents
- They shrink payloads and lock the query surface
- Open question — how do persisted queries interact with schema evolution?

## Related
- [[wiki/api-protocols/graphql-basics|GraphQL Basics]] — related coverage in the same cluster
- [[wiki/frontend-frameworks/query-depth-limit|Query Depth Limits]] — related coverage in the same cluster
- [[wiki/frontend-frameworks/graphql-aliases|GraphQL Aliases]] — related coverage in the same cluster
- [[wiki/frontend-frameworks/graphql-variables|GraphQL Variables]] — related coverage in the same cluster
- [[wiki/api-protocols/graphql|GraphQL]] — related coverage in the same cluster
- [[wiki/api-protocols/graphql-schema-design|GraphQL Schema Design]] — related coverage in the same cluster
- [[wiki/api-protocols/graphql-security|GraphQL Security]] — related coverage in the same cluster
