---
type: "entity"
title: "Lucene"
description: "High-performance open-source full-text search library written in Java"
tags: ["lucene", "search", "indexing", "fts"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
---

# Lucene

## Summary
Lucene is the Java full-text search library underpinning Elasticsearch and Solr, providing inverted indexes, analyzers, and BM25 ranking. It is the reference implementation for lexical search infrastructure — the code path most production search runs through.

## Details
- Core: an inverted index maps analyzed tokens to postings; term dictionaries, skip lists, and segment merging make retrieval fast; scoring is pluggable with BM25 as the modern default and TF-IDF supported; per-segment indexes merge in the background for write performance.
- Analyzers: tokenization, stemming, stopwords, and synonyms are configured per field or language; the analyzer chain determines what tokens exist, so analyzer changes require reindexing.
- Concrete example: Elasticsearch documents indexed through a standard analyzer produce lowercase, stemmed tokens; a query for running matches run; a custom analyzer adds synonyms so car matches automobile; a field with keyword analysis is exact-match only.
- Failure modes: analyzer mismatch between index and query, silently missing matches; reindexing needed after analyzer changes, forgotten until search degrades; segment bloat without merges; scoring surprises from default parameters on skewed fields; memory pressure from large term dictionaries.
- Tradeoffs: Lucene is a library, not a service — you embed it or run it via Elasticsearch/Solr; the alternative, SQL FTS (SQLite FTS5), is simpler and embedded, with a smaller feature set; the mature pattern is Lucene-class engines for real search workloads and embedded FTS for small corpora.
- Operational notes: test analyzer changes with reindexes, monitor merge and segment health, and benchmark queries against real corpora.
- RSIS3 relevance: any serious FTS layer over wiki text will inherit Lucene's analyzers and BM25 defaults via Elasticsearch — the reference behavior mykb's search approximates.

## Practice
- Wrap Lucene with a managed layer (Elasticsearch) unless the corpus is small enough that the library alone is sufficient.
## Related
- [[wiki/data-storage/bm25|BM25]] — Lucene's default ranking function
- [[wiki/data-storage/elasticsearch|Elasticsearch]] — the distributed engine built on Lucene
- [[wiki/data-storage/tf-idf|TF-IDF]] — the classic similarity Lucene also supports
- [[wiki/data-storage/tokenization|Tokenization]] — the analyzer step before indexing
- [[wiki/data-storage/00-index|Data Storage]] — search libraries
