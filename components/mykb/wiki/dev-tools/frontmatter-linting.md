---
type: "concept"
title: "Frontmatter Linting"
description: "Automated validation of YAML frontmatter fields and values"
tags: ["frontmatter", "linting", "validation", "tooling"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Frontmatter Linting

## Summary
Frontmatter linting checks every article's metadata block: required fields present, types correct, status in the allowed set, tags non-empty, description a single sentence.

## Details
- It catches the failures that break graph tooling — a missing timestamp, a typo in status, an unquoted title — before they propagate into indexes and dashboards.
- Lint rules should match the format spec exactly, so the linter is the executable version of the wiki's frontmatter contract.
- For mykb, frontmatter linting runs at write time and in the global verification pass; a lint failure blocks promotion.

## Related
- [[wiki/data-storage/yaml-frontmatter|YAML Frontmatter]]
- [[wiki/ai-ml/metadata-score|Metadata Score]]
- [[wiki/dev-tools/markdown-linting|Markdown Linting]]
- [[wiki/data-storage/open-knowledge-format|Open Knowledge Format]]
- [[wiki/concepts/promotion-checklist|Promotion Checklist]]
- [[wiki/dev-tools/frontmatter-linting|Frontmatter Linting]]
