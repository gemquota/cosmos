---
type: "concept"
title: "Archive Policies"
description: "Rules for moving old, cold data to cheap long-term storage"
tags: ["archive", "policies", "storage", "lifecycle"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Archive Policies

## Summary
Archive policies define when data leaves hot storage for cheap archives — age, access patterns, compliance windows. Lifecycle automation (S3 lifecycle, GCS object lifecycle) applies them without humans.

## Details
- Tier by access frequency: hot for active, cold for occasional, archive for rare.
- Archive policies must respect retention and legal-hold requirements.
- Archives are slow to access; make latency expectations explicit to users.
- mykb relevance: old agent logs archive to object storage after the hot window.

## Related
- [[wiki/tooling/retention-policies|Retention Policies]]
- [[wiki/tooling/storage-tiers|Storage Tiers]]
- [[wiki/cloud-infra/glacier-and-s3-lifecycle|Glacier and S3 Lifecycle]]
- [[wiki/dev-tools/log-retention|Log Retention]]
- [[wiki/compositions/backup-and-restore|Backup and Restore]]
