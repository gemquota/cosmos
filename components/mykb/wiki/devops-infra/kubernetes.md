---
type: "concept"
title: "Kubernetes"
description: "Portable container-orchestration platform for deploying, scaling, and managing containerized workloads"
tags: ["kubernetes", "containers", "orchestration", "devops", "cloud"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Kubernetes

## Summary
Kubernetes (K8s) automates deployment, scaling, and operations of containerized applications across clusters of nodes. Pods, Deployments, Services, and Ingress form the core object model.

## Details
- Control plane (API server, scheduler, controller manager) manages worker nodes running kubelet and container runtimes.
- Probes, resource limits, and horizontal autoscaling give strong reliability primitives.
- Add-ons: Helm for packaging, Istio for the mesh, admission policies for security.

## Related
- [[wiki/devops-infra/helm|Helm]] — package manager for K8s charts
- [[wiki/devops-infra/istio|Istio]] — service mesh on K8s
- [[wiki/api-protocols/readiness-probes|Readiness Probes]] — pod traffic gating
- [[wiki/api-protocols/liveness-probes|Liveness Probes]] — pod restarts
- [[wiki/security/container-hardening|Container Hardening]] — image and runtime security
- [[wiki/devops-infra/terraform|Terraform]] — provision clusters as code
