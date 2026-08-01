---
type: "concept"
title: "Reserved Capacity"
description: "Committed-use discounts that trade flexibility for predictable, lower compute pricing"
tags: ["reserved", "compute", "cost", "finops"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
---

# Reserved Capacity

## Summary
Reserved capacity commits to a certain compute usage for one to three years in exchange for significant discounts over on-demand.

## Details
- Committed-use discounts (savings plans, reserved instances) can cut compute cost by 30–70%.
- Risk: commitments become waste if demand drops; convertible plans and savings plans soften that.
- Match commitments to measured baseline usage, not peaks — leave spikes to on-demand or spot.
- Open question: how to manage commitments across multiple clouds and accounts.

## Related
- [[wiki/cloud-infra/virtual-machines|Virtual Machines]] — the capacity being committed
- [[wiki/cloud-infra/spot-instances|Spot Instances]] — the flexible counterpart
- [[wiki/cloud-infra/cloud-cost-optimization|Cloud Cost Optimization]] — commitments as a cost lever
- [[wiki/devops-infra/terraform|Terraform]] — provisioning committed capacity as code
