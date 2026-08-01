---
type: "concept"
title: "SQLite FTS5"
description: "Full-text search extension built into SQLite with BM25 ranking"
tags: ["sqlite", "fts5", "full-text", "embedded"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# SQLite FTS5

## Summary
FTS5 is SQLite's built-in full-text search extension: an inverted index with tokenizers, prefix queries, and a ready-made `bm25()` ranking function. It gives small applications real search with zero servers.

## Details
- **Usage** — `CREATE VIRTUAL TABLE notes USING fts5(title, body);` then `... WHERE notes MATCH 'memory AND consolidation'`.
- **Ranking** — `ORDER BY bm25(notes)` applies the BM25 scoring out of the box.
- **Agent relevance** — mykb's data layer already favors SQLite; FTS5 is the natural lexical search engine for the wiki.

## Related
- [[wiki/data-storage/bm25|BM25]] — the ranking function FTS5 exposes
- [[wiki/data-storage/tf-idf|TF-IDF]] — the lexical baseline FTS5 implements variants of
- [[wiki/data-storage/postgres-tsvector|PostgreSQL tsvector]] — the server-side FTS alternative
- [[wiki/data-storage/lucene|Lucene]] — the heavyweight library alternative
- [[wiki/concepts/mykb-implementation-report|Mykb Implementation Report]] — records mykb's storage choices
- [[wiki/data-storage/index|Data Storage]] — embedded databases
