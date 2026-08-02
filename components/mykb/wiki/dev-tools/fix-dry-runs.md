---
type: "concept"
title: "Fix Dry Runs"
description: "Previewing link fixes before applying them to the wiki"
tags: ["links", "dry-run", "automation", "safety"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Fix Dry Runs

## Summary
A fix dry run computes what a link-fix automation would change — targets rewritten, files touched — and prints the diff without writing anything.

## Details
- Dry runs make automated fixes reviewable: a human checks the proposed changes, especially the display-text and context decisions.
- They also bound blast radius: if a dry run would touch fifty files, that is a decision point, not an automatic action.
- For mykb, dry runs precede every link-fix automation run and their output is what goes to the review queue.

## Related
- [[wiki/dev-tools/link-fix-automation|Link-Fix Automation]]
- [[wiki/dev-tools/global-link-check|Global Link Check]]
- [[wiki/dev-tools/broken-link-reports|Broken Link Reports]]
- [[wiki/dev-tools/link-updates|Link Updates]]
- [[wiki/agent-systems/approval-workflows-wiki|Approval Workflows]]
- [[wiki/dev-tools/diff-viewing|Diff Viewing]]
