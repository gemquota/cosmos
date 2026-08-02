---
type: "concept"
title: "Code Review Practices"
description: "The habits and formats that make peer review effective"
tags: ["code-review", "collaboration", "quality", "practices"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/Code_review", "https://en.wikipedia.org/wiki/Software_craftsmanship"]
---

# Code Review Practices

## Summary
Code review practices cover when, how, and at what size code gets reviewed: small diffs, fast turnaround, explicit owners, and review focused on design and correctness rather than style. Done well, review is the team's cheapest defect filter and a teaching instrument.

## Details
- Small, focused diffs review faster and better; a 1000-line PR is a review theater.
- Review for behavior and design first — correctness, edge cases, and test quality — leaving style to linters.
- Fast turnaround matters: review latency is queueing time; hours are fine, days erode value.
- Four-eyes principle with named owners beats anonymous 'someone should review this'.
- Feedback should be kind, specific, and actionable; questions outrank commands.
- Review is also a learning path: juniors learn idioms, seniors learn about unfamiliar areas.
- For the mykb bundle, wiki article PRs review frontmatter, links, and source quality with the same discipline as code.

Worked example — a 40-line wiki CI change gets reviewed by two engineers in under four hours: one checks pipeline logic, the other checks the failure semantics. Two comments, one fix, merged.

## Related
- [[wiki/communities/software-craftsmanship|Software Craftsmanship]]
- [[wiki/dev-tools/continuous-integration|Continuous Integration]]
- [[wiki/software-engineering/coding-standards|Coding Standards]]
- [[wiki/communities/github-flow|GitHub Flow]]
- [[wiki/software-engineering/pair-programming|Pair Programming]]
- [[wiki/software-engineering/code-ownership|Code Ownership]]
- [[wiki/communities/commit-messages|Commit Messages]]
- [[wiki/communities/pre-commit-hooks|Pre-Commit Hooks]]
- [[wiki/software-engineering/code-review|Code Review]]
