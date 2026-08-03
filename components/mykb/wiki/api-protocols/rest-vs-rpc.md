---
type: "concept"
title: "REST vs RPC"
description: "Resource-oriented HTTP APIs versus action-oriented remote procedure calls"
tags: ["api", "rest", "rpc", "architecture"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# REST vs RPC

## Summary
REST and RPC disagree about what an API should model: REST organizes the world into resources addressed by URLs and acted on by a fixed verb set, while RPC organizes the world into named operations that read like function calls. The styles are not mutually exclusive, and most production APIs end up as a pragmatic blend.

## Details
- Mechanism: a REST interface exposes nouns (a user, an order, a document) and lets clients read or mutate them with GET, POST, PUT, PATCH, DELETE; state transitions happen by replacing or patching resource representations. An RPC interface exposes verbs (`createUser`, `chargeCard`, `startJob`) that map one-to-one onto implementation functions, with arguments and return values carried in a request/response envelope. The difference shows up in URLs: `/orders/42` versus `/orders/42/charge`.
- Concrete examples: CRUD-heavy domains like account management fit REST well because the operations are exactly create/read/update/delete. Domains with irregular actions fit RPC better: sending an email, rebalancing a portfolio, or invoking a payment capture have no natural resource representation, and forcing them into REST produces endpoints like `POST /emails/send` or `POST /payments/123/capture` that are RPC calls wearing a resource costume. Command-based systems (CQRS) and most internal service boundaries use RPC-style operations for the same reason.
- Tradeoffs: REST wins on uniformity, cacheability, discoverability, and long-term evolvability because the verb set is fixed and stable; RPC wins on ergonomics and expressiveness for domain-specific actions, at the cost of inventing new verbs forever, making each endpoint bespoke and harder to generalize. RPC also tends to hide state behind opaque calls, which complicates idempotency and caching; REST makes state explicit, which helps those concerns.
- Failure modes: pure REST purism produces absurd endpoints and forces clients to issue multiple round trips to express one intent, while pure RPC produces a sprawling, undiscoverable surface where every endpoint needs bespoke docs, validation, and retry rules. The worst hybrid is RPC semantics behind REST-looking URLs without consistent conventions, leaving clients guessing whether a POST mutates a resource or invokes a command.
- Operational guidance: choose the dominant style by domain shape, then be consistent: keep the resource layer for data entities and add an explicit command layer (suffix or prefix) for actions, document which verbs are idempotent, and version both layers. Use OpenAPI to describe either style so tooling and mocks stay uniform.
- RSIS3/mykb relevance: MyKB and RSIS3 expose both shapes naturally: articles and registry entries are resources read through GET-style lookups, while loop actions (optimize, evolve, checkpoint) are commands; modeling them as a command layer over a resource store keeps the memory layer uniform and the action layer explicit.

## Related
- [[wiki/api-protocols/rest-api-design|REST API Design]]
- [[wiki/api-protocols/rest-vs-graphql|REST vs GraphQL]]
- [[wiki/api-protocols/rest-vs-grpc|REST vs gRPC]]
- [[wiki/api-protocols/rest-apis|REST APIs]]
- [[wiki/api-protocols/rpc-styles|RPC Styles]]
- [[wiki/api-protocols/graphql|GraphQL]]
