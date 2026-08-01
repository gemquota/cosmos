---
type: "concept"
title: "Stopwords"
description: "High-frequency function words typically removed before indexing to save space"
tags: ["stopwords", "preprocessing", "ir", "filtering"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Stopwords

## Summary
Stopwords are very common words ('the', 'and', 'is') that carry little retrieval signal and are often filtered before indexing. Removing them shrinks indexes, though modern ranking systems often keep them with low weight.

## Details
- **Trade-off** — removal saves space and boosts precision for content words; it can hurt phrase queries ('to be or not to be').
- **Lists** — language-specific lists; domain corpora may add local noise words.
- **Agent relevance** — mykb's TF-IDF engine benefits from a stopword list tuned to its technical vocabulary.

## Related
- [[wiki/data-storage/tokenization|Tokenization]] — stopword filtering happens after tokenization
- [[wiki/data-storage/stemming|Stemming]] — another normalization step in the same pipeline
- [[wiki/data-storage/tf-idf|TF-IDF]] — stopwords barely affect IDF but waste space
- [[wiki/data-storage/bm25|BM25]] — BM25 downweights but may keep stopwords
- [[wiki/data-storage/index|Data Storage]] — text preprocessing
