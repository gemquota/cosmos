---
type: "concept"
title: "Estimation Techniques"
description: "Methods for predicting the effort or size of software work, from story points to t-shirt sizes"
tags: ["estimation", "planning", "agile", "process"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
---
# Estimation Techniques

## Summary

Estimation techniques turn uncertain work into usable planning ranges — story points with velocity, t-shirt sizes, time-based estimates, and probabilistic methods. The goal is not accuracy but decision-grade ranges: enough to sequence work and set expectations without false precision.

## Details
- Mechanism: relative sizing (points/t-shirts) compares work to known references, decoupling from time; velocity converts completed points to throughput; time-based estimates (hours/days) work best for well-understood work; probabilistic methods (three-point: optimistic/nominal/pessimistic, or Monte Carlo over historical cycle time) produce ranges and confidence intervals.
- Concrete example: a team sizes a backlog against a reference story (points), tracks velocity over sprints, and forecasts with confidence bands instead of a single date; a data team estimates a migration with three-point ranges and a 90% confidence interval; a lone engineer uses time-boxed spikes to shrink uncertainty before committing.
- Failure modes: anchoring and planning fallacy (estimates rationalized by last optimistic number); estimating before understanding (no spikes, no discovery); treating estimates as commitments (punishing misses trains inflating); and velocity gaming (point inflation) when numbers become targets.
- Operational tradeoffs: estimation costs time and produces ranges, not guarantees; the discipline is estimate the uncertain things, keep the unit consistent, track actuals against estimates, and use ranges for decisions that tolerate them. For low-stakes work, skip estimation entirely.
- RSIS3/mykb relevance: the wiki's loop plans would use three-point ranges and track actuals, so improvement cycles get calibrated forecasts instead of confident guesses.
- Calibration loop: compare estimates to actuals at a regular cadence; a team that never measures its misses is guessing with extra steps.
- Uncertainty handling: split large uncertain items into spikes and smaller cards until the range is decision-grade; estimation of the unknown is the main source of error.

## Related
- [[wiki/software-engineering/technical-debt|Technical Debt]] — debt inflates estimates until repaid
- [[wiki/software-engineering/agile-ceremonies|Agile Ceremonies]] — estimation happens inside sprint ceremonies
- [[wiki/software-engineering/code-review|Code Review]] — review load should be included in estimates
- [[wiki/memory/spaced-repetition|Spaced Repetition]] — scheduling analog for reviewing knowledge
- [[wiki/agent-systems/planning-systems|Planning Systems]] — agents plan under the same uncertainty
