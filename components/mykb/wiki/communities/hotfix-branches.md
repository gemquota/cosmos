---
type: "concept"
title: "Hotfix Branches"
description: "Emergency branches that fix production without waiting for the next release"
tags: ["hotfix-branches", "git", "incidents", "branching"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Hotfix Branches

## Summary
Hotfix branches cut from the release or main at the production tag, carry a single urgent fix, and merge to both production and main. They keep incident response fast without contaminating in-flight development.

## Details
- **Mechanics** — the hotfix branch is created from the exact commit that is running in production (the release tag or the tip of the release branch), never from the development branch, so the fix sits on top of precisely what customers have; the fix is committed, tested against the production shape, then merged forward in two directions: into the release branch (or tagged as the new production release) and into main so the fix is not lost when the next release catches up.
- **Why two merges** — if the fix lands only on the release branch, the next release from main reintroduces the bug; if it lands only on main, production never gets it; the dual merge is the entire point of the pattern, and automation (merge request per target, or cherry-pick with a tracking note) is what prevents the second merge from being forgotten under pressure.
- **Keep hotfixes tiny and surgical** — one fix, one review, fast path to production: a hotfix should change the minimum code that resolves the incident — often a revert, a config change, a dependency pin, or a one-line guard — because every extra change multiplies the risk that the emergency patch itself introduces a new outage; refactors and features belong on main, not in the hotfix.
- **Failure modes** — the common incidents are: hotfixing from the wrong base (the developer branch, which may be days ahead of production) and shipping changes that were never on production; forgetting the main-ward merge and discovering the bug 'returns' in the next release; hotfix branches that linger and accrete multiple unrelated fixes, making the emergency path indistinguishable from normal development; and skipping the review because it is urgent — an unreviewed hotfix trades one incident for another.
- **Process smell** — frequent hotfixes usually signal a missing capability: if every outage requires a code change, the team lacks a feature flag to disable the broken behaviour, a rollback path for the previous release, or sufficient pre-release validation; the corrective action is to build the toggle or rollback mechanism, not to speed up the hotfix pipeline.
- **Relationship to other strategies** — a hotfix is one of several incident responses: revert the offending commit when the bug is recent and cleanly reversible; roll back the release when the last deploy is the cause; toggle a feature flag when the failure is isolated behind a flag; and hotfix only when a corrective code change is genuinely required — the choice depends on which lever is fastest and safest for the specific incident.
- **mykb relevance** — a broken wiki link-checker ships via hotfix branch and merges back to trunk: the emergency path exists so the publishing pipeline can be repaired within minutes, and the post-incident note should record both the code fix and the process gap (missing CI link check) so the same class of outage does not recur.

## Related
- [[wiki/communities/release-branches|Release Branches]]
- [[wiki/communities/revert-strategies|Revert Strategies]]
- [[wiki/communities/incident-management|Incident Management]]
- [[wiki/dev-tools/rollback-strategies|Rollback Strategies]]
- [[wiki/communities/cherry-picks|Cherry-Picks]]
