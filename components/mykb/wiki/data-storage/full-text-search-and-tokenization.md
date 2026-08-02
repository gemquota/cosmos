---
type: "concept"
title: "Full-Text Search and Tokenization"
description: "From raw text to searchable tokens"
tags: ["full-text-search", "tokenization", "nlp", "indexing"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/Full-text_search", "https://www.elastic.co/guide/en/elasticsearch/reference/current/index.html"]
---

# Full-Text Search and Tokenization

## Summary

Full-text search turns raw text into tokens that can be indexed and matched.
Tokenization, normalization, and stop-word handling shape recall and precision.
Search quality depends more on analysis than on the engine.
Analysis pipelines are the difference between search that finds things and search that misses them.

## Details

- Tokenizers split text; stemmers and lemmatizers reduce word variants.
- Stop-word removal trades recall for index size.
- N-grams handle partial matches and multilingual text.
- BM25 and TF-IDF weight terms by importance.
- Phrase and prefix queries extend keyword matching.
- Test analyzers against real user queries and misspellings.
- Multilingual content needs language-aware tokenization.
- Search quality is an analysis problem: iterate on analyzers before blaming the engine.

## Related

- [[wiki/data-storage/search-engines-elasticsearch|Search Engines Elasticsearch]] — engine
- [[wiki/data-storage/tokenization|Tokenization]] — existing note
- [[wiki/data-storage/bm25|BM25]] — BM25
- [[wiki/data-storage/stemming|Stemming]] — stemming
- [[wiki/data-storage/data-quality-dimensions|Data Quality Dimensions]] — quality dimensions
- [[wiki/data-storage/data-observability-and-monitoring|Data Observability and Monitoring]] — observability
- [[wiki/data-storage/data-testing-frameworks|Data Testing Frameworks]] — testing
- [[wiki/data-storage/feature-stores-and-ml-features|Feature Stores and ML Features]] — ML features
- [[wiki/data-storage/data-contracts-and-agreements|Data Contracts and Agreements]] — data contracts
- [[wiki/data-storage/incremental-loading-strategies|Incremental Loading Strategies]] — incremental loading
- [[wiki/data-storage/schema-evolution-in-streams|Schema Evolution In Streams]] — schema evolution
- [[wiki/data-storage/streaming-sinks-and-sources|Streaming Sinks And Sources]] — streams

