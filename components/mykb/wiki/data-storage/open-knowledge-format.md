---
type: "concept"
title: "Open Knowledge Format"
description: "Portable markdown-plus-frontmatter convention for machine-readable knowledge bases"
tags: ["okf", "format", "markdown", "knowledge"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://help.obsidian.md/Editing+and+formatting/Properties", "https://yaml.org/spec/1.2.2/"]
---

# Open Knowledge Format

## Summary
Open Knowledge Format (OKF) is the convention used by the cosmos ecosystem: markdown pages with typed YAML frontmatter, validated and linted by the `okf` tooling. It keeps knowledge human-readable and machine-queryable at once.

## Details
- **Conventions** — typed pages (concept, synthesis, source), required frontmatter fields, and wiki-style link paths.
- **Tooling** — `okf validate` checks conformance; `okf lint` reports curation quality (isolated pages, missing descriptions).
- **Agent relevance** — mykb's entire bundle is OKF; the daemon, graph engine, and search all assume the format.
- Open Knowledge Format (OKF) is the portable knowledge format used across the mykb ecosystem: markdown files with YAML frontmatter, typed content, and explicit link relationships.
- Its properties are chosen for durability: plain text, no proprietary tooling, human-readable diffs, and machine-parseable metadata.
- A knowledge base in OKF can be rendered by any markdown tool, queried by its graph layer, and versioned with standard git workflows.
- The format's discipline — required frontmatter fields, typed status, kebab-case slugs — is what makes the corpus consistent at scale.
- **Worked example / comparison** — Worked example — a concept note in OKF has type 'concept', a one-sentence description, tags, a timestamp, and status 'stub' or 'growing', with wikilinks to related notes.
- For mykb, OKF is the format this entire wiki is written in; its rules are the article-format rules of the worker guide.

## Related
- [[wiki/data-storage/yaml-frontmatter|YAML Frontmatter]]
- [[wiki/memory/knowledge-curation|Knowledge Curation]]
- [[wiki/memory/provenance|Provenance]]
- [[wiki/data-storage/metadata-filtering|Metadata Filtering]]
- [[wiki/memory/README|Memory Layer]]
- [[wiki/index|Wiki Index]]
- [[wiki/concepts/promotion-readiness|Promotion Readiness]]
- [[wiki/concepts/tags-practice|Tags Practice]]
