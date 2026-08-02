---
type: "concept"
title: "Sync Days"
description: "Scheduled days for synchronizing wiki copies"
tags: ["sync", "days", "process", "maintenance"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Sync Days

## Summary
Sync days are calendar blocks for reconciling wiki copies — local, device, remote — so the canonical bundle matches everywhere.

## Details
- Sync work includes conflict resolution, which is why it gets a day rather than happening ad hoc.
- A sync day starts from a diff report and ends with all copies at the same revision.
- For mykb, sync days keep the mobile and desktop copies aligned with the canonical bundle.

## Related
- [[wiki/android-core/backup-days|Backup Days]]
- [[wiki/android-core/sync-days|Sync Days]]
- [[wiki/android-core/verify-days|Verify Days]]
- [[wiki/dev-tools/merge-conflicts|Merge Conflicts]]
- [[wiki/devops-infra/release-days|Release Days]]
- [[wiki/data-storage/data-versioning|Versioning]]
