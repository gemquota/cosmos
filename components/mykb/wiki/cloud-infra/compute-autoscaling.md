---
type: "concept"
title: "Compute Autoscaling"
description: "Adding and removing capacity in response to demand"
tags: ["autoscaling", "compute", "cloud", "capacity"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: [
  "https://docs.aws.amazon.com/autoscaling/ec2/userguide/what-is-amazon-ec2-auto-scaling.html",
  "https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/",
]
---

# Compute Autoscaling

## Summary
Autoscaling adds and removes compute capacity in response to demand, from VM fleets to Kubernetes pods. Scaling policies balance cost, latency, and stability under changing load. Autoscaling is the operational heart of elastic cloud computing and a core reliability mechanism.

## Details
- AWS EC2 Auto Scaling maintains desired capacity across groups with health checks and scaling policies.
- Kubernetes HPA scales pods on metrics such as CPU, memory, or custom application signals.
- Scaling policies such as target tracking, step, and scheduled trade responsiveness for oscillation risk.
- Cooldowns and stabilization windows prevent thrashing during load spikes.
- Right-sizing requests and instance types determines how well scaling actually works in practice.
- In mykb, autoscaling connects to spot instances, capacity planning, and Kubernetes scheduling.
- Predictive scaling uses history to provision ahead of spikes, complementing reactive policies for bursty traffic.
- Provider consoles and CLI workflows differ, so the provider-specific articles in this cluster record the concrete steps and gotchas.

## Related
- [[wiki/infrastructure/gpu-compute-infrastructure|GPU Compute Infrastructure]]
- [[wiki/cloud-infra/compute-shapes-and-skus|Compute Shapes & SKUs]]
- [[wiki/cloud-infra/autoscaling|Autoscaling]]
- [[wiki/infrastructure/on-demand-vs-reserved-compute|On Demand Vs Reserved Compute]]
