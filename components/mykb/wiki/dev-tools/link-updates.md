---
type: "concept"
title: "Link Updates"
description: "The process of updating wikilinks after structural changes"
tags: ["links", "updates", "maintenance", "renaming"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Link Updates

## Summary
Link updates are the edits that keep wikilinks pointing at the right target after a rename, merge, split, or redirect change.

## Details
- They are the most mechanical part of curation, which makes them the best candidate for automation: find references, rewrite targets, verify, dry-run first.
- Link updates must respect context — the same target path may need different display text in different articles.
- For mykb, link-updates follow every slug change and are validated by the global link check before the rename is considered done.

## Related
- [[wiki/dev-tools/global-link-check|Global Link Check]]
- [[wiki/dev-tools/fix-dry-runs|Fix Dry Runs]]
- [[wiki/dev-tools/link-fix-automation|Link-Fix Automation]]
- [[wiki/dev-tools/slug-changes|Slug Changes]]
- [[wiki/dev-tools/renaming-procedure|Renaming Procedure]]
- [[wiki/dev-tools/broken-link-reports|Broken Link Reports]]
