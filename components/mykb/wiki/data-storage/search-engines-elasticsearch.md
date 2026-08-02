---
type: "concept"
title: "Search Engines: Elasticsearch"
description: "Distributed full-text search and analytics over inverted indexes"
tags: ["elasticsearch", "search", "inverted-index", "analytics"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://www.elastic.co/guide/en/elasticsearch/reference/current/index.html", "https://en.wikipedia.org/wiki/Full-text_search"]
---

# Search Engines: Elasticsearch

## Summary

Elasticsearch is a distributed search and analytics engine built on Lucene.
It indexes documents with inverted indexes and scores relevance.
It is the standard for log analytics and site search.
Elasticsearch's power comes from Lucene's mature analysis and scoring machinery.

## Details

- Inverted indexes map terms to documents for fast lookup.
- Analyzer pipelines tokenize and normalize text at index time.
- BM25 scoring ranks results by term frequency and document rarity.
- Shards distribute data; replicas provide availability.
- Aggregations turn search indexes into analytics engines.
- Index mapping decisions (analyzers, fields) are hard to change later.
- Aggregations make the same index serve analytics.
- Elasticsearch remains the default for log analytics and site search because the ecosystem is unmatched.

## Related

- [[wiki/data-storage/full-text-search-and-tokenization|Full-Text Search and Tokenization]] — analysis
- [[wiki/data-storage/search-and-relevance-ranking|Search And Relevance Ranking]] — relevance
- [[wiki/data-storage/elasticsearch|Elasticsearch]] — existing note
- [[wiki/data-storage/lucene|Lucene]] — Lucene
- [[wiki/data-storage/inverted-index|Inverted Index]] — index
- [[wiki/data-storage/data-quality-dimensions|Data Quality Dimensions]] — quality dimensions
- [[wiki/data-storage/data-observability-and-monitoring|Data Observability and Monitoring]] — observability
- [[wiki/data-storage/data-testing-frameworks|Data Testing Frameworks]] — testing
- [[wiki/data-storage/feature-stores-and-ml-features|Feature Stores and ML Features]] — ML features
- [[wiki/data-storage/data-contracts-and-agreements|Data Contracts and Agreements]] — data contracts
- [[wiki/data-storage/incremental-loading-strategies|Incremental Loading Strategies]] — incremental loading
- [[wiki/data-storage/schema-evolution-in-streams|Schema Evolution In Streams]] — schema evolution

