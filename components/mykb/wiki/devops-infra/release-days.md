---
type: "concept"
title: "Release Days"
description: "Scheduled days for publishing wiki releases"
tags: ["release", "days", "process", "publication"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Release Days

## Summary
Release days are when a versioned snapshot of the wiki would be cut and published — the bundle, the export, the graph rebuild.

## Details
- Releases would make the wiki's state addressable: readers and tools can point at 'release 2026-08' rather than a moving target.
- A release needs a checklist: verification passed, changelog written, archive built, and the dashboard updated.
- For mykb, release days would formalize the bundle's snapshot cycle and pair with publish-days.

- A release should be reproducible: the archive, the export, and the graph rebuild must come from the same tagged state, so any consumer can rebuild the bundle and verify that the published artifact matches.
- Snapshot contents: each release bundles the corpus (articles and captures), the generated export, and the rebuilt knowledge graph, so a reader or tool can reconstruct the wiki's state at that date without touching the live store.
- Pre-release gates: verification must pass on the tagged commit, the changelog must be written, the archive must build cleanly, and the dashboard must point at the new snapshot before publication.
- Post-release steps: publish the snapshot, update index and dashboard pointers, record the release in the bundle's release log, and route anything verification flagged into the maintenance queue.
- Rollback discipline: if a published release proves broken, the standing rule is to re-cut from the last good tag and document the revert in the changelog rather than mutating the released snapshot in place.
- Cadence: a monthly release day gives consumers a predictable target while keeping the window between snapshots short enough to matter; the cadence is a policy choice, not a technical constraint.
- Versioning: releases use calendar-style names such as '2026-08' so addressability is chronological, and breaking changes or feature additions are documented in the changelog that ships with the release.
- Relationship to audit days: the audit that verifies the wiki's invariants should run before the release is cut, so the snapshot is only published from a state that has already been checked.
## Related
- [[wiki/devops-infra/publish-days|Publish Days]]
- [[wiki/devops-infra/release-days|Release Days]]
- [[wiki/concepts/verified-tag|Verified Tag]]
- [[wiki/devops-infra/release-days|Changelog]]
- [[wiki/android-core/backup-days|Backup Days]]
- [[wiki/data-storage/data-versioning|Versioning]]
