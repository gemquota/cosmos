---
type: "concept"
title: "Consistency Score"
description: "The sub-score rating how consistent an article is with the corpus"
tags: ["score", "consistency", "metrics", "quality"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Consistency Score

## Summary
The consistency score rates whether an article follows the wiki's conventions: title casing, section structure, tag vocabulary, link style, and source format.

## Details
- Consistency is mechanical to check because the conventions are lint rules.
- Consistency matters at corpus scale: an individual inconsistency is trivial, a thousand of them make the wiki unreadable.
- For mykb, the consistency score aggregates the linting results and feeds the metadata score.

## Related
- [[wiki/ai-ml/score-components|Score Components]]
- [[wiki/concepts/consistency-score|Consistency Score]]
- [[wiki/dev-tools/style-enforcement|Style Enforcement]]
- [[wiki/dev-tools/consistent-titles|Consistent Titles]]
- [[wiki/dev-tools/frontmatter-linting|Frontmatter Linting]]
- [[wiki/ai-ml/metadata-score|Metadata Score]]
