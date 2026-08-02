---
type: "concept"
title: "Capacity Planning"
description: "Forecasting resource demand and sizing infrastructure to meet it within budget and risk tolerance"
tags: ["capacity", "planning", "scaling", "finops"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/Capacity_planning", "https://docs.aws.amazon.com/whitepapers/latest/cost-optimization-laying-the-foundation/capacity-planning.html"]
---

# Capacity Planning

## Summary
Capacity planning matches infrastructure supply to predicted demand — enough headroom for peaks, not so much that money idles. It is the strategic counterpart to autoscaling's tactical adjustments.

## Details
- Inputs: traffic trends, seasonality, launch schedules, and SLO targets; outputs: min/max fleet sizes and budgets.
- Headroom policy balances cost against risk: tight headroom saves money, loose headroom absorbs spikes.
- Autoscaling handles short-term variance; capacity planning sets the envelope it operates within.
- Open questions: how to model AI workloads, whose demand curves are bursty and hard to forecast.
- Capacity planning predicts the compute, storage, and network resources a workload needs, matching supply to demand without waste or shortfall.
- It combines demand forecasting with utilization data, buffer sizing, and scaling strategy — horizontal, vertical, or serverless.
- Over-provisioning wastes money; under-provisioning causes outages; the art is sizing buffers to the demand forecast's uncertainty.
- Modern cloud practice shifts from up-front sizing toward autoscaling and on-demand models, making planning about policies rather than purchases.
- **Worked example / comparison** — Worked example — a wiki export service sees peak demand at month-end; planning adds 30% headroom above the forecast and configures autoscaling for the residual variance.
- For mykb, capacity planning is documented as the demand-side counterpart to demand-forecasting and finops-practices.

## Related
- [[wiki/cloud-infra/autoscaling|Autoscaling]]
- [[wiki/cloud-infra/demand-forecasting|Demand Forecasting]]
- [[wiki/cloud-infra/right-sizing|Right-Sizing]]
- [[wiki/concepts/promotion-readiness|Promotion Readiness]]
- [[wiki/ai-ml/article-health-scores|Article Health Scores]]
- [[wiki/concepts/decision-guides|Decision Guides]]
