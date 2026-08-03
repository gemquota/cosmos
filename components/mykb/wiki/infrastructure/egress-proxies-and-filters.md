---
type: "concept"
title: "Egress Proxies & Filters"
description: "Controlling outbound traffic with proxies, filters, and NAT"
tags: ["e2gress", "proxy", "firewall", "security"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Egress Proxies & Filters

## Summary
Egress control manages the traffic leaving your network: which hosts may reach which destinations, through what path, and with what inspection. Ingress control (what comes in) gets most of the attention, but egress control is where data exfiltration, malware callbacks, and accidental data leaks actually happen — a compromised or misconfigured host sending data out is only stoppable if outbound traffic is governed.

## Details
- The threat model: outbound traffic is the channel for the most damaging failures. A compromised host exfiltrates data (the attacker's payload leaves through the same path as legitimate traffic); malware phones home to a command server; an application bug or misconfiguration ships internal data to an external service (an analytics SDK receiving PII, a log forwarder pointed at the wrong endpoint); and DNS alone is a surprisingly capable exfiltration channel (data encoded in DNS queries to attacker-controlled nameservers). None of these are visible if egress is unrestricted.
- The mechanisms: egress proxies (a forward proxy that all outbound HTTP(S) traverses, enabling inspection, allow-listing, and logging), explicit allow-lists (egress firewall rules that default-deny: only approved destinations and ports), DNS filtering (blocking known-bad domains at resolution time), and NAT (which hides internal topology but is not a control — NAT alone blocks nothing). The modern pattern for cloud: egress through a managed gateway/NAT with a proxy layer, or zero-egress designs where workloads cannot reach the internet at all and only approved integrations (via a service gateway) can.
- The design tension: security versus operability. Aggressive egress allow-lists break the modern workflow — software updates, package downloads, SaaS integrations, and external APIs all need outbound access, and each new integration requires a policy change. The practical design: default-deny for the unknown, allow-listed by service identity and destination, with TLS inspection at the proxy for visibility (which requires the proxy to terminate/re-encrypt — itself a trust decision), and logging that captures the metadata (who, to where, how much, how often) needed to detect exfiltration patterns.
- Failure modes: allow-lists that are actually allow-everything (wildcard rules, "temporary" broad exceptions), egress proxies that become a single point of failure (a proxy outage takes down all outbound traffic — the reason proxies need redundancy), and inspection gaps (TLS-encrypted traffic bypassing inspection when the proxy is not in the path).
- For mykb: the node connects the egress cluster — egress/ingress filters, reverse proxies, and ingress/egress policies — and the same "default-deny with reviewed exceptions" discipline applies to the RSIS3 bundle's own outbound calls (which endpoints may its workers contact?).

## Related
- [[wiki/infrastructure/egress-and-ingress-filters|Egress & Ingress Filters]]
- [[wiki/devops-infra/reverse-proxies|Reverse Proxies]]
- [[wiki/infrastructure/tcpdump-filters-and-capture|tcpdump Filters & Capture]]
- [[wiki/devops-infra/ingress-egress-policies|Ingress & Egress Policies]]
- [[wiki/syntheses/knowledge-acquisition-workflow|Knowledge Acquisition Workflow]] — how stubs grow into full articles in mykb
- [[wiki/syntheses/mykb-acquisition-curation-and-practices|Acquisition, Curation & Practices]] — the curation loop this stub belongs to
