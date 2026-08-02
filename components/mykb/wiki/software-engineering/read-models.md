---
type: "concept"
title: "Read Models"
description: "Dedicated data shapes optimized for how the system reads"
tags: ["read-models", "cqrs", "projections", "architecture"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Read Models

## Summary
A read model is a data shape built for a specific query pattern — a dashboard row, a search document — separate from the write model. CQRS systems keep read models in sync via events, letting each side evolve independently.

## Details
- Read models trade write-path simplicity for query performance and shape fit.
- They are projections: derived, denormalized, and rebuildable.
- Consistency is eventual; hide the lag or design around it.
- mykb relevance: the wiki search index is a read model over the article write model.

## Related
- [[wiki/software-engineering/projections|Projections]]
- [[wiki/software-engineering/command-query-separation|Command Query Separation]]
- [[wiki/software-engineering/cqrs-pattern|CQRS Pattern]]
- [[wiki/software-engineering/event-carried-state|Event-Carried State]]
- [[wiki/software-engineering/denormalization-practice|Denormalization Practice]]
