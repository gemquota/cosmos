---
type: "concept"
title: "Data Modeling Methodology"
description: "Choosing the modeling approach that fits your organization"
tags: ["methodology", "modeling", "kimball", "vault"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/Dimensional_modeling", "https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/kimball-techniques/dimensional-modeling-techniques/"]
---

# Data Modeling Methodology

## Summary

Modeling methodology is the set of conventions for how source data becomes analytical models.
Kimball, Inmon, and Data Vault represent different tradeoffs of speed, rigor, and history.
A pragmatic methodology documents naming, ownership, and promotion rules on top of the chosen style.
A methodology is only as good as its enforcement; document, automate, and review the conventions.

## Details

- Start from business questions, not source schemas: grain and metrics first.
- Conformed dimensions and consistent naming prevent mart drift.
- Model review, versioning, and testing are part of the methodology.
- Modern stacks embed methodology in tools: dbt conventions, catalog ownership, CI checks.
- Document decisions in design docs and RFCs so the approach survives team churn.
- Conventions cover naming, grain, key strategy, and change process.
- Model reviews catch drift early; schedule them with feature work.
- Methodology is most valuable at the edges: naming collisions, ambiguous grain, and ownership gaps are where modeling discipline pays off.

## Related

- [[wiki/data-storage/kimball-vs-inmon|Kimball vs Inmon]] — approaches
- [[wiki/infrastructure/data-design-docs|Data Design Docs]] — documenting choices
- [[wiki/infrastructure/data-rfc-process|Data Rfc Process]] — decision process
- [[wiki/data-storage/data-modeling|Data Modeling]] — modeling
- [[wiki/data-storage/data-contracts-and-agreements|Data Contracts and Agreements]] — conventions
- [[wiki/data-storage/data-warehouse|Data Warehouse]] — warehouse reference

