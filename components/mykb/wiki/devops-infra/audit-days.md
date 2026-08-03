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
Audit days are scheduled passes that would verify the wiki's invariants: all links resolve, frontmatter is valid, tags are clean, sources are alive.

## Details
- Audits are where the automated checks get human follow-through on the exceptions.
- The audit ends with a report: what passed, what failed, and what entered the maintenance queue.
- For mykb, audit days would run the global link check, tag report, and source checks, then feed maintenance-tasks.

- Audit scope: the invariants an audit checks are mechanical — links resolve, frontmatter parses, tags come from the vocabulary, sources respond — so the audit is scripted and human time is spent on exceptions rather than enumeration.
- Follow-through is the point: an audit that only reports is a checklist; items in the maintenance queue need owners, and failed invariants should be fixed or explicitly accepted before the next audit.
- Cadence: audit days pair with release days, because a release should only be cut from a state the audit has already verified; running the audit just before the snapshot is cut keeps the published bundle honest.
- Scheduling: audit days are scheduled passes on a fixed calendar cadence so drift is caught early, and the exceptions they find should be small enough to clear within the maintenance queue.
- Human and tool collaboration: the automated checks find violations, and the human decides which exceptions are real, which need rework, and which indicate a rule that should change.
- Exit condition: the audit is complete when the report is written, the maintenance queue is populated with owners, and the next audit date is set; an open-ended audit never closes.
- Escalation: a failing invariant that blocks a release should escalate to the owner and the release planner, so the release is delayed or re-scoped explicitly rather than shipped with known violations.
- Outputs: the audit's findings would feed the same maintenance-tasks queue as release-day follow-ups, so there is one backlog rather than competing lists.
## Related
- [[wiki/devops-infra/quality-days|Quality Days]]
- [[wiki/devops-infra/audit-days|Audit Days]]
- [[wiki/dev-tools/global-link-check|Global Link Check]]
- [[wiki/concepts/tag-hygiene|Tag Hygiene]]
- [[wiki/concepts/maintenance-tasks|Maintenance Tasks]]
- [[wiki/android-core/verify-days|Verify Days]]
