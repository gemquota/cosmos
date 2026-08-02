---
type: "concept"
title: "GraphQL N+1 Problem"
description: "Query explosion and DataLoader patterns"
tags: ["graphql", "n-plus-one", "dataloader", "performance", "batching"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://www.apollographql.com/docs/apollo-server/data/fetching-best-practices/#dataloader", "https://github.com/graphql/dataloader"]
---

# GraphQL N+1 Problem

## Summary
The N+1 problem occurs when resolving a list executes one query for the list and one query per item: fetching 100 posts then their authors issues 101 database calls. GraphQL's per-field resolver model makes this easy to trigger, and the DataLoader pattern is the standard cure.

## Details
- Mechanism: resolving posts executes SELECT ... FROM posts, then each author field resolver runs SELECT ... FROM users WHERE id = ?, once per post.
- Why GraphQL makes it worse: clients control nesting, so an innocent-looking query can fan out across relations and repeated list fields.
- DataLoader: per-request, per-key batching — resolvers request keys, DataLoader coalesces them into one batch query, and a per-request cache prevents duplicate loads.
- Batching across requests must never happen: a new DataLoader instance per request (or per context) keeps caches request-scoped and avoids stale or cross-user data.
- Beyond DataLoader: JOIN-based parent queries, SQL prefetching of related rows, and graph-aware data sources (Hasura-style engines) remove N+1 at the source.
- Detection: log resolver timings and per-field query counts; tools like Apollo tracing and OpenTelemetry spans reveal hot paths.
- Fix the symptom and the shape: batch queries first, then consider denormalizing hot edges or moving the relation into the parent fetch.

## Related
- [[wiki/api-protocols/graphql-resolvers|GraphQL Resolvers]] — the execution model that creates N+1
- [[wiki/api-protocols/graphql-schema-design|GraphQL Schema Design]] — deep schema graphs amplify fan-out
- [[wiki/devops-infra/database-indexing|Database Indexing]] — indexed lookups make batch fetches fast
- [[wiki/devops-infra/connection-pooling|Connection Pooling]] — batched loads avoid pool exhaustion
- [[wiki/api-protocols/backpressure|Backpressure]] — limiting nested work protects downstream systems
