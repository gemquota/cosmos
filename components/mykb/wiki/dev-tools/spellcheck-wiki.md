---
type: "concept"
title: "Spellcheck for the Wiki"
description: "Automated spelling verification across all articles"
tags: ["spelling", "linting", "quality", "tooling"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Spellcheck for the Wiki

## Summary
Wiki spellcheck runs a dictionary over every article, with a project glossary of technical terms and names that the spellchecker must accept.

## Details
- The glossary is the hard part: domain terms (RSIS3, mykb, kebab-case, Obsidian) are legitimate words for this wiki and must be maintained deliberately.
- False positives destroy trust in the tool, so unknown words are triaged into glossary-add or fix-spelling rather than silently ignored.
- For mykb, spellcheck runs in the same verification pass as frontmatter and markdown linting, keeping the bar consistent.

## Related
- [[wiki/dev-tools/prose-linting|Prose Linting]]
- [[wiki/dev-tools/frontmatter-linting|Frontmatter Linting]]
- [[wiki/dev-tools/style-enforcement|Style Enforcement]]
- [[wiki/dev-tools/consistent-titles|Consistent Titles]]
- [[wiki/data-storage/glossaries-wiki|Glossaries]]
- [[wiki/concepts/accuracy-score|Accuracy Score]]
