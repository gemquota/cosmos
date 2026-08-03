---
type: "concept"
title: "Snapshot Lifecycle Policies"
description: "Automating snapshot creation, retention, and deletion"
tags: ["snapshot", "lifecycle", "backup", "cloud"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Snapshot Lifecycle Policies

## Summary

Snapshot lifecycle policies automate snapshot creation, retention, and deletion — daily/weekly/monthly cadences, age-based expiry, cross-region copies. They are the difference between "we have backups" and "we have restorable backups that we can afford".

## Details
- Mechanism: policies (AWS DLM, Azure backup policies, GCP snapshot schedules) create snapshots on a schedule, tag them, retain N copies or age-based windows (e.g. 7 daily, 4 weekly, 12 monthly), and delete expired ones automatically; cross-region replication can be part of the policy. Snapshots are incremental — deletion cost depends on dependent chains.
- Concrete example: a database volume keeps 7 daily + 4 weekly + 12 monthly snapshots with 30-day cross-region copies for DR; a dev environment keeps only the last 2 snapshots to control cost; a lifecycle misconfiguration that deletes all snapshots after 1 day is the nightmare — retention defaults must be explicit.
- Failure modes: policies deleting the only recovery point (retention too short); snapshot chains where deleting one snapshot forces materialization of its parents (cost spike); missed schedules (policy paused or misconfigured after region moves); and assuming snapshots are tested — an untested restore is not a backup.
- Operational tradeoffs: automation trades a little cost for reliability; the discipline is explicit retention matrices per data class, scheduled restore drills, and monitoring (snapshot age, success rate). Keep cross-region copies only where the RTO/RPO story needs them.
- RSIS3/mykb relevance: the wiki's backup policies are recorded with their retention matrices here; the loop's DR review validates restores, not just snapshot existence.
- Restore testing: schedule a quarterly restore of the oldest snapshot in the retention window; the snapshot that has never been restored is not a backup.
- Tagging: tag snapshots with source, owner, and retention class; untagged snapshots are unreclaimable inventory nobody can safely delete.

## Related
- [[wiki/infrastructure/snapshot-and-clone-techniques|Snapshot & Clone Techniques]]
- [[wiki/cloud-infra/function-execution-lifecycle|Function Execution Lifecycle]]
- [[wiki/devops-infra/ingress-egress-policies|Ingress & Egress Policies]]
- [[wiki/devops-infra/network-policies-kubernetes|Kubernetes Network Policies]]
- [[wiki/syntheses/knowledge-acquisition-workflow|Knowledge Acquisition Workflow]]
- [[wiki/syntheses/mykb-acquisition-curation-and-practices|Acquisition, Curation & Practices]]
