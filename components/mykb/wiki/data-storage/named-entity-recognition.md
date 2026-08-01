---
type: "concept"
title: "Named Entity Recognition"
description: "Extracting typed entities such as people, places, and organizations from text"
tags: ["ner", "nlp", "extraction", "entities"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Named Entity Recognition

## Summary
Named entity recognition (NER) finds spans in text and labels them as people, organizations, locations, dates, and more. It is the extraction half of building an entity graph from a corpus.

## Details
- **Approaches** — rule-based gazetteers, classic sequence models (CRF), and transformer taggers (BERT-based).
- **Output** — typed spans feeding entity resolution and knowledge-graph construction.
- **Agent relevance** — mykb's entity extraction from sessions is NER plus resolution; the results populate `wiki/entities/`.

## Related
- [[wiki/data-storage/entity-resolution|Entity Resolution]] — links extracted names to canonical entities
- [[wiki/data-storage/knowledge-graph|Knowledge Graph]] — NER is the graph's front end
- [[wiki/data-storage/topic-modeling|Topic Modeling]] — document-level themes vs span-level entities
- [[wiki/data-storage/embeddings|Embeddings]] — contextual embeddings power modern NER
- [[wiki/data-storage/index|Data Storage]] — NLP extraction family
