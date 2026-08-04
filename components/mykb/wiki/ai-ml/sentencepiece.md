---
type: "entity"
title: "SentencePiece"
description: "A library for language-independent subword tokenization (BPE or Unigram), used by many multilingual models"
tags: ["sentencepiece", "tokenization", "libraries"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://github.com/google/sentencepiece", "https://arxiv.org/abs/1808.06226"]
---

# SentencePiece

## Summary
SentencePiece trains subword models directly on raw text, treating whitespace as a character and supporting BPE and Unigram. It is the tokenizer behind T5, Llama-2-era models, and many multilingual systems.

## Details
- Whitespace-preserving design removes the need for pre-tokenization in most languages.
- Unigram mode picks the most probable segmentation under a learned language model.
- Supports byte fallback for out-of-vocabulary characters.
- RSIS3 relevance: multilingual mykb content tokenizes predictably when SentencePiece-style tokenizers are used.
- SentencePiece is a language-agnostic subword tokenizer that treats raw text as a sequence of Unicode characters or bytes, so it needs no pre-tokenization from spaces.
- It implements both unigram and BPE algorithms and is the tokenizer behind many multilingual and LLM systems, including T5 and LLaMA.
- Because it handles whitespace as a regular character, it can round-trip text losslessly, which matters for detokenization and data pipelines.
- Training options — vocabulary size, character coverage, and normalization rules — have measurable effects on downstream model quality.
- **Worked example / comparison** — Worked example — SentencePiece trains a 32k-vocabulary unigram model on a corpus, then serializes the model file so training and serving use the identical segmentation.
- For mykb, SentencePiece is the reference implementation for subword tokenization and is documented alongside BPE.

## Related
- [[wiki/ai-ml/subword-tokenization|Subword Tokenization]]
- [[wiki/ai-ml/byte-pair-encoding|Byte-Pair Encoding]]
- [[wiki/prompt-engineering/token-budgets|Token Budgets]]
- [[wiki/ml-frameworks/hugging-face|Hugging Face]]
- [[wiki/concepts/promotion-readiness|Promotion Readiness]]
- [[wiki/ai-ml/article-health-scores|Article Health Scores]]
- [[wiki/concepts/explainers|Explainers]]
