---
type: "concept"
title: "YAML Frontmatter"
description: "YAML metadata block at the top of markdown files for titles, tags, and fields"
tags: ["yaml", "frontmatter", "metadata", "markdown"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# YAML Frontmatter

## Summary
YAML frontmatter is a `---`-delimited YAML block at the top of a markdown file carrying metadata like title, tags, and status. It gives plain notes a queryable schema without leaving the text format.

## Details
- **Shape** — `---` then `key: value` pairs then `---`; consumed by Obsidian, Hugo, Jekyll, and mykb's daemon.
- **Value** — filtering, templating, graph labels, and provenance all read from frontmatter.
- **Agent relevance** — every mykb page carries `type`, `title`, `description`, `tags`, and `timestamp`; metadata filtering runs over these fields.

## Related
- [[wiki/data-storage/open-knowledge-format|Open Knowledge Format]] — formalizes frontmatter conventions
- [[wiki/data-storage/metadata-filtering|Metadata Filtering]] — the retrieval feature frontmatter powers
- [[wiki/memory/obsidian|Obsidian]] — the tool that made frontmatter mainstream
- [[wiki/memory/provenance|Provenance]] — source fields live in frontmatter
- [[wiki/syntheses/knowledge-system|Knowledge System]] — typed pages drive the knowledge loop
