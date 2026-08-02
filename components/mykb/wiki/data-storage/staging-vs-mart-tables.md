---
type: "concept"
title: "Staging vs Mart Tables"
description: "Transient load area versus consumer-facing models"
tags: ["staging", "marts", "warehouse", "modeling"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Staging vs Mart Tables

## Summary

A stub to be expanded into a full article; frames the concept and open questions.

## Details

- Staging tables mirror sources for transformation; they are transient and disposable.
- Marts are curated, modeled tables optimized for consumption.
- Keep staging thin; push business logic into marts or dbt models.
- Naming and ownership should make the distinction obvious.

## Related

- [[wiki/data-storage/data-warehouse|Data Warehouse]] — warehouse
- [[wiki/data-storage/dimensional-modeling|Dimensional Modeling]] — mart design
- [[wiki/data-storage/data-modeling-star-schema|Data Modeling Star Schema]] — star schemas
- [[wiki/data-storage/semantic-layers-and-metrics|Semantic Layers And Metrics]] — consumption layer
- [[wiki/data-storage/data-engineering-fundamentals|Data Engineering Fundamentals]] — core data engineering concepts
