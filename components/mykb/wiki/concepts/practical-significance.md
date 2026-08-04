---
type: "concept"
title: "Practical Significance"
description: "Whether an effect matters in real-world terms"
tags: ["significance", "decisions", "statistics"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Practical Significance

## Summary

Practical significance asks whether an observed effect is large enough to matter in the real world, beyond merely being statistically detectable. It matters because large samples make trivial effects statistically significant, and decisions need effect magnitude, not just p-values. Assessing practical significance requires context: costs, benefits, and the stakes of the decision.

## Details

- **Definition** — An effect is practically significant when its size has meaningful real-world consequences, judged against decision context and costs.
- **Statistical versus practical** — Statistical significance answers whether the effect is detectable; practical significance answers whether it is worth acting on.
- **Effect size** — Standardized measures like Cohen's d and raw units like dollars or days quantify magnitude in decision-relevant terms.
- **Worked example** — A two-millisecond improvement in a rarely used page load is statistically significant with enough traffic but practically irrelevant; a one-second cut on a checkout page is not.
- **Common failure modes** — Equating significance with importance, chasing tiny effects in big samples, and ignoring the costs and risks of acting on small gains.
- **Practical relevance** — Product decisions, policy, and clinical practice all hinge on translating effect sizes into consequences, which is why reporting should include magnitudes.
- **Context** — What is trivial in one setting is material in another; the same effect size can be practically significant or not depending on stakes.
- **Limits** — Practical significance is a judgment informed by evidence, not a computation; transparent reasoning about costs and benefits is part of the analysis.
- **Reporting magnitudes** — Reporting effect sizes and raw units alongside p-values keeps decision-makers focused on how much rather than merely whether.
- **Minimal detectable** — Power analysis can target the smallest effect worth acting on, aligning sample design with practical thresholds.
- **Worked example** — A tutoring program's effect of half a grade point is practically significant for a district; the same effect size is not for a program costing ten times as much.
- **Judgment** — Practical significance is a decision framed by evidence — stakeholders, costs, and consequences — not a purely statistical output.

## Related

- [[wiki/concepts/effect-size-interpretation|Effect Size Interpretation]] — the magnitude question
- [[wiki/concepts/confidence-intervals|Confidence Intervals]] — the plausible range
- [[wiki/data-storage/p-value-and-confidence-intervals|P-Values and Confidence Intervals]] — significance mechanics
- [[wiki/concepts/statistical-reasoning|Statistical Reasoning]] — the analytic frame
- [[wiki/concepts/replication-crisis|Replication Crisis]] — inflated effect sizes
- [[wiki/concepts/probabilistic-literacy|Probabilistic Literacy]] — reading the numbers
