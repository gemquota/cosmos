---
type: "concept"
title: "Code Review"
description: "Systematic examination of code changes by other developers before merging"
tags: ["code-review", "quality", "collaboration", "process"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://google.github.io/eng-practices/review/"]
---

# Code Review

## Summary
Code review is the practice of having one or more developers examine a change before it lands, catching defects, improving design, and spreading knowledge across the team. It is one of the highest-leverage quality gates in software engineering, and the review culture matters more than the tooling.

## Details
- Reviewers look for design, functionality, complexity, tests, naming, and comments — in roughly that order of priority — not just style.
- Small, focused changes review faster and more accurately; huge diffs get rubber-stamped and defects slip through.
- The author speeds review by writing a good description, splitting logically separable changes, and responding to comments promptly.
- Automation should handle style (formatters, linters), leaving humans for judgment calls about design and correctness.
- Psychological safety matters: reviews are conversations about the code, not the person; the Google eng-practices guide emphasizes clarity and kindness.
- RSIS3 relevance: mykb's acquisition round is a form of review — a human checks the agent's articles before they become permanent memory.
- Metrics like review latency and comment density are useful signals but can be gamed; treat them as diagnostics.

## Related
- [[wiki/software-engineering/pair-programming|Pair Programming]] — the continuous alternative to asynchronous review
- [[wiki/software-engineering/refactoring|Refactoring]] — review comments often translate into refactoring follow-ups
- [[wiki/software-engineering/code-ownership|Code Ownership]] — review assigns responsibility for the changed code
- [[wiki/software-engineering/static-analysis-tools|Static Analysis Tools]] — automate the mechanical parts of review
- [[wiki/software-engineering/code-formatters|Code Formatters]] — remove style debates from review
- [[wiki/devops-infra/entities/ci-cd-patterns|CI/CD Patterns]] — CI gates run before human review starts
- [[wiki/agent-systems/agent-evaluation|Agent Evaluation]] — review standards mirror how agent outputs are judged
