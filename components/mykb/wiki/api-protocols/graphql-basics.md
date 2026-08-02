---
type: "concept"
title: "GraphQL Basics"
description: "Query language and runtime letting clients request exactly the data they need from a typed schema"
tags: ["graphql", "api", "query-language", "schema", "frontend"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://graphql.org/learn/", "https://spec.graphql.org/October2021/"]
---
# GraphQL Basics

## Summary
GraphQL is a query language and server runtime where a typed schema defines available types, fields, queries, and mutations. Clients send declarative operations and receive exactly the requested shape, eliminating REST's over- and under-fetching. The single /graphql endpoint serves all operations, with resolvers on the server filling in data.

## Details
- **Typed schema** — object types, scalars, enums, and interfaces are declared up front; introspection exposes the schema to tooling and generated clients.
- **Queries, mutations, subscriptions** — reads, writes, and realtime streams are separated; arguments, aliases, fragments, and variables shape operations.
- **Resolver model** — each field maps to a resolver; naive resolvers cause N+1 fetches, so data loaders and batching are standard practice.
- **Caching trade-off** — HTTP-level caching is harder because POST dominates; persisted queries, normalized client caches, and CDN GETs mitigate.
- **Worked example** — an agent dashboard could query exactly the pulse fields it renders; the mykb wiki tracks schema design, resolvers, and security so GraphQL adoption is deliberate.
- **Relevance** — for RSIS3-style agents, GraphQL's explicit data requirements map cleanly to tool contracts.

## Related
- [[wiki/frontend-frameworks/apollo-client|Apollo Client]] — adjacent concept in this wiki
- [[wiki/frontend-frameworks/urql-practice|urql in Practice]] — adjacent concept in this wiki
- [[wiki/frontend-frameworks/relay-practice|Relay in Practice]] — adjacent concept in this wiki
- [[wiki/frontend-frameworks/rtk-query|RTK Query]] — adjacent concept in this wiki
- [[wiki/api-protocols/graphql|GraphQL]] — existing coverage
- [[wiki/api-protocols/graphql-queries-mutations|GraphQL Queries & Mutations]] — existing coverage
- [[wiki/api-protocols/graphql-schema-design|GraphQL Schema Design]] — existing coverage
