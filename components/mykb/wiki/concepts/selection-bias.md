---
type: "concept"
title: "Selection Bias"
description: "Systematic distortion from non-representative sampling"
tags: ["bias", "sampling", "inference"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Selection Bias

## Summary

Selection bias is the systematic distortion that occurs when the data or participants included in a study are not representative of the population the conclusions claim to cover. It matters because no amount of analysis can repair a biased sample — the error enters at selection time. Recognizing selection mechanisms is the first step to avoiding or correcting them.

## Details

- **Definition** — Selection bias arises when inclusion in the sample depends on the variables under study, so observed associations differ from population truth.
- **Common forms** — Survivorship, volunteer, self-selection, and convenience sampling each skew results in recognizable ways.
- **Mechanism** — If selection correlates with the outcome or exposure, the sample is no longer exchangeable with the target population.
- **Worked example** — Surveying only active users overstates satisfaction because dissatisfied users churn before the survey runs — a self-selection mechanism.
- **Detection** — Comparing sample characteristics to known population values, and modeling who is missing, reveal the direction and size of bias.
- **Common failure modes** — Generalizing beyond the sampled population, ignoring non-response, and using biased samples as if they were random.
- **Practical relevance** — Evaluation sets, user studies, and model training data all suffer selection bias, making it a data-engineering concern, not just a statistics one.
- **Variants** — Berkson's bias, collider bias, and sampling on the outcome are specialized cases with distinct corrective strategies.
- **Remedies** — Random sampling, weighting, and explicit scope statements limit or disclose the bias; honesty about limits often matters most.
- **Generalization** — Results generalize only to the population the sampling design actually represents; overclaiming breadth is the most common error.
- **Observational data** — Administrative and observational datasets always have selection mechanisms; analysts should name them even when correction is impossible.
- **Worked example** — A model trained on logged user behavior overrepresents power users; deployment to new users underperforms until the sampling gap is acknowledged.
- **Reporting** — Describing inclusion criteria, non-response, and exclusions in methods sections lets readers judge how far results travel.

## Related

- [[wiki/concepts/survivorship-bias|Survivorship Bias]] — a famous subtype
- [[wiki/concepts/replication-crisis|Replication Crisis]] — biased evidence at scale
- [[wiki/concepts/open-science-practices|Open Science Practices]] — countermeasures
- [[wiki/concepts/statistical-reasoning|Statistical Reasoning]] — interpreting samples
- [[wiki/concepts/systematic-review|Systematic Review]] — combating selection in reviews
- [[wiki/concepts/debiasing-techniques|Debiasing Techniques]] — correction strategies
