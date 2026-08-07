---
type: "concept"
title: "Best-of-N Sampling"
description: "Generating several candidate outputs and selecting the best by a reward model or judge"
tags: ["sampling", "reward", "alignment"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Best-of-N Sampling

## Summary
Best-of-N sampling generates several candidate outputs from a model and keeps the one ranked best by a reward model, LLM judge, or task metric. It is the simplest compute-scaling method for improving output quality, at the price of multiplying inference cost by N.

## Details
- **How it works** — sample N completions independently (temperature above 0), score each, and return the argmax; quality gains come from the right tail of the sample distribution.
- **Selectors** — a learned reward model, an LLM-as-a-judge with a rubric, or a direct task metric (exact match, unit tests, ground-truth similarity) can play the scorer role.
- **N and returns** — quality rises sublinearly with N; the practical sweet spot depends on task difficulty and selector reliability, and diminishing returns set in quickly.
- **Relationship to rejection sampling** — rejection sampling filters candidates against a threshold; best-of-N is the variant that always returns the single best-ranked candidate.
- **Uses** — RLHF preference-data collection, code and math tasks with verifiable rewards, and any pipeline where a cheap judge can rank candidates better than chance.
- **Failure modes** — a biased or noisy selector amplifies its preferences across N candidates; judges can also be gamed, so candidate diversity and selector calibration matter.
- **Cost control** — N can be tuned per difficulty tier or query type rather than fixed globally, since hard tasks benefit more from extra candidates.

- **Naming in RLHF practice** — the same idea appears as rejection sampling in RLHF pipelines where a threshold filters candidates, and as best-of-N when exactly the top-ranked candidate is kept; preference datasets produced this way feed direct-preference-optimization training.
- **Candidate diversity** — samples drawn at the same temperature cluster together; lowering temperature or varying prompts widens coverage, and selector quality matters more than raw sample count once the top candidates are similar.
## Related
- [[wiki/ai-ml/rejection-sampling|Rejection Sampling]] — threshold-filtering variant
- [[wiki/ai-ml/reward-model-training|Reward Model Training]] — training the selector
- [[wiki/ai-ml/llm-as-judge|LLM-as-a-Judge]] — judge-based selection
- [[wiki/prompt-engineering/sampling-vs-greedy|Sampling vs Greedy Decoding]] — sampling family
- [[wiki/ai-ml/preference-datasets|Preference Datasets]] — what the pipeline produces
- [[wiki/prompt-engineering/temperature-sampling|Temperature Sampling]] — controlling candidate diversity
