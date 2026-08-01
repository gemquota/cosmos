---
type: "concept"
title: "Lucene"
description: "High-performance open-source full-text search library written in Java"
tags: ["lucene", "search", "indexing", "fts"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Lucene

## Summary
Lucene is the Java full-text search library underpinning Elasticsearch and Solr, providing inverted indexes, analyzers, and BM25 ranking. It is the reference implementation for lexical search infrastructure.

## Details
- **Core** — inverted index over analyzed tokens, term dictionaries, and scored retrieval with pluggable similarities.
- **Analyzers** — tokenization, stemming, stopwords, and synonyms are configured per field or language.
- **Agent relevance** — any serious FTS layer over wiki text will inherit Lucene's analyzers and BM25 defaults via Elasticsearch.

## Related
- [[wiki/data-storage/bm25|BM25]] — Lucene's default ranking function
- [[wiki/data-storage/elasticsearch|Elasticsearch]] — the distributed engine built on Lucene
- [[wiki/data-storage/tf-idf|TF-IDF]] — the classic similarity Lucene also supports
- [[wiki/data-storage/tokenization|Tokenization]] — the analyzer step before indexing
- [[wiki/data-storage/index|Data Storage]] — search libraries
