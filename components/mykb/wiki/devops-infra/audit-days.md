---
type: "concept"
title: "Audit Days"
description: "Scheduled days for checking wiki-wide invariants"
tags: ["audit", "days", "process", "maintenance"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Audit Days

## Summary
Audit days are scheduled passes that verify the wiki's invariants: all links resolve, frontmatter is valid, tags are clean, sources are alive.

## Details
- Audits are where the automated checks get human follow-through on the exceptions.
- The audit ends with a report: what passed, what failed, and what entered the maintenance queue.
- For mykb, audit days run the global link check, tag report, and source checks, then feed maintenance-tasks.

## Related
- [[wiki/devops-infra/quality-days|Quality Days]]
- [[wiki/devops-infra/audit-days|Audit Days]]
- [[wiki/dev-tools/global-link-check|Global Link Check]]
- [[wiki/concepts/tag-hygiene|Tag Hygiene]]
- [[wiki/concepts/maintenance-tasks|Maintenance Tasks]]
- [[wiki/android-core/verify-days|Verify Days]]
