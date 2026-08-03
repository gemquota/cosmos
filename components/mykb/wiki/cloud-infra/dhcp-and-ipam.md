---
type: "concept"
title: "DHCP & IPAM"
description: "Dynamic address assignment and IP address management at fleet scale"
tags: ["dhcp", "ipam", "addressing", "networking"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# DHCP & IPAM

## Summary

DHCP hands out IP addresses and network configuration automatically; IPAM (IP address management) plans, tracks, and reclaims that space. Together they are the operational backbone of every network — and the source of duplicate-address, exhaustion, and documentation-drift incidents.

## Details
- Mechanism: DHCP servers lease addresses to clients (IP, mask, gateway, DNS, NTP) for a lease time; clients renew before expiry; static reservations pin identities. Cloud VPCs hide DHCP behind the platform (subnets auto-assign), but on-prem and hybrid networks still run DHCP servers and need IPAM (spreadsheets, NetBox/phpIPAM, or vendor tools) to plan subnets and track usage.
- Concrete example: an office DHCP scope of 10.10.20.0/24 with reservations for printers and fixed leases for BYOD; an IPAM tool shows 87% utilization so the team adds a scope before exhaustion causes mysterious DHCP failures; a cloud VPC reserves the first four addresses per subnet for platform services — the reason manual hosts must avoid them.
- Failure modes: DHCP starvation (attacker or exhaustion consuming all addresses); duplicate scopes or overlapping CIDRs causing address conflicts; lease-time mismatches (too short floods the server, too long delays reclaim); and IPAM drift where reality (cloud auto-scaling, containers) diverges from the spreadsheet.
- Operational tradeoffs: DHCP is the default for endpoint mobility; static addressing still wins for servers and appliances where identity must not change. The discipline is IPAM-first: plan the space, automate reservations, and reconcile actual usage against the record regularly.
- RSIS3/mykb relevance: lab networks for experiments use a documented IPAM plan from this note so the loop's provisioning never collides with reserved ranges.
- Conflict detection: run periodic IPAM reconciliation against actual lease tables; silent drift between the plan and reality is how duplicate-address incidents start.
- Scope documentation: record lease times and reservations per scope; the DHCP config is the network's contract with every device.

## Related
- [[wiki/os-shell/dhcp-and-ip-allocation|DHCP & IP Allocation]]
- [[wiki/cloud-infra/networking-fundamentals|Networking Fundamentals]]
- [[wiki/cloud-infra/tcp-ip-stack|TCP/IP Stack]]
- [[wiki/syntheses/knowledge-acquisition-workflow|Knowledge Acquisition Workflow]]
- [[wiki/syntheses/mykb-acquisition-curation-and-practices|Acquisition, Curation & Practices]]
