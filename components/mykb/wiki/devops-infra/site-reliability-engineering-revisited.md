---
type: "concept"
title: "Site Reliability Engineering"
description: "Applying engineering discipline to operations"
tags: ["sre", "reliability", "operations", "engineering"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: [
  "https://sre.google/sre-book/foreword/",
  "https://en.wikipedia.org/wiki/Site_reliability_engineering",
]
---

# Site Reliability Engineering

## Summary
Site reliability engineering applies software engineering practices to operations, with SLOs, automation, and on-call as core mechanisms. SREs treat operations as a software problem rather than a support burden. It is the discipline behind reliable large-scale services and a major thread in the mykb ops cluster.

## Details
- SRE pairs operational responsibility with engineering time spent on automation and tools.
- The SRE book defines the model, from SLOs to capacity planning to incident management.
- Toil reduction is a stated goal: repeated manual work should be automated away.
- Error budgets decide when releases are safe and when reliability work takes priority.
- Adopting SRE is a cultural change as much as a technical one.
- In mykb, SRE connects to SLOs, incident response, on-call, and postmortems.
- SRE hiring and team structure pair operational responsibility with engineering autonomy.
- Capacity planning and performance work are part of the SRE mandate, not just incident handling.
- Operationally, alerting thresholds and runbook steps for this concept belong in the SLO, incident, and runbook articles of this cluster.

## Related
- [[wiki/cloud-infra/site-to-site-vpn|Site-to-Site VPN]]
- [[wiki/devops-infra/release-engineering-trains|Release Engineering Trains]]
- [[wiki/devops-infra/site-reliability-engineering|Site Reliability Engineering]]
- [[wiki/devops-infra/chaos-engineering|Chaos Engineering]]
