---
type: "concept"
title: "GraphQL Batching"
description: "Coalescing multiple operations into one HTTP request"
tags: ["graphql", "batching", "performance", "api"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# GraphQL Batching

## Summary
GraphQL batching is the practice of sending multiple operations in fewer HTTP requests: either multiple queries in one request body (query batching) or several requests multiplexed over one connection (transport batching). It reduces round-trip latency and connection churn, and it became a hot topic again as HTTP/2 multiplexing changed the cost calculus.

## Details
- Mechanism: query batching sends an array of operations in one POST — `[{ query: "...", variables: {...} }, ...]` — and the server returns an array of responses, letting a client that needs ten small queries collapse them into one round trip. Transport batching, the older Apollo-style approach, opens a single TCP connection and pipelines multiple GraphQL requests over it, reusing TLS and connection state. The two are complementary: query batching cuts round trips, transport batching cuts connection setup, and HTTP/2 (which multiplexes many streams over one connection) makes transport-level batching largely unnecessary while making per-request stream costs the new metric.
- Concrete examples: a mobile home screen that needs profile, feed, and notification counts can send one batched request instead of three sequential fetches; a server-rendered page that queries several sections can batch them into one request to the GraphQL gateway; libraries like `graphql-request` and Apollo support batching options, and gateways like Apollo Server and Mercurius handle batched bodies natively.
- Failure modes: batching changes error semantics — one failing operation in a batch can fail the whole request or return partial results depending on the server, so clients must handle both; batch size limits are essential because an unbounded batch is a request-amplification vector (one request runs hundreds of operations, bypassing per-request rate limits); and batching + HTTP caching interact poorly, since a batch endpoint is almost never cacheable. Latency also changes character: the server processes a batch serially or in parallel depending on implementation, so one slow resolver can delay the whole batch.
- Operational tradeoffs: query batching is most valuable on high-latency mobile networks and for server-side composition; on desktop with HTTP/2, the win shrinks to header and request overhead. The security tradeoff is real: cost controls must be enforced per operation inside the batch, not per request, or batching becomes a DDoS amplifier. Some teams disable client-side batching entirely and rely on HTTP/2 multiplexing plus persisted queries, which gives most of the latency win without the semantic complications.
- RSIS3/mykb relevance: the daemon could batch MyKB lookups (article, graph node, related links) for the dashboard; the lesson is to enforce per-operation budgets inside the batch and treat each operation as an independently costed unit, the same way RSIS3 accounts for each loop's work even when runs are coalesced.

## Related
- [[wiki/api-protocols/graphql-basics|GraphQL Basics]]
- [[wiki/frontend-frameworks/graphql-caching|GraphQL Caching]]
- [[wiki/frontend-frameworks/persisted-queries|Persisted GraphQL Queries]]
- [[wiki/frontend-frameworks/query-depth-limit|Query Depth Limits]]
- [[wiki/api-protocols/graphql|GraphQL]]
- [[wiki/api-protocols/graphql-schema-design|GraphQL Schema Design]]
- [[wiki/api-protocols/graphql-security|GraphQL Security]]
