---
type: "concept"
title: "Elasticsearch"
description: "Distributed search and analytics engine built on Lucene"
tags: ["elasticsearch", "search", "log-analysis", "distributed"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Elasticsearch

## Summary
Elasticsearch clusters Lucene shards across nodes to deliver near-real-time full-text search and analytics at scale. It is the default choice when wiki-scale search outgrows embedded engines.

## Details
- **Model** — documents with dynamic or explicit mappings; inverted indexes per shard; BM25 relevance by default.
- **Operations** — clusters, replicas, and rolling upgrades trade simplicity for scale and availability.
- **Agent relevance** — mykb currently uses lighter embedded search; Elasticsearch is the scale-out path if the wiki grows past local limits.

## Related
- [[wiki/data-storage/lucene|Lucene]] — the underlying search library
- [[wiki/data-storage/bm25|BM25]] — its default ranking
- [[wiki/data-storage/sqlite-fts5|SQLite FTS5]] — the embedded alternative
- [[wiki/data-storage/hybrid-search|Hybrid Search]] — ES supports vector and lexical fusion
- [[wiki/data-storage/index|Data Storage]] — search engines
