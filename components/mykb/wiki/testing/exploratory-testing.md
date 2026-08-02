---
type: "concept"
title: "Exploratory Testing"
description: "Unscripted, session-based testing guided by heuristics"
tags: ["exploratory-testing", "testing", "heuristics", "discovery"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://www.ibm.com/topics/exploratory-testing", "https://www.satisfice.com/blog/archives/1509"]
---

# Exploratory Testing

## Summary
Exploratory testing is unscripted testing guided by heuristics and curiosity, designing and executing tests in parallel with learning. It finds bugs scripted suites miss, especially in new, complex, or poorly specified areas.

## Details
- Charter-driven: define a mission and timebox; freedom exists within the charter.
- Heuristics such as Whittaker tours and SFDPOT guide systematic exploration.
- Combine with session-based testing for structure and reporting.
- Ideal for new features, complex integrations, usability, and unclear requirements.
- Document findings as bug reports with steps, evidence, and severity.
- Tools: session sheets, note capture, and screen recording.
- Pair with automation: exploratory findings become regression tests.

## Related
- [[wiki/testing/session-based-testing|Session-Based Testing]] — structuring exploratory work
- [[wiki/testing/error-guessing|Error Guessing]] — heuristics both approaches share
- [[wiki/testing/manual-testing|Manual Testing]] — the human execution mode
- [[wiki/testing/risk-based-testing|Risk-Based Testing]] — charters targeting risk
- [[wiki/testing/regression-testing|Regression Testing]] — discoveries become regression tests
- [[wiki/testing/ui-testing|UI Testing]] — interface-level exploration
