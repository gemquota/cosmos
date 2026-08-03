---
type: "concept"
title: "Fact Tables and Measures"
description: "The numeric core of a star schema recording what happened at a grain"
tags: ["facts", "measures", "star-schema", "dimensional-modeling"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Fact Tables and Measures

## Summary
Fact tables store the numeric core of a star schema: measures (additive, semi-additive, non-additive) plus foreign keys to dimensions at a declared grain. The grain determines what each row means — one row per transaction, line item, event, or snapshot period — and additive measures like revenue sum across any dimension.

## Details
- Mechanism: a fact table records what happened at a grain; measure types decide how they aggregate — additive (revenue, quantity) sums across any dimension; semi-additive (account balance) sums across some dimensions but not time; non-additive (ratios, averages) must be recomputed from components; factless facts record events or coverage with no measures.
- Concrete example: a sales fact at line-item grain has product, customer, date, store foreign keys and amount, quantity, discount measures; revenue sums across product and date; a balance fact is semi-additive — summing balances across accounts is fine, across time is not; a factless fact records which products were in stock on which days.
- Failure modes: grain ambiguity causing double counting when two teams aggregate the same table differently; storing non-additive measures as if additive (averaging averages); fact rows without a declared grain, uninterpretable later; too-fine grains exploding row counts; facts joined to dimensions on the wrong keys, multiplying rows.
- Tradeoffs: fact tables optimize query performance and comprehension at the cost of modeling discipline — the grain and additivity rules must be enforced; the alternative, raw event tables, are flexible and hard to aggregate correctly; the mature pattern is declared grains, documented additivity, and consistent conformed dimensions.
- Operational notes: document grain and additivity per fact, test that aggregations do not multiply rows, and review new measures for type.
- RSIS3 relevance: wiki analytics (article reads, curation events by status and tag) are natural facts — declaring grain and additivity prevents double-counted dashboard metrics.

## Related

- [[wiki/data-storage/dimensional-modeling|Dimensional Modeling]] — fact/dimension design as a whole
- [[wiki/data-storage/dimension-tables-and-grains|Dimension Tables And Grains]] — the grain story from the dimension side
- [[wiki/data-storage/factless-fact-tables|Factless Fact Tables]] — facts that carry no measures
- [[wiki/data-storage/grain-and-additivity|Grain And Additivity]] — grain and additivity rules
- [[wiki/data-storage/transactional-facts|Transactional Facts]] — transaction-grained facts
