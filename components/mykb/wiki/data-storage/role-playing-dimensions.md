---
type: "concept"
title: "Role-Playing Dimensions"
description: "One dimension table used in multiple roles"
tags: ["role-playing-dimensions", "modeling", "star-schema"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Role-Playing Dimensions

## Summary

A stub to be expanded into a full article; frames the concept and open questions.

## Details

- A date dimension joins as order_date, ship_date, or due_date — each a role.
- Role-playing avoids duplicating the dimension table.
- Aliases in queries keep roles readable.
- Grain and keys stay identical across roles.

## Related

- [[wiki/data-storage/dimensional-modeling|Dimensional Modeling]] — modeling
- [[wiki/data-storage/dimension-tables-and-grains|Dimension Tables And Grains]] — dimensions
- [[wiki/data-storage/conformed-dimensions|Conformed Dimensions]] — conformance
- [[wiki/data-storage/fact-tables-and-measures|Fact Tables And Measures]] — facts
- [[wiki/data-storage/data-engineering-fundamentals|Data Engineering Fundamentals]] — core data engineering concepts
