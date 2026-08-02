---
type: "concept"
title: "Git Flow"
description: "A branching model with long-lived develop and release branches"
tags: ["git-flow", "git", "branching", "releases"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Git Flow

## Summary
Git Flow maintains main (production) and develop branches, with feature, release, and hotfix branches flowing between them. It suits scheduled releases with strict stability; it adds ceremony that many teams find heavy for continuous delivery.

## Details
- Features branch from develop; releases branch from develop into main; hotfixes branch from main.
- The model's strength is multi-version support; its cost is merge complexity and branch debt.
- Teams on continuous delivery often prefer trunk-based or GitHub Flow instead.
- mykb relevance: the wiki bundle uses a lighter flow; git-flow ideas guide release tagging.

## Related
- [[wiki/communities/branch-strategies|Branch Strategies]]
- [[wiki/communities/github-flow|GitHub Flow]]
- [[wiki/communities/release-branches|Release Branches]]
- [[wiki/communities/hotfix-branches|Hotfix Branches]]
- [[wiki/software-engineering/git-workflows|Git Workflows]]
