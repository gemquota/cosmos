---
type: "concept"
title: "Zero Trust Networking"
description: "Never trust network location; authenticate and authorize every request"
tags: ["zero-trust", "security", "networking", "identity"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Zero Trust Networking

## Summary
Zero-trust networking is the model where no network is trusted by default: every request is authenticated, authorized, and encrypted, whether it crosses the public internet or stays inside the data center. "Revisited" reflects its maturity — from a buzzword to a concrete stack of identity-aware proxies, mTLS service meshes, and device posture checks.

## Details
- Mechanism: identity and policy replace network location as the trust basis; north-south access goes through identity-aware proxies, east-west traffic gets mTLS from service meshes or network overlays (Tailscale, Cilium), and every decision is logged; network segments and firewalls become defense-in-depth, not the boundary.
- Concrete example: an internal app reachable only through an access proxy that checks SSO and device posture; service-to-service calls encrypted and authenticated via mTLS in the mesh; a remote worker reaching the service through an overlay network with per-identity policy — no VPN, no full-network access.
- Failure modes: partial adoption — some services exempted from mTLS, creating trusted paths attackers find; identity sprawl where service accounts and human identities are not distinct, weakening audit; performance overhead from per-request checks and encryption; policy complexity that makes teams default to allow-all; legacy systems that cannot participate, becoming the weak link.
- Tradeoffs: zero trust shrinks the blast radius of any compromise to the authenticated identities involved, but it is operationally heavier than perimeter security — identity infrastructure, certificate rotation, policy management; the alternative, network trust, is simpler and catastrophically flat once breached; adoption is a journey: access proxies first, then mTLS for internal traffic.
- Operational notes: adopt incrementally, audit identity decisions, keep certificates rotating, and test what happens when the identity provider fails.
- RSIS3 relevance: the cosmos deployment (dashboard, daemon, wiki) benefits from zero-trust principles — every access authenticated and scoped, internal calls mTLS-verified — matching RSIS3's own guardrail philosophy.

## Related
- [[wiki/cloud-infra/networking-fundamentals|Networking Fundamentals]]
- [[wiki/infrastructure/vlan-networking|VLAN Networking]]
- [[wiki/devops-infra/zero-trust-access-proxies|Zero Trust Access Proxies]]
- [[wiki/cloud-infra/multicast-networking|Multicast Networking]]
- [[wiki/syntheses/knowledge-acquisition-workflow|Knowledge Acquisition Workflow]] — how stubs grow into full articles in mykb
- [[wiki/syntheses/mykb-acquisition-curation-and-practices|Acquisition, Curation & Practices]] — the curation loop this stub belongs to
