---
type: "concept"
title: "Node Pools"
description: "Groups of cluster nodes with distinct machine types, scaling, and taints for workload segregation"
tags: ["kubernetes", "nodes", "clusters", "scaling"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
---

# Node Pools

## Summary
Node pools group cluster nodes by machine type, labels, and autoscaling policy so different workloads get the right resources. They are how clusters mix general, GPU, spot, and system nodes — one cluster, several classes of compute, each with its own capacity and cost behavior.

## Details
- Pools map to instance families or spot vs on-demand; taints keep pools exclusive to matching workloads. A pool is a named group of nodes with the same machine type (general-purpose, memory-optimized, GPU), the same image, and the same autoscaling bounds. The segregation mechanism is taints: a GPU pool is tainted (say `gpu=true:NoSchedule`), and only workloads that tolerate the taint (with the matching toleration) can schedule there — so GPU pods land on GPU nodes and general pods never get evicted from them. Labels on the pool give finer control (nodeSelector/affinity), and the combination taints + labels + requests is the standard vocabulary for placement policy.
- Cluster autoscaler scales each pool independently, so pool sizing is a cost lever. When pods are pending because no node in a pool fits them, the autoscaler adds a node from that pool; when nodes are underutilized, it removes them. Because each pool scales independently, the pools define the cost structure: a spot pool scales up cheaply and can be preempted; an on-demand pool is reliable but expensive; a GPU pool's minimum size is a budget commitment (GPU nodes are costly even when idle). The failure modes: pools sized with a minimum that exceeds the workload (idle nodes burning money), autoscaler lag (a burst exceeds the pool's max-add rate — pods wait), and spot preemption storms (a spot pool evaporates and the workload has no fallback).
- System pools (ingress, monitoring) should be separated from workload pools. The practice: critical infrastructure (ingress controllers, DNS, monitoring, the cluster's own add-ons) runs in a dedicated, tainted system pool with on-demand, reliable nodes — so a spot-pool preemption or a workload autoscaling event never takes down the ingress or the monitoring that would report the problem. The tradeoff: system pools add nodes (cost) and management surface; the failure mode of not having them is the cascade — the workload burst preempts the nodes running the monitoring that would have caught it.
- Open question: how many pools is the right number before management overhead outweighs isolation — every pool adds autoscaler state, taint/toleration bookkeeping, and cost review, and the answer is workload-dependent.
- For mykb: node pools are the resource-planning layer of the Kubernetes cluster — autoscaling, scheduling, and pod lifecycle all interact with pool design.

## Related
- [[wiki/cloud-infra/autoscaling|Autoscaling]] — pool scaling policies
- [[wiki/infrastructure/container-scheduling|Container Scheduling]] — placement across pools
- [[wiki/infrastructure/pod-lifecycle|Pod Lifecycle]] — pods bound to pool taints
- [[wiki/devops-infra/kubernetes|Kubernetes]] — the cluster pools belong to
