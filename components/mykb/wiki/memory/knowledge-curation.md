---
type: "concept"
title: "Knowledge Curation"
description: "Deliberate selection, organization, and maintenance of knowledge items so they stay useful over time"
tags: ["curation", "knowledge", "organization", "workflow", "pkm"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/Digital_curation"]
---

# Knowledge Curation

## Summary
Knowledge curation is the active practice of selecting, structuring, and pruning knowledge items so the collection stays findable, trustworthy, and connected. It is the human-or-agent counterpart to search: no retriever can fix a corpus that is messy. mykb's capture-to-synthesis loop is a curation pipeline, not just a storage layer.

## Details
- **Capture vs curate** — capture is cheap (drop everything into an inbox); curation is expensive and continuous (dedupe, re-title, link, retire).
- **Operations** — triage, summarize, tag, link, merge duplicates, demote stale items, and promote syntheses from raw notes.
- **Worked example** — a weekly mykb review: empty the inbox, resolve dangling links, merge two pages about the same paper, and add provenance to a claim that RSIS3 will reuse.
- **Automation** — deduplication, entity resolution, and metadata extraction assist; editorial judgment about what to keep remains the bottleneck.
- **Why it matters for agents** — an LLM's retrieval quality degrades as noise accumulates; curated, linked notes make semantic search dramatically more reliable.

## Related
- [[wiki/memory/knowledge-capture|Knowledge Capture]] — the cheap front half of the curation pipeline
- [[wiki/memory/provenance|Provenance]] — records where curated items came from
- [[wiki/memory/personal-knowledge-management|Personal Knowledge Management]] — the personal practice curation operationalizes
- [[wiki/memory/progressive-summarization|Progressive Summarization]] — a curation technique for layering summaries
- [[wiki/memory/wiki-science|Wiki Science]] — what we know about how wikis stay coherent
- [[wiki/memory/zettelkasten|Zettelkasten]] — a curation method built on atomic notes and links
- [[wiki/syntheses/knowledge-system|Knowledge System]] — the capture-process-connect-synthesize loop
- [[wiki/sources/README|Sources]] — the raw material curation starts from
