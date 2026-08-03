---
type: "concept"
title: "Data Governance Frameworks"
description: "Structures for deciding who can do what with data and holding them accountable"
tags: ["governance", "stewardship", "policy", "compliance"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Data Governance Frameworks

## Summary

Data governance frameworks are the structures for deciding who can do what with data, and holding someone accountable for those decisions. Without governance, data access is either chaotic (everyone can do anything) or paralyzed (nobody is allowed to do anything); a framework replaces both failure modes with explicit ownership, explicit policy, and a review process.

## Details

- Governance covers ownership, classification, access, quality, lifecycle, and usage policy for data assets. Ownership assigns an accountable person or team to each dataset — the "data owner" who decides purpose and access. Classification tags data by sensitivity (public, internal, confidential, PII) so protection scales with risk. Access policy defines who may read, write, or derive from each class. Quality policy defines the standards (accuracy, completeness, timeliness) the data must meet and who fixes it when it does not. Lifecycle policy governs retention and deletion. Usage policy governs what analyses and products may consume the data. Each dimension is a decision area — the framework is the structure that makes the decisions, records them, and reviews them.
- Frameworks (DAMA-DMBOK, DCAM, custom) define roles, councils, policies, and operating procedures. DAMA-DMBOK is the reference body of knowledge (data governance, architecture, quality, metadata, etc.); DCAM (EDM Council) is an assessment model that scores an organization's data-management maturity. The common skeleton: a governance council (executive sponsor, data owners, stewards) that sets policy; data stewards who implement it day to day; and documented operating procedures — how to request access, how to classify new data, how to resolve disputes, how to audit compliance. A framework's value is not the document; it is the existence of an escalation path and a decision record.
- Practical governance starts with a data dictionary, owners, and access reviews; automation scales it. The minimal viable governance: an inventory of data assets (the dictionary), a named owner per asset, and a recurring access review (who still needs access? who has orphaned permissions?). Automation scales the practice — policy-as-code (access control from declarative policy), automated data classification, and automated access reviews — but the decisions still need humans; automation makes the humans' time count.
- Good governance is an enabler: clear owners and contracts speed up safe self-serve analytics. The counterintuitive result: teams move faster with governance than without, because "can I use this data?" has an answer instead of a stall, and the answer is backed by an owner who knows the data. Governance that only blocks is misdesigned; governance that clarifies is a productivity tool.
- For mykb: the node anchors the governance cluster — ownership, dictionaries, warehouse governance, and access requests are its sub-topics.


## Related
- [[wiki/security-auth/compliance-frameworks|Compliance Frameworks]] — compliance side of governance
- [[wiki/infrastructure/data-ownership-and-stewardship|Data Ownership And Stewardship]] — assigning accountability
- [[wiki/infrastructure/data-dictionary-and-glossary|Data Dictionary And Glossary]] — the vocabulary governance needs
- [[wiki/infrastructure/data-warehouse-governance|Data Warehouse Governance]] — governance applied to the warehouse
- [[wiki/infrastructure/data-access-requests|Data Access Requests]] — operationalizing access policy
