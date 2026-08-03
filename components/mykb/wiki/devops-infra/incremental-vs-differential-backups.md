---
type: "concept"
title: "Incremental vs Differential Backups"
description: "Change-based backup levels and their restore tradeoffs"
tags: ["backup", "incremental", "differential", "recovery"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Incremental vs Differential Backups

## Summary
Incremental backups store only changes since the last backup of any kind; differential backups store changes since the last full backup. Incrementals are smallest and fastest but depend on the whole chain being intact; differentials are larger but restore with just the last full plus one differential.

## Details
- Mechanics: a full backup establishes a baseline; an incremental chain records changes since the previous increment (full, then inc1, inc2, inc3); a differential records changes since the last full (full, diff1, diff2...), where each differential contains all previous ones. Restore cost: incrementals replay every link of the chain; differentials need only the last full plus the newest differential.
- Concrete example: nightly backups — Monday full, then incremental on Tuesday-Friday restores by applying four incrementals; with differentials, Friday's differential alone (plus Monday's full) restores the week; corrupted Tuesday incremental kills the whole chain, while a bad differential only loses that day.
- Failure modes: chain breakage — a missing or corrupt incremental makes everything after it unrecoverable (verify chains with restore drills); backup software bugs in change tracking silently skipping files; restore-time complexity escalating with chain length; retention interacting with chains (pruning a base invalidates descendants unless the tool rewrites them).
- Tradeoffs: incremental minimizes storage and backup window but maximizes restore time and fragility; differential trades storage for simpler, more robust restores; the practical hybrid is periodic fulls plus incremental chains with frequent restore tests, or forever-incremental tools (restic, Borg) that dedupe and make each snapshot independently restorable.
- Operational notes: test the full chain restore, monitor chain integrity, and set retention that keeps enough fulls for the restore SLA.
- RSIS3 relevance: the wiki's git history is effectively an incremental chain — every commit is a recoverable point, but the restore path should be rehearsed, exactly as with tape or object-storage chains.

## Related
- [[wiki/devops-infra/backups|Backups]] — related coverage in the same cluster
- [[wiki/devops-infra/kubernetes-control-plane|Kubernetes Control Plane]] — related coverage in the same cluster
- [[wiki/devops-infra/observability-pillars|Observability Pillars]] — related coverage in the same cluster
- [[wiki/syntheses/knowledge-acquisition-workflow|Knowledge Acquisition Workflow]] — how stubs grow into full articles in mykb
- [[wiki/syntheses/mykb-acquisition-curation-and-practices|Acquisition, Curation & Practices]] — the curation loop this stub belongs to
