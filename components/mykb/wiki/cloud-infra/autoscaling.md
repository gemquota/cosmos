---
type: "concept"
title: "Autoscaling"
description: "Automatically adjusting compute capacity to demand through horizontal, vertical, and predictive scaling policies"
tags: ["autoscaling", "scaling", "kubernetes", "capacity", "cloud"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/"]
---

# Autoscaling

## Summary
Autoscaling adds or removes capacity in response to demand so systems neither under-provision (outages, latency) nor over-provision (waste). Horizontal scaling changes instance or pod count, vertical scaling resizes individual instances, and predictive scaling anticipates demand curves. Kubernetes Horizontal Pod Autoscaler is the canonical implementation of the control loop.

## Details
- Horizontal Pod Autoscaling: a controller measures utilization (CPU, memory, or custom metrics) against targets and adjusts the replica count between configured min and max.
- Vertical scaling resizes CPU and memory of existing instances; it is simpler but causes restarts and has hard instance-size ceilings.
- Reactive scaling lags demand; scheduled and predictive scaling (based on traffic forecasts) pre-position capacity for known peaks like batch windows.
- Policies: target utilization, cooldown/stabilization windows, scale-down aggressiveness, and per-metric weights avoid oscillation and thrashing.
- Autoscaling only helps if the bottleneck is the scaled resource — a database or quota can cap the benefit; capacity planning still matters.
- Worked example: an HPA on a mykb API deployment with target CPU 70%, min 2 / max 10, plus a cron-driven pre-scale before the weekly pulse batch.
- Cloud autoscaling groups extend the same loop to VMs, including spot capacity, and integrate with load-balancer targets and health checks.

## Related
- [[wiki/cloud-infra/capacity-planning|Capacity Planning]] — setting min/max and budget context
- [[wiki/cloud-infra/demand-forecasting|Demand Forecasting]] — predictive input for scaling policies
- [[wiki/cloud-infra/right-sizing|Right-Sizing]] — vertical dimension of capacity fit
- [[wiki/devops-infra/kubernetes|Kubernetes]] — hosts the HPA control loop
- [[wiki/devops-infra/observability|Observability]] — metrics that drive scaling decisions
- [[wiki/api-protocols/timeouts|Timeouts]] — latency behavior under scale-up pressure
