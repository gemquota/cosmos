---
type: "concept"
title: "Ingress Controllers"
description: "The layer that routes external traffic into Kubernetes"
tags: ["ingress", "kubernetes", "routing", "proxy"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: [
  "https://kubernetes.io/docs/concepts/services-networking/ingress/",
  "https://kubernetes.github.io/ingress-nginx/",
]
---

# Ingress Controllers

## Summary
Ingress controllers route external HTTP traffic into Kubernetes clusters according to Ingress resources. They are the cluster's reverse proxy layer, combining routing rules with TLS termination. The Ingress API is the standard north-south entry point.

## Details
- An Ingress resource declares host/path routing rules, TLS hosts, and default backends.
- The controller watches Ingress objects and programs a proxy (NGINX, Envoy, Traefik) to match.
- NGINX Ingress Controller is the most widely deployed implementation and the reference point for annotations.
- TLS certificates, annotations, and rewrite rules vary by controller, which is the main portability cost.
- Gateway API is the successor abstraction, splitting routing into Gateway, GatewayClass, and HTTPRoute resources.
- In mykb, ingress controllers connect to reverse proxies, load balancing, and service mesh.
- Operationally, alerting thresholds and runbook steps for this concept belong in the SLO, incident, and runbook articles of this cluster.
- Pipelines and GitOps practices in the delivery articles show how this concept is deployed and promoted safely.

## Related
- [[wiki/devops-infra/ingress-egress-policies|Ingress & Egress Policies]]
- [[wiki/devops-infra/admission-controllers-and-webhooks|Admission Controllers & Webhooks]]
- [[wiki/devops-infra/acid|ACID]]
- [[wiki/devops-infra/alert-fatigue|Alert Fatigue]]
