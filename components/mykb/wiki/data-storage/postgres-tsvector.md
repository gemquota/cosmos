---
type: "concept"
title: "PostgreSQL tsvector"
description: "PostgreSQL's native full-text search over lexemes with ranking support"
tags: ["postgres", "tsvector", "full-text", "sql"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
---

# PostgreSQL tsvector

## Summary
PostgreSQL's tsvector/tsquery types implement full-text search inside SQL: text is normalized into lexemes, matched with operators, and ranked. It lets a relational database double as a search engine without extra infrastructure — filters, joins, and FTS in one query.

## Details
- Mechanics: `to_tsvector('english', body)` parses and normalizes text into lexemes with positions; `to_tsquery('memory & consolidation')` builds a query expression; the `@@` operator matches; `ts_rank` and `ts_rank_cd` score results; weights on columns let title matches outrank body matches.
- Concrete example: a Postgres-backed mykb stores articles with a generated `tsvector` column; a search for `memory AND consolidation` returns ranked articles, filtered by tag and date in the same SQL; an index (`GIN`) keeps the match fast; language dictionaries handle stemming per locale.
- Failure modes: missing indexes, so every search is a full scan; analyzer mismatches between insert and query (searching consolidated does not match consolidating if stemming is off); `ts_rank` favoring long documents without normalization; forgetting to maintain the tsvector on updates; locale or stopword surprises across languages.
- Tradeoffs: tsvector gives real full-text search inside the database you already run — zero new infrastructure — at the cost of ranking sophistication and scale limits compared to dedicated engines; the alternative, Elasticsearch or Lucene, is more powerful and more to operate; the mature pattern is tsvector for mid-size relational search and a dedicated engine when scale demands.
- Operational notes: add a generated column for the tsvector, index it with GIN, and test ranking on real queries.
- RSIS3 relevance: a Postgres-backed mykb could add FTS beside its metadata columns, with filtering in the same query — search without a new system.

## Practice
- Rebuild the tsvector on update with triggers or generated columns so the index never silently goes stale.
## Related
- [[wiki/data-storage/sqlite-fts5|SQLite FTS5]] — the embedded FTS alternative
- [[wiki/data-storage/tf-idf|TF-IDF]] — lexical weighting behind ts_rank
- [[wiki/data-storage/bm25|BM25]] — the ranking ts_rank approximates
- [[wiki/data-storage/metadata-filtering|Metadata Filtering]] — SQL filters combine with FTS naturally
- [[wiki/data-storage/index|Data Storage]] — database technologies
