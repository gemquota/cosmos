---
type: "concept"
title: "GraphQL Connections"
description: "Relay-style cursor connections and edges"
tags: ["graphql", "connections", "relay", "pagination", "cursor"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://relay.dev/graphql/connections.htm", "https://graphql.org/learn/pagination/"]
---

# GraphQL Connections

## Summary
Relay connections are the standardized GraphQL pagination pattern: a connection type wraps edges, each edge carries a cursor and a node, and pageInfo reports hasNextPage and cursors. The shape makes lists paginable, orderable, and incrementally updateable in normalized client caches.

## Details
- Shape: User.friends: FriendConnection with edges: [FriendEdge], pageInfo { hasNextPage hasPreviousPage startCursor endCursor }, and totalCount where useful.
- Arguments: first, last, before, after (cursors) — first and last clamp the page size; after/before seek by opaque cursor.
- Edges exist because relationship data (friendship date, role, position) belongs on the edge, not the node.
- Why connections beat plain lists: stable cursors survive inserts, metadata slots into edges, and cache normalization keys edges by cursor.
- Implementation: resolver maps cursor <-> (offset or keyset key); the spec defines cursor encoding rules but leaves encoding opaque to clients.
- Counts: totalCount needs a separate count query; clients should not assume it is cheap.
- Adoption: Relay, Apollo, and code-first tools (graphql-relay-js, Nexus, Pothos) generate connection scaffolding.

## Related
- [[wiki/api-protocols/cursor-pagination|Cursor Pagination]] — the cursor mechanics connections formalize
- [[wiki/api-protocols/keyset-pagination|Keyset Pagination]] — the seek implementation behind cursors
- [[wiki/api-protocols/graphql-schema-design|GraphQL Schema Design]] — connection types live in the schema
- [[wiki/api-protocols/graphql-fragments|GraphQL Fragments]] — edge fragments select node fields
- [[wiki/api-protocols/rest-query-parameters|REST Query Parameters]] — REST's cursor conventions mirror connections
