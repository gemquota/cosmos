---
type: "concept"
title: "Storage Locks & Retention"
description: "Preventing deletion or modification for compliance"
tags: ["storage-lock", "retention", "compliance", "cloud"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Storage Locks & Retention

## Summary

Storage locks and retention policies enforce how long data must live and who can delete it: object locks/immutability, bucket/container retention policies, and lifecycle rules. They implement compliance requirements and defend against accidental or malicious deletion — and they fight with operational cleanup needs.

## Details
- Mechanism: S3 object lock (compliance/governance modes + legal holds), Azure immutability (time-based, legal hold), GCP retention policies (bucket/object, lockable) prevent deletion/modification during the retention window; lifecycle rules delete by age; the interaction matters — locks win over lifecycle, so a locked object ignores expiration rules; versioning is a prerequisite for most lock implementations.
- Concrete example: a compliance bucket locks audit logs for 365 days so neither automation nor admins can purge them; a ransomware-resistant backup uses compliance lock so even a stolen admin key cannot delete recovery points; a dev bucket with 7-day lifecycle hits a legal hold and stops expiring — someone must reconcile the hold against retention.
- Failure modes: locks blocking legitimate cleanup (deleted data accumulates, cost grows); retention too long making storage un-reclaimable; governance locks that an attacker with elevated permissions can lift; and lifecycle rules that delete before retention (the reason locks must be tested against policies).
- Operational tradeoffs: retention guarantees cost flexibility and money; the discipline is a retention matrix per data class (how long, why, who can override), lock modes chosen by threat model (governance vs compliance), and periodic audits that reconcile holds, locks, and lifecycle.
- RSIS3/mykb relevance: the wiki's retention matrix maps data classes to lock modes; this note is the reference the loop uses before altering lifecycle rules.
- Threat model: choose compliance lock where the threat is an attacker with admin access, governance where the threat is automation; the lock mode is a security decision, not a checkbox.

## Related
- [[wiki/infrastructure/storage-systems|Storage Systems]]
- [[wiki/infrastructure/block-storage-file-storage|Block vs File Storage]]
- [[wiki/devops-infra/container-storage-interfaces|Container Storage Interfaces]]
- [[wiki/devops-infra/storage-classes-and-provisioners|Storage Classes & Provisioners]]
- [[wiki/syntheses/knowledge-acquisition-workflow|Knowledge Acquisition Workflow]]
- [[wiki/syntheses/mykb-acquisition-curation-and-practices|Acquisition, Curation & Practices]]
