---
type: "concept"
title: "GraphQL Queries & Mutations"
description: "Operations, arguments, and variables"
tags: ["graphql", "queries", "mutations", "operations", "api-design"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://graphql.org/learn/queries/", "https://spec.graphql.org/October2021/#sec-Language.Operations"]
---

# GraphQL Queries & Mutations

## Summary
GraphQL operations — queries, mutations, and subscriptions — are written in the GraphQL language and executed against the schema. Queries fetch data, mutations change it, and both support arguments, variables, aliases, and operation names that make requests reusable and cacheable.

## Details
- Operation shape: query, mutation, or subscription keyword, optional operation name, variable definitions, and a selection set; anonymous operations are allowed but named ones aid debugging.
- Arguments: field-level arguments parameterize selection (user(id: 42) { name }); lists and input objects pass complex filters.
- Variables: $id: ID! declared at the top and passed as a separate JSON variables map, keeping queries static and cache-friendly.
- Aliases: two selections of the same field with different arguments need aliases (first: user(id: 1), second: user(id: 2)) to coexist in one response.
- Mutations run serially in order, while query fields may resolve in parallel — a semantic guarantee clients rely on for sequential side effects.
- Mutation conventions: return the changed resource and enough context to update the client cache (for example { updateUser(input: ...) { user { id name } } }).
- Directives (@include, @skip, @deprecated) modify execution and evolve schemas without breaking clients.

## Related
- [[wiki/api-protocols/graphql-schema-design|GraphQL Schema Design]] — root types define valid operations
- [[wiki/api-protocols/graphql-resolvers|GraphQL Resolvers]] — operations trigger resolver execution
- [[wiki/api-protocols/graphql-subscriptions|GraphQL Subscriptions]] — the third operation type for realtime
- [[wiki/api-protocols/graphql-fragments|GraphQL Fragments]] — fragments make operation selections reusable
- [[wiki/api-protocols/graphql-error-handling|GraphQL Error Handling]] — operations return both data and errors
