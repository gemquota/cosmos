---
type: "concept"
title: "Requirements Engineering"
description: "The discipline of discovering, specifying, and validating what a system must do"
tags: ["requirements", "analysis", "specification", "engineering"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/Requirements_engineering", "https://en.wikipedia.org/wiki/Functional_requirement"]
---

# Requirements Engineering

## Summary
Requirements engineering covers the discovery, analysis, specification, and validation of what a system must do — functional and non-functional. Its output is a shared understanding precise enough to build against and test against.

## Details
- Gather from users, stakeholders, and systems; distinguish wants from needs through questions and prototypes.
- Specify with the right precision: user stories for intent, acceptance criteria for tests, models for behavior.
- Non-functional requirements (performance, security, reliability) are requirements too — they bite when ignored.
- Validation is continuous: walk through scenarios, prototype, and confirm before building deep.
- Requirements are living: they change with understanding, so version them and manage the change.
- The cost of ambiguity compounds downstream — a vague requirement becomes a wrong feature.
- For the mykb bundle, requirements engineering defines what articles must contain, how links are verified, and what the API promises.

Worked example — a requirement 'articles link correctly' is vague; refined: 'every wikilink resolves to a file; the build fails on broken links; 95% of links resolve within one sync'. That is testable.

## Related
- [[wiki/software-engineering/user-stories|User Stories]]
- [[wiki/software-engineering/acceptance-criteria|Acceptance Criteria]]
- [[wiki/software-engineering/specification-by-example|Specification by Example]]
- [[wiki/communities/stakeholder-management|Stakeholder Management]]
- [[wiki/software-engineering/software-estimation|Software Estimation]]
- [[wiki/software-engineering/user-research-methods|User Research Methods]]
- [[wiki/software-engineering/documentation-as-code|Documentation as Code]]
- [[wiki/software-engineering/agile-ceremonies|Agile Ceremonies]]
- [[wiki/dev-tools/error-contracts|Error Contracts]]
- [[wiki/dev-tools/error-codes|Error Codes]]
