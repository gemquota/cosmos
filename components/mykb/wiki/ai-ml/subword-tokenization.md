---
type: "concept"
title: "Subword Tokenization"
description: "Splitting text into units between characters and words, balancing vocabulary size with coverage"
tags: ["tokenization", "subword", "llm", "nlp"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Subword Tokenization

## Summary
Subword tokenization turns text into a fixed vocabulary of frequent subword units, so rare words decompose into known pieces. It is the standard front end of every modern LLM.

## Details
- Methods: BPE (byte pair encoding), WordPiece, and Unigram (SentencePiece).
- Vocabulary sizes typically 32K-256K; tokenizers are trained on the pretraining corpus.
- Tokenization quirks (numbers, whitespace, Unicode) measurably affect model behaviour and prompt design.
- RSIS3 relevance: token counts and budgets are denominated in subword tokens; logit bias operates on token IDs.

## Related
- [[wiki/ai-ml/byte-pair-encoding|Byte-Pair Encoding]] — The dominant subword algorithm
- [[wiki/ai-ml/sentencepiece|SentencePiece]] — The library for subword training
- [[wiki/prompt-engineering/token-budgets|Token Budgets]] — Budgeting is done in tokens
- [[wiki/prompt-engineering/logit-bias|Logit Bias]] — Bias operates on token IDs
- [[wiki/prompt-engineering/context-windows|Context Windows]] — Window capacity in tokens
