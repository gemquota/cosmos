---
type: "concept"
title: "Slug Changes"
description: "The tracking and execution of article filename changes"
tags: ["slugs", "changes", "links", "maintenance"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Slug Changes

## Summary
Slug changes are the concrete events where an article's filename changes; each one is a graph mutation that must be propagated to every referrer.

## Details
- A slug change is only complete when the old slug either redirects or has zero remaining inbound links, verified by the global link check.
- Changes should carry a reason in the edit summary or changelog so future curators can see why a path differs from the pattern.
- For mykb, slug changes are batched into link-fix sprints so that renames and their link updates land as one reviewed unit.

## Related
- [[wiki/dev-tools/slug-stability|Slug Stability]]
- [[wiki/dev-tools/renaming-procedure|Renaming Procedure]]
- [[wiki/dev-tools/link-updates|Link Updates]]
- [[wiki/dev-tools/global-link-check|Global Link Check]]
- [[wiki/concepts/redirect-criteria|Redirect Criteria]]
- [[wiki/dev-tools/edit-summaries-wiki|Edit Summaries]]
