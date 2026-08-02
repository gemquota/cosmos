---
type: "concept"
title: "Snapshot Hierarchy"
description: "Organizing snapshots into generations: fulls, parents, children, and promotion"
tags: ["snapshots", "hierarchy", "backups", "storage"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Snapshot Hierarchy

## Summary
A snapshot hierarchy structures backups into generations — a full, its incremental children, and scheduled retention tiers (hourly, daily, weekly) — so restores are fast and retention is predictable. Promotion and pruning keep the tree bounded.

## Details
- Generational schemes (grandfather-father-son) are classic retention hierarchies.
- Promote a snapshot when it becomes the new anchor; prune children after their parent dies.
- Consistency across the tree matters: a broken parent orphans its children for restore.
- mykb relevance: the wiki snapshot tree keeps hourly capture layers under a weekly anchor.

## Related
- [[wiki/tooling/backup-types|Backup Types]]
- [[wiki/tooling/full-backups|Full Backups]]
- [[wiki/cloud-infra/snapshot-lifecycle-policies|Snapshot Lifecycle Policies]]
- [[wiki/tooling/retention-policies|Retention Policies]]
- [[wiki/tooling/backup-verification|Backup Verification]]
