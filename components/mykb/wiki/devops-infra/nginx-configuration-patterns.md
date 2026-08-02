---
type: "concept"
title: "NGINX Configuration Patterns"
description: "Server blocks, locations, upstreams, and proxy directives done right"
tags: ["nginx", "proxy", "configuration", "web"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# NGINX Configuration Patterns

## Summary
Server blocks, locations, upstreams, and proxy directives done right. This stub frames the concept and its place in the mykb Systems & Infrastructure cluster; expand it into a full article with worked examples, failure modes, and verified sources.

## Details
- Definition anchor: Server blocks, locations, upstreams, and proxy directives done right.
- Open questions: how this interacts with adjacent delivery, reliability, and Kubernetes operations topics, the failure modes that matter, and the operational tradeoffs to document.
- Ties to RSIS3/mykb: keeping this node discoverable makes it easier to surface from related protocols and tooling during retrieval.
- Next step: verify sources and promote to a growing article with protocol or configuration detail.

## Related
- [[wiki/cloud-infra/serverless-computing-patterns|Serverless Computing Patterns]] — related coverage in the same cluster
- [[wiki/devops-infra/configuration-management-revisited|Configuration Management]] — related coverage in the same cluster
- [[wiki/devops-infra/haproxy-vs-nginx|HAProxy vs NGINX]] — related coverage in the same cluster
- [[wiki/devops-infra/api-mesh-patterns|API Mesh Patterns]] — related coverage in the same cluster
- [[wiki/syntheses/knowledge-acquisition-workflow|Knowledge Acquisition Workflow]] — how stubs grow into full articles in mykb
- [[wiki/syntheses/mykb-acquisition-curation-and-practices|Acquisition, Curation & Practices]] — the curation loop this stub belongs to
