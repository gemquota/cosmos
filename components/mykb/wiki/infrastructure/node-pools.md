---
type: "concept"
title: "Node Pools"
description: "Groups of cluster nodes with distinct machine types, scaling, and taints for workload segregation"
tags: ["kubernetes", "nodes", "clusters", "scaling"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
---

# Node Pools

## Summary
Node pools group nodes by machine type, labels, and autoscaling policy so different workloads get the right resources. They are how clusters mix general, GPU, spot, and system nodes.

## Details
- Pools map to instance families or spot vs on-demand; taints keep pools exclusive to matching workloads.
- Cluster autoscaler scales each pool independently, so pool sizing is a cost lever.
- System pools (ingress, monitoring) should be separated from workload pools.
- Open question: how many pools is the right number before management overhead outweighs isolation.

## Related
- [[wiki/cloud-infra/autoscaling|Autoscaling]] — pool scaling policies
- [[wiki/infrastructure/container-scheduling|Container Scheduling]] — placement across pools
- [[wiki/infrastructure/pod-lifecycle|Pod Lifecycle]] — pods bound to pool taints
- [[wiki/devops-infra/kubernetes|Kubernetes]] — the cluster pools belong to
