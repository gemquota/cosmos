---
type: "concept"
title: "Global Link Check"
description: "A wiki-wide scan that every wikilink resolves to a real file"
tags: ["links", "verification", "linting", "maintenance"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Global Link Check

## Summary
A global link check scans every article and resolves every wikilink against the filesystem, reporting any target that does not exist.

## Details
- It is the safety net for curation operations: renames, merges, and deletions break links, and only a full scan proves none slipped through.
- The check should report the referring file and link text so fixes are direct, and it should run in CI or as a pre-commit gate.
- For mykb, the global link check is the final verification step of every promotion and every link-fix sprint.

## Related
- [[wiki/dev-tools/broken-link-reports|Broken Link Reports]]
- [[wiki/dev-tools/link-updates|Link Updates]]
- [[wiki/dev-tools/fix-dry-runs|Fix Dry Runs]]
- [[wiki/dev-tools/markdown-linting|Markdown Linting]]
- [[wiki/dev-tools/link-fix-automation|Link-Fix Automation]]
- [[wiki/syntheses/graph-health-checks|Graph Health Checks]]
