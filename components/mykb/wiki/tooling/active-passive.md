---
type: "concept"
title: "Active-Passive"
description: "One site serving traffic while another stands by for failover"
tags: ["active-passive", "failover", "availability", "architecture"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Active-Passive

## Summary
Active-passive runs one site in service and a standby site idle or read-only, promoting the standby on failure. It is simpler and cheaper than active-active, with a defined failover time and potential data-loss window.

## Details
- The passive site must be kept warm: replicated data, tested config, ready images.
- Failover time is a product decision — RTO defines how warm the standby must be.
- Drill the promotion regularly; the passive site that has never failed over is untested.
- mykb relevance: a standby wiki mirror with replicated data is promoted on primary loss.

## Related
- [[wiki/tooling/active-active|Active-Active]]
- [[wiki/tooling/failover-practice|Failover Practice]]
- [[wiki/tooling/rpo-rto|RPO/RTO]]
- [[wiki/tooling/multi-region|Multi-Region]]
- [[wiki/tooling/business-continuity|Business Continuity]]
