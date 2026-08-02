---
type: "concept"
title: "Markdown Linting"
description: "Automated checks on markdown structure and syntax"
tags: ["markdown", "linting", "tooling", "quality"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Markdown Linting

## Summary
Markdown linting validates document structure: heading hierarchy, blank lines around blocks, list consistency, code fences, and table shape.

## Details
- Consistent markdown keeps every renderer — Obsidian, the web graph, exporters — producing the same result.
- Lint rules that fight the writer cause rule rot; rules should encode the format the wiki already uses, not an idealized one.
- For mykb, markdown linting complements frontmatter linting and prose linting as the three automated quality gates.

## Related
- [[wiki/dev-tools/frontmatter-linting|Frontmatter Linting]]
- [[wiki/dev-tools/prose-linting|Prose Linting]]
- [[wiki/dev-tools/markdown-linting|Markdown in the Wiki]]
- [[wiki/data-storage/tables-in-wiki|Tables in the Wiki]]
- [[wiki/dev-tools/style-enforcement|Style Enforcement]]
- [[wiki/dev-tools/spellcheck-wiki|Spellcheck for the Wiki]]
