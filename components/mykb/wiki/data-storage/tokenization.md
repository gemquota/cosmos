---
type: "concept"
title: "Tokenization"
description: "Splitting text into tokens — words, subwords, or characters — for processing"
tags: ["tokenization", "nlp", "preprocessing", "tokens"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Tokenization

## Summary
Tokenization breaks raw text into the units a downstream system consumes: whitespace words, punctuation-aware tokens, or subword pieces like BPE. Every retriever and language model depends on this first step.

## Details
- **Granularity** — word tokens are human-readable; subword tokens (BPE, WordPiece) handle rare words and unknown vocabulary.
- **Effects** — tokenizer choice changes term statistics and can break or fix matching ('don't' vs 'dont').
- **Agent relevance** — mykb's TF-IDF pipeline and any embedding model each apply their own tokenizer; consistency matters for hybrid fusion.

## Related
- [[wiki/data-storage/n-grams|N-grams]] — contiguous token sequences built after tokenization
- [[wiki/data-storage/stemming|Stemming]] — normalizes tokens to root forms
- [[wiki/data-storage/stopwords|Stopwords]] — tokens often filtered after tokenization
- [[wiki/data-storage/tf-idf|TF-IDF]] — the weighting scheme that consumes tokens
- [[wiki/data-storage/chunking-strategies|Chunking Strategies]] — chunk sizes are measured in tokens
- [[wiki/data-storage/index|Data Storage]] — text preprocessing
