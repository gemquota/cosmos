---
type: "concept"
title: "Survivorship Bias"
description: "Drawing conclusions only from those who made it through selection"
tags: ["bias", "sampling", "inference"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Survivorship Bias

## Summary

Survivorship bias is the error of drawing conclusions from a set of survivors — cases that passed a selection process — while ignoring the cases that did not. It matters because the invisible non-survivors often carry the most information, and ignoring them flatters the survivors' apparent qualities. Classic examples range from WWII planes to startup advice.

## Details

- **Definition** — When analysis conditions on survival, the sample is systematically selected, and inferred causes of survival are confounded by the selection process.
- **Classic example** — Armoring the parts of returning aircraft where they were most damaged ignored the planes that did not return, where the fatal damage was.
- **Mechanism** — Survival correlates with unobserved variables — skill, luck, resources — so survivor-only data misattribute outcomes to visible traits.
- **Worked example** — Advice from successful founders ignores the many failures with the same habits; without the denominator, the causal claim is untestable.
- **Detection** — Asking what the missing cases looked like, and reconstructing the full population, reveals the direction of the bias.
- **Common failure modes** — Generalizing from success stories, backtesting on companies that survived, and evaluating strategies only on completed projects.
- **Practical relevance** — Evaluation pipelines, model training sets, and historical analyses all inherit the bias when dropped-out cases vanish from the record.
- **Variants** — Attrition bias and censoring are the statistical relatives, handled with survival analysis and weighting.
- **Remedy** — Collecting and modeling the full cohort — including failures — is the only complete correction.
- **Business and investing** — Index survivorship — funds that close vanish from databases — inflates historical performance; survivor-adjusted data corrects it.
- **Engineering** — Reliability analysis using only deployed components misses the failures that never shipped, distorting failure-rate estimates.
- **Worked example** — A study of successful products lists shared traits, but comparing against failed products with the same traits shows the traits predict little.
- **Communication** — Reporting the denominator and the excluded cases makes any survivor-based claim honest and testable.

## Related

- [[wiki/concepts/selection-bias|Selection Bias]] — the general family
- [[wiki/concepts/publication-bias|Publication Bias]] — surviving the review process
- [[wiki/memory/availability-heuristic|Availability Heuristic]] — vivid survivors dominate memory
- [[wiki/memory/representativeness-heuristic|Representativeness Heuristic]] — stereotype-based inference
- [[wiki/concepts/statistical-reasoning|Statistical Reasoning]] — reading the denominator
- [[wiki/concepts/systematic-review|Systematic Review]] — including the missing studies
