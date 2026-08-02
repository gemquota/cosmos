---
type: "concept"
title: "FinOps Practices"
description: "The operational discipline of managing cloud cost: visibility, allocation, and continuous optimization"
tags: ["finops", "cost", "governance", "cloud"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://www.finops.org/introduction/what-is-finops/", "https://www.finops.org/framework/"]
---

# FinOps Practices

## Summary
FinOps is a culture and set of practices that make cloud spending visible, allocated, and optimized — finance, engineering, and product sharing the cost conversation.

## Details
- Core loop: inform (show spend), optimize (reduce waste), operate (budgets and accountability).
- Unit economics beat raw totals: cost per request, per user, per model call.
- Tagging and ownership allocate spend so optimization has an owner.
- Open question: how to apply FinOps to AI/GPU spend, where unit costs are new and volatile.
- FinOps is the operational discipline of managing cloud spend: finance, engineering, and business teams share accountability for cost decisions.
- The core loop is inform (visibility and allocation), optimize (rightsizing and commitments), and operate (continuous governance).
- Unit economics are the key metric — cost per request, per user, per article — because raw totals hide whether spending is efficient.
- The practice is cultural: engineers must see the cost of their choices and own the tradeoff between performance and spend.
- **Worked example / comparison** — Worked example — the wiki team tracks cost per exported bundle; when a release doubles the metric, the report makes the regression visible and attributable to the change.
- For mykb, finops-practices ties together budget-alerts, capacity-planning, and cloud-cost-optimization into one operating discipline.

## Related
- [[wiki/cloud-infra/cloud-cost-optimization|Cloud Cost Optimization]]
- [[wiki/cloud-infra/resource-tagging|Resource Tagging]]
- [[wiki/cloud-infra/budget-alerts|Budget Alerts]]
- [[wiki/cloud-infra/multi-cloud-strategy|Multi-Cloud Strategy]]
- [[wiki/concepts/promotion-readiness|Promotion Readiness]]
- [[wiki/dev-tools/global-link-check|Global Link Check]]
- [[wiki/concepts/decision-guides|Decision Guides]]
