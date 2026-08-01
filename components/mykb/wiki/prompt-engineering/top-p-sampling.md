---
type: "concept"
title: "Top-P Sampling"
description: "Nucleus sampling: restricting next-token choices to the smallest set whose cumulative probability exceeds p"
tags: ["top-p", "sampling", "decoding", "llm"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
source: ["https://platform.openai.com/docs/api-reference/chat/create"]
---

# Top-P Sampling

## Summary
Top-p (nucleus) sampling picks tokens from the smallest set whose combined probability mass reaches a threshold p, cutting off the long tail of unlikely tokens. It adapts to the distribution's shape, unlike fixed top-k, and is a standard diversity control beside temperature.

## Details
- Nucleus sampling was introduced in 'The Curious Case of Neural Text Degeneration' as a fix for repetitive, degenerate text from pure sampling.
- p near 1 keeps the tail (more varied), p near 0.5 or lower becomes near-greedy; APIs expose it as a request parameter.
- Unlike temperature, top-p renormalizes over a dynamic set, which behaves differently on peaked vs. flat distributions.
- Best practice: tune top-p and temperature jointly — a common default pair is temperature ~0.7 with top-p ~0.9 for creative work.
- For deterministic tasks, many teams use temperature 0 and leave top-p at 1, since sampling is effectively disabled.
- RSIS3 relevance: RRP ideation phases benefit from higher top-p; refinement and test phases run near-greedy.

## Related
- [[wiki/prompt-engineering/temperature-sampling|Temperature Sampling]] — The companion scale knob
- [[wiki/prompt-engineering/logit-bias|Logit Bias]] — Fine-grained token-level control beyond sampling
- [[wiki/prompt-engineering/structured-output|Structured Output]] — Strict schemas typically run near-greedy decoding
- [[wiki/ai-ml/gpt-4|GPT-4]] — Reference model with documented top-p support
- [[wiki/prompt-engineering/prompt-chaining|Prompt Chaining]] — Different chain stages can use different sampling
- [[wiki/syntheses/knowledge-system|Knowledge System Overview]] — Sampling settings logged as wiki metadata
- [[wiki/ai-ml/mistral|Mistral]] — Open family commonly tuned with top-p
- [[wiki/concepts/mykb-analysis|mykb: Personal LLM Wiki — Analysis & Enrichment Theory]] — Sampling metadata enriches analysis
