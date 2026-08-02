---
type: "concept"
title: "Fact Tables and Measures"
description: "The numeric core of a star schema recording what happened at a grain"
tags: ["facts", "measures", "star-schema", "dimensional-modeling"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Fact Tables and Measures

## Summary

A stub to be expanded into a full article; frames the concept and open questions.

## Details

- Fact tables store measures (additive, semi-additive, non-additive) plus foreign keys to dimensions at a declared grain.
- Additive measures like revenue sum across any dimension; semi-additive ones like balances sum across some; ratios are non-additive.
- Fact grain determines what each row means: one row per transaction, per line item, per event, or per snapshot period.
- Factless facts record events or coverage with no measures at all.

## Related

- [[wiki/data-storage/dimensional-modeling|Dimensional Modeling]] — fact/dimension design as a whole
- [[wiki/data-storage/dimension-tables-and-grains|Dimension Tables And Grains]] — the grain story from the dimension side
- [[wiki/data-storage/factless-fact-tables|Factless Fact Tables]] — facts that carry no measures
- [[wiki/data-storage/grain-and-additivity|Grain And Additivity]] — grain and additivity rules
- [[wiki/data-storage/transactional-facts|Transactional Facts]] — transaction-grained facts
