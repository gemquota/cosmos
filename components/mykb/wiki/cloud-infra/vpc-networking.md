---
type: "concept"
title: "VPC Networking"
description: "Private virtual networks in the cloud: CIDR ranges, subnets, routing, and isolation"
tags: ["vpc", "networking", "cloud", "security"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
---

# VPC Networking

## Summary
A VPC is a logically isolated virtual network where cloud resources get private IPs, subnets, and route tables.

## Details
- CIDR planning decides the address space; too small and you renumber later, too large and route tables get noisy.
- Subnets carve the VPC into failure domains and public/private tiers; route tables and gateways control egress.
- Security groups and network ACLs filter traffic; VPC-level policy is the outer ring of zero-trust network design.
- Open questions: private vs public subnet layout, multi-account VPC sharing, and IP exhaustion strategies.

## Related
- [[wiki/cloud-infra/dns-management|DNS Management]] — private DNS in the VPC
- [[wiki/cloud-infra/virtual-machines|Virtual Machines]] — compute placed inside VPCs
- [[wiki/infrastructure/network-policy|Network Policy]] — in-cluster complement to VPC rules
