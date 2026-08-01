---
type: "concept"
title: "Git Bisect"
description: "Binary search through commit history to find the commit that introduced a regression"
tags: ["git", "debugging", "history", "bisect"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
---

# Git Bisect

## Summary
`git bisect` runs a binary search over commit history: you mark a good and a bad commit, and git checks out the midpoint for you to test until the offending commit is found. Regression hunting becomes O(log n) commits.

## Details
- Automate with `git bisect run <script>` where the script exits 0 (good) or non-zero (bad).
- Best with linear history; merge-heavy history can confuse the search.
- RSIS3 relevance: agent rollback decisions benefit from knowing exactly which change broke behavior.

## Related
- [[wiki/software-engineering/git-workflows|Git Workflows]] — the history bisect operates on
- [[wiki/dev-tools/debuggers|Debuggers]] — bisect narrows the search before the debugger zooms in
- [[wiki/testing/regression-testing-for-llms|Regression Testing for LLMs]] — bisect finds the change behind a regression
- [[wiki/agent-systems/rollback-and-recovery|Rollback and Recovery]] — the recovery path after finding the bad commit
