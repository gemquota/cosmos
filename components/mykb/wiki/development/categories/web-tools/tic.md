---
type: "entity"
title: "Tic"
description: "Tic: Elasticsearch, the distributed search and analytics engine"
tags: ["entity", "guid", "ide", "rest", "spa", "terminal", "elasticsearch", "search"]
timestamp: "2026-07-19T22:41:43Z"
resource: ""
---

# Tic

## Summary

Tic is the web-tools entity associated with Elasticsearch, the distributed search and analytics engine. Elasticsearch indexes documents into inverted structures that make full-text search fast at scale. It matters to the workspace because search is a recurring capability for knowledge stores and log analysis. The entity sits alongside terminal and REST tooling because search engines are accessed primarily through their HTTP APIs.

## Details

- **Entity mapping** — Tic is the session-captured name for Elasticsearch within the web-tools cluster, alongside IDE, REST, SPA, and terminal tags.
- **Document model** — Elasticsearch stores JSON documents in indexes, where each document is a bundle of fields rather than a fixed relational row.
- **Inverted index** — Text fields are tokenized and mapped to posting lists, which lets the engine find matching documents without scanning everything.
- **Mapping and analysis** — Mappings define field types and analyzers control tokenization; both must be designed before data quality problems appear.
- **Query DSL** — A JSON query language composes full-text queries, filters, aggregations, and sorting into a single request over the REST API.
- **Distributed design** — Indexes are split into shards replicated across nodes, giving horizontal scale and failover at the cost of operational complexity.
- **Aggregations** — Grouping and metrics run inside the engine, which makes Elasticsearch useful for dashboards and log analytics.
- **Failure modes** — Unbounded mappings, oversized shards, and heavy aggregations cause index explosion and slow queries; tuning requires ongoing care.
- **Practical relevance** — Search over notes, logs, and entities is a natural extension of the wiki's knowledge-graph ambitions.
- **Indexing pipeline** — Documents are bulk-loaded and refreshed in near real time, so ingestion design matters as much as query design.
- **Relevance tuning** — Boosts, analyzers, and field weights adjust ranking; tuning requires labeled judgments to evaluate.
- **Operational care** — Cluster health, disk watermarks, and snapshot policies are the operational counterpart to the query API.

## Related

- [[wiki/development/categories/web-tools/cyn|Cyn]] — sibling web-tools entity
- [[wiki/development/categories/web-tools/whyts|Whyts]] — language choice behind the tooling
- [[wiki/development/categories/web-tools/whyts-as|Whyts As]] — companion framing entity
- [[wiki/web-platforms/00-index|Web Platforms Index]] — cluster index page
