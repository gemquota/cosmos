---
type: "concept"
title: "GraphQL Variables"
description: "Parameterizing queries and mutations with typed variables"
tags: ["graphql", "queries", "variables", "api"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# GraphQL Variables

## Summary
GraphQL variables are the typed parameters that keep dynamic values out of the query string: the operation declares `query User($id: ID!)`, the document uses `$id` where the value belongs, and the client sends `{ "id": "42" }` separately. Variables make queries reusable, cacheable, and safe from the interpolation bugs that plague string-built REST URLs.

## Details
- Mechanism: an operation declares variables with types and optional defaults — `query ($id: ID!, $withEmail: Boolean = false)` — and the values are passed in a separate `variables` map on the request. The server validates the values against the declared types before execution (required variables that are missing or mistyped fail with a validation error), and the same document can be executed repeatedly with different values. Defaults let a client omit optional inputs, and nested variables work naturally inside arguments, directives, and input object fields.
- Concrete examples: a user detail query is written once as `query User($id: ID!) { user(id: $id) { name email } }` and reused across the app with different IDs; a search screen sends `query Search($term: String!, $limit: Int = 20)` with `{ term: "signals", limit: 50 }`; a mutation `mutation UpdateProfile($input: ProfileInput!)` receives a whole typed input object, so a form library can pass its values map directly. Because the document is stable, clients can hash it for persisted queries and cache results per (document, variables) pair.
- Failure modes: the classic failures are treating variables as optional when they are not (missing required values produce validation errors at runtime, not compile time, unless codegen catches them), embedding values in the document instead of variables (which breaks caching and persisted queries and invites injection), and type drift between the schema's input types and the client's payloads when codegen is skipped. Input objects that change shape (fields added) are the compatibility trap: clients built against an older schema send unknown fields, which the server may ignore or reject depending on configuration.
- Operational tradeoffs: variables are a free, universal win — they improve caching, security, and maintainability with no downside except the extra field in the request. The operational decision is how strictly to type them: codegen from the schema (GraphQL Code Generator, gql.tada) turns variable mistakes into compile errors and keeps the client and server in sync, at the cost of a build step; hand-written documents rely on runtime validation. Persisted queries depend on variables being external to the document, so the discipline pays off doubly.
- RSIS3/mykb relevance: MyKB's daemon queries (search term, article id, window) should all be parameterized — the same discipline as SQL parameterization, applied to GraphQL — keeping the request documents stable and the values validated, which is exactly how RSIS3 separates code from data.

## Related
- [[wiki/api-protocols/graphql-basics|GraphQL Basics]]
- [[wiki/frontend-frameworks/graphql-directives|GraphQL Directives]]
- [[wiki/frontend-frameworks/graphql-batching|GraphQL Batching]]
- [[wiki/frontend-frameworks/graphql-caching|GraphQL Caching]]
- [[wiki/api-protocols/graphql|GraphQL]]
- [[wiki/api-protocols/graphql-schema-design|GraphQL Schema Design]]
- [[wiki/api-protocols/graphql-security|GraphQL Security]]
