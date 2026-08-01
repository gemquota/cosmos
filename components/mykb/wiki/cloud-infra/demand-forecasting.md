---
type: "concept"
title: "Demand Forecasting"
description: "Predicting future traffic and resource demand using history, seasonality, and business signals"
tags: ["forecasting", "capacity", "autoscaling", "data"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
---

# Demand Forecasting

## Summary
Demand forecasting projects future load from historical trends, seasonality, and scheduled events. Good forecasts make capacity planning proactive instead of reactive and tune predictive autoscaling.

## Details
- Time-series methods (moving averages, seasonality decomposition, ML models) handle daily and weekly cycles.
- Business calendars matter more than statistics: launches, campaigns, and batch windows move demand.
- Forecasts feed capacity planning and predictive scaling policies, with error bars that set the safety margin.
- Open question: how to forecast demand for agentic workloads, which are bursty and self-generated.

## Related
- [[wiki/cloud-infra/autoscaling|Autoscaling]] — predictive policies consume forecasts
- [[wiki/cloud-infra/capacity-planning|Capacity Planning]] — forecasts become capacity decisions
- [[wiki/devops-infra/error-budgets|Error Budgets]] — demand surprises spend budgets
- [[wiki/devops-infra/observability|Observability]] — historical data for forecasts
