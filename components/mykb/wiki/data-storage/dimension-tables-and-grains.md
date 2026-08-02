---
type: "concept"
title: "Dimension Tables and Grains"
description: "The descriptive context tables that give facts their business meaning"
tags: ["dimensions", "grain", "star-schema", "modeling"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Dimension Tables and Grains

## Summary

A stub to be expanded into a full article; frames the concept and open questions.

## Details

- Dimension tables hold descriptive attributes: who, what, where, when — the context for slicing fact measures.
- The grain is the level of detail a row represents; agreeing the grain before modeling prevents double counting.
- Dimensions are often conformed (shared across marts) and slowly changing (Type 1/2) as attributes evolve.
- Degenerate, role-playing, and junk dimensions are common variants that keep the schema lean.

## Related

- [[wiki/data-storage/dimensional-modeling|Dimensional Modeling]] — core modeling reference
- [[wiki/data-storage/surrogate-keys|Surrogate vs Natural Keys]] — stable keys for dimension rows
- [[wiki/data-storage/fact-tables-and-measures|Fact Tables And Measures]] — the counterpart table type
- [[wiki/data-storage/conformed-dimensions|Conformed Dimensions]] — shared dimensions across marts
- [[wiki/data-storage/role-playing-dimensions|Role Playing Dimensions]] — dimension reuse with roles
