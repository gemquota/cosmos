---
type: "concept"
title: "GraphQL"
description: "Query language and runtime for APIs where clients request exactly the fields and relations they need"
tags: ["graphql", "api", "query-language", "schema", "web-platforms"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
source: ["https://graphql.org/learn/"]
---

# GraphQL

## Summary
GraphQL is a query language and runtime created by Meta that lets clients request exactly the fields they need from a single typed endpoint. A strong schema defines types, queries, mutations, and subscriptions, and resolvers fetch the requested data server-side. It solves REST's over-fetching and under-fetching problems at the cost of caching and complexity.

## Details
- Single endpoint (usually `/graphql`); operations are `query`, `mutation`, and `subscription` for real-time pushes.
- The schema is the contract: types, fields, arguments, and interfaces are introspectable, which powers IDE autocomplete and tooling like GraphiQL.
- Resolvers compose: a `wikiPage(id)` query can resolve authors, tags, and backlinks in one round trip, unlike N+1 REST calls.
- Fragments and aliases reuse field sets; variables parameterize operations; `@deprecated` marks evolving fields.
- Caching is harder than REST because POST bodies don't map to URLs; tools like Apollo and Relay use normalized client caches.
- Worked example: the existing `wiki/api-protocols/entities/graphql` entity notes GraphQL was explored for mykb search but REST remained primary; a GraphQL layer could power the dashboard's knowledge-graph explorer.
- Comparison: REST wins for simplicity and HTTP caching, gRPC wins for typed internal RPC, GraphQL wins for client-driven data shaping.

## Related
- [[wiki/api-protocols/rest-apis|REST APIs]] — the default style GraphQL contrasts with
- [[wiki/api-protocols/json-schema|JSON Schema]] — typed payload validation complements GraphQL schemas
- [[wiki/api-protocols/websockets|WebSockets]] — transport for GraphQL subscriptions
- [[wiki/api-protocols/grpc|gRPC]] — alternative typed contract approach
- [[wiki/concepts/mykb-analysis|Mykb Analysis]] — knowledge graph queries motivate flexible data shaping
- [[wiki/js-ts-ecosystem/entities/typescript-patterns|TypeScript Ecosystem]] — typed clients generated from schemas
- [[wiki/api-protocols/kafka|Apache Kafka]] — event streams can feed live subscriptions
