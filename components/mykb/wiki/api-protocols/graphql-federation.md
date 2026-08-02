---
type: "concept"
title: "GraphQL Federation"
description: "Composing a distributed schema across services"
tags: ["graphql", "federation", "microservices", "schema-composition", "distributed-systems"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://www.apollographql.com/docs/federation/", "https://www.apollographql.com/blog/graphql/federation/explaining-federation/"]
---

# GraphQL Federation

## Summary
GraphQL federation composes one supergraph from many subgraphs: each service owns part of the schema and declares how its types extend others. A router/gateway stitches the pieces, so clients query a single endpoint while teams keep independent GraphQL services.

## Details
- Core concepts: subgraphs (per-service schemas), the supergraph (composed schema), entities (types shared across subgraphs), and the router that executes cross-subgraph queries.
- Entities are identified by @key (for example type Product @key(fields: "id")), and subgraphs contribute fields via @extends or @external references.
- Composition: Apollo Rover or the composition engine validates that subgraphs agree on shared types, reference resolvers, and value types.
- Query planning: the router plans execution, fans out to multiple subgraphs, and joins results — N subgraph calls per client query, so latency adds up.
- Versioning: v1 @key, v2 with @shareable and @interfaceObject, and v3 (Apollo Federation 2.x) with @link — newer versions simplify ownership rules.
- Alternatives: Schema Stitching (manual merging at runtime) and subgraph-per-team without federation (clients call each service).
- Watch-outs: shared fields need @shareable, entity keys must be resolvable by reference, and every subgraph hop adds a network round trip.

## Related
- [[wiki/api-protocols/graphql-schema-design|GraphQL Schema Design]] — subgraphs are designed like independent schemas
- [[wiki/api-protocols/graphql-resolvers|GraphQL Resolvers]] — each subgraph resolves its own fields
- [[wiki/software-engineering/microservices-architecture|Microservices Architecture]] — federation is a GraphQL microservices pattern
- [[wiki/api-protocols/service-mesh|Service Mesh]] — service-to-service transport for subgraph calls
- [[wiki/api-protocols/api-gateway|API Gateway]] — the router is a GraphQL-specific gateway
