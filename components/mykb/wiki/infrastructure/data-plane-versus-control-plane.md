---
type: "concept"
title: "Data Plane vs Control Plane"
description: "Separating packet forwarding from routing and policy decisions"
tags: ["control-plane", "data-plane", "networking", "architecture"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Data Plane vs Control Plane

## Summary
The data plane and control plane split is the organizing principle of networked systems: the data plane handles the fast, repetitive, per-packet (or per-request) work, while the control plane handles the slow, decision-making work of configuring the data plane. In networking, the data plane forwards packets at line rate and the control plane runs routing protocols and programs the forwarding tables; the same split reappears in Kubernetes, service meshes, and SDN.

## Details
- In a switch or router, the data plane is the hardware path every packet traverses — parse, lookup, edit, queue, transmit — executing against tables that are already programmed. The control plane is where the intelligence lives: routing protocols (OSPF, BGP) exchange topology information, compute routes, and write the forwarding tables that the data plane reads. The separation is what makes both halves good at their jobs: the data plane is optimized to do one thing at extreme speed with no thinking, and the control plane can afford to think slowly because it is not in the per-packet path.
- The same architecture organizes software systems. Kubernetes: the control plane (API server, scheduler, controllers) reconciles desired state, while the kubelets on nodes (the data-plane-ish layer) execute pod operations; the design's resilience comes from the control plane being replaceable without interrupting the workloads. Service meshes: the control plane (Istiod, Envoy xDS) computes routing and policy, and the sidecar data plane (Envoy) executes it per request. SDN: a centralized controller (control plane) programs OpenFlow/P4 switches (data plane) — the split made explicit as an architecture.
- The design rules: the data plane must be fast, deterministic, and resilient to control-plane outages — it should keep forwarding on its last-known tables even if the controller dies (the control plane failing should degrade configuration, not forwarding). The control plane must be consistent and auditable, because its decisions propagate to every data-plane element.
- Failure modes: control-plane overload (routing flaps or controller churn overwhelm the control plane, and the data plane runs on stale state), data-plane bugs (a forwarding bug is invisible to control-plane monitoring), and coupling violations (a control-plane feature leaking into the per-packet path destroys the performance budget).
- For mykb: the split is the lens for the whole SDN and networking cluster — flow tables, OpenFlow pipelines, and VXLAN all inherit this architecture, and it also generalizes to the RSIS3 loops (the check-practices verifier is the control plane; the pass execution is the data plane).

## Related
- [[wiki/devops-infra/kubernetes-control-plane|Kubernetes Control Plane]] — related coverage in the same cluster
- [[wiki/os-shell/job-control-and-background-tasks|Job Control & Background Tasks]] — related coverage in the same cluster
- [[wiki/devops-infra/envoy-data-plane|Envoy Data Plane]] — related coverage in the same cluster
- [[wiki/cloud-infra/congestion-control-algorithms|Congestion Control Algorithms]] — related coverage in the same cluster
- [[wiki/syntheses/knowledge-acquisition-workflow|Knowledge Acquisition Workflow]] — how stubs grow into full articles in mykb
- [[wiki/syntheses/mykb-acquisition-curation-and-practices|Acquisition, Curation & Practices]] — the curation loop this stub belongs to
