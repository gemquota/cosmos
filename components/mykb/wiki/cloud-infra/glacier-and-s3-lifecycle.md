---
type: "concept"
title: "Glacier & S3 Lifecycle"
description: "Automating transitions to archive tiers with lifecycle rules"
tags: ["glacier", "s3", "lifecycle", "archive"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Glacier & S3 Lifecycle

## Summary

S3 lifecycle policies automate object transitions — from Standard to IA/Glacier tiers, then deletion — based on age or tags. Combined with S3 Glacier's classes, they are the cost-control engine for long-tail data; misconfigured, they delete or overcharge.

## Details
- Mechanism: lifecycle rules have transitions (e.g. Standard → Glacier Instant Retrieval at 30 days, → Glacier Flexible at 90, → Deep Archive at 365) and expirations; each class has minimum durations, retrieval models (Instant: ms; Flexible: minutes-hours; Deep Archive: hours up to 12+), and per-GB retrieval fees; S3 Intelligent-Tiering automates movement with a monitoring fee instead of lifecycle rules.
- Concrete example: a media archive lifecycle moves raw files to Glacier after 90 days and Deep Archive after 365, with expirations on temporary uploads after 7 days; an analytics bucket keeps 30 days hot, then transitions to IA for the quarterly query pattern. Wrong access assumptions (reading Flexible monthly) rack up retrieval fees that dwarf storage savings.
- Failure modes: expiration rules deleting data before retention requires (a one-character prefix error is a data-loss incident); early-deletion charges when objects leave a class before minimum duration; lifecycle rules that do not match access patterns (hot data tiered cold); and Glacier restore concurrency limits stalling large recoveries.
- Operational tradeoffs: lifecycle is the standard answer for retention and tiering, but every rule is a policy: define retention per data class, test expirations on a bucket copy, and monitor transitions to catch cost drift. Deep Archive is for the truly cold — budget restore RTO for DR, not just storage savings.
- RSIS3/mykb relevance: the wiki's backup lifecycle (30/90/365) would be recorded here with its restore tests, so the loop's retention reviews have a verified baseline.
- Expiration safety: test lifecycle expirations on a bucket copy with a deletion dry-run; a typo in a prefix is irreversible at the object level.

## Related
- [[wiki/cloud-infra/function-execution-lifecycle|Function Execution Lifecycle]]
- [[wiki/os-shell/process-signals-and-lifecycle|Process Signals & Lifecycle]]
- [[wiki/cloud-infra/snapshot-lifecycle-policies|Snapshot Lifecycle Policies]]
- [[wiki/infrastructure/pod-lifecycle|Pod Lifecycle]]
