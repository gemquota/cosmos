---
type: "concept"
title: "Inverted Index"
description: "Postings lists mapping terms to documents for full-text search"
tags: ["inverted-index", "full-text-search", "information-retrieval", "lucene"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://lucene.apache.org/core/9_12_1/core/org/apache/lucene/codecs/lucene95/package-summary.html", "https://www.postgresql.org/docs/current/textsearch-intro.html"]
---

# Inverted Index

## Summary
An inverted index maps every term in a corpus to a postings list of documents containing it. Instead of scanning each document for every query term, the engine looks up the terms directly, making full-text search effectively proportional to the number of matching documents.

## Details
- **Dictionary** — a sorted structure (often a B-tree or hash table) mapping normalized terms to postings; lookup is the first step of every query.
- **Postings lists** — each list stores document IDs and, in modern engines like Lucene, term frequency and per-position data so phrase queries and scoring can be computed without re-reading the text.
- **Normalization pipeline** — text is tokenized, lowercased, stemmed or lemmatized, and stopwords may be dropped before terms enter the index; the same pipeline runs at query time.
- **Scoring** — engines compute BM25 or TF-IDF-style relevance by combining term frequency, document frequency, and document length from index metadata alone.
- **Deletions and updates** — segments are immutable in Lucene-style engines; updates write new segments and merge old ones, while PostgreSQL's GIN index uses pending lists and fastupdate for insert-heavy loads.
- **mykb relevance** — the local wiki's full-text search (Postgres tsvector and SQLite FTS5) is an inverted index over note text; understanding postings explains ranking behavior.

## Related
- [[wiki/data-storage/bm25|BM25]] — the dominant relevance scoring model
- [[wiki/data-storage/postgres-tsvector|PostgreSQL tsvector]] — GIN-backed inverted index for SQL
- [[wiki/data-storage/tokenization|Tokenization]] — the first stage of the indexing pipeline
- [[wiki/data-storage/lucene|Lucene]] — the reference inverted-index implementation
- [[wiki/data-storage/compression-codecs|Compression Codecs]] — how postings lists stay compact
- [[wiki/data-storage/vector-databases|Vector Databases]] — the semantic-search alternative
