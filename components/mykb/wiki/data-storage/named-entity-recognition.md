---
type: "concept"
title: "Named Entity Recognition"
description: "Extracting typed entities such as people, places, and organizations from text"
tags: ["ner", "nlp", "extraction", "entities"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
---

# Named Entity Recognition

## Summary
Named entity recognition (NER) finds spans in text and labels them as people, organizations, locations, dates, and more. It is the extraction half of building an entity graph from a corpus — the raw material that entity resolution then links into canonical entities.

## Details
- Approaches: rule-based gazetteers match known names against dictionaries; classic sequence models (CRF) label token sequences with features; transformer taggers (BERT-based) treat NER as a token-classification task and capture context — a doctor in one sentence and a street in another disambiguate correctly.
- Output: typed spans (person, org, location, date, product) feeding entity resolution and knowledge-graph construction; each span carries start/end offsets and a confidence when the model provides it.
- Concrete example: a session note mentions Dr. Lee at Acme Hospital in Berlin — NER labels Dr. Lee as person, Acme Hospital as org, Berlin as location; entity resolution links Dr. Lee to the canonical people/lee entry in the wiki; the graph edge connects the article to the person entity.
- Failure modes: over-extraction (labeling common nouns as entities) polluting the graph; under-extraction missing entities the corpus needs; unresolved aliases fragmenting the same entity across spellings; NER errors propagating into downstream resolution without confidence thresholds; language and domain mismatch — a model trained on news misbehaves on technical notes.
- Tradeoffs: transformer NER gives the best accuracy at the cost of model size and inference time; rule-based and CRF approaches are fast and interpretable but brittle; the mature pattern is a hybrid — rules for high-precision domains, models for recall — with confidence thresholds before graph writes.
- Operational notes: evaluate on a labeled sample of the real corpus, log false positives, and version the model with the extraction pipeline.
- RSIS3 relevance: mykb's entity extraction from sessions is NER plus resolution; the results populate the entities directory — the front end of the knowledge graph.

## Related
- [[wiki/data-storage/entity-resolution|Entity Resolution]] — links extracted names to canonical entities
- [[wiki/data-storage/knowledge-graph|Knowledge Graph]] — NER is the graph's front end
- [[wiki/data-storage/topic-modeling|Topic Modeling]] — document-level themes vs span-level entities
- [[wiki/data-storage/embeddings|Embeddings]] — contextual embeddings power modern NER
- [[wiki/data-storage/index|Data Storage]] — NLP extraction family
