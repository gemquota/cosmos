---
type: "concept"
title: "Algorithmic Impact Assessments"
description: "Evaluating how automated systems affect individuals and groups before deployment"
timestamp: "2026-08-02T00:00:00Z"
---
tags: ["impact-assessments", "governance", "assessment", "responsible-ai", "risk"]
status: "growing"

# Algorithmic Impact Assessments

## Summary
An algorithmic impact assessment evaluates how an automated system affects individuals and groups before it is deployed. It matters because harms are cheaper to prevent than to remediate, and regulators increasingly expect documented analysis. The assessment turns vague risk concerns into a structured, reviewable process with named owners.

## Details
- **Definition** — an impact assessment identifies affected populations, potential harms, and the severity and likelihood of each before deployment.
- **Scope** — assessments apply to systems with meaningful effects on people, such as hiring, lending, health, and content ranking decisions.
- **Harm categories** — the analysis covers discrimination, privacy intrusion, safety failures, and erosion of user agency or trust.
- **Stakeholder input** — affected groups and domain experts should inform the assessment, because harms are often visible only from their perspective.
- **Mitigation plans** — findings must map to concrete actions: design changes, testing, monitoring, or deployment restrictions.
- **Regulatory context** — many jurisdictions now require impact assessments for high-risk automated decisions, making them a compliance artifact as well as a practice.
- **Documentation** — the assessment should be versioned with the system, because changes in scope, data, or model can invalidate earlier conclusions.
- **Common failure modes** — checkbox assessments that rubber-stamp decisions, missing affected groups, and analysis that never influences the design.
- **Worked example** — a team deploying a resume-ranking model documents the populations affected, measures bias across groups, and commits to monitoring before launch.
- **Practical relevance** — a rigorous assessment connects bias testing and governance into one accountable pipeline.

- **Severity and likelihood** — scoring each harm by impact and probability focuses mitigation effort where it matters most.
- **Lifecycle** — assessments must be revisited as the system, data, or population changes, not just at launch.
- **Review ownership** — a named owner and review board make the assessment binding rather than advisory.
## Related
- [[wiki/testing/bias-and-fairness-eval|Bias and Fairness Evaluation]] — technical input
- [[wiki/testing/responsible-ai-principles|Responsible AI Principles]] — framework
- [[wiki/testing/ai-governance-frameworks|AI Governance Frameworks]] — policy umbrella
- [[wiki/testing/model-cards-and-datasheets|Model Cards and Datasheets]] — documentation
- [[wiki/testing/red-team-processes|Red Team Processes]] — assurance
- [[wiki/agent-systems/accountability-ai|Accountability for AI]] — owning outcomes
