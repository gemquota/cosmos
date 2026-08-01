---
type: "concept"
title: "Taxonomy"
description: "Hierarchical classification of a domain into ordered categories used for organization and retrieval"
tags: ["taxonomy", "classification", "hierarchy", "organization", "retrieval"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/Taxonomy_(general)"]
---

# Taxonomy

## Summary
A taxonomy organizes a domain into a hierarchical tree of categories, from broad classes down to specific items. It gives every item one canonical place, which is great for browsing and governance and limiting for ideas that belong in several places. Wiki systems blend taxonomies (namespaces) with linking to escape that limitation.

## Details
- **Structure** — tree of parent-child categories; items may be leaves or further subdivided; depth and breadth trade browseability against maintenance.
- **Where it shines** — file systems, library classification, permissions, and faceted navigation with controlled vocabularies.
- **Where it fails** — cross-cutting topics (e.g., 'memory' spanning psychology, databases, and wikis) must be duplicated or forced into one branch.
- **Worked example** — mykb's `wiki/domains/ai-ml/supercategories/` tree classifies notes by field; a note on RAG could arguably live in three branches, so links rather than deep nesting resolve the ambiguity.
- **Comparison** — taxonomy (strict hierarchy) vs ontology (multiple relations) vs folksonomy (free tags).

## Related
- [[wiki/memory/ontology-design|Ontology Design]] — richer than taxonomy: multiple relation types
- [[wiki/memory/folksonomy|Folksonomy]] — tag-based classification without hierarchy
- [[wiki/memory/information-architecture|Information Architecture]] — the discipline taxonomies serve
- [[wiki/data-storage/topic-modeling|Topic Modeling]] — data-driven alternative to manual taxonomy
- [[wiki/memory/wiki-science|Wiki Science]] — how wikis handle taxonomy vs linking
- [[wiki/data-storage/index|Data Storage]] — a taxonomy branch in mykb's wiki
- [[wiki/concepts/mykb-analysis|Mykb Analysis]] — analyzes mykb's domain classification
