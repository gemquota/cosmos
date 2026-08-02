---
type: "concept"
title: "Denormalization Practice"
description: "Duplicating data deliberately to make reads fast and simple"
tags: ["denormalization", "database", "read-models", "design"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Denormalization Practice

## Summary
Denormalization copies data into read-friendly shapes — precomputed counts, embedded lists, cached joins — trading write and storage cost for query speed. Done with discipline, it is how read-heavy systems scale; done casually, it rots.

## Details
- Denormalize where reads dominate and consistency can tolerate lag or repairs.
- Own the sync: triggers, jobs, or events must keep duplicates fresh, or they drift.
- Document which copy is canonical; backfills fix drift, they do not justify it.
- mykb relevance: article tag counts and backlink lists are denormalized index fields.

## Related
- [[wiki/software-engineering/read-models|Read Models]]
- [[wiki/compositions/denormalization-tradeoffs|Denormalization Tradeoffs]]
- [[wiki/software-engineering/projections|Projections]]
- [[wiki/compositions/database-migrations|Database Migrations]]
- [[wiki/compositions/data-backfills|Data Backfills]]
