---
type: "concept"
title: "YAML Frontmatter"
description: "YAML metadata block at the top of markdown files for titles, tags, and fields"
tags: ["yaml", "frontmatter", "metadata", "markdown"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://jekyllrb.com/docs/front-matter/", "https://en.wikipedia.org/wiki/YAML"]
---

# YAML Frontmatter

## Summary
YAML frontmatter is a `---`-delimited YAML block at the top of a markdown file carrying metadata like title, tags, and status. It gives plain notes a queryable schema without leaving the text format.

## Details
- **Shape** — `---` then `key: value` pairs then `---`; consumed by Obsidian, Hugo, Jekyll, and mykb's daemon.
- **Value** — filtering, templating, graph labels, and provenance all read from frontmatter.
- **Agent relevance** — every mykb page carries `type`, `title`, `description`, `tags`, and `timestamp`; metadata filtering runs over these fields.
- YAML frontmatter is a metadata block at the top of a markdown file, delimited by --- lines, containing key-value fields in YAML.
- It is the standard way static-site generators and knowledge tools attach structured metadata — title, tags, dates, status — to plain-text content.
- The format is strict: a YAML syntax error can silently break the whole page or the site build, which is why linting matters.
- Frontmatter fields should be a fixed, documented schema so tooling can rely on them.
- **Worked example / comparison** — Worked example — a wiki article's frontmatter declares type, title, description, tags, timestamp, and status; the graph builder reads these fields to construct the knowledge graph.
- For mykb, yaml-frontmatter is the format contract of every article and the input to the wiki's linters and graph tooling.

## Related
- [[wiki/data-storage/open-knowledge-format|Open Knowledge Format]]
- [[wiki/data-storage/metadata-filtering|Metadata Filtering]]
- [[wiki/memory/obsidian|Obsidian]]
- [[wiki/memory/provenance|Provenance]]
- [[wiki/syntheses/knowledge-system|Knowledge System]]
- [[wiki/concepts/promotion-readiness|Promotion Readiness]]
- [[wiki/dev-tools/frontmatter-linting|Frontmatter Linting]]
- [[wiki/ai-ml/metadata-score|Metadata Score]]
