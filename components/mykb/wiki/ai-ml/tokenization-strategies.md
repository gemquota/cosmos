---
type: "concept"
title: "Tokenization Strategies"
description: "How text is split into tokens and how that affects cost and behavior"
tags: ["tokenization", "subword", "vocabulary", "llm"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://arxiv.org/abs/1609.08144", "https://github.com/openai/tiktoken"]
---

# Tokenization Strategies

## Summary
Tokenization splits text into the tokens a model consumes and generates; it determines context limits, cost, and some failure modes. Subword methods like BPE and SentencePiece dominate modern LLMs. Tokenization is an engineering constraint with surprising behavioral side effects.

## Details
- **Methods** — byte-pair encoding merges frequent character pairs; SentencePiece trains subword units directly; byte-level fallbacks handle rare characters.
- **Cost impact** — non-Latin scripts, code, and special characters tokenize less efficiently; token counts vary 2–4x across languages.
- **Behavioral effects** — number arithmetic, spelling, and in-context patterns are affected by how units split; token-boundary bugs are documented failure classes.
- **Worked example** — a multilingual app measures token cost per language and finds German costs 1.7x English per message, informing model routing.
- **Tooling** — tiktoken and HF tokenizers expose vocabularies and encode/decode for accurate budgeting.
- **mykb relevance** — token budgets and cost accounting depend on precise tokenization measurements; mykb documents subword tokenization.
- Vocabulary size and tokenizer choice directly drive cost per request, so teams benchmark tokenizers before committing to a model.

## Related
- [[wiki/ml-frameworks/token-accounting-and-cost|Token Accounting and Cost]] — cost per token
- [[wiki/ai-ml/byte-pair-encoding|Byte-Pair Encoding]] — the BPE algorithm
- [[wiki/ai-ml/sentencepiece|SentencePiece]] — SentencePiece tooling
- [[wiki/ai-ml/subword-tokenization|Subword Tokenization]] — subword methods
- [[wiki/prompt-engineering/token-budget-planning|Token Budget Planning]] — budgeting with tokenizers
- [[wiki/prompt-engineering/context-window-management|Context Window Management]] — tokens define the window
- [[wiki/ai-ml/model-capabilities-frontier|Model Capabilities Frontier]] — token limits across models
- [[wiki/ml-frameworks/inference-engines|Inference Engines]] — where tokenizers ship
