---
type: "concept"
title: "SentencePiece"
description: "A library for language-independent subword tokenization (BPE or Unigram), used by many multilingual models"
tags: ["sentencepiece", "tokenization", "libraries"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# SentencePiece

## Summary
SentencePiece trains subword models directly on raw text, treating whitespace as a character and supporting BPE and Unigram. It is the tokenizer behind T5, Llama-2-era models, and many multilingual systems.

## Details
- Whitespace-preserving design removes the need for pre-tokenization in most languages.
- Unigram mode picks the most probable segmentation under a learned language model.
- Supports byte fallback for out-of-vocabulary characters.
- RSIS3 relevance: multilingual mykb content tokenizes predictably when SentencePiece-style tokenizers are used.

## Related
- [[wiki/ai-ml/subword-tokenization|Subword Tokenization]] — The task SentencePiece solves
- [[wiki/ai-ml/byte-pair-encoding|Byte-Pair Encoding]] — One of the algorithms it implements
- [[wiki/prompt-engineering/token-budgets|Token Budgets]] — Tokenizer choice affects budgets
- [[wiki/ml-frameworks/hugging-face|Hugging Face]] — The ecosystem distributing SentencePiece models
