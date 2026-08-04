---
type: "entity"
title: "Elasticsearch"
description: "Distributed search and analytics engine built on Lucene"
tags: ["elasticsearch", "search", "log-analysis", "distributed"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
---

# Elasticsearch

## Summary
Elasticsearch clusters Lucene shards across nodes to deliver near-real-time full-text search and analytics at scale. Documents with dynamic or explicit mappings land in inverted indexes per shard, ranked by BM25 by default — the scale-out path when wiki-scale search outgrows embedded engines.

## Details
- Mechanism: documents are indexed into shards, each backed by Lucene with an inverted index; mappings define field types and analysis; queries fan out across shards and merge results; replicas provide availability and read scaling; the cluster coordinates routing, recovery, and rolling upgrades.
- Concrete example: a wiki with millions of articles indexes title, body, and tags; search queries use BM25 with field boosting; aggregations power facet counts and analytics; a growing corpus adds shards and nodes; index lifecycle policies roll old data to cold storage.
- Failure modes: mapping explosions — dynamic mapping creating thousands of fields, exhausting memory; shard imbalance or too many small shards degrading performance; cluster health ignored until red status means data is unassigned; split-brain in older configs (modern versions use quorum-based voting); index bloat from no lifecycle policy; query patterns (wildcards, deep pagination) that kill performance.
- Tradeoffs: Elasticsearch trades operational weight (a cluster to run) for scale, near-real-time indexing, and rich querying; the alternative, embedded search (SQLite FTS5, Lucene directly), is simpler and limited to a single machine; the mature pattern is embedded search for small corpora and Elasticsearch for scale, with explicit mappings and lifecycle policies.
- Operational notes: manage mappings deliberately, monitor cluster health and shard counts, and test query performance before scaling.
- RSIS3 relevance: mykb currently uses lighter embedded search; Elasticsearch is the scale-out path if the wiki grows past local limits — the same tradeoff RSIS3 weighs for its own indexes.

## Related
- [[wiki/data-storage/lucene|Lucene]] — the underlying search library
- [[wiki/data-storage/bm25|BM25]] — its default ranking
- [[wiki/data-storage/sqlite-fts5|SQLite FTS5]] — the embedded alternative
- [[wiki/data-storage/hybrid-search|Hybrid Search]] — ES supports vector and lexical fusion
- [[wiki/data-storage/00-index|Data Storage]] — search engines
