---
type: "concept"
title: "Identity-Aware Proxies"
description: "Google IAP-style gateways that authorize by identity, not network"
tags: ["iap", "proxy", "identity", "access"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Identity-Aware Proxies

## Summary
Identity-aware proxies (IAPs) put authentication and authorization in front of applications at the network edge: the proxy verifies identity (OIDC, SSO, mTLS) and applies access policy before any request reaches the app, so internal tools and APIs are reachable only by authorized users without exposing VPN or complex per-app auth.

## Details
- Mechanism: the IAP terminates the session — a user authenticates with the IdP (Google Workspace, Okta, Entra ID, GitHub), the proxy issues a short-lived session, and each request is checked against policy (group membership, IP allowlists, context); the upstream app receives identity headers (email, groups) and can trust them because only the proxy can set them.
- Concrete example: Google Cloud IAP in front of an internal dashboard — users sign in with their corporate account, only members of the ops group can access, and the app reads the verified email header; Cloudflare Access or Pomerium apply the same pattern to arbitrary origins; BeyondCorp-style zero trust replaces the VPN.
- Failure modes: trusting identity headers from direct access — if the app is reachable past the proxy, attackers can forge `X-User-Email`; session expiry surprises killing long-running requests; policy that is permissive by default (any authenticated user when only a subset should pass); proxy outages becoming a single point of failure for all protected apps; browser cookie and CORS misconfigurations leaking sessions.
- Tradeoffs: IAPs centralize auth and remove per-app login logic, but they add a hop, an external dependency on the IdP, and a trust boundary that must be airtight; the alternative — per-app auth — is more flexible but multiplies implementation and audit surface.
- Operational notes: enforce that upstream apps reject identity headers when not behind the proxy, keep policies in code, and monitor proxy availability.
- RSIS3 relevance: the wiki daemon and dashboard are exactly the internal tools an IAP protects — SSO-gated access with verified identity headers beats homegrown auth for a personal knowledge base.

## Related
- [[wiki/devops-infra/reverse-proxies|Reverse Proxies]]
- [[wiki/devops-infra/workload-identity-federation|Workload Identity Federation]]
- [[wiki/devops-infra/zero-trust-access-proxies|Zero Trust Access Proxies]]
- [[wiki/shell-environment/categories/web-dev/subcategories/css-html/identity-distribution|Identity Distribution]]
- [[wiki/devops-infra/kubernetes-control-plane|Kubernetes Control Plane]]
- [[wiki/syntheses/knowledge-acquisition-workflow|Knowledge Acquisition Workflow]] — how stubs grow into full articles in mykb
- [[wiki/syntheses/mykb-acquisition-curation-and-practices|Acquisition, Curation & Practices]] — the curation loop this stub belongs to
