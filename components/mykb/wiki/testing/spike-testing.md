---
type: "concept"
title: "Spike Testing"
description: "Sudden traffic bursts to verify elasticity and recovery"
tags: ["spike-testing", "testing", "autoscaling", "elasticity"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://grafana.com/docs/k6/latest/testing-guides/spike-testing/", "https://www.ibm.com/topics/spike-testing"]
---

# Spike Testing

## Summary
Spike testing applies sudden, extreme traffic bursts far above steady load to verify elasticity and recovery. It models flash sales, viral events, and release-day surges that gradual load tests never reproduce.

## Details
- Jump from near zero to five to ten times normal load in seconds, hold briefly, then drop.
- Observe autoscaling reaction time, queue drain, rate-limit behavior, and error spikes.
- The recovery phase matters as much as the burst: the system must return to baseline.
- Validate autoscaling policies, warm pools, CDN caching, and connection limits.
- Coordinate with load balancing and database connection pooling.
- k6 documents spike testing as a distinct scenario type.
- Replay real traffic shapes where possible for authenticity.

## Related
- [[wiki/testing/stress-testing|Stress Testing]] — sustained overload versus bursts
- [[wiki/testing/load-testing|Load Testing]] — the steady-state baseline
- [[wiki/cloud-infra/autoscaling|Autoscaling]] — elastic response to bursts
- [[wiki/testing/recovery-testing|Recovery Testing]] — returning to baseline after bursts
- [[wiki/api-protocols/rate-limiting|Rate Limiting]] — protecting services during spikes
- [[wiki/devops-infra/load-balancing|Load Balancing]] — distributing burst traffic
