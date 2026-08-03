---
type: "concept"
title: "Scaling Laws"
description: "Empirical power laws relating model performance to parameters, data, and compute"
tags: ["scaling-laws", "llm", "training", "research"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
---

# Scaling Laws

## Summary
Scaling laws quantify how loss falls as models get bigger, trained on more data, with more compute. They turned model building into a predictable engineering discipline and drove the 'bigger is better' era.

## Details
- **Kaplan et al. (2020)** — found smooth power-law improvements with parameters, data, and compute, and famously recommended scaling model size faster than data; this shaped the first generation of frontier training runs.
- **Chinchilla (2022)** — revised the guidance: for a fixed compute budget, parameters and training tokens should scale roughly equally, meaning most 2020-era models were undertrained on data; the follow-up runs that trained smaller models on far more tokens matched or beat much larger ones.
- **The three budgets** — loss improves predictably in each of parameters, data, and compute; because the exponents differ, there is an optimal allocation for any fixed budget, and frontier training budgets are now planned explicitly against these curves before a single GPU hour is spent.
- **Limits and caveats** — power laws flatten as capabilities saturate in a given regime; they predict loss, not task performance, so downstream evals are still needed; architectural changes and data quality shifts bend the curves; and the laws are measured on controlled runs, not on the messy data mixes of real deployments.
- **Operational tradeoffs** — scaling up raises inference latency, serving cost, and infrastructure complexity; a smaller, well-tuned model trained on domain data often wins on cost-per-quality for a specific task, which is why scaling-law planning must be paired with model-selection strategies rather than applied blindly.
- **RSIS3 relevance** — capability expectations (and costs) for any chosen model size are forecast from scaling laws: mykb can use them to sanity-check whether a proposed model upgrade for RSIS3 loops is worth the added token cost, or whether data-side improvements to the wiki would buy more capability per dollar.

## Related
- [[wiki/ai-ml/chinchilla-law|Chinchilla Law]] — The compute-optimal refinement of scaling laws
- [[wiki/prompt-engineering/emergent-abilities|Emergent Abilities]] — Capability jumps attributed to scale
- [[wiki/ai-ml/gpt-4|GPT-4]] — A product of scaling-law planning
- [[wiki/prompt-engineering/context-windows|Context Windows]] — A capacity that scales with model size
- [[wiki/testing/llm-evaluation|LLM Evaluation]] — Scaling predictions are verified by evals
