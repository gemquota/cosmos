---
type: "concept"
title: "JSON-LD"
description: "JSON syntax for linked data that embeds graphs and IRIs in ordinary JSON"
tags: ["json-ld", "linked-data", "rdf", "semantic-web"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# JSON-LD

## Summary
JSON-LD encodes linked data as JSON, linking terms to IRIs via a `@context` and letting any JSON document participate in the semantic web. It is the format Google and schema.org use for structured data on the web.

## Details
- **Mechanics** — `@context` maps terms to IRIs; `@id` identifies nodes; nested JSON expands into an RDF graph.
- **Why JSON** — developers can ignore the RDF machinery and still emit interoperable data.
- **Agent relevance** — exporting mykb concepts as JSON-LD would make the wiki consumable by external knowledge-graph tools.

## Related
- [[wiki/data-storage/rdf|RDF]] — the abstract graph model JSON-LD serializes
- [[wiki/data-storage/knowledge-graph|Knowledge Graph]] — the graph JSON-LD describes
- [[wiki/memory/ontology-design|Ontology Design]] — contexts map to ontology terms
- [[wiki/data-storage/sparql|SPARQL]] — querying JSON-LD-expanded graphs
- [[wiki/data-storage/index|Data Storage]] — linked-data formats
