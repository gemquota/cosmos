---
type: "concept"
title: "GraphQL Error Handling"
description: "Errors array, partial results, and extensions"
tags: ["graphql", "errors", "error-handling", "partial-results", "api-design"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://spec.graphql.org/October2021/#sec-Errors", "https://www.apollographql.com/docs/apollo-server/data/errors/"]
---

# GraphQL Error Handling

## Summary
GraphQL responses separate data from errors: a response has an optional data object plus an errors array, so one field can fail while others succeed. Errors carry message, path, and extensions for codes and retry hints — a fundamentally different contract from HTTP status codes.

## Details
- Response shape: { "data": {...}, "errors": [{ "message": "...", "path": ["user","email"], "extensions": {...} }] }.
- Partial results: if user resolves but user.email throws, data contains user with email null and errors names the failing path; clients must handle both.
- HTTP status: GraphQL over HTTP usually returns 200 even with errors, because the operation itself executed; 400/401/429 are reserved for transport or request-level failures.
- Extensions: standardized extensions key (code, retryable, classification) lets clients branch programmatically without parsing messages.
- Resolver errors: throw inside resolvers, but never leak internal stack traces or SQL details into messages — map them to safe public errors.
- Request-level errors (parse failure, validation failure, unknown operation) return errors with no data at all.
- Tooling: Apollo Server, GraphQL Yoga, and federation gateways standardize error codes and masking.

## Related
- [[wiki/api-protocols/problem-details|Problem Details]] — the REST-side structured error format
- [[wiki/api-protocols/error-contract-design|Error Contract Design]] — consistent codes across the API surface
- [[wiki/api-protocols/graphql-resolvers|GraphQL Resolvers]] — resolver throws become error entries
- [[wiki/api-protocols/graphql-security|GraphQL Security]] — complexity errors use the same errors array
- [[wiki/api-protocols/graphql-queries-mutations|GraphQL Queries & Mutations]] — operations return data plus errors
