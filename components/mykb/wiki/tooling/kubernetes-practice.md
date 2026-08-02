---
type: "concept"
title: "Kubernetes Practice"
description: "Running containerized workloads with orchestration: scheduling, scaling, and healing"
tags: ["kubernetes", "orchestration", "containers", "practice"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://kubernetes.io/docs/concepts/overview/", "https://en.wikipedia.org/wiki/Kubernetes"]
---

# Kubernetes Practice

## Summary
Kubernetes orchestrates containers: it schedules workloads, restarts failures, scales replicas, and routes traffic. Practice means treating the API as the interface — declarative manifests, health probes, resource requests, and GitOps as the delivery model.

## Details
- Declarative desired state: you write what should exist (Deployments, Services), and the control plane converges to it.
- Health probes (liveness, readiness) are how the scheduler knows what healthy means; misconfigured probes cause outages.
- Resource requests and limits are admission contracts: requests schedule, limits constrain, and neither can be skipped safely.
- Rollouts (rolling, canary, blue-green) replace manual deploys; GitOps (Argo CD, Flux) makes git the source of truth.
- Operational surface is real: nodes, networking, storage, upgrades, and security policies all need ownership.
- For the mykb bundle, Kubernetes is optional: the wiki pipeline runs as containers on any schedule; K8s adds orchestration when scale demands.
- Worked example — the wiki sync Deployment declares 2 replicas, readiness probes on the health endpoint, and a canary rollout that promotes on metric health.

Worked example — the wiki sync Deployment declares 2 replicas, readiness probes on the health endpoint, and a canary rollout that promotes on metric health.

## Related
- [[wiki/tooling/containerization-practice|Containerization Practice]]
- [[wiki/devops-infra/kubernetes|Kubernetes]]
- [[wiki/devops-infra/gitops-argocd|GitOps and Argo CD]]
- [[wiki/tooling/cloud-native-principles|Cloud Native Principles]]
- [[wiki/tooling/automated-canary|Automated Canary]]
- [[wiki/devops-infra/kubernetes-control-plane|Kubernetes Control Plane]]
- [[wiki/tooling/smoke-tests|Smoke Tests]]
