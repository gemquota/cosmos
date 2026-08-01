---
type: "concept"
title: "CQRS"
description: "Command Query Responsibility Segregation: separate write and read models for scalability and clarity"
tags: ["cqrs", "architecture", "event-sourcing", "scalability", "data"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# CQRS

## Summary
CQRS separates commands (state-changing writes) from queries (reads), often with different models, stores, and scaling characteristics for each side.

## Details
- Benefits: read models can be denormalized for queries; write side stays strict; each side scales independently.
- Costs: eventual consistency between write and read models; more moving parts.
- Commonly paired with event sourcing — events flow from write side to read projections.

## Related
- [[wiki/api-protocols/event-sourcing|Event Sourcing]] — canonical companion pattern
- [[wiki/devops-infra/replication|Replication]] — read replicas serve queries
- [[wiki/devops-infra/query-planning|Query Planning]] — read-model optimization
- [[wiki/api-protocols/graphql|GraphQL]] — client-driven read shaping
- [[wiki/concepts/mykb-analysis|Mykb Analysis]] — search index as read model
