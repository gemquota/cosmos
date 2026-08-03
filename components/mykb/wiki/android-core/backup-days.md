---
type: "concept"
title: "Backup Days"
description: "Scheduled days for verifying and creating backups"
tags: ["backup", "days", "process", "maintenance"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Backup Days

## Summary
Backup days are calendar blocks for creating and testing backups of the wiki bundle and its state.

## Details
- A backup that has never been restored is a hope, not a backup — the day includes a restore drill.
- Backups would be scheduled, labeled, and rotated so the wiki has a known recovery path.
- The day has a fixed checklist: create a fresh backup, verify its manifest, restore it to a scratch location, and confirm the recovered tree passes the same integrity checks as the live one.
- Backup labeling encodes what the archive contains: date, scope (full bundle or state files), and verification status, so any later restore starts from a known-good copy rather than an unverified one.
- Rotation keeps a bounded window of recoverable states: the newest full backup plus the increments between it and the present, with older copies retired only after the newest restore drill passes.
- A backup day also validates the restore path itself — permissions, device availability, and the unpack commands are exercised, not assumed, because a procedure that has never run is where recovery failures hide.
- The cadence is what makes the practice effective: a schedule that slips becomes a hope, so the day is treated like a release — blocked time, an owner, and a defined definition of done.
- Restore drills surface silent failures early: media corruption, missing files, and wrong retention are cheap to fix on a scheduled day and expensive on the day they are actually needed.
- A backup day that ends without a successful restore is recorded as a failed drill, and the failure is investigated before the next cycle rather than papered over.
- For mykb, backup days protect the bundle across devices and are the last line of defense for curation work.

## Related
- [[wiki/android-core/backup-days|Backup Days]]
- [[wiki/android-core/verify-days|Verify Days]]
- [[wiki/android-core/sync-days|Sync Days]]
- [[wiki/devops-infra/archive-days|Archive Days]]
- [[wiki/data-storage/data-versioning|Data Versioning]]
- [[wiki/devops-infra/release-days|Release Days]]
