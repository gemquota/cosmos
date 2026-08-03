---
type: "concept"
title: "Pod-to-Pod Communication"
description: "Routing between pods across nodes with overlays and routing tables"
tags: ["kubernetes", "networking", "pods", "overlay"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Pod-to-Pod Communication

## Summary
Pod-to-pod communication in Kubernetes flows through the cluster network: pods get their own IPs, and the CNI provides connectivity across nodes — via overlays, direct routing, or cloud VPC integration. Services, DNS, and NetworkPolicy layer on top for stable names, discovery, and segmentation.

## Details
- Mechanism: each pod receives an IP from the CNI (IPAM); the CNI sets up routing (veth pairs, overlays like VXLAN, or native routes) so any pod can reach any other pod's IP regardless of node; Services provide stable virtual IPs with DNS names; kube-proxy or eBPF load-balances Service traffic to pod endpoints; NetworkPolicy filters between pods.
- Concrete example: pod A calls pod B by Service DNS (`b.svc.cluster.local:8080`); the request hits the Service ClusterIP, is forwarded to a backend pod, and the CNI routes it across the node boundary; with Cilium, eBPF performs the load balancing and policy enforcement in the kernel path.
- Failure modes: CNI outages killing all cross-node traffic; IPAM exhaustion or duplicate IPs breaking routing; kube-proxy/iptables scale limits with thousands of Services; Service endpoints going stale after pod deletion; MTU mismatches fragmenting packets on overlays; NetworkPolicy accidentally blocking the very communication it was meant to segment.
- Tradeoffs: the cluster network abstracts away node topology — a huge operational win — but adds layers (CNI, Service proxy) whose failures are hard to diagnose; direct pod IPs are fast but unstable (pods churn), so Services and DNS are the norm; the tradeoff is simplicity of use versus the complexity of the network stack underneath.
- Operational notes: monitor CNI health, Service endpoint counts, and connection errors; test cross-node connectivity in staging; keep NetworkPolicy rules reviewed.
- RSIS3 relevance: when RSIS3's loops call each other across pods, understanding the network path (CNI, Service, policy) explains intermittent failures that application logs miss.

## Related
- [[wiki/devops-infra/pod-disruption-budgets|Pod Disruption Budgets]] — related coverage in the same cluster
- [[wiki/infrastructure/pod-lifecycle|Pod Lifecycle]] — related coverage in the same cluster
- [[wiki/devops-infra/kubernetes-control-plane|Kubernetes Control Plane]] — related coverage in the same cluster
- [[wiki/devops-infra/observability-pillars|Observability Pillars]] — related coverage in the same cluster
- [[wiki/syntheses/knowledge-acquisition-workflow|Knowledge Acquisition Workflow]] — how stubs grow into full articles in mykb
- [[wiki/syntheses/mykb-acquisition-curation-and-practices|Acquisition, Curation & Practices]] — the curation loop this stub belongs to
