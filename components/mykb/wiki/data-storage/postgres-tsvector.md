---
type: "concept"
title: "PostgreSQL tsvector"
description: "PostgreSQL's native full-text search over lexemes with ranking support"
tags: ["postgres", "tsvector", "full-text", "sql"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# PostgreSQL tsvector

## Summary
PostgreSQL's `tsvector`/`tsquery` types implement full-text search inside SQL: text is normalized into lexemes, matched with operators, and ranked. It lets a relational database double as a search engine without extra infrastructure.

## Details
- **Mechanics** — `to_tsvector('english', body)` builds lexemes; `@@` matches against `to_tsquery('memory & consolidation')`.
- **Features** — language dictionaries, weights on columns, and `ts_rank` scoring.
- **Agent relevance** — a Postgres-backed mykb could add FTS beside its metadata columns, with filtering in the same query.

## Related
- [[wiki/data-storage/sqlite-fts5|SQLite FTS5]] — the embedded FTS alternative
- [[wiki/data-storage/tf-idf|TF-IDF]] — lexical weighting behind ts_rank
- [[wiki/data-storage/bm25|BM25]] — the ranking ts_rank approximates
- [[wiki/data-storage/metadata-filtering|Metadata Filtering]] — SQL filters combine with FTS naturally
- [[wiki/data-storage/index|Data Storage]] — database technologies
