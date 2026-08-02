---
type: "concept"
title: "Tag Suggestions"
description: "Automated proposals for tags an article is missing"
tags: ["tags", "suggestions", "automation", "metadata"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Tag Suggestions

## Summary
Tag suggestions derive candidate tags for an article from its text and from tags used by similar articles, closing the gap where authors forgot or never knew the vocabulary.

## Details
- Suggestions are advisory: the pipeline proposes, a human accepts, because an automated tag can be confidently wrong.
- The suggestions model is only as good as the tag hygiene underneath it — a dirty vocabulary trains bad suggestions.
- For mykb, tag suggestions feed the curation review queue and keep new articles in the existing cluster structure.

## Related
- [[wiki/concepts/tags-practice|Tags Practice]]
- [[wiki/concepts/tag-hygiene|Tag Hygiene]]
- [[wiki/concepts/tag-merging|Tag Merging]]
- [[wiki/concepts/tag-cascade|Tag Cascade]]
- [[wiki/concepts/tag-suggestions|Tag Suggestions]]
- [[wiki/concepts/tag-splitting|Tag Splitting]]
