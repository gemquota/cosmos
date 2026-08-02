---
type: "concept"
title: "Subword Tokenization"
description: "Splitting text into units between characters and words, balancing vocabulary size with coverage"
tags: ["tokenization", "subword", "llm", "nlp"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://arxiv.org/abs/1508.07909", "https://huggingface.co/docs/tokenizers/"]
---

# Subword Tokenization

## Summary
Subword tokenization turns text into a fixed vocabulary of frequent subword units, so rare words decompose into known pieces. It is the standard front end of every modern LLM.

## Details
- Methods: BPE (byte pair encoding), WordPiece, and Unigram (SentencePiece).
- Vocabulary sizes typically 32K-256K; tokenizers are trained on the pretraining corpus.
- Tokenization quirks (numbers, whitespace, Unicode) measurably affect model behaviour and prompt design.
- RSIS3 relevance: token counts and budgets are denominated in subword tokens; logit bias operates on token IDs.
- Subword tokenization splits text into units between characters and words, balancing vocabulary size against sequence length: frequent words stay whole, rare words break into smaller pieces.
- It solves the open-vocabulary problem — no out-of-vocabulary token is needed because any unknown string can be segmented into known subwords.
- The tokenizer is trained on a corpus and is a fixed component of the model; tokenizer drift between training and serving silently degrades quality.
- Choice of algorithm (BPE, unigram, WordPiece) changes the segmentation, so tokenizer identity matters for reproducibility.
- **Worked example / comparison** — Worked example — 'tokenization' might stay one token while 'tokenizationability' splits into pieces, keeping the vocabulary compact and coverage complete.
- For mykb, subword-tokenization grounds how the wiki describes LLM inputs; the byte-pair-encoding and sentencepiece articles provide the algorithm details.

## Related
- [[wiki/ai-ml/byte-pair-encoding|Byte-Pair Encoding]]
- [[wiki/ai-ml/sentencepiece|SentencePiece]]
- [[wiki/prompt-engineering/token-budgets|Token Budgets]]
- [[wiki/prompt-engineering/logit-bias|Logit Bias]]
- [[wiki/prompt-engineering/context-windows|Context Windows]]
- [[wiki/concepts/promotion-readiness|Promotion Readiness]]
- [[wiki/ai-ml/article-health-scores|Article Health Scores]]
- [[wiki/concepts/explainers|Explainers]]
