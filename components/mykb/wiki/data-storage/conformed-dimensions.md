---
type: "concept"
title: "Conformed Dimensions"
description: "Shared dimensions used consistently across marts"
tags: ["conformed-dimensions", "dimensional-modeling", "star-schema"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Conformed Dimensions

## Summary

A stub to be expanded into a full article; frames the concept and open questions.

## Details

- A conformed dimension has the same keys, attributes, and grain everywhere.
- It lets facts from different processes join on a common view of the business.
- Built once, owned centrally, reused across marts.
- Drift breaks cross-mart analysis, so govern changes carefully.

## Related

- [[wiki/data-storage/dimensional-modeling|Dimensional Modeling]] — dimensional modeling
- [[wiki/data-storage/dimension-tables-and-grains|Dimension Tables And Grains]] — dimensions
- [[wiki/infrastructure/data-dictionary-and-glossary|Data Dictionary And Glossary]] — shared vocabulary
- [[wiki/data-storage/role-playing-dimensions|Role Playing Dimensions]] — dimension variants
- [[wiki/data-storage/data-engineering-fundamentals|Data Engineering Fundamentals]] — core data engineering concepts
