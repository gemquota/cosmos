---
type: "concept"
title: "Savings Plans"
description: "Flexible hourly commitments that discount compute spend"
tags: ["savings-plans", "pricing", "cost", "aws"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Savings Plans

## Summary

Savings Plans are AWS's flexible commitment model: commit to $/hour of compute spend for 1 or 3 years and get discounted rates across instance families, sizes, and regions (Compute SP) or narrower scopes. They replaced RIs as the default commitment vehicle.

## Details
- Mechanism: you commit to a per-hour spend; usage up to the commitment is billed at the discounted rate, anything beyond at on-demand rates; Compute Savings Plans cover EC2, Fargate, and Lambda with family/region flexibility; EC2 Instance SPs lock family+region for a deeper discount; payment options (all up front, partial, none) trade cash timing for discount depth.
- Concrete example: a team commits $800/hour on a 3-year Compute SP covering its EC2+Fargate baseline; a workload migrates from c5 to c6i without renegotiating; a second team's burst above the commitment pays on-demand. The failure pattern: committing against projected spend that never materializes, stranding the commitment.
- Failure modes: over-committing on uncertain or seasonal workloads; forgetting that SPs cover compute usage, not storage/data-transfer; regional or family lock-in with EC2 Instance SPs; and coverage drift — unused commitment is wasted even though it is "flexible".
- Operational tradeoffs: commitment buys 15-70% discounts; the discipline is to model the floor (stable baseline across teams) and buy against it, reviewing coverage monthly. Prefer Compute SPs for flexibility unless the deepest discount on a fixed fleet outweighs it.
- RSIS3/mykb relevance: the wiki's cost model tracks savings-plan coverage vs actual usage; the loop's quarterly reviews adjust commitments from that data instead of annual guesswork.
- Coverage tooling: AWS provides utilization and coverage reports; alert when coverage drops below the target so the loop buys/reshapes commitments from data, not budgets.
- Lifecycle: set a quarterly review calendar — the 3-year commitment is a financial instrument, and usage shifts make stale commitments the most common waste.

## Related
- [[wiki/devops-infra/rollback-plans|Rollback Plans]]
- [[wiki/cloud-infra/networking-fundamentals|Networking Fundamentals]]
- [[wiki/cloud-infra/tcp-ip-stack|TCP/IP Stack]]
- [[wiki/syntheses/knowledge-acquisition-workflow|Knowledge Acquisition Workflow]]
- [[wiki/syntheses/mykb-acquisition-curation-and-practices|Acquisition, Curation & Practices]]
