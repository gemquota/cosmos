---
type: "concept"
title: "Stopwords"
description: "High-frequency function words typically removed before indexing to save space"
tags: ["stopwords", "preprocessing", "ir", "filtering"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
---

# Stopwords

## Summary
Stopwords are very common words (the, and, is) that carry little retrieval signal and are often filtered before indexing. Removing them shrinks indexes and boosts precision for content words, though modern ranking systems often keep them with low weight.

## Details
- Trade-off: removal saves space and focuses ranking on content words; it can hurt phrase queries — to be or not to be becomes empty after filtering, and phrase matching across a stopword boundary behaves oddly.
- Lists: language-specific lists are the baseline; domain corpora add local noise words (e.g. in a devops wiki, words like server or issue may still carry signal and should not be removed blindly).
- Concrete example: a TF-IDF index over mykb text filters the, and, of before counting, shrinking the vocabulary and raising IDF for technical terms; a phrase search for out of memory still works because engines treat stopwords as placeholders in phrase queries; a domain list adds nothing from the technical vocabulary.
- Failure modes: over-filtering — removing words that carry signal in the domain; under-filtering, wasting index space on noise; inconsistent lists between index and query; removing stopwords that appear inside multi-word terms; treating stopword filtering as optional metadata instead of part of the analyzer contract.
- Tradeoffs: stopword removal trades index size and precision for phrase-query robustness; the modern alternative, keeping stopwords with low weights (BM25 downweights but may keep them), preserves phrases at more cost; the mature pattern is a tuned, domain-aware list.
- Operational notes: keep the list versioned with the analyzer, test phrase queries, and review list changes as index behavior changes.
- RSIS3 relevance: mykb's TF-IDF engine benefits from a stopword list tuned to its technical vocabulary — domain-aware filtering keeps retrieval signal on content words.

## Related
- [[wiki/data-storage/tokenization|Tokenization]] — stopword filtering happens after tokenization
- [[wiki/data-storage/stemming|Stemming]] — another normalization step in the same pipeline
- [[wiki/data-storage/tf-idf|TF-IDF]] — stopwords barely affect IDF but waste space
- [[wiki/data-storage/bm25|BM25]] — BM25 downweights but may keep stopwords
- [[wiki/data-storage/index|Data Storage]] — text preprocessing
