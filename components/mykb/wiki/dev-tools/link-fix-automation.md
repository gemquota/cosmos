---
type: "concept"
title: "Link-Fix Automation"
description: "Automated tooling that repairs broken or stale wikilinks"
tags: ["links", "automation", "tooling", "maintenance"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Link-Fix Automation

## Summary
Link-fix automation rewrites broken or stale wikilinks using a target map, replacing an old path with its successor across all referrers. It turns link repair from a manual sweep into a dry-runnable, reviewable batch operation.

## Details
- Mechanism: a target map records old slug to new slug (from renames and merges); the tool scans every article, finds links whose target is in the map, and rewrites them; every fix runs as a dry run first, then a reviewed batch, then a global link check to prove the graph is clean.
- Concrete example: a rename of article X to Y generates a map entry; the automation rewrites 14 referring articles in one batch; the diff shows each change; the global link check confirms zero broken links; an ambiguous case — a rename that split into two articles — is routed to a human decision instead of a guess.
- Failure modes: automation guessing on ambiguous mappings, rewriting links to the wrong target; batch fixes applied without review, corrupting articles; dry runs and real runs diverging (state changes between them); the target map itself drifting out of date; fixes that resolve the link but leave the display text wrong.
- Tradeoffs: automation makes link repair fast and complete — the alternative, manual fixing, misses links and is slow; the risk is incorrect rewrites, managed by unambiguous mappings, dry runs, and review; the payoff is that curation operations (renames, merges) become safe to do at scale.
- Operational notes: keep the target map generated from real renames, require dry-run-plus-review, and always finish with the global link check.
- RSIS3 relevance: for mykb, link-fix automation is the payoff of consistent slug naming — the better slugs are, the more fixes can be mechanical.

- Keep the automation idempotent: running the fix twice must not double-edit or break already-fixed links.
## Related
- [[wiki/dev-tools/fix-dry-runs|Fix Dry Runs]]
- [[wiki/dev-tools/link-updates|Link Updates]]
- [[wiki/dev-tools/global-link-check|Global Link Check]]
- [[wiki/dev-tools/broken-link-reports|Broken Link Reports]]
- [[wiki/dev-tools/slug-stability|Slug Stability]]
- [[wiki/devops-infra/link-fix-sprints|Link-Fix Sprints]]
