---
type: "concept"
title: "Golden Paths"
description: "Blessed, supported ways to build and ship that are fast by default"
tags: ["golden-paths", "platform-engineering", "developer-experience", "standards"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/Internal_developer_platform", "https://en.wikipedia.org/wiki/Platform_engineering"]
---

# Golden Paths

## Summary
A golden path is the recommended, fully supported route for a common task — deploying a service, adding an article, opening an environment — where the safe way is also the fast way. Golden paths reduce cognitive load by making defaults correct, with escape hatches for the genuinely exceptional.

## Details
- Golden paths encode best practice in tooling: templates, generators, and defaults beat documentation that begs to be followed.
- They are not walls: the path must be fast enough that bypassing it is never tempting.
- Ownership matters: a golden path without a supporting team is a brochure.
- Measure them like products: time-to-first-deploy, escape-hatch usage, and feedback.
- Anti-pattern: golden paths as frozen monoculture that blocks legitimate variance.
- For the mykb bundle, the golden path is the article workflow: capture, stub, verify sources, publish — with templates and validators at each step.

Worked example — the wiki's golden path for a new article: a generator scaffolds frontmatter, CI validates links and sources, and promotion to growing is one command. Contributors who follow it ship in minutes.

## Related
- [[wiki/tooling/platform-engineering|Platform Engineering]]
- [[wiki/software-engineering/internal-developer-platforms|Internal Developer Platforms]]
- [[wiki/software-engineering/developer-experience|Developer Experience]]
- [[wiki/software-engineering/project-scaffolding|Project Scaffolding]]
- [[wiki/software-engineering/coding-standards|Coding Standards]]
- [[wiki/software-engineering/onboarding-docs|Onboarding Docs]]
- [[wiki/communities/pre-commit-hooks|Pre-Commit Hooks]]
- [[wiki/communities/lint-staged|Lint-Staged]]
