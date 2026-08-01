---
type: "concept"
title: "Documentation as Code"
description: "Treating documentation with the same rigor as source code: versioned, reviewed, and built"
tags: ["documentation", "docs-as-code", "writing", "tooling"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://www.writethedocs.org/guide/docs-as-code/"]
---

# Documentation as Code

## Summary
Documentation as code applies software engineering practices to documentation: plain-text source, version control, automated builds, review, and continuous publication. Write the Docs is the community hub for the practice, which makes docs testable, reviewable, and durable.

## Details
- Source is plain text — Markdown, reStructuredText, AsciiDoc — stored in the repository next to code or in a docs repo with its own CI.
- The same pipeline applies: pull requests, review, linting of links and structure, and automated publishing to a site.
- Tooling ranges from MkDocs, Hugo, and Sphinx to Docusaurus; docs-as-code sites emphasize navigable structure and search.
- Quality signals: broken-link checks, spelling linting, and freshness reviews are the 'tests' of documentation.
- Docs live and die by proximity: docs near the code are more likely to stay true, which is why READMEs and ADRs live in-repo.
- RSIS3 relevance: mykb is documentation-as-code at scale — a wiki of markdown in git, with validation and curation as its CI.
- Worked example: a change to an API ships with its docs in the same pull request, so docs and behavior cannot drift.

## Related
- [[wiki/dev-tools/markdown-authoring|Markdown Authoring]] — the plain-text source format for most docs-as-code
- [[wiki/software-engineering/architecture-decision-records|Architecture Decision Records]] — decision docs written and reviewed like code
- [[wiki/software-engineering/onboarding-docs|Onboarding Docs]] — the highest-ROI documentation a team writes
- [[wiki/data-storage/open-knowledge-format|Open Knowledge Format]] — a portable markdown knowledge format
- [[wiki/memory/personal-knowledge-management|Personal Knowledge Management]] — the personal practice docs-as-code extends
- [[wiki/devops-infra/entities/ci-cd-patterns|CI/CD Patterns]] — the pipeline that builds and publishes docs
- [[wiki/sources/README|Sources]] — provenance discipline inside the wiki
