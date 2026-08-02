---
type: "concept"
title: "Business Continuity"
description: "Keeping the organization functioning through disruptions"
tags: ["business-continuity", "disaster-recovery", "planning", "resilience"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/Business_continuity_planning", "https://en.wikipedia.org/wiki/Backup"]
---

# Business Continuity

## Summary
Business continuity planning prepares an organization to keep operating through disruptions — outages, disasters, and crises. It spans people, processes, and technology, with recovery plans tested before they are needed.

## Details
- Business impact analysis ranks processes by recovery priority; that ranking drives RTO and RPO targets.
- Continuity plans cover communication, alternates (locations, suppliers, people), and manual fallbacks.
- Disaster recovery is the technical subset: failover, backups, and restoration of systems and data.
- Plans rot fast: review on a schedule and exercise the critical paths (drills, tabletop, game days).
- The goal is graceful, rehearsed degradation, not heroics at the moment of crisis.
- For the mykb bundle, continuity means the knowledge base survives loss of a device or host.
- Worked example — the wiki's continuity plan: geo-redundant archive, a standby mirror, quarterly restore drills, and a communication plan naming who rebuilds what if the primary host is lost.

Worked example — the wiki's continuity plan: geo-redundant archive, a standby mirror, quarterly restore drills, and a communication plan naming who rebuilds what if the primary host is lost.

## Related
- [[wiki/compositions/backup-and-restore|Backup and Restore]]
- [[wiki/tooling/failover-practice|Failover Practice]]
- [[wiki/tooling/geo-redundancy|Geo-Redundancy]]
- [[wiki/tooling/rpo-rto|RPO/RTO]]
- [[wiki/communities/incident-management|Incident Management]]
- [[wiki/tooling/game-days|Game Days]]
- [[wiki/devops-infra/disaster-recovery|Disaster Recovery]]
- [[wiki/devops-infra/disaster-recovery-tiers|Disaster Recovery Tiers]]
