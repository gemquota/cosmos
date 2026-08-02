---
type: "concept"
title: "Navigability Score"
description: "The sub-score rating how easy an article is to navigate"
tags: ["score", "navigability", "metrics", "quality"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Navigability Score

## Summary
The navigability score rates how easily a reader moves through the article and its cluster: clear headings, working links, and a sensible position in the hierarchy.

## Details
- It combines structural checks (heading hierarchy, section order) with graph checks (are the neighbors reachable?).
- Navigability is a reading-experience metric and is closely tied to the structure-needed flag.
- For mykb, navigability scoring flags articles whose structure fights the reader.

## Related
- [[wiki/ai-ml/score-components|Score Components]]
- [[wiki/concepts/navigability-score|Navigability Score]]
- [[wiki/concepts/structure-needed|Structure Needed]]
- [[wiki/concepts/link-placement|Link Placement]]
- [[wiki/data-storage/navigation-boxes|Navigation Boxes]]
- [[wiki/concepts/parent-child-articles|Parent-Child Articles]]
