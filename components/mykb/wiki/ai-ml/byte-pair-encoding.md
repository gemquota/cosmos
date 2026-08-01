---
type: "concept"
title: "Byte-Pair Encoding"
description: "BPE: a bottom-up subword algorithm that iteratively merges the most frequent adjacent symbol pairs"
tags: ["byte-pair-encoding", "bpe", "tokenization"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Byte-Pair Encoding

## Summary
BPE builds a token vocabulary by repeatedly merging the most frequent pair of adjacent symbols in a corpus until the target vocabulary size is reached. GPT, Llama, and many other LLM tokenizers use BPE (often byte-level).

## Details
- Byte-level BPE avoids out-of-vocabulary characters entirely by starting from bytes.
- Vocabulary merges reflect corpus statistics, so domain text tokenizes more efficiently after custom training.
- Tokenizer choice changes token counts by tens of percent on the same text — relevant for cost.
- RSIS3 relevance: mykb's token accounting should use the exact tokenizer of the model in use, not estimates.

## Related
- [[wiki/ai-ml/subword-tokenization|Subword Tokenization]] — The family BPE belongs to
- [[wiki/ai-ml/sentencepiece|SentencePiece]] — A library implementing BPE/Unigram
- [[wiki/prompt-engineering/token-budgets|Token Budgets]] — Token efficiency depends on tokenizer
- [[wiki/ai-ml/llama|Llama]] — Reference family using byte-level BPE
- [[wiki/ml-frameworks/hugging-face|Hugging Face]] — Tokenizers library hosts BPE implementations
