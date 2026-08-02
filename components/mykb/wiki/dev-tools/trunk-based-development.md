---
type: "concept"
title: "Trunk-Based Development"
description: "Short-lived branches merging to mainline frequently, with toggles hiding incomplete work"
tags: ["trunk-based", "git", "branching", "cd"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://trunkbaseddevelopment.com/", "https://en.wikipedia.org/wiki/Continuous_integration"]
---

# Trunk-Based Development

## Summary
Trunk-based development keeps all work on or near the mainline: branches live hours to a couple of days, and incomplete features are hidden behind feature toggles rather than long-lived branches. It is the branching model that makes CI and CD work at scale.

## Details
- Small, frequent merges keep integration costs near zero; the mainline is always in a releasable state.
- Feature toggles replace branches as the mechanism for hiding incomplete or risky work.
- Release branches exist only briefly at release time; hotfixes are small and merge back immediately.
- Code review happens on short-lived branches or via pair review before direct commits, depending on the team's risk profile.
- Long-lived branches, merge trains, and quarterly integration hell are the symptoms trunk-based development cures.
- DORA consistently finds trunk-based development associated with higher delivery performance.
- For the mykb bundle, article batches merge to main daily, with content-quality toggles gating publication.

Worked example — a wiki contributor works on a branch for two hours, opens a small PR, merges after CI passes, and continues. A half-finished curation feature ships dark behind a toggle, flipped on after verification.

## Related
- [[wiki/communities/trunk-strategy|Trunk Strategy]]
- [[wiki/compositions/feature-toggles|Feature Toggles]]
- [[wiki/dev-tools/continuous-integration|Continuous Integration]]
- [[wiki/dev-tools/continuous-delivery|Continuous Delivery]]
- [[wiki/communities/branch-strategies|Branch Strategies]]
- [[wiki/communities/code-review-practices|Code Review Practices]]
- [[wiki/tooling/flag-cleanup|Flag Cleanup]]
- [[wiki/software-engineering/git-workflows|Git Workflows]]
- [[wiki/devops-infra/ci-cd-best-practices|CI/CD Best Practices]]
