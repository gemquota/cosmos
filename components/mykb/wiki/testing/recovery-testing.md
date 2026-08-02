---
type: "concept"
title: "Recovery Testing"
description: "Verifying systems restart and recover correctly after failures"
tags: ["recovery-testing", "testing", "resilience", "disaster-recovery"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://www.ibm.com/topics/recovery-testing", "https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/welcome.html"]
---

# Recovery Testing

## Summary
Recovery testing verifies that a system restarts and recovers correctly after failures, crashes, restarts, network partitions, and data corruption. It checks restartability, data integrity, and service restoration rather than assuming they work.

## Details
- Scenarios: kill the process, reboot the host, fail over, and restore from backup.
- Verify clean startup, state reconciliation, queue replay, and no data loss or duplication.
- Include crash-consistency checks for writes in flight during the crash.
- Automate scripted kill-and-verify tests in CI for critical services.
- Recovery time objectives and recovery point objectives set the targets.
- Pair with backups, replication, and disaster-recovery drills.
- Log recovery outcomes; failures here indicate weak state design.

## Related
- [[wiki/testing/chaos-engineering|Chaos Engineering]] — injecting the failures recovery tests verify
- [[wiki/devops-infra/disaster-recovery|Disaster Recovery]] — large-scale recovery planning
- [[wiki/devops-infra/backups|Backups]] — restore paths recovery exercises
- [[wiki/devops-infra/point-in-time-recovery|Point-in-Time Recovery]] — data restoration targets
- [[wiki/devops-infra/rollback-plans|Rollback Plans]] — recovery during deployments
- [[wiki/testing/fault-injection|Fault Injection]] — inducing the faults to recover from
