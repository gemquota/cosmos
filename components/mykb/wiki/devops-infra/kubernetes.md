---
type: "concept"
title: "Kubernetes"
description: "Portable container-orchestration platform for deploying, scaling, and managing containerized workloads"
tags: ["kubernetes", "containers", "orchestration", "devops", "cloud"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://kubernetes.io/docs/concepts/overview/", "https://kubernetes.io/docs/concepts/architecture/"]
---

# Kubernetes

## Summary
Kubernetes (K8s) automates deployment, scaling, and operations of containerized applications across clusters of nodes. Pods, Deployments, Services, and Ingress form the core object model.

## Details
- Control plane (API server, scheduler, controller manager) manages worker nodes running kubelet and container runtimes.
- Probes, resource limits, and horizontal autoscaling give strong reliability primitives.
- Add-ons: Helm for packaging, Istio for the mesh, admission policies for security.
- Kubernetes automates deployment, scaling, and operations of containerized applications across a cluster: pods are the unit, controllers reconcile desired state, and the API server is the control plane's front door.
- The core object model — Deployments, Services, Ingress, ConfigMaps, and Namespaces — turns infrastructure into declarative, reviewable manifests.
- Self-healing is the headline property: the control loop continuously compares observed state to desired state and acts on the difference.
- The cost is operational complexity: the control plane, networking, storage, and security model all have steep learning curves.
- **Worked example / comparison** — Worked example — a Deployment declares 3 replicas; when one pod crashes, the ReplicaSet controller notices the drift and schedules a replacement without human action.
- For mykb, kubernetes is documented as the orchestration capstone of the devops-infra cluster, with kubernetes-security as its security companion.

## Related
- [[wiki/devops-infra/helm|Helm]]
- [[wiki/devops-infra/istio|Istio]]
- [[wiki/api-protocols/readiness-probes|Readiness Probes]]
- [[wiki/api-protocols/liveness-probes|Liveness Probes]]
- [[wiki/security/container-hardening|Container Hardening]]
- [[wiki/devops-infra/terraform|Terraform]]
- [[wiki/concepts/promotion-readiness|Promotion Readiness]]
- [[wiki/ai-ml/article-health-scores|Article Health Scores]]
- [[wiki/concepts/deep-dives|Deep Dives]]
