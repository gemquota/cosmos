---
type: "concept"
title: "Kubernetes Networking Models"
description: "How pods, services, and ingress connect in a cluster"
tags: ["kubernetes", "networking", "cni", "services"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: [
  "https://kubernetes.io/docs/concepts/services-networking/",
  "https://kubernetes.io/docs/concepts/cluster-administration/networking/",
]
---

# Kubernetes Networking Models

## Summary
Kubernetes networking defines four requirements: pods can talk to all other pods without NAT, nodes to pods, and pods to services. The CNI plugin implements this model in each cluster. Understanding the model is prerequisite to debugging cluster traffic.

## Details
- Every pod gets a cluster-wide unique IP, and the network must deliver pod-to-pod traffic across nodes without NAT.
- Services provide stable virtual IPs and DNS names backed by endpoint selection.
- The official networking docs describe the model, services, ingress, and DNS.
- CNI plugins (Calico, Cilium, Flannel) implement the data path, from overlays to eBPF.
- Network policies filter pod-to-pod traffic as L3/L4 allowlist rules enforced by the CNI plugin.
- In mykb, networking models connect to CNI plugins, network policies, service mesh, and ingress controllers.
- Operationally, alerting thresholds and runbook steps for this concept belong in the SLO, incident, and runbook articles of this cluster.
- Pipelines and GitOps practices in the delivery articles show how this concept is deployed and promoted safely.

## Related
- [[wiki/cloud-infra/multicast-networking|Multicast Networking]]
- [[wiki/infrastructure/software-defined-networking|Software-Defined Networking]]
- [[wiki/cloud-infra/vpc-networking|VPC Networking]]
- [[wiki/devops-infra/kubernetes|Kubernetes]]
