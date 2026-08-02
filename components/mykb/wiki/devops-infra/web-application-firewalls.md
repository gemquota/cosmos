---
type: "concept"
title: "Web Application Firewalls"
description: "Filtering HTTP traffic for injection and exploit patterns"
tags: ["waf", "security", "http", "filtering"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: [
  "https://owasp.org/www-community/Web_Application_Firewall",
  "https://en.wikipedia.org/wiki/Web_application_firewall",
]
---

# Web Application Firewalls

## Summary
A web application firewall inspects HTTP traffic for attacks that network firewalls miss. It filters injection, cross-site scripting, and bot traffic using signatures and rules. WAFs are a compensating control when application hardening is incomplete.

## Details
- WAFs operate at layer 7, understanding URLs, headers, and bodies rather than IP addresses and ports.
- OWASP maintains guidance and rule sets for the most common web attack classes, including SQLi and XSS.
- Managed WAFs (Cloudflare, AWS WAF) update rule sets continuously and integrate with DDoS protection.
- False positives are the operational cost: rules must be tuned against real application traffic.
- Placement matters: the WAF usually sits at the edge or in front of the origin, inline or in detection mode.
- In this cluster, WAF content connects to egress/ingress filtering, reverse proxies, and API gateway security.
- Operationally, alerting thresholds and runbook steps for this concept belong in the SLO, incident, and runbook articles of this cluster.

## Related
- [[wiki/devops-infra/stateful-application-patterns|Stateful Application Patterns]]
- [[wiki/devops-infra/envoy-data-plane|Envoy Data Plane]]
- [[wiki/os-shell/firewalls-and-netfilter|Firewalls & netfilter]]
- [[wiki/devops-infra/acid|ACID]]
