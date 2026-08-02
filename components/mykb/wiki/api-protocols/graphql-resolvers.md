---
type: "concept"
title: "GraphQL Resolvers"
description: "Resolver functions, data fetching, and batching"
tags: ["graphql", "resolvers", "data-fetching", "backend", "performance"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://graphql.org/learn/execution/", "https://www.apollographql.com/docs/apollo-server/data/resolvers/"]
---

# GraphQL Resolvers

## Summary
Resolvers are the functions that produce values for schema fields. GraphQL executes queries depth-first by calling resolvers, so each field can fetch from a different source — database, REST service, or in-memory cache. Resolver design determines latency, load, and correctness of the whole API.

## Details
- Every field can have a resolver; the default walks the parent object's properties, which works only for already-loaded data.
- Execution model: resolvers are awaited in parallel where possible (siblings), but a parent must resolve before its children, creating N+1 hazard at each level.
- The resolver signature receives (parent, args, context, info); context carries shared state such as the current user, data sources, and tracing spans.
- Batching: DataLoader deduplicates and coalesces per-request loads — collect keys, fire one query, fan results back — turning N+1 into 2 queries.
- Keep resolvers thin: fetch and shape data, push business logic into services, and never leak ORM entities straight into responses.
- Error handling: resolvers throw or return errors in the errors array; partial results still succeed, so clients must handle mixed success.
- Performance: query cost grows with nesting, so add depth limits and resolve hotspots; trace resolver timings to find slow branches.

## Related
- [[wiki/api-protocols/graphql-n-plus-one|GraphQL N+1 Problem]] — the failure mode resolver batching prevents
- [[wiki/api-protocols/graphql-schema-design|GraphQL Schema Design]] — fields in the schema become resolvers
- [[wiki/api-protocols/graphql-error-handling|GraphQL Error Handling]] — resolver failures surface in the errors array
- [[wiki/api-protocols/graphql-security|GraphQL Security]] — depth and complexity limits constrain resolver work
- [[wiki/api-protocols/graphql-queries-mutations|GraphQL Queries & Mutations]] — operations select which resolvers run
