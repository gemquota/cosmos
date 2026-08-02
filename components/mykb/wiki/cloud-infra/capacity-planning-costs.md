---
type: "concept"
title: "Capacity Planning & Costs"
description: "Right-sizing and forecasting to control cloud spend"
tags: ["capacity", "planning", "cost", "cloud"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: [
  "https://docs.aws.amazon.com/cost-management/latest/userguide/what-is-costmanagement.html",
  "https://www.finops.org/",
]
---

# Capacity Planning & Costs

## Summary
Capacity planning forecasts compute, storage, and network needs, while cost management keeps cloud spend aligned with business value. Right-sizing, utilization tracking, and commitment discounts are the main levers. Together they turn infrastructure into a controlled budget line rather than an open-ended expense.

## Details
- Forecasting starts from traffic models and per-unit resource requirements, then adds headroom and growth.
- Utilization dashboards reveal over-provisioned instances that right-sizing can reclaim.
- Committed-use discounts (reserved instances, savings plans) reduce cost for steady baseline capacity.
- FinOps practices assign cost ownership to teams and product lines.
- Autoscaling plus spot capacity covers variable demand cheaply.
- In mykb, capacity planning connects to autoscaling, spot instances, and cost-of-bandwidth articles.
- Capacity reviews should happen on a regular cadence tied to product roadmaps and traffic forecasts.
- Unit economics, such as cost per request or per active user, make cloud spend comparable across teams.
- Provider consoles and CLI workflows differ, so the provider-specific articles in this cluster record the concrete steps and gotchas.

## Related
- [[wiki/cloud-infra/dns-over-https|DNS over HTTPS]]
- [[wiki/cloud-infra/anycast-routing|Anycast Routing]]
- [[wiki/cloud-infra/capacity-planning|Capacity Planning]]
- [[wiki/cloud-infra/reserved-capacity|Reserved Capacity]]
