---
type: "concept"
title: "Logit Bias"
description: "A per-token score added to logits before sampling, biasing the model toward or away from specific tokens"
tags: ["logit-bias", "decoding", "tokenization", "llm"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
source: ["https://platform.openai.com/docs/api-reference/chat/create"]
---

# Logit Bias

## Summary
Logit bias injects a per-token adjustment into the pre-sampling logits, making specific tokens more or less likely to appear. It is a surgical decoding control used for the last 10% of reliability problems — steering format tokens, blocking words, or forcing identifiers.

## Details
- OpenAI's API reference documents logit_bias as a map from token IDs to bias values in [-100, 100]; -100 makes a token effectively impossible, +100 near-certain.
- Bias applies to token IDs, not words: the same word can map to multiple tokens (subword splits), so you must resolve tokenizer IDs first.
- Common uses: force JSON delimiters, block profanity or leaked prompt terms, pin enum values, and stop the model from emitting a specific phrase.
- It is brittle: an over-aggressive bias can distort grammar and neighbouring tokens, so prefer prompt or schema fixes first.
- Logit bias is deterministic and cheap at inference time, which makes it attractive for production guardrails on top of prompting.
- RSIS3 relevance: mykb's guardrail layer can bias against its own internal codewords to prevent leakage into public outputs.

## Related
- [[wiki/prompt-engineering/temperature-sampling|Temperature Sampling]] — Distribution-level control vs. token-level bias
- [[wiki/prompt-engineering/top-p-sampling|Top-P Sampling]] — The other sampling knob logit bias composes with
- [[wiki/prompt-engineering/refusal-behaviour|Refusal Behaviour]] — Token biasing can support refusal mechanisms
- [[wiki/ai-ml/subword-tokenization|Subword Tokenization]] — Why token IDs, not words, are the bias unit
- [[wiki/prompt-engineering/structured-output|Structured Output]] — Schema enforcement makes logit bias mostly unnecessary
- [[wiki/concepts/mykb-implementation-report|mykb Implementation Report: 6-Phase Buildout — Actual State, Architecture, and Results]] — Token-level controls implemented in the buildout
