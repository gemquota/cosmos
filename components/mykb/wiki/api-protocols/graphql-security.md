---
type: "concept"
title: "GraphQL Security"
description: "Query complexity, depth limits, and introspection control"
tags: ["graphql", "security", "query-complexity", "dos", "api-security"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://www.apollographql.com/blog/graphql/security/why-you-should-be-thinking-about-graphql-security/", "https://escape.tech/blog/graphql-security/"]
---

# GraphQL Security

## Summary
GraphQL's power is also its attack surface: one client can issue arbitrarily deep or wide queries that fan out into expensive resolver work. Security controls — complexity scoring, depth limits, alias caps, and introspection policy — keep the schema open without leaving the backend open to abuse.

## Details
- Depth limits: cap nesting (for example 8 levels) so queries cannot recurse through cyclic schema relationships.
- Complexity scoring: assign cost to fields (list fields weighted higher) and reject queries above a budget with 400 and a complexity error.
- Alias abuse: a query can repeat the same field with hundreds of aliases, so limit alias count per operation.
- Introspection: disable or gate introspection (__schema, __type) in production or for unauthenticated clients; developer tools can use a separate endpoint.
- Authorization must live in resolvers or a directive layer, never rely on schema hiding — field-level access control (for example @auth directives) checks per request.
- Batching abuse: a single HTTP request can contain many operations (batching), so cap operations per request and rate-limit by authenticated user.
- Persisted queries: allowlisting known query hashes blocks arbitrary queries while keeping caching and safe defaults.

## Related
- [[wiki/api-protocols/graphql-error-handling|GraphQL Error Handling]] — security rejections use the error contract
- [[wiki/api-protocols/rate-limit-algorithms|Rate Limit Algorithms]] — per-user budgets complement query limits
- [[wiki/security-auth/ssrf-prevention|SSRF Prevention]] — resolvers that fetch URLs need outbound controls
- [[wiki/security-auth/role-based-access-control|Role-Based Access Control]] — field-level authorization patterns
- [[wiki/api-protocols/graphql-resolvers|GraphQL Resolvers]] — resolver cost drives complexity scoring
