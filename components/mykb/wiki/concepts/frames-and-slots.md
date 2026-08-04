---
type: "concept"
title: "Frames and Slots"
description: "Structured knowledge representations with named attributes"
tags: ["knowledge", "representation", "schemas"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Frames and Slots

## Summary

Frames and slots are a knowledge representation in which concepts are structures with named attributes — slots — that hold values, defaults, or constraints. They matter because they give reasoning systems and cognitive models a way to organize expectations: a frame for a restaurant has slots for name, cuisine, and price. Frames support default reasoning, inheritance, and expectation-driven processing.

## Details

- **Definition** — A frame represents a stereotyped situation or concept; slots are its attributes, filled with specific values or filled by defaults.
- **Defaults and inheritance** — Slots can carry default values inherited from super-frames, enabling reasoning with incomplete information.
- **Expectation** — Activated frames set expectations: seeing a restaurant cues the restaurant frame and guides what is noticed and inferred.
- **Worked example** — A travel assistant fills a hotel frame's slots — location, price range, amenities — using defaults until user input overrides them.
- **Common failure modes** — Overly rigid frames that resist novel instances, defaults that silently apply wrong values, and slot taxonomies that fragment meaning.
- **Practical relevance** — Frames anticipate object-oriented modeling and schemas in software, and they ground theories of comprehension and memory.
- **Variants** — Scripts are temporal frames for event sequences; semantic networks emphasize relations between frames.
- **Limits** — Frame choice is itself a modeling decision: the same situation can be framed many ways, changing what the system expects and infers.
- **Reasoning** — Frames support default reasoning: missing slot values fall back to defaults, enabling conclusions from partial information.
- **Computational use** — Frame languages anticipated object orientation and schema-driven systems; modern schemas, records, and typed objects are direct descendants.
- **Worked example** — A frame for a meeting has slots for attendees, agenda, and location; a scheduler fills defaults for location from the organizer's profile.
- **Cognitive role** — Comprehension research shows frames guide inference and recall, filling unstated details from stereotyped expectations.

## Related

- [[wiki/concepts/scripts-and-schemas|Scripts and Schemas]] — event-structured frames
- [[wiki/concepts/category-learning|Category Learning]] — acquiring frame structure
- [[wiki/concepts/concept-formation|Concept Formation]] — building frames
- [[wiki/concepts/schema-theory|Schema Theory]] — the broader account
- [[wiki/concepts/semantic-memory|Semantic Memory]] — stored conceptual knowledge
- [[wiki/concepts/conceptual-blending|Conceptual Blending]] — composing frames
