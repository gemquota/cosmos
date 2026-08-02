---
type: "concept"
title: "GraphQL Fragments"
description: "Reusable field selections and inline fragments"
tags: ["graphql", "fragments", "queries", "reusability", "type-system"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://graphql.org/learn/queries/#fragments", "https://www.apollographql.com/docs/react/data/fragments/"]
---

# GraphQL Fragments

## Summary
Fragments are named, reusable selection sets that keep GraphQL operations DRY. A fragment attaches to a specific type and can be spread into any selection of that type, while inline fragments switch on runtime type for interfaces and unions.

## Details
- Named fragment: fragment UserFields on User { id name } then ...UserFields spreads it; fragments compose and nest.
- Type safety: a fragment can only be spread on selections whose type matches, so interfaces and unions require inline fragments to access concrete fields.
- Inline fragments: ... on Admin { permissions } inside a User selection branches on the runtime type returned.
- Client caching: Apollo and Relay key cached entities by __typename + id, so fragments that include both enable cache normalization and updates after mutations.
- Colocation: co-locating fragments on the components that render them keeps UI data requirements explicit and avoids over-fetching.
- Performance: fragments do not change server cost by themselves — the full selection set is what resolves — but they dramatically improve maintainability.

## Related
- [[wiki/api-protocols/graphql-schema-design|GraphQL Schema Design]] — fragments depend on stable type shapes
- [[wiki/api-protocols/graphql-queries-mutations|GraphQL Queries & Mutations]] — operations spread fragments
- [[wiki/api-protocols/json-api-spec|JSON:API]] — sparse fieldsets are JSON:API's selection analog
- [[wiki/api-protocols/graphql-resolvers|GraphQL Resolvers]] — fragment fields still resolve per field
- [[wiki/api-protocols/graphql-connections|GraphQL Connections]] — edge fragments select node fields
