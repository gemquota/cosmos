---
type: "concept"
title: "Site-to-Site VPN"
description: "Persistent encrypted links between offices and clouds"
tags: ["site-to-site", "vpn", "ipsec", "networking"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Site-to-Site VPN

## Summary

Site-to-site VPNs connect two networks over the internet via encrypted tunnels — cloud VPC to on-prem, branch to HQ, or VPC to VPC without peering. They are the pragmatic connectivity default, with throughput, latency, and reliability limits that dedicated links solve.

## Details
- Mechanism: a VPN gateway on each side establishes IPsec tunnels (IKEv2, AES-GCM, multiple tunnels per connection for redundancy); routing exchanges (BGP over the tunnel) advertise networks; AWS VPN is per-connection with two tunnels for HA, Azure and GCP similar; throughput is capped by gateway size (typically 1.25-10 Gbps on cloud gateways) and shares the public internet.
- Concrete example: a company connects its office to a cloud VPC with a site-to-site VPN for management traffic, keeping the datacenter link for bulk data; a hybrid deployment joins on-prem Active Directory to cloud workloads; two VPCs in different regions without peering use a VPN gateway pair.
- Failure modes: tunnel flapping on unstable ISPs; MTU issues inside tunnels (see MSS clamping); BGP misconfiguration advertising overlapping routes; single-tunnel designs (use two); and treating VPN throughput as guaranteed — it is best-effort over the internet, so latency-sensitive or bulk traffic needs dedicated connectivity.
- Operational tradeoffs: VPNs are fast to deploy and cheap vs dedicated links, but add latency, bandwidth ceilings, and internet dependence; the standard is VPN as the baseline with dedicated/private links (Direct Connect, Interconnect) for latency-critical or high-volume paths. Monitor tunnel status and failover as first-class metrics, alerting on BGP session state rather than raw interface counters.
- RSIS3/mykb relevance: the wiki's hybrid connectivity uses dual tunnels with BGP; this note records the tunnel and route policy the loop checks during network changes.
- Dual-carrier design: terminate tunnels on independent ISPs or paths where uptime matters; a single-ISP tunnel is a single point of failure wearing a VPN label. Include dead-peer detection and route-failover timers so the standby tunnel actually carries traffic.

## Related
- [[wiki/cloud-infra/vpn-technologies|VPN Technologies]]
- [[wiki/devops-infra/site-reliability-engineering-revisited|Site Reliability Engineering]]
- [[wiki/cloud-infra/vpn-split-tunneling|VPN Split Tunneling]]
- [[wiki/cloud-infra/client-vpn-profile|Client VPN Profiles]]
