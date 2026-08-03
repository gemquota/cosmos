---
type: "concept"
title: "GraphQL Directives"
description: "@include and @skip conditional execution in queries"
tags: ["graphql", "directives", "queries", "api"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# GraphQL Directives

## Summary
GraphQL directives are annotations that alter how a query executes. The built-in `@include(if:)` and `@skip(if:)` conditionally include or exclude fields based on variables, and servers can define custom directives (`@auth`, `@cache`, `@deprecated`) to extend behavior declaratively at the schema or query level.

## Details
- Mechanism: `@include(if: $showEmail)` executes the annotated field only when the variable is true; `@skip(if: $hideSection)` is its inverse. The condition is evaluated at runtime from variables, so one query document can serve several UI states without string interpolation. Custom directives are declared in the schema (`directive @auth(role: String) on FIELD_DEFINITION`) and implemented by the server: a schema directive runs at definition time (permission gates, default values), while a query-time directive runs per field selection (logging, field-level caching, cost hints).
- Concrete examples: a profile query fetches `email` only when `$includeEmail` is true; a dashboard includes the expensive `analytics` field only when the tab is visible; a schema uses `@deprecated(reason: "...")` to mark legacy fields so tools flag them in dev; an enterprise API uses `@auth(role: "admin")` on field definitions so authorization is enforced uniformly across all clients instead of scattered in resolvers.
- Failure modes: the classic failure is over-using custom directives to hide business logic: resolver behavior that jumps through `@something` indirection is hard to trace, test, and debug, especially when directives compose (order matters). Directive misuse also breaks tools: clients that do not know a custom directive may reject the whole query, and schema-driven codegen can drop fields hidden behind directives. `@include`/`@skip` interplay with caching is subtle — the same document with different variable values produces different effective queries, so caches keyed by document hash can serve the wrong slice if variables are ignored.
- Operational tradeoffs: built-in directives are free and safe; custom directives are a contract extension that must be documented, versioned, and supported by all tooling — every directive is API surface. The payoff is declarative, cross-cutting behavior (auth, caching, redaction) enforced at the schema boundary rather than repeated in resolvers. Cost analysis must treat conditional fields conservatively: a field that may execute under `@include` counts against the budget as if it executes.
- RSIS3/mykb relevance: declarative policy via directives mirrors RSIS3's approach of encoding rules in configuration rather than scattering checks through loop code; the discipline is to keep custom directives few, documented, and testable so the graph API's behavior stays auditable.

## Related
- [[wiki/api-protocols/graphql-basics|GraphQL Basics]] — related coverage in the same cluster
- [[wiki/frontend-frameworks/graphql-batching|GraphQL Batching]] — related coverage in the same cluster
- [[wiki/frontend-frameworks/graphql-caching|GraphQL Caching]] — related coverage in the same cluster
- [[wiki/frontend-frameworks/persisted-queries|Persisted GraphQL Queries]] — related coverage in the same cluster
- [[wiki/api-protocols/graphql|GraphQL]] — related coverage in the same cluster
- [[wiki/api-protocols/graphql-schema-design|GraphQL Schema Design]] — related coverage in the same cluster
- [[wiki/api-protocols/graphql-security|GraphQL Security]] — related coverage in the same cluster
