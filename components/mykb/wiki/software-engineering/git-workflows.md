---
type: "concept"
title: "Git Workflows"
description: "Branching and merging conventions that teams follow to coordinate changes in git"
tags: ["git", "branching", "workflow", "version-control"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://git-scm.com/book/en/v2/Git-Branching-Branching-Workflows"]
---

# Git Workflows

## Summary
A git workflow is the set of conventions a team adopts for branches, merges, and releases. The Pro Git book describes several classic models — centralized, feature branches, and fork-based — while modern teams layer on trunk-based development or git-flow to suit their release cadence.

## Details
- Centralized workflow: everyone commits to a single main branch; simple but collides under concurrent work.
- Feature branch workflow: each change gets its own branch, merged via pull request after review and CI; the default for most teams today.
- Gitflow: long-lived develop and main branches with release and hotfix branches; suits scheduled releases but adds ceremony.
- Trunk-based development: short-lived branches merged to main within a day or two, gated by CI; enables continuous deployment.
- Forking workflow: contributors fork the repository and submit cross-repo pull requests; standard for open source.
- Whatever the model, the key is discipline: small merges, meaningful branch names, and a protected main branch.
- RSIS3 relevance: cosmos uses git for both code and wiki; the acquisition round is a feature-branch-style change reviewed before merge.

## Related
- [[wiki/software-engineering/monorepo-strategies|Monorepo Strategies]] — the repo layout constrains which workflows make sense
- [[wiki/dev-tools/conventional-commits|Conventional Commits]] — message conventions that drive changelogs and releases
- [[wiki/dev-tools/git-rebase|Git Rebase]] — rewriting history to keep branches clean
- [[wiki/dev-tools/git-bisect|Git Bisect]] — binary search through history to find regression commits
- [[wiki/devops-infra/entities/ci-cd-patterns|CI/CD Patterns]] — CI gates every branch before merge
- [[wiki/memory/git-for-notes|Git for Notes]] — the same workflows version the wiki
- [[wiki/agent-systems/rollback-and-recovery|Rollback and Recovery]] — git history is the agent's rollback mechanism
