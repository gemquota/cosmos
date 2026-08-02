---
type: "concept"
title: "Release Branches"
description: "Branches that stabilize and freeze a release while main moves on"
tags: ["release-branches", "git", "releases", "branching"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Release Branches

## Summary
Release branches fork from main at release time, receiving only fixes until the release ships, so stabilization does not block new development. They are the multi-version backbone of Git Flow and enterprise release trains.

## Details
- Cherry-pick fixes back to main so the fix is not lost to the release branch.
- Multiple active releases need multiple branches; each needs its own CI and tagging.
- Release branches add merge load — prefer tags and toggles when you can ship often.
- mykb relevance: the wiki's monthly bundle release freezes a branch for QA.

## Related
- [[wiki/communities/git-flow|Git Flow]]
- [[wiki/communities/hotfix-branches|Hotfix Branches]]
- [[wiki/communities/cherry-picks|Cherry-Picks]]
- [[wiki/dev-tools/release-management|Release Management]]
- [[wiki/communities/tag-strategies|Tag Strategies]]
