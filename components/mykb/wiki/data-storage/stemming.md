---
type: "concept"
title: "Stemming"
description: "Reducing words to their base or root form by chopping affixes"
tags: ["stemming", "nlp", "normalization", "lexical"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Stemming

## Summary
Stemming crudely removes suffixes so 'running', 'runs', and 'ran' all match 'run'. It is a fast, language-specific normalization that improves lexical recall at the cost of precision.

## Details
- **Algorithms** — Porter (English, rule-based) and Snowball variants; aggressive for some word forms ('ponies' → 'poni').
- **Trade-off** — higher recall for inflected forms; conflated distinct words and ugly stems.
- **Agent relevance** — FTS engines over mykb text can enable stemmers so 'embedding' and 'embeddings' retrieve the same pages.

## Related
- [[wiki/data-storage/lemmatization|Lemmatization]] — the dictionary-based, more accurate alternative
- [[wiki/data-storage/tokenization|Tokenization]] — the step before stemming
- [[wiki/data-storage/stopwords|Stopwords]] — filtering that typically precedes stemming
- [[wiki/data-storage/tf-idf|TF-IDF]] — stemmed terms change TF-IDF weights
- [[wiki/data-storage/bm25|BM25]] — BM25 indexes stemmed terms in most engines
- [[wiki/data-storage/index|Data Storage]] — text normalization
