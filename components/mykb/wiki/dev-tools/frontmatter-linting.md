---
type: "concept"
title: "Frontmatter Linting"
description: "Automated validation of YAML frontmatter fields and values"
tags: ["frontmatter", "linting", "validation", "tooling"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Frontmatter Linting

## Summary
Frontmatter linting checks every article's metadata block: required fields present, types correct, status in the allowed set, tags non-empty, description well-formed. It is the executable version of the wiki's frontmatter contract — the linter encodes the spec so violations fail early.

## Details
- Mechanism: a linter parses the YAML block and validates fields against the format spec: required fields (type, title, description, tags, timestamp, status), type checks, allowed status values, tag non-emptiness, description length and sentence shape; it runs at write time, in CI, and in the global verification pass.
- Concrete example: a missing timestamp, a typo in status (growng instead of growing), or an unquoted title with special characters breaks graph tooling; the linter catches each with a precise message naming the field and file; a promotion pipeline blocks an article whose lint fails.
- Failure modes: lint rules that drift from the spec — the linter becomes a second, contradictory source of truth; rules too strict, blocking legitimate metadata (an unusual title, a long description); a linter that passes but does not check the things tooling actually needs (wikilink format, date validity); lint failures that are bypassable in the write path.
- Tradeoffs: linting costs rule maintenance but prevents the failure class that corrupts indexes, graphs, and dashboards; the alternative, manual review, misses the mechanical errors; the mature pattern is lint rules generated from or diffed against the format spec, with the same checks in write-time and CI.
- Operational notes: keep the linter in the repo, run it in the global verification pass, and treat lint failures as promotion blockers.
- RSIS3 relevance: frontmatter linting runs at write time and in the global verification pass — the same schema-enforcement discipline RSIS3 applies to its state files.

- Report lint violations with file, field, and expected value so fixes are mechanical, and keep the rule set versioned with the spec.
## Related
- [[wiki/data-storage/yaml-frontmatter|YAML Frontmatter]]
- [[wiki/ai-ml/metadata-score|Metadata Score]]
- [[wiki/dev-tools/markdown-linting|Markdown Linting]]
- [[wiki/data-storage/open-knowledge-format|Open Knowledge Format]]
- [[wiki/concepts/promotion-checklist|Promotion Checklist]]
