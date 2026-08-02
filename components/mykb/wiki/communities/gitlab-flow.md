---
type: "concept"
title: "GitLab Flow"
description: "GitLab's branching model: main plus environment and feature branches with environments"
tags: ["gitlab-flow", "git", "branching", "environments"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# GitLab Flow

## Summary
GitLab Flow adds environment branches (staging, production) and feature branches to a main-centric model, bridging continuous delivery with deployable environments. It keeps GitLab Flow's simplicity while supporting staged releases.

## Details
- Feature branches merge to main; environment branches track deploys (staging, production).
- Promote by merging forward: main -> staging -> production keeps each env a real branch.
- Release tags mark production snapshots for rollback and audit.
- mykb relevance: the wiki deploy maps to GitLab-style env branches for staged rollout.

## Related
- [[wiki/communities/branch-strategies|Branch Strategies]]
- [[wiki/communities/github-flow|GitHub Flow]]
- [[wiki/communities/release-branches|Release Branches]]
- [[wiki/tooling/environment-management|Environment Management]]
- [[wiki/software-engineering/git-workflows|Git Workflows]]
