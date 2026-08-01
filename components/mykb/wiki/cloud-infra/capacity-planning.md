---
type: "concept"
title: "Capacity Planning"
description: "Forecasting resource demand and sizing infrastructure to meet it within budget and risk tolerance"
tags: ["capacity", "planning", "scaling", "finops"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
---

# Capacity Planning

## Summary
Capacity planning matches infrastructure supply to predicted demand — enough headroom for peaks, not so much that money idles. It is the strategic counterpart to autoscaling's tactical adjustments.

## Details
- Inputs: traffic trends, seasonality, launch schedules, and SLO targets; outputs: min/max fleet sizes and budgets.
- Headroom policy balances cost against risk: tight headroom saves money, loose headroom absorbs spikes.
- Autoscaling handles short-term variance; capacity planning sets the envelope it operates within.
- Open questions: how to model AI workloads, whose demand curves are bursty and hard to forecast.

## Related
- [[wiki/cloud-infra/autoscaling|Autoscaling]] — the tactical scaling loop
- [[wiki/cloud-infra/demand-forecasting|Demand Forecasting]] — the predictive input
- [[wiki/cloud-infra/right-sizing|Right-Sizing]] — matching resources to load
