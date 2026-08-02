---
type: "concept"
title: "Link-Fix Automation"
description: "Automated tooling that repairs broken or stale wikilinks"
tags: ["links", "automation", "tooling", "maintenance"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Link-Fix Automation

## Summary
Link-fix automation rewrites broken or stale wikilinks using a target map, replacing an old path with its successor across all referrers.

## Details
- Automation is safe when the mapping is unambiguous; ambiguous cases (a rename that split into two articles) must be routed to a human decision.
- Every automated fix runs as a dry run first, then a reviewed batch, then a global link check to prove the graph is clean.
- For mykb, link-fix automation is the payoff of consistent slug naming: the better slugs are, the more fixes can be mechanical.

## Related
- [[wiki/dev-tools/fix-dry-runs|Fix Dry Runs]]
- [[wiki/dev-tools/link-updates|Link Updates]]
- [[wiki/dev-tools/global-link-check|Global Link Check]]
- [[wiki/dev-tools/broken-link-reports|Broken Link Reports]]
- [[wiki/dev-tools/slug-stability|Slug Stability]]
- [[wiki/devops-infra/link-fix-sprints|Link-Fix Sprints]]
