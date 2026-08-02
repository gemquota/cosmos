---
type: "concept"
title: "CQRS"
description: "Command Query Responsibility Segregation: separate write and read models for scalability and clarity"
tags: ["cqrs", "architecture", "event-sourcing", "scalability", "data"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://martinfowler.com/bliki/CQRS.html", "https://microservices.io/patterns/data/cqrs.html"]
---

# CQRS

## Summary
CQRS separates commands (state-changing writes) from queries (reads), often with different models, stores, and scaling characteristics for each side.

## Details
- Benefits: read models can be denormalized for queries; write side stays strict; each side scales independently.
- Costs: eventual consistency between write and read models; more moving parts.
- Commonly paired with event sourcing — events flow from write side to read projections.
- Command Query Responsibility Segregation splits a system into a command side that changes state and a query side that reads it, each optimized separately.
- Commands and queries often use different models: writes append events or mutate an authoritative store, while reads serve precomputed projections.
- The benefit is independent scaling and modeling — heavy read traffic does not compete with writes, and each side uses the shape that fits.
- The cost is eventual consistency between write and read sides, plus the operational burden of keeping projections current.
- **Worked example / comparison** — Worked example — a knowledge graph writes events to a log (command side) and maintains search indexes and link maps as projections (query side).
- For mykb, CQRS describes the split between the wiki's markdown source of truth and its derived graph, indexes, and dashboards.

## Related
- [[wiki/api-protocols/event-sourcing|Event Sourcing]]
- [[wiki/devops-infra/replication|Replication]]
- [[wiki/devops-infra/query-planning|Query Planning]]
- [[wiki/api-protocols/graphql|GraphQL]]
- [[wiki/concepts/mykb-analysis|Mykb Analysis]]
- [[wiki/concepts/promotion-readiness|Promotion Readiness]]
- [[wiki/dev-tools/global-link-check|Global Link Check]]
- [[wiki/concepts/explainers|Explainers]]
