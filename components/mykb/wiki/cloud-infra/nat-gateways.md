---
type: "concept"
title: "NAT Gateways"
description: "Managed network address translation that gives private resources outbound internet access without inbound exposure"
tags: ["nat", "networking", "egress", "cloud"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
---
# NAT Gateways

## Summary

NAT gateways give private instances outbound internet access while hiding their addresses: managed services (AWS NAT Gateway, Cloud NAT, Azure NAT Gateway) replace fragile NAT instances. They are simple to use and easy to under-plan — port exhaustion and cost are the usual surprises.

## Details
- Mechanism: the gateway translates private source IPs to its public IP(s), tracking sessions (source IP:port); each public IP supports ~55,000 concurrent connections per protocol; traffic passes through per-GB pricing plus hourly cost. AWS NAT gateways are per-AZ (one per AZ for resilience); GCP Cloud NAT is regional; Azure NAT Gateway attaches to subnets with explicit IP/port scaling.
- Concrete example: a private subnet's outbound API calls flow through a NAT gateway in the same AZ; an autoscaling fleet of 200 instances bursts to 60,000 concurrent connections and exhausts one gateway's ports — the fix is more public IPs or per-AZ gateways. Egress-heavy jobs (pulling images, uploading artifacts) inflate the per-GB bill.
- Failure modes: port exhaustion under connection churn (short-lived connections should reuse, not recreate); single-AZ gateways taking down egress when the AZ fails; NAT + VPC endpoints confusion — endpoints are cheaper and more secure for AWS/GCP services; and NAT in the path of high-volume traffic adding both latency and cost.
- Operational tradeoffs: managed NAT is the default egress path — resilient, but with per-GB pricing and connection limits; VPC endpoints/PrivateLink bypass NAT entirely for provider services; direct egress via public IPs suits workloads that can tolerate exposure. Size IP counts from peak concurrent connections, not traffic volume.
- RSIS3/mykb relevance: the wiki's egress architecture (NAT + endpoints per region) is documented with its port-scaling rules, so the loop's autoscaling plans would include NAT capacity.
- Connection-churn engineering: reuse keep-alive connections and connection pools so steady-state concurrency stays far below the per-IP port ceiling; monitor NAT metrics for near-exhaustion trends.
- Cost control: prefer VPC endpoints for provider APIs and CDN egress for public content; review NAT per-GB spend monthly since it tracks application chatiness as much as traffic size.

## Related
- [[wiki/cloud-infra/subnet-design|Subnet Design]] — private subnets need NAT
- [[wiki/cloud-infra/vpc-networking|VPC Networking]] — routing context for NAT
- [[wiki/cloud-infra/virtual-machines|Virtual Machines]] — the workloads that need egress
