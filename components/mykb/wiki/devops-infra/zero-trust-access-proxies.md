---
type: "concept"
title: "Zero Trust Access Proxies"
description: "Proxies that verify identity and device posture before granting app access"
tags: ["zero-trust", "proxy", "access", "security"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Zero Trust Access Proxies

## Summary
Zero-trust access proxies (Cloudflare Access, Google IAP, Pomerium, Tailscale) replace VPN-based network access with identity- and policy-based access to specific applications: every request is authenticated, authorized, and logged regardless of the client's network location. The model is per-request verification, not network trust.

## Details
- Mechanism: the proxy sits in front of applications; a user authenticates with SSO (OIDC/SAML); policy evaluates identity, group membership, device posture, and context; the proxy forwards only approved requests, injecting verified identity headers; clients never get network-level access to anything beyond what the policy allows.
- Concrete example: an internal dashboard behind Cloudflare Access — only members of the ops group with a compliant device can open it, from anywhere; Pomerium protects multiple internal apps with one identity layer; a service API requires mTLS client certificates plus SSO policy.
- Failure modes: trust boundary leaks — an app reachable by another route (public IP, load balancer) bypasses the proxy; identity headers trusted from outside the proxy (apps must reject them unless the proxy is guaranteed in front); policy misconfigurations that allow too much (any authenticated user versus the right group); proxy availability becoming a single point of failure for all protected apps.
- Tradeoffs: zero-trust access centralizes control and removes the VPN's network-wide exposure, but it adds a dependency on the identity provider and the proxy itself; the alternative, VPN, is familiar but grants network access far beyond what users need; the mature pattern is per-app access with strong identity, audited decisions, and short sessions.
- Operational notes: enforce the proxy as the only ingress, keep policies in code, monitor access decisions, and test the bypass paths.
- RSIS3 relevance: the wiki and dashboard are exactly the internal surfaces zero-trust proxies protect — identity-gated, audited access instead of a network trust boundary.

## Related
- [[wiki/devops-infra/reverse-proxies|Reverse Proxies]] — related coverage in the same cluster
- [[wiki/devops-infra/zero-trust-networking-revisited|Zero Trust Networking]] — related coverage in the same cluster
- [[wiki/cloud-infra/remote-access-methods|Remote Access Methods]] — related coverage in the same cluster
- [[wiki/infrastructure/zero-downtime-deploys|Zero-Downtime Deploys]] — related coverage in the same cluster
- [[wiki/devops-infra/kubernetes-control-plane|Kubernetes Control Plane]] — related coverage in the same cluster
- [[wiki/syntheses/knowledge-acquisition-workflow|Knowledge Acquisition Workflow]] — how stubs grow into full articles in mykb
- [[wiki/syntheses/mykb-acquisition-curation-and-practices|Acquisition, Curation & Practices]] — the curation loop this stub belongs to
