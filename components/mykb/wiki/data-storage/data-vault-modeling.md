---
type: "concept"
title: "Data Vault Modeling"
description: "Audit-friendly modeling that separates hubs, links, and satellites"
tags: ["data-vault", "modeling", "history", "audit"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/Data_vault_modeling", "https://en.wikipedia.org/wiki/Data_warehouse"]
---

# Data Vault Modeling

## Summary

Data Vault models raw business facts in three constructs: hubs (business keys), links (relationships), and satellites (descriptive attributes).
It preserves full history and is highly resilient to source changes, which suits integration-heavy warehouses.
The cost is complexity: more tables, more joins, and heavier load logic.
Vault loads are insert-only, which makes them ideal for audited environments and replayable integrations.

## Details

- Hubs store unique business keys with surrogate IDs and load metadata.
- Links model relationships between hubs; satellites carry attribute history over time.
- Loading is insert-only, making the vault auditable and replayable.
- Presentation layers (marts) sit on top for consumption.
- Vault suits regulated, heterogeneous source environments.
- Satellites track attribute history with load and effect timestamps.
- Marts on top of the vault keep consumers on simple star shapes.
- Vault modeling shines in many-source integration hubs, but the added join complexity must be justified by audit and history needs.

## Related

- [[wiki/data-storage/kimball-vs-inmon|Kimball Vs Inmon]] — competing approaches
- [[wiki/data-storage/surrogate-and-natural-keys|Surrogate And Natural Keys]] — key handling
- [[wiki/data-storage/scd-type-2-slowly-changing-dimensions|Scd Type 2 Slowly Changing Dimensions]] — history alternative
- [[wiki/data-storage/data-modeling|Data Modeling]] — modeling
- [[wiki/data-storage/database-normalization|Database Normalization]] — normalization

