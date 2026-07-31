# Series 4: Procedural Breadth

**x = 3 rounds · y = 2 open-ended per round · z = 3 choices per open-ended**

Scopes the workflow, decision branching, and step granularity informed by the entity model and relationship graph.

Context from Series 2 & 3: entities=`{entity_list}`, relationships=`{relationship_graph}`, steps=`{procedure_steps}`

---

## Round 1: Scope and Step Count

### Open-Ended 4.1.1
**What is the overall scope of the procedure or workflow? What does it start from and what is its end state?**

Write freely. Define the boundaries of the process in terms of time, inputs, and outputs.

**After answering, choose one:**
- a) Narrow — a single well-defined task with clear boundaries
- b) Moderate — an end-to-end process with several stages
- c) Broad — a multi-phase workflow spanning distinct sub-processes

---

### Open-Ended 4.1.2
**How many distinct steps, stages, or phases should the procedure contain? What is the natural breakdown?**

Write freely. Map the flow from start to finish, listing each logical step.

**After answering, choose one:**
- a) 2–4 steps — quick process with few handoffs
- b) 5–8 steps — moderate complexity with clear waypoints
- c) 9+ steps — comprehensive procedure with fine-grained stages

---

## Round 2: Decision Points and Inputs/Outputs

### Open-Ended 4.2.1
**Where are the key decision points, branches, or conditional paths? At which steps must a choice be made that affects the rest of the flow?**

Write freely. Identify each fork, its alternatives, and what determines the path taken.

**After answering, choose one:**
- a) No branching — a single linear path from start to finish
- b) Few branches — 1–2 decision points with 2–3 choices each
- c) Moderate branching — multiple decision points with varying path counts

---

### Open-Ended 4.2.2
**What are the expected inputs and outputs at each stage? What data or artifacts flow between steps?**

Write freely. For each step, describe what it consumes and produces.

**After answering, choose one:**
- a) Simple I/O — each step takes one input and produces one output
- b) Multi-I/O — some steps consume or produce multiple items
- c) Network I/O — steps pass data through a shared context rather than direct handoffs

---

## Round 3: Error Handling and Granularity

### Open-Ended 4.3.1
**What fallback paths, error handling, or recovery procedures should be included for when things go wrong?**

Write freely. Consider what could fail at each step and how to respond.

**After answering, choose one:**
- a) Minimal — errors abort the procedure with a clear message
- b) Retry-based — failed steps can be retried with backoff
- c) Recovery paths — dedicated handling for known failure modes with alternative flows

---

### Open-Ended 4.3.2
**How granular should each procedural step be? Should steps be coarse (several actions) or fine (one action per step)?**

Write freely. Consider who or what will execute the procedure.

**After answering, choose one:**
- a) Coarse — each step is a meaningful phase (2–5 sub-actions per step)
- b) Fine — each step is a single atomic action
- c) Mixed — core steps are fine; well-established procedures are coarser
