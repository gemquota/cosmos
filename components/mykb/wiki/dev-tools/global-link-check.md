---
type: "concept"
title: "Global Link Check"
description: "A wiki-wide scan that every wikilink resolves to a real file"
tags: ["links", "verification", "linting", "maintenance"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Global Link Check

## Summary
A global link check scans every article and resolves every wikilink against the filesystem, reporting any target that does not exist. It is the safety net for curation operations — renames, merges, and deletions break links, and only a full scan proves none slipped through.

## Details
- Mechanism: the checker walks every article, extracts every wikilink, resolves the target path against the wiki tree, and reports broken targets with the referring file and link text; it runs in CI or as a pre-commit gate, and as the final step of promotion and link-fix sprints.
- Concrete example: a rename of article X leaves ten articles linking to the old slug; the global check lists each referring file and the broken target, so fixes are direct; a merge removes a page and the check flags the orphaned links before promotion; the check runs on every PR, keeping the graph healthy continuously.
- Failure modes: checks that resolve links against the wrong root (case, encoding, or path variants), producing false positives or misses; link targets that exist but point at the wrong article (a semantic problem the check cannot see); checks skipped in CI, so breakage accumulates; reports without the referring context, making fixes slow.
- Tradeoffs: a global link check is cheap and mechanical but only catches existence, not correctness — the alternative, manual review, catches semantics and misses existence; the mature pattern is the automated check as the gate plus review for meaning.
- Operational notes: run it in CI and pre-promotion, report referring files and link text, and treat broken links as release blockers.
- RSIS3 relevance: the global link check is the final verification step of every promotion and every link-fix sprint — the same invariant-checking RSIS3 applies to its graph.

## Related
- [[wiki/dev-tools/broken-link-reports|Broken Link Reports]]
- [[wiki/dev-tools/link-updates|Link Updates]]
- [[wiki/dev-tools/fix-dry-runs|Fix Dry Runs]]
- [[wiki/dev-tools/markdown-linting|Markdown Linting]]
- [[wiki/dev-tools/link-fix-automation|Link-Fix Automation]]
- [[wiki/syntheses/graph-health-checks|Graph Health Checks]]
