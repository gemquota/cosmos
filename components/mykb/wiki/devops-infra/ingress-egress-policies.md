---
type: "concept"
title: "Ingress & Egress Policies"
description: "Directional traffic rules at gateways, firewalls, and service boundaries"
tags: ["ingress", "egress", "policy", "networking"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Ingress & Egress Policies

## Summary
Ingress and egress policies control what traffic may enter and leave a workload or network: Kubernetes NetworkPolicy, cloud security groups, and firewall rules define allowed sources, destinations, and ports. The policies are the difference between a flat, blast-radius-everywhere network and one where a compromise in one pod cannot reach the rest.

## Details
- Mechanism: Kubernetes NetworkPolicy is namespace- and pod-scoped, selecting pods by label and declaring ingress (from peers) and egress (to peers) rules with ports; cloud security groups attach to instances or VPC endpoints; service-mesh policies (AuthorizationPolicy) add L7 rules; default behavior matters — no policy means allow-all.
- Concrete example: a NetworkPolicy allowing only the frontend pods to reach the API pods on 8080, and only the API to reach the database; an egress rule permitting the API to call only the payment service; a default-deny policy in each namespace that whitelists required paths.
- Failure modes: a default-deny rollout breaking services whose flows were never enumerated (map flows first with observability); rules that are too broad (allow-all from a namespace) recreating the flat network; policy bloat — hundreds of overlapping rules that are unmaintainable and unverifiable; egress gaps that block legitimate traffic (package repos, monitoring), causing hard-to-debug outages.
- Tradeoffs: strict policies shrink blast radius and satisfy compliance but cost ongoing flow-mapping and debugging effort; allow-all is operationally cheapest and worst for security; the practical path is default-deny with explicit, reviewed exceptions plus network-flow monitoring to catch what breaks.
- Operational notes: test policy changes in staging, generate policies from observed flows, and keep a review process for new rules.
- RSIS3 relevance: if cosmos services run on Kubernetes, ingress-egress policies bound what a compromised wiki daemon could reach — and RSIS3's own loops should have explicit allowed paths between components.

## Related
- [[wiki/infrastructure/egress-and-ingress-filters|Egress & Ingress Filters]]
- [[wiki/devops-infra/ingress-controllers|Ingress Controllers]]
- [[wiki/devops-infra/network-policies-kubernetes|Kubernetes Network Policies]]
- [[wiki/infrastructure/egress-proxies-and-filters|Egress Proxies & Filters]]
- [[wiki/syntheses/knowledge-acquisition-workflow|Knowledge Acquisition Workflow]] — how stubs grow into full articles in mykb
- [[wiki/syntheses/mykb-acquisition-curation-and-practices|Acquisition, Curation & Practices]] — the curation loop this stub belongs to
