---
type: "concept"
title: "Slug Changes"
description: "The tracking and execution of article filename changes"
tags: ["slugs", "changes", "links", "maintenance"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Slug Changes

## Summary
Slug changes are the concrete events where an article's filename changes; each one is a graph mutation that must be propagated to every referrer. A rename is not done until the old slug redirects or has zero remaining inbound links, verified by the global link check.

## Details
- Mechanism: a rename changes the file path; every article linking to the old slug must be updated; the change carries a reason in the edit summary or changelog so future curators see why the path differs from the pattern; the global link check proves the graph is clean before the change is considered complete.
- Concrete example: article X becomes Y; a target map records the mapping; automation rewrites the referrers; the diff shows the renamed file plus each link update as one reviewed unit; a link check confirms zero broken links; the changelog entry explains the rename (accuracy, disambiguation, pattern alignment).
- Failure modes: renames applied without link updates, leaving broken links; redirects that mask the break, hiding the true link state; slug changes with no reason recorded, so the pattern is unknowable; rename churn — frequent renames that destabilize the graph and burn link-fix effort; changes that break external references (URLs, citations).
- Tradeoffs: clean, stable slugs reduce the need for renames and fixes — the alternative, frequent renames, accumulates link-fix cost; the mature pattern is deliberate rename procedures, batched updates, and a global link check as the completion gate.
- Operational notes: batch slug changes into link-fix sprints, record reasons, and always finish with the global link check.
- RSIS3 relevance: for mykb, slug changes are graph mutations — the same change-management discipline RSIS3 applies to its state transitions.

- Keep a slug-change log so curators can spot rename churn and correct the underlying naming pattern.
## Related
- [[wiki/dev-tools/slug-stability|Slug Stability]]
- [[wiki/dev-tools/renaming-procedure|Renaming Procedure]]
- [[wiki/dev-tools/link-updates|Link Updates]]
- [[wiki/dev-tools/global-link-check|Global Link Check]]
- [[wiki/concepts/redirect-criteria|Redirect Criteria]]
- [[wiki/dev-tools/edit-summaries-wiki|Edit Summaries]]
