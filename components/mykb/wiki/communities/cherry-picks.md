---
type: "concept"
title: "Cherry-Picks"
description: "Applying a specific commit to another branch"
tags: ["cherry-picks", "git", "workflow", "releases"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Cherry-Picks

## Summary
Cherry-picking copies a single commit onto another branch, used to move a fix to a release branch or a hotfix back to main. It is precise but detached: the copy has a new identity and no commit relationship to the original.

## Details
- Cherry-picked copies do not carry the original's merge history — conflicts can repeat.
- Track cherry-picks explicitly (notes, commit trailers) so fixes are not lost in the shuffle.
- Frequent cherry-picking between branches usually signals a workflow problem.
- mykb relevance: the wiki hotfix cherry-picks from release to trunk with a trailer.

## Related
- [[wiki/communities/release-branches|Release Branches]]
- [[wiki/communities/hotfix-branches|Hotfix Branches]]
- [[wiki/communities/revert-strategies|Revert Strategies]]
- [[wiki/communities/commit-messages|Commit Messages]]
- [[wiki/software-engineering/git-workflows|Git Workflows]]
