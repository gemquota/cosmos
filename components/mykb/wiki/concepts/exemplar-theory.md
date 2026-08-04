---
type: "concept"
title: "Exemplar Theory"
description: "Categorization by similarity to stored individual instances"
tags: ["categorization", "memory", "examples"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Exemplar Theory

## Summary

Exemplar theory holds that categories are represented by stored individual instances — exemplars — and that new items are categorized by their similarity to those memories. It matters because it explains subtle categorization behavior that averaged prototypes cannot: sensitivity to typicality, variability, and correlations among features. It also connects categorization directly to memory.

## Details

- **Definition** — Instead of storing a single category average, the mind stores many examples; classification compares a novel item against all of them.
- **Similarity** — Classification sums or weights similarity to stored exemplars, so a category is effectively a region of memory space.
- **Strengths** — Exemplar models capture typicality gradients, within-category variability, and correlated features without extra machinery.
- **Worked example** — People classify a robin as a bird quickly because it is similar to many stored bird exemplars, while a penguin is slower because it resembles few.
- **Costs** — Storing every instance is memory-hungry, and classification time grows with the number of stored exemplars.
- **Common failure modes** — Over-reliance on superficial similarity to a few vivid exemplars, and sensitivity to which examples happen to have been encoded.
- **Practical relevance** — Instructional examples, few-shot prompting, and case-based systems exploit the same instance-driven mechanism.
- **Comparison** — Prototype theory stores an average; exemplar theory stores the set — the two make different predictions about variability and category boundaries.
- **Hybrids** — Mixed models combine prototypes for typical structure with exemplars for boundary detail, fitting data better than either alone.
- **Typicality effects** — Because categories are collections of instances, typical members are classified faster and more accurately, matching observed behavior.
- **Context sensitivity** — Exemplar storage preserves context, so category judgments shift with which examples are active in memory.
- **Worked example** — A doctor who has seen many pneumonia cases with atypical presentation classifies a new ambiguous case correctly by similarity to those stored instances.
- **Applications** — Case-based reasoning systems implement the theory computationally, retrieving stored cases to solve new problems.

## Related

- [[wiki/concepts/prototype-theory|Prototype Theory]] — the averaging alternative
- [[wiki/concepts/category-learning|Category Learning]] — acquiring category knowledge
- [[wiki/memory/concept-formation|Concept Formation]] — building concepts from instances
- [[wiki/concepts/semantic-memory|Semantic Memory]] — storing the exemplars
- [[wiki/memory/availability-heuristic|Availability Heuristic]] — vivid exemplar effects
- [[wiki/concepts/analogical-reasoning|Analogical Reasoning]] — instance-based mapping
