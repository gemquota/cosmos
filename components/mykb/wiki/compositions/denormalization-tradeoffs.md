---
type: "concept"
title: "Denormalization Tradeoffs"
description: "The costs and benefits of duplicating data for read performance"
tags: ["denormalization", "tradeoffs", "databases", "design"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Denormalization Tradeoffs

## Summary
Denormalization trades write complexity and storage for faster, simpler reads. The tradeoffs are concrete: sync machinery, drift risk, and backfill jobs buy you joins avoided at read time.

## Details
- Win: hot reads skip joins and scans; read models match query shapes exactly.
- Cost: every denormalized copy needs maintenance — triggers, events, or jobs.
- Drift is the real tax: two copies of a fact disagree until the sync runs.
- mykb relevance: wiki backlink lists are denormalized and event-synced from the graph.

## Related
- [[wiki/software-engineering/denormalization-practice|Denormalization Practice]]
- [[wiki/compositions/schema-normalization|Schema Normalization]]
- [[wiki/software-engineering/read-models|Read Models]]
- [[wiki/software-engineering/projections|Projections]]
- [[wiki/compositions/database-migrations|Database Migrations]]
