---
type: "concept"
title: "Renaming Procedure"
description: "The defined steps for renaming an article without breaking the graph"
tags: ["renaming", "procedure", "links", "maintenance"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Renaming Procedure

## Summary
The renaming procedure is the checklist for changing a slug: update the file, update every inbound wikilink, update aliases and redirects, then verify with a global link check.

## Details
- The order matters: links are fixed first, then the file moves, so no intermediate state leaves readers on a broken path.
- Renames should be batched and reviewed because each one touches multiple files and inflates diff noise.
- For mykb, renaming is where slug-stability earns its keep — fewer renames means less link-update churn across the graph.

## Related
- [[wiki/dev-tools/slug-stability|Slug Stability]]
- [[wiki/dev-tools/link-updates|Link Updates]]
- [[wiki/dev-tools/global-link-check|Global Link Check]]
- [[wiki/concepts/redirect-criteria|Redirect Criteria]]
- [[wiki/dev-tools/slug-changes|Slug Changes]]
- [[wiki/dev-tools/renaming-procedure|Renaming Procedure]]
