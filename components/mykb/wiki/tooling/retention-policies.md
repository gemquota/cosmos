---
type: "concept"
title: "Retention Policies"
description: "Rules for how long data is kept and when it is deleted"
tags: ["retention", "policies", "compliance", "storage"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Retention Policies

## Summary
Retention policies specify how long each data class lives — backups, logs, records — and what happens at expiry. They balance cost, compliance, and legal obligations, and they must be enforced, not just documented.

## Details
- Define retention per data class with an owner and a review date.
- Automated deletion needs guardrails: legal holds, audit proofs, and reversibility windows.
- Retention is a legal question too — know your jurisdiction's requirements.
- mykb relevance: the wiki keeps curated articles forever but prunes raw captures after review.

## Related
- [[wiki/tooling/archive-policies|Archive Policies]]
- [[wiki/dev-tools/log-retention|Log Retention]]
- [[wiki/cloud-infra/storage-locks-and-retention|Storage Locks and Retention]]
- [[wiki/tooling/immutability-backups|Immutability Backups]]
- [[wiki/tooling/business-continuity|Business Continuity]]
