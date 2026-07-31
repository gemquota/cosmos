# Structured Prompt Creation Framework v1.0.0

A multi-series, multi-round prompt elicitation framework that alternates open-ended and multi-choice questions to produce a complete development specification. Each series is a stage in a dev spec plan build — answers flow forward to inform later stages.

---

## How It Works

The framework has **7 series**, each targeting a distinct dimension of specification. Within each series there are **x rounds**. Every round begins with **y open-ended questions** followed by **z multi-choice follow-ups** for each open-ended question.

- **Open-ended** — draws out context, nuance, and user-specific details
- **Multi-choice** — locks down a commitment with discriminating options

Series must be completed **in order**. Each series's questions may reference your answers from earlier series.

---

## Series Overview

| # | Series | Description | Rounds (x) | OE per Round (y) | MC per OE (z) | Total Questions |
|---|--------|-------------|:----------:|:----------------:|:-------------:|:---------------:|
| 1 | **Conceptual Depth** | Calibrates register, audience, vocabulary, and complexity scaffolding | 3 | 2 | 3 | 24 |
| 2 | **Ontological Characteristics** | Discovers, classifies, refines, and validates domain entities | 5 | 3 | 5 | 90 |
| 3 | **Semantic Relationships** | Maps direct, hierarchical, causal, and dynamic entity connections | 4 | 2 | 4 | 40 |
| 4 | **Procedural Breadth** | Scopes workflow, decision branching, and step granularity | 3 | 2 | 3 | 24 |
| 5 | **Technical Specifications** | Captures hardware, software, performance, integration, timeline | 4 | 5 | 4 | 100 |
| 6 | **Development Methodologies** | Determines workflow cadence, quality, and collaboration patterns | 3 | 2 | 3 | 24 |
| 7 | **Operational / Functional** | Defines deployment, runtime behavior, monitoring, maintenance | 3 | 2 | 3 | 24 |

**Totals:** 25 rounds, 67 open-ended questions, 259 multi-choice follow-ups (326 total probes)

---

## Dependency Chain

```
Series 1: Conceptual Depth
  │  domain, audience_level, terminology, scaffolding
  ▼
Series 2: Ontological Characteristics
  │  entity_list, attributes, categories, boundaries
  ▼
Series 3: Semantic Relationships
  │  relationship_graph, dependency_chains, hierarchy
  ▼
Series 4: Procedural Breadth
  │  procedure_steps, decision_points, branching
  ▼
Series 5: Technical Specifications
  │  tech_stack, platform, performance, timeline
  ▼
Series 6: Development Methodologies
  │  cadence, review_process, team_composition
  ▼
Series 7: Operational / Functional Preferences
  │  deployment, runtime, monitoring, maintenance
```

---

## File Structure

```
framework.json          # Master machine-readable spec
FRAMEWORK.md            # This file — master human-readable guide
series/
├── 01-conceptual-depth/
│   ├── series.json     # Machine-readable: rounds, questions, choices
│   └── md/       # Human-readable: formatted Q&A sessions
├── 02-ontological-characteristics/  (same structure)
├── 03-semantic-relationships/       (same structure)
├── 04-procedural-breadth/           (same structure)
├── 05-technical-specifications/     (same structure)
├── 06-development-methodologies/    (same structure)
└── 07-operational-functional/       (same structure)
```

---

## Execution Pattern

1. **Open the md/** for the current series. Read the context at the top.
2. **For each round**, answer the open-ended questions (write freely).
3. **After each open-ended answer**, select from the multi-choice options to formalize your intent.
4. **Accumulate** responses into a running artifact. Later series reference prior answers.
5. **Continue** through all 7 series in order.

Estimated completion: 45–75 minutes for a thorough pass.

---

## Quick Reference Table

| Parameter | Range | Description |
|-----------|:-----:|-------------|
| x | 3–5 | Number of rounds per series |
| y | 2–5 | Number of open-ended questions per round |
| z | 3–5 | Number of multi-choice options per open-ended question |
