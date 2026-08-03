---
type: "concept"
title: "JSON-LD"
description: "JSON syntax for linked data that embeds graphs and IRIs in ordinary JSON"
tags: ["json-ld", "linked-data", "rdf", "semantic-web"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://json-ld.org/", "https://www.w3.org/TR/json-ld11/"]
---

# JSON-LD

## Summary
JSON-LD encodes linked data as JSON, linking terms to IRIs via a `@context` and letting any JSON document participate in the semantic web. It is the format Google and schema.org use for structured data on the web.

## Details
- **Mechanics** — `@context` maps terms to IRIs; `@id` identifies nodes; nested JSON expands into an RDF graph.
- **Why JSON** — developers can ignore the RDF machinery and still emit interoperable data.
- **Agent relevance** — exporting mykb concepts as JSON-LD would make the wiki consumable by external knowledge-graph tools.
- JSON-LD is a JSON-based format for expressing linked data, using the @context to map short terms to full IRIs.
- It brings RDF-style semantics into the JSON world developers already use, which is why it powers schema.org markup and many APIs.
- A JSON-LD document can be plain JSON to a casual consumer and a fully linked graph to a semantic processor.
- The @context is the contract: it defines the vocabulary, and remote contexts can be cached and versioned.
- **Worked example / comparison** — Worked example — an article's metadata is published as JSON-LD with an @context mapping 'title', 'author', and 'mentions' to schema.org terms, so search engines and graph tools both understand it.
- For mykb, JSON-LD is documented as the JSON-friendly bridge into the RDF family that the data-storage cluster covers.

## Related
- [[wiki/data-storage/rdf|RDF]]
- [[wiki/data-storage/knowledge-graph|Knowledge Graph]]
- [[wiki/memory/ontology-design|Ontology Design]]
- [[wiki/data-storage/sparql|SPARQL]]
- [[wiki/data-storage/00-index|Data Storage]]
- [[wiki/concepts/promotion-readiness|Promotion Readiness]]
- [[wiki/dev-tools/global-link-check|Global Link Check]]
- [[wiki/concepts/explainers|Explainers]]
