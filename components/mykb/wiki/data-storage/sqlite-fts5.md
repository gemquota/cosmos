---
type: "concept"
title: "SQLite FTS5"
description: "Full-text search extension built into SQLite with BM25 ranking"
tags: ["sqlite", "fts5", "full-text", "embedded"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
---

# SQLite FTS5

## Summary
FTS5 is SQLite's built-in full-text search extension: an inverted index with tokenizers, prefix queries, and a ready-made bm25() ranking function. It gives small applications real search with zero servers — CREATE VIRTUAL TABLE notes USING fts5(title, body) and query with MATCH.

## Details
- Usage: virtual tables store the indexed text; `notes MATCH 'memory AND consolidation'` performs boolean and phrase matching; `ORDER BY bm25(notes)` ranks with BM25 out of the box; tokenizers (unicode61, porter, trigram) control how text is split; external-content and contentless tables index text stored elsewhere.
- Concrete example: mykb's data layer favors SQLite; a notes FTS5 table over article titles and bodies gives lexical search beside the metadata columns; prefix queries complete as-you-type; a trigram tokenizer adds substring matching for partial words.
- Failure modes: index and content tables out of sync (external-content tables need triggers or manual sync); tokenizer choice mismatched to the language (unicode61 vs porter vs trigram); missing OR/AND parentheses in queries causing precedence surprises; ranking without a fallback, so no-match queries return nothing useful; FTS5 tables bloating the database without a merge/optimize pass.
- Tradeoffs: FTS5 is embedded, zero-config, and fast for mid-size corpora, at the cost of single-machine scale and ranking sophistication; the alternative, Postgres tsvector, shares the relational model with more server features; Lucene-class engines scale further with operations; the mature pattern is FTS5 for embedded single-user search.
- Operational notes: run optimize after bulk loads, keep tokenizer choice deliberate, and test query syntax in CI.
- RSIS3 relevance: mykb's data layer already favors SQLite — FTS5 is the natural lexical search engine for the wiki.

## Related
- [[wiki/data-storage/bm25|BM25]] — the ranking function FTS5 exposes
- [[wiki/data-storage/tf-idf|TF-IDF]] — the lexical baseline FTS5 implements variants of
- [[wiki/data-storage/postgres-tsvector|PostgreSQL tsvector]] — the server-side FTS alternative
- [[wiki/data-storage/lucene|Lucene]] — the heavyweight library alternative
- [[wiki/concepts/mykb-implementation-report|Mykb Implementation Report]] — records mykb's storage choices
- [[wiki/data-storage/00-index|Data Storage]] — embedded databases
