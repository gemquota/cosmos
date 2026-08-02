---
type: "concept"
title: "Git Bisect"
description: "Binary search through commit history to find the commit that introduced a regression"
tags: ["git", "debugging", "history", "bisect"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://git-scm.com/docs/git-bisect", "https://www.kernel.org/pub/software/scm/git/docs/git-bisect.html"]
---

# Git Bisect

## Summary
`git bisect` runs a binary search over commit history: you mark a good and a bad commit, and git checks out the midpoint for you to test until the offending commit is found. Regression hunting becomes O(log n) commits.

## Details
- Automate with `git bisect run <script>` where the script exits 0 (good) or non-zero (bad).
- Best with linear history; merge-heavy history can confuse the search.
- RSIS3 relevance: agent rollback decisions benefit from knowing exactly which change broke behavior.
- git bisect runs a binary search over commit history, checking out midpoints between a known-good and a known-bad commit until the offending change is found.
- Manual bisecting works by marking each checkout good or bad; automated bisecting uses git bisect run with a script that exits 0 (good) or non-zero (bad).
- Bisect is most effective on linear, well-documented history; merge-heavy and poorly described commits make the search harder to interpret.
- The payoff is logarithmic: a thousand-commit range needs about ten tests to isolate a regression.
- **Worked example / comparison** — Worked example — a wiki export broke this week; bisect between last week's good release and today's bad commit isolates the exact PR that introduced the regression.
- For mykb, git-bisect is documented as the regression-hunting tool that pairs with the wiki's checkpoint-rollback practice.

## Related
- [[wiki/software-engineering/git-workflows|Git Workflows]]
- [[wiki/dev-tools/debuggers|Debuggers]]
- [[wiki/testing/regression-testing-for-llms|Regression Testing for LLMs]]
- [[wiki/agent-systems/rollback-and-recovery|Rollback and Recovery]]
- [[wiki/concepts/promotion-readiness|Promotion Readiness]]
- [[wiki/dev-tools/global-link-check|Global Link Check]]
- [[wiki/concepts/explainers|Explainers]]
