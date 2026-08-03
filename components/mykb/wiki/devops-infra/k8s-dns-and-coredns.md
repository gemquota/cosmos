---
type: "concept"
title: "Kubernetes DNS & CoreDNS"
description: "Cluster DNS resolution, headless services, and CoreDNS plugins"
tags: ["kubernetes", "dns", "coredns", "service-discovery"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Kubernetes DNS & CoreDNS

## Summary
DNS in Kubernetes maps service names to cluster IPs: CoreDNS runs as the cluster DNS server, serving Service records, pod records, and external lookups, with search domains and resolv.conf rewriting handled by kubelet. It is the quiet foundation that every pod-to-pod and pod-to-service connection depends on.

## Details
- Mechanism: kubelet writes `/etc/resolv.conf` with the CoreDNS ClusterIP and search domains (`<ns>.svc.cluster.local svc.cluster.local cluster.local`); CoreDNS resolves `svc` records (A and SRV), pod names, and forwards external queries upstream; `ndots:5` makes short names try the search domains first, causing NXDOMAIN amplification for external lookups.
- Concrete example: a pod resolving `api.default.svc.cluster.local` gets the Service's cluster IP; with headless services, DNS returns the pod IPs; with `externalName`, DNS aliases an external host; CoreDNS plugin chains (cache, errors, forward, rewrite) shape behavior per cluster.
- Failure modes: the classic `ndots` problem — short hostnames generate many extra upstream queries, multiplying DNS latency (lower ndots or use FQDNs); CoreDNS being scaled to zero or restarted during a DNS outage causes cluster-wide resolution failures; search-domain typos resolving to wrong namespaces; cache TTLs serving stale endpoints after a service deletion; upstream DNS failures cascading to all pods.
- Tradeoffs: the cluster DNS server centralizes resolution and enables service discovery but is a single point of failure — run multiple replicas with anti-affinity; node-local DNS caches reduce latency and upstream load at the cost of another moving part; DNS-based discovery is simple but eventually consistent, unlike an API-based registry.
- Operational notes: monitor CoreDNS latency and error rates, test resolution paths in CI, and keep upstream resolvers redundant.
- Debugging: resolve from inside the pod, then query the cluster DNS server directly; enable CoreDNS `errors` and `log` plugins under investigation to isolate the failing link.
- RSIS3 relevance: if cosmos services resolve each other by DNS, a CoreDNS hiccup explains "the daemon is unreachable" failures — RSIS3's monitoring should distinguish DNS failures from service failures.

## Related
- [[wiki/cloud-infra/dns-resolution-process|DNS Resolution Process]]
- [[wiki/cloud-infra/dns-over-https|DNS over HTTPS]]
- [[wiki/cloud-infra/dns-zone-transfers|DNS Zone Transfers]]
- [[wiki/cloud-infra/dns-management|DNS Management]]
- [[wiki/devops-infra/kubernetes-control-plane|Kubernetes Control Plane]]
