---
type: "concept"
title: "API Gateways"
description: "Policy, auth, and routing control points in front of services"
tags: ["api-gateway", "api", "routing", "policies"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: [
  "https://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html",
  "https://docs.konghq.com/gateway/latest/",
]
---

# API Gateways

## Summary
An API gateway is a policy and routing control point in front of backend APIs. It centralizes authentication, rate limiting, request transformation, and observability. Gateways trade a single choke point for simplified clients and consistent policy.

## Details
- Gateways route requests by path and version to the right service, decoupling clients from internal service topology.
- Authentication and authorization at the gateway apply policy once instead of in every service.
- Rate limiting and quotas protect backends from abuse and runaway clients.
- Request and response transformation lets gateways bridge protocol and payload differences between clients and services.
- Observability is a core feature: access logs, metrics, and tracing correlation happen at the boundary.
- Cloud-native options include AWS API Gateway, Kong, and Envoy-based gateways, all covered in this cluster's devops-infra articles.
- Operationally, alerting thresholds and runbook steps for this concept belong in the SLO, incident, and runbook articles of this cluster.
- Pipelines and GitOps practices in the delivery articles show how this concept is deployed and promoted safely.

## Related
- [[wiki/devops-infra/api-mesh-patterns|API Mesh Patterns]]
- [[wiki/cloud-infra/vpc-peering-and-transit-gateways|VPC Peering & Transit Gateways]]
- [[wiki/cloud-infra/nat-gateways|NAT Gateways]]
- [[wiki/devops-infra/api-gateway-patterns|API Gateway Patterns]]
