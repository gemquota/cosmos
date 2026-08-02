---
type: "concept"
title: "GraphQL Schema Design"
description: "SDL types, fields, and naming conventions"
tags: ["graphql", "schema", "sdl", "api-design", "type-system"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://spec.graphql.org/October2021/#sec-Type-System", "https://graphql.org/learn/schema/"]
---

# GraphQL Schema Design

## Summary
The GraphQL schema is the contract: an SDL (Schema Definition Language) description of types, fields, arguments, and relationships that clients can introspect. Schema design determines developer experience, query power, and evolution safety — field naming, nullability, and type granularity are decisions made once and felt everywhere.

## Details
- SDL basics: type Query, type Mutation, and optional type Subscription are the root types; object types, scalars, enums, interfaces, unions, and input types fill out the graph.
- Naming: PascalCase for type names, camelCase for fields, plural names for lists; the schema uses a single namespace, so collisions force deliberate prefixes.
- Nullability is a contract: non-null (String!) fields promise values but break whole queries when violated, so reserve ! for fields that genuinely cannot fail.
- Arguments: each field can take inputs, enabling filtering, sorting, and pagination; input types must be defined for complex argument objects.
- Interfaces and unions model polymorphic data; interfaces let fragments share fields, unions allow heterogeneous lists.
- Deprecation: mark evolving fields with @deprecated(reason:) instead of deleting them, keeping backward compatibility while steering clients to replacements.
- Design for queries clients actually write: deep nesting (user -> posts -> comments) is natural in GraphQL, so model relationships as graph edges, not flat tables.

## Related
- [[wiki/api-protocols/graphql|GraphQL]] — schema is the heart of the GraphQL runtime
- [[wiki/api-protocols/graphql-queries-mutations|GraphQL Queries & Mutations]] — root types define the operation surface
- [[wiki/api-protocols/json-schema|JSON Schema]] — the JSON-side validation counterpart
- [[wiki/api-protocols/graphql-fragments|GraphQL Fragments]] — fragments rely on shared type shapes
- [[wiki/api-protocols/graphql-connections|GraphQL Connections]] — connection types are schema-level pagination patterns
