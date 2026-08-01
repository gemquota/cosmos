---
type: "concept"
title: "Third-Party Risk"
description: "Managing security risk introduced by vendors, suppliers, and external dependencies"
tags: ["third-party", "supply-chain", "risk", "vendors"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
source: ["https://csrc.nist.gov/pubs/sp/800/161/r1/final"]
---

# Third-Party Risk

- Third-party risk covers vendors, SaaS providers, contractors, and open-source dependencies whose compromise can reach your data.
- NIST SP 800-161r1 frames it as supply-chain risk management: assess, contract, monitor, and respond.
- Controls: vendor security questionnaires, contractual obligations, continuous monitoring, and exit plans.
- For mykb: every external API and library is a third party; SBOMs and dependency monitoring make the risk visible.

## Related

- [[wiki/security/supply-chain-security|Software Supply Chain Security]] — the supply-chain lens on third parties
- [[wiki/security/sbom|SBOM]] — inventorying software components
- [[wiki/api-services/sca|Software Composition Analysis]] — dependency vulnerability tracking
- [[wiki/security-auth/data-breach-response|Data Breach Response]] — vendor breaches cascade to you
- [[wiki/security-auth/compliance-frameworks|Compliance Frameworks]] — vendor management as a compliance duty
