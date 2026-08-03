---
type: "concept"
title: "Azure VNet & NSGs"
description: "Virtual networks, subnets, and network security groups on Azure"
tags: ["azure", "vnet", "nsg", "cloud"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Azure VNet & NSGs

## Summary

Azure VNets and network security groups (NSGs) define the isolation and filtering of Azure networking: VNets carve address space and subnets, NSGs filter traffic per subnet/interface with rule precedence. They are the primary security boundary for Azure workloads.

## Details
- Mechanism: a VNet owns a CIDR and contains subnets; each subnet has a route table and can be attached to NSGs (applied at subnet or NIC level); NSG rules are evaluated in priority order with explicit allows/denies, and default rules allow intra-VNet traffic and deny internet ingress. Azure Firewall and VNet peering extend the model; service endpoints and private endpoints bypass NSG filtering for PaaS traffic, so the applicable model per subnet must be documented.
- Concrete example: an app subnet with an NSG allowing 443 from the load balancer's subnet only and denying everything else inbound; a management subnet restricted to a bastion; peering connects VNets for hub-spoke routing while NSGs still filter per subnet. NSG flow logs feed analysis and alerting.
- Failure modes: NSG priority mistakes (a broad deny shadowed by a later allow, or vice versa); applying NSGs only at NIC level so subnet-wide traffic bypasses expectations; asymmetric rules that allow one direction but not responses; and CIDR overlap between peered VNets breaking routing silently. Rule lists that outgrow maintainability invite additions by habit rather than design.
- Operational tradeoffs: NSGs are stateful and cheap — the default filter layer — while Azure Firewall adds centralized inspection, DNS, and logging at a cost; choose by compliance need. Keep rules minimal and documented, and enable flow logs before incidents, not after.
- RSIS3/mykb relevance: experiment environments inherit a documented NSG baseline from this note, so loop-provisioned VNets start secure instead of relying on default rules.
- Flow logs: enable NSG flow logs before incidents; retroactive analysis is impossible, and the logs are the difference between a root cause and a guess.

## Related
- [[wiki/cloud-infra/cloud-providers-aws-azure-gcp|Cloud Providers: AWS, Azure, GCP]]
- [[wiki/cloud-infra/azure-managed-disks|Azure Managed Disks]]
- [[wiki/cloud-infra/parameter-stores-aws-ssm-azure-keyvault-gcp-secretmanager|Cloud Parameter Stores]]
- [[wiki/infrastructure/azure-synapse|Azure Synapse]]
