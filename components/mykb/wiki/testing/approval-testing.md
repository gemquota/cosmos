---
type: "concept"
title: "Approval Testing"
description: "Human-reviewed diffs against stored baselines before accepting changes"
tags: ["approval-testing", "testing", "baselines", "review"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://approvaltests.com/", "https://github.com/approvals/ApprovalTests.Python"]
---

# Approval Testing

## Summary
Approval testing captures actual output as a baseline and requires human approval of any change, turning every output difference into an explicit decision. It formalizes a review workflow around generated output of any kind.

## Details
- ApprovalTests libraries exist for Java, .NET, Python, JavaScript, and other ecosystems.
- Flow: the test produces an output file, it is diffed against the approved baseline, and a human approves or fixes.
- Excellent for legacy code, report generators, serializers, and complex text output.
- Review discipline is everything: approving blindly defeats the purpose.
- Surface diffs in PR review with build-time diff reporting.
- Contrast with snapshots: approval tools emphasize human sign-off and structured review.
- Pairs with characterization testing to lock behavior before refactoring.

## Related
- [[wiki/testing/snapshot-testing|Snapshot Testing]] — automated baseline diffs without sign-off
- [[wiki/testing/characterization-testing|Characterization Testing]] — locking behavior that approvals verify
- [[wiki/testing/golden-file-management|Golden File Management]] — curating baseline output files
- [[wiki/testing/legacy-code-testing|Legacy Code Testing]] — approvals tame untested systems
- [[wiki/testing/code-review-for-tests|Code Review for Tests]] — reviewing the diffs approvals surface
- [[wiki/testing/visual-regression-testing|Visual Regression Testing]] — visual diffs with the same approval model
