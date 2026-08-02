---
type: "concept"
title: "Characterization Testing"
description: "Locking in existing untested behavior with post-hoc tests"
tags: ["characterization-testing", "testing", "legacy", "baselines"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://understandlegacycode.com/blog/characterization-testing/", "https://www.ibm.com/topics/characterization-testing"]
---

# Characterization Testing

## Summary
Characterization testing documents existing behavior with tests written after the fact, asserting what code currently does rather than what it should do. It freezes current behavior so changes become visible and reviewable.

## Details
- Write tests from observed behavior; any assertion failure reveals a behavior change.
- Golden and approval tests fit characterization workflows naturally.
- Value: enables safe refactoring and pinpoints unintended drift.
- Label characterization tests clearly; review odd behaviors before locking them in.
- Later, replace wrong behavior specifications with correct expectations deliberately.
- Pair with coverage to find untested paths.
- Especially valuable for legacy systems and third-party integrations.

## Related
- [[wiki/testing/legacy-code-testing|Legacy Code Testing]] — the workflow characterization starts
- [[wiki/testing/approval-testing|Approval Testing]] — baseline review of characterized output
- [[wiki/testing/golden-file-management|Golden File Management]] — stored baselines for behavior
- [[wiki/testing/snapshot-testing|Snapshot Testing]] — automated characterization
- [[wiki/software-engineering/refactoring|Refactoring]] — the safety net refactors need
- [[wiki/testing/regression-testing|Regression Testing]] — characterized behavior protection
