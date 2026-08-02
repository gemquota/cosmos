---
type: "concept"
title: "Degenerate Dimensions"
description: "Fact attributes with no separate dimension table"
tags: ["degenerate-dimensions", "facts", "modeling", "star-schema"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Degenerate Dimensions

## Summary

A stub to be expanded into a full article; frames the concept and open questions.

## Details

- Degenerate dimensions are identifiers on the fact (order number, ticket ID) with no attributes.
- Keeping them on the fact preserves grain and filtering without extra joins.
- They are common in transactional fact tables.
- Promote to a real dimension only when attributes accumulate.

## Related

- [[wiki/data-storage/dimensional-modeling|Dimensional Modeling]] — modeling
- [[wiki/data-storage/fact-tables-and-measures|Fact Tables And Measures]] — facts
- [[wiki/data-storage/transactional-facts|Transactional Facts]] — transaction facts
- [[wiki/data-storage/grain-and-additivity|Grain And Additivity]] — grain
- [[wiki/data-storage/data-engineering-fundamentals|Data Engineering Fundamentals]] — core data engineering concepts
