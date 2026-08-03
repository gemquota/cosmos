---
type: "concept"
title: "Demand Forecasting"
description: "Predicting future traffic and resource demand using history, seasonality, and business signals"
tags: ["forecasting", "capacity", "autoscaling", "data"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://docs.aws.amazon.com/forecast/latest/dg/what-is-forecast.html", "https://en.wikipedia.org/wiki/Forecasting"]
---

# Demand Forecasting

## Summary
Demand forecasting projects future load from historical trends, seasonality, and scheduled events. Good forecasts make capacity planning proactive instead of reactive and tune predictive autoscaling.

## Details
- Time-series methods (moving averages, seasonality decomposition, ML models) handle daily and weekly cycles.
- Business calendars matter more than statistics: launches, campaigns, and batch windows move demand.
- Forecasts feed capacity planning and predictive scaling policies, with error bars that set the safety margin.
- Open question: how to forecast demand for agentic workloads, which are bursty and self-generated.
- Demand forecasting estimates future resource or workload demand from historical patterns, seasonality, and leading indicators.
- It is the input to capacity planning: a forecast with uncertainty bounds drives buffer sizing and scaling policy.
- Forecast quality decays with horizon and changes in the underlying drivers, so forecasts need re-evaluation cadence.
- Methods range from naive baselines to statistical models and machine learning; the baseline comparison matters more than the algorithm.
- **Worked example / comparison** — Worked example — the wiki's monthly export traffic would be forecast from twelve months of history with a weekly seasonality; the 90th-percentile bound would size the autoscaling pool.
- For mykb, demand-forecasting is documented as the quantitative foundation under capacity-planning.

## Related
- [[wiki/cloud-infra/autoscaling|Autoscaling]]
- [[wiki/cloud-infra/capacity-planning|Capacity Planning]]
- [[wiki/devops-infra/error-budgets|Error Budgets]]
- [[wiki/devops-infra/observability|Observability]]
- [[wiki/concepts/promotion-readiness|Promotion Readiness]]
- [[wiki/ai-ml/article-health-scores|Article Health Scores]]
- [[wiki/concepts/decision-guides|Decision Guides]]
