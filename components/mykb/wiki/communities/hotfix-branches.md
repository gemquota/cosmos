---
type: "concept"
title: "Hotfix Branches"
description: "Emergency branches that fix production without waiting for the next release"
tags: ["hotfix-branches", "git", "incidents", "branching"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Hotfix Branches

## Summary
Hotfix branches cut from the release or main at the production tag, carry a single urgent fix, and merge to both production and main. They keep incident response fast without contaminating in-flight development.

## Details
- Keep hotfixes tiny and surgical — one fix, one review, fast path to production.
- Always merge the hotfix back to main so it is not lost in the next release.
- Hotfixes are a process smell if frequent: they usually signal a missing rollback or toggle path.
- mykb relevance: a broken wiki link-checker ships via hotfix branch and merges back to trunk.

## Related
- [[wiki/communities/release-branches|Release Branches]]
- [[wiki/communities/revert-strategies|Revert Strategies]]
- [[wiki/communities/incident-management|Incident Management]]
- [[wiki/dev-tools/rollback-strategies|Rollback Strategies]]
- [[wiki/communities/cherry-picks|Cherry-Picks]]
