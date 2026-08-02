---
type: "concept"
title: "Metadata Score"
description: "The sub-score rating an article's frontmatter and metadata"
tags: ["score", "metadata", "metrics", "quality"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Metadata Score

## Summary
The metadata score rates the article's frontmatter: description quality, tag hygiene, timestamps, status, and source fields.

## Details
- Metadata is fully checkable, so this component is mechanical — a missing field or malformed tag reduces the score directly.
- Metadata scoring enforces the format contract, which is why linting and scoring share the same rules.
- For mykb, the metadata score is the cheapest component to fix and the first thing promotion review checks.

## Related
- [[wiki/ai-ml/score-components|Score Components]]
- [[wiki/ai-ml/metadata-score|Metadata Score]]
- [[wiki/dev-tools/frontmatter-linting|Frontmatter Linting]]
- [[wiki/dev-tools/description-quality|Description Quality]]
- [[wiki/concepts/tags-practice|Tags Practice]]
- [[wiki/ai-ml/article-score|Article Score]]
