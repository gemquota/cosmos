---
type: "concept"
title: "Temperature Sampling"
description: "The decoding parameter that controls how peaked or flat the next-token probability distribution is"
tags: ["temperature", "sampling", "decoding", "llm"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
source: ["https://platform.openai.com/docs/api-reference/chat/create"]
---

# Temperature Sampling

## Summary
Temperature scales the logits before sampling: low values concentrate probability on the most likely tokens (deterministic), high values flatten the distribution (creative, varied). It is the most common decoding knob for trading reproducibility against diversity.

## Details
- At temperature 0 (or greedy decoding) the model always picks the argmax token; many APIs still leave some nondeterminism from batching.
- OpenAI's API reference documents temperature as a per-request parameter with recommended ranges and disclaims deterministic guarantees.
- Low temperature suits extraction, classification, code, and anything schema-bound; higher temperature suits brainstorming and creative writing.
- Temperature interacts with the model's calibration: over-conservative models may need a bump, overconfident ones a trim.
- Sampling family: temperature, top-p, top-k, and min-p all shape the same distribution; they compose, so tune them together.
- RSIS3 relevance: L2/L3 loops should record temperature per experiment so mykb can correlate creativity settings with eval outcomes.

## Related
- [[wiki/prompt-engineering/top-p-sampling|Top-P Sampling]] — The companion probability-mass cutoff
- [[wiki/prompt-engineering/logit-bias|Logit Bias]] — Direct logit manipulation, orthogonal to temperature
- [[wiki/prompt-engineering/token-budgets|Token Budgets]] — Decoding parameters sit beside budget planning
- [[wiki/testing/llm-evaluation|LLM Evaluation]] — Temperature variance is a confound in evals
- [[wiki/ai-ml/gpt-4|GPT-4]] — Reference model family with documented sampling defaults
- [[wiki/concepts/mykb-analysis|mykb: Personal LLM Wiki — Analysis & Enrichment Theory]] — Parameter telemetry feeds mykb enrichment
- [[wiki/ai-ml/llama|Llama]] — Open family with documented sampling behaviour
- [[wiki/syntheses/weekly-review|Weekly Review]] — Sampling experiments surface in weekly review
