---
type: "concept"
title: "Code Ownership"
description: "The policy deciding who is responsible for reviewing and maintaining a given piece of code"
tags: ["ownership", "team", "process", "maintenance"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
---
# Code Ownership

## Summary

Code ownership assigns responsibility for quality and review to teams or individuals, creating accountability and stable expertise. The modern practice is team-level ownership with automated review routing — CODEOWNERS, directory-based ownership — balancing accountability against bus-factor risk.

## Details
- Mechanism: ownership maps directories/globs to owners (GitHub CODEOWNERS, GitLab, Gerrit); changes touching owned paths require owner review; owners steward design, review, and incident response for their area; team-level ownership avoids the single-person bus factor while retaining a named accountable party.
- Concrete example: an infra team owns terraform/ and deployment/, and every infra PR requires their review; a library's owners maintain its ADR and deprecation policy; a cross-cutting change touches three owned areas and routes to all three reviewers — sometimes slow, but accountability is clear.
- Failure modes: ownership that becomes gatekeeping (owners as blockers, not stewards); unowned code (orphan directories nobody reviews); ownership by person rather than team, recreating bus-factor risk; and review requirements so strict they encourage workarounds.
- Operational tradeoffs: ownership trades review latency for quality and clarity; the pattern is team ownership, CODEOWNERS automation, and periodic ownership review (code moves, teams change). Keep the owner map as code and audit orphan paths.
- RSIS3/mykb relevance: the wiki's components record their owning team, so loop changes to shared surfaces route through the right reviewers automatically.
- Ownership review cadence: re-run the owner map against the repo quarterly — teams and modules drift, and stale owners become accidental gatekeepers.
- Unowned-path policy: fail CI on changes to paths with no owner, or explicitly route them to a default steward, so orphans cannot accumulate.

## Related
- [[wiki/software-engineering/bus-factor|Bus Factor]] — ownership concentration directly affects the bus factor
- [[wiki/software-engineering/code-review|Code Review]] — owners are the required reviewers
- [[wiki/software-engineering/pair-programming|Pair Programming]] — collaboration dilutes single-owner risk
- [[wiki/concepts/identity-system|RSIS3 Identity System]] — who owns what is an identity question
- [[wiki/memory/knowledge-curation|Knowledge Curation]] — knowledge areas need owners too
