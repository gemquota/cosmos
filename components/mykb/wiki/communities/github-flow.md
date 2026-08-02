---
type: "concept"
title: "GitHub Flow"
description: "The simple branch model: everything branches from main and merges via pull request"
tags: ["github-flow", "git", "branching", "pull-requests"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# GitHub Flow

## Summary
GitHub Flow keeps a single main branch: every change gets a short-lived feature branch, a pull request, review, and CI, then merges to main and deploys. It is the default workflow for continuous delivery teams.

## Details
- The model assumes main is always deployable — CI gates and small merges make that true.
- Pull requests are the review, discussion, and test surface; keep them small and fast.
- Deploy from main (or a tagged commit) so release == merge.
- mykb relevance: the wiki repo's PRs follow GitHub Flow with lint and link-check CI.

## Related
- [[wiki/communities/branch-strategies|Branch Strategies]]
- [[wiki/dev-tools/trunk-based-development|Trunk-Based Development]]
- [[wiki/communities/code-review-practices|Code Review Practices]]
- [[wiki/dev-tools/continuous-integration|Continuous Integration]]
- [[wiki/communities/git-flow|Git Flow]]
