---
type: "concept"
title: "Tag Cascade"
description: "The ripple of changes a tag operation triggers across articles"
tags: ["tags", "cascade", "metadata", "maintenance"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Tag Cascade

## Summary
A tag cascade is the full set of article edits produced by one tag operation — merge, split, or rename — propagated to every affected file.

## Details
- Cascades are why tag operations are batched and dry-run first: a small decision can touch dozens of articles.
- The cascade is complete only when the global tag report shows no stragglers using old or orphaned tags.
- For mykb, the tag cascade is the mechanical layer underneath tag hygiene, and its verification is part of the audit checklist.

## Related
- [[wiki/concepts/tag-merging|Tag Merging]]
- [[wiki/concepts/tag-splitting|Tag Splitting]]
- [[wiki/concepts/tag-renaming|Tag Renaming]]
- [[wiki/concepts/tag-hygiene|Tag Hygiene]]
- [[wiki/dev-tools/fix-dry-runs|Fix Dry Runs]]
- [[wiki/dev-tools/global-link-check|Global Link Check]]
