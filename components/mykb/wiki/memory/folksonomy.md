---
type: "concept"
title: "Folksonomy"
description: "User-generated, flat tagging of items that emerges bottom-up instead of from a controlled hierarchy"
tags: ["tags", "folksonomy", "classification", "metadata", "pkm"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/Folksonomy"]
---

# Folksonomy

## Summary
A folksonomy is classification by free-form tags applied by users (or agents), forming a flat, emergent vocabulary. It is cheap to create, adapts to how people actually describe things, and powers retrieval without a curated hierarchy. Its cost is ambiguity: synonyms, plurals, and inconsistent tagging dilute precision.

## Details
- **Emergence** — tags aggregate into co-occurrence networks; 'popular tags' views emerge from usage rather than authority.
- **Strengths** — zero setup, captures multiple perspectives, adapts quickly to new domains; ideal for personal notes and small teams.
- **Weaknesses** — no synonym control (memory/remembrance), no hierarchy, tag spam; retrieval relies on tag frequency and fuzzy matching.
- **Worked example** — mykb pages are tagged `[rag, retrieval, grounding]` by different authors; search must treat these as related via co-occurrence, and curation can later merge them into one convention.
- **Hybrid pattern** — controlled vocabularies for critical fields (type, status) plus free tags for exploration; mykb's frontmatter does exactly this.

## Related
- [[wiki/memory/taxonomy|Taxonomy]] — the hierarchical alternative folksonomy avoids
- [[wiki/memory/ontology-design|Ontology Design]] — formal schema vs emergent tags
- [[wiki/data-storage/yaml-frontmatter|YAML Frontmatter]] — where tags physically live in markdown
- [[wiki/memory/backlinks|Backlinks]] — another emergent connectivity signal
- [[wiki/meta-learning/cluster-analysis|Cluster Analysis]] — groups tags into de-facto categories
- [[wiki/memory/knowledge-curation|Knowledge Curation]] — curating tags keeps folksonomies usable
- [[wiki/concepts/mykb-analysis|Mykb Analysis]] — mykb's tagging conventions in practice
- [[wiki/reflections/index|Reflections]] — tagged retrospective records
