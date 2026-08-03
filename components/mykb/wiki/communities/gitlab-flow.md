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
- mykb relevance: the wiki deploy would map to GitLab-style env branches for staged rollout.

Environment branches make each stage a long-lived branch that only receives merges from the branch below it, so the history at any environment mirrors exactly what is deployed there and promotion is a reviewed merge rather than an ad hoc deploy; production hotfixes branch off main and merge both forward and down, keeping the fix in every environment while preserving the single-source-of-truth model, at the cost of a little merge ceremony compared with trunk-based flows.

Release tags mark production snapshots, environment branches stay close to main so staging and production never drift far from the integration line, and the diff between environments is always visible in the branch graph; when a release fails in production, the team merges the fix into main and forward-merges it through the environment chain before tagging the new snapshot, so the audit trail is the merge history itself, which is why GitLab Flow pairs naturally with conventional commit messages and changelog automation, and keeps every promotion auditable from the branch graph alone.

The main tradeoff is that long-lived environment branches accumulate merge conflicts when features sit in staging too long, so the model rewards short staging dwell times, frequent forward merges, and a promotion checklist that runs the same verification at every environment hop, keeping the difference between environments a matter of scale rather than drift.

## Related
- [[wiki/communities/branch-strategies|Branch Strategies]]
- [[wiki/communities/github-flow|GitHub Flow]]
- [[wiki/communities/release-branches|Release Branches]]
- [[wiki/tooling/environment-management|Environment Management]]
- [[wiki/software-engineering/git-workflows|Git Workflows]]
