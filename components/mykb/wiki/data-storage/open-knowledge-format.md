---
type: "concept"
title: "Open Knowledge Format"
description: "Portable markdown-plus-frontmatter convention for machine-readable knowledge bases"
tags: ["okf", "format", "markdown", "knowledge"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Open Knowledge Format

## Summary
Open Knowledge Format (OKF) is the convention used by the cosmos ecosystem: markdown pages with typed YAML frontmatter, validated and linted by the `okf` tooling. It keeps knowledge human-readable and machine-queryable at once.

## Details
- **Conventions** — typed pages (concept, synthesis, source), required frontmatter fields, and wiki-style link paths.
- **Tooling** — `okf validate` checks conformance; `okf lint` reports curation quality (isolated pages, missing descriptions).
- **Agent relevance** — mykb's entire bundle is OKF; the daemon, graph engine, and search all assume the format.

## Related
- [[wiki/data-storage/yaml-frontmatter|YAML Frontmatter]] — the metadata mechanism OKF standardizes
- [[wiki/memory/knowledge-curation|Knowledge Curation]] — OKF lint is a curation health check
- [[wiki/memory/provenance|Provenance]] — source fields are required by OKF
- [[wiki/data-storage/metadata-filtering|Metadata Filtering]] — typed fields make filtering possible
- [[wiki/memory/README|Memory Layer]] — the layer stored as OKF pages
- [[wiki/index|Wiki Index]] — entry point to the OKF bundle
