---
type: "concept"
title: "Slug Stability"
description: "The practice of keeping article filenames stable once published"
tags: ["slugs", "stability", "naming", "maintenance"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Slug Stability

## Summary
Slug stability means a published article keeps its kebab-case filename unless there is a strong reason to change it, because slugs are the graph's addressing layer.

## Details
- Stable slugs protect inbound links, bookmarks, and any external references; each rename propagates work across the whole wiki.
- Stability is traded against correctness: a genuinely wrong slug (typo, wrong word) should be fixed early, before many links accumulate.
- For mykb, slug-stability is enforced by the renaming-procedure and redirect-criteria: changes are possible, but they are a reviewed event, not a casual edit.

## Related
- [[wiki/dev-tools/renaming-procedure|Renaming Procedure]]
- [[wiki/dev-tools/slug-changes|Slug Changes]]
- [[wiki/dev-tools/link-updates|Link Updates]]
- [[wiki/concepts/redirect-criteria|Redirect Criteria]]
- [[wiki/dev-tools/slug-stability|Slug Stability]]
- [[wiki/dev-tools/consistent-titles|Consistent Titles]]
