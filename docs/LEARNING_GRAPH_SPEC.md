# Learning Graph Specification — Adaptive AI Onboarding Tutor

## 1. Purpose

This document defines the initial conceptual model for the Learning Graph of the Adaptive AI Onboarding Tutor.

The Learning Graph should allow the tutor to represent:

- major professional learning domains;
- concepts contained within each domain;
- prerequisite relationships between knowledge elements;
- learning objectives;
- the learner's current learning state;
- historical learning evidence;
- knowledge gaps that require reinforcement;
- progression conditions;
- delayed re-evaluation of previously demonstrated knowledge.

The objective is not to represent only a fixed sequence of lessons.

The system should use the Learning Graph to support pedagogical decisions such as:

**what to teach → what to verify → when to reinforce → when to revisit a prerequisite → when to allow progression**

The conceptual architecture is:

**Learning Graph + Learner State + Evidence History + Tutor Policy → Pedagogical Decision**

---

## 2. Graph Principles

The Learning Graph should follow these principles:

1. Learning should not be treated as a rigid sequence of modules that must be completed at 100%.

2. Major domains represent meaningful stages of professional progression.

3. Individual concepts provide enough granularity to identify specific knowledge gaps within a domain.

4. The learner does not need to reach `mastered` in every concept before progressing.

5. Every concept in the current domain must reach at least `sufficient` before progression to the next major domain.

6. In addition to individual concept readiness, the domain itself must reach at least `sufficient` through an integrative activity.

7. Gaps discovered later may trigger targeted reinforcement without forcing the learner to repeat an entire domain.

8. Learner-specific state must remain separate from the structural definition of knowledge.

9. Learning evidence must be preserved over time rather than overwritten by later assessments.

10. The LLM may interpret evidence and propose pedagogical hypotheses, but structural progression rules must remain explicit, deterministic, and auditable.

---

## 3. Graph Structure

The initial model contains two primary node types:

### 3.1 Domain Node

A `Domain Node` represents a major knowledge or professional competency area.

Examples:

- Contact Center Fundamentals;
- Contact Center Metrics;
- Genesys Cloud;
- Genesys Data Access;
- Programming;
- Statistics;
- Data Visualization.

### 3.2 Concept Node

A `Concept Node` represents a specific concept contained within a domain.

Examples within Contact Center Metrics include:

- AHT;
- ASA;
- Service Level;
- Hold;
- ACW;
- Abandonment;
- Overflow.

Concept-level granularity allows the tutor to identify more precisely where a learning difficulty occurs.

---

## 4. Domain Node

Each major domain should contain at least:

```text
id
name
description
learning_objective
```

Example:

```text
id:
contact_center_metrics

name:
Contact Center Metrics

description:
A domain covering the understanding and interpretation
of key metrics used in Contact Center operations and
analytics.

learning_objective:
The learner should be able to understand the main
metrics in the domain, relate them to one another,
and use them together to interpret operational scenarios.
```

The domain `learning_objective` must be **integrative**.

It should not simply repeat the objectives of its individual concepts.

Its purpose is to verify whether the learner can combine several concepts within the domain coherently.

---

## 5. Concept Node

Each concept should contain at least:

```text
id
name
description
learning_objective
domain_id
```

Example:

```text
id:
service_level

name:
Service Level

description:
A Contact Center metric representing the proportion
of interactions answered within a defined time threshold.

learning_objective:
The learner should understand the meaning of Service
Level, relate it to other operational metrics, and
use it to interpret Contact Center scenarios.

domain_id:
contact_center_metrics
```

Every concept must have its own `learning_objective`.

The objective should make it possible to evaluate whether the learner can:

**explain → relate → apply → justify**

---

## 6. Edge Types

The MVP will initially use only two edge types.

### 6.1 `contains`

Represents membership between a domain and its concepts.

Example:

```text
Contact Center Metrics
    ── contains ──► Service Level
```

This means:

> Service Level is a concept contained within the Contact Center Metrics domain.

### 6.2 `prerequisite_for`

Represents a pedagogical dependency.

Example between domains:

```text
Contact Center Fundamentals
    ── prerequisite_for ──► Contact Center Metrics
```

Example between concepts:

```text
JSON
    ── prerequisite_for ──► API Response Interpretation
```

The first version will support relationships between:

```text
DOMAIN → DOMAIN
CONCEPT → CONCEPT
```

Additional edge types should not be introduced into the MVP without a demonstrated need.

No different edge weights will be used in the initial version.

---

## 7. Graph Relationship Policy

Relationships stored in the approved graph are the structural source of truth for the Learning Map.

The LLM must not silently add new dependencies.

If the tutor detects during training that a difficulty may depend on knowledge that is not currently represented as a prerequisite, the possible relationship should be treated as a hypothesis.

The process is:

```text
observed difficulty
        ↓
LLM identifies a possible dependency
        ↓
pedagogical hypothesis
        ↓
verification with the learner
        ↓
evidence
        ↓
later validation
        ↓
possible future addition to the graph
```

The architecture is therefore hybrid:

**approved graph = validated relationships**

**LLM = identification of possible new relationships**

A relationship hypothesized by the LLM must not automatically modify the approved graph.

---

## 8. Pedagogical Matrix

All `Concept Nodes` and `Domain Nodes` are evaluated using a shared pedagogical matrix.

The four dimensions are:

### EXPLAIN

The learner can explain the knowledge using their own words.

### RELATE

The learner can relate the knowledge to other relevant concepts.

### APPLY

The learner can use the knowledge in a new situation.

### JUSTIFY

The learner can justify the reasoning, interpretation, hypothesis, or decision used.

The matrix is common across the system.

The `learning_objective` of each node defines the specific knowledge that should be demonstrated within these dimensions.

---

## 9. Concept Assessment

The LLM may generate exercises appropriate to each concept's `learning_objective`.

The assessment structure must nevertheless remain explicit and auditable.

A complete exercise may contain four phases:

```text
PHASE 1 — EXPLAIN
Explain the concept using your own words.

PHASE 2 — RELATE
Relate the concept to other relevant knowledge.

PHASE 3 — APPLY
Use the concept in a new scenario.

PHASE 4 — JUSTIFY
Justify the interpretation or application used.
```

The four skills do not need to be evaluated in the same interaction.

For example:

```text
initial interaction
→ Explain

later interaction
→ Relate

future professional scenario
→ Apply + Justify
```

The system should also use valid evidence that emerges naturally during training or professional problem solving.

---

## 10. Binary Evidence

For the MVP, each skill can produce only two outcomes:

```text
demonstrated
not_demonstrated
```

The initial version will not use:

- mastery percentages;
- continuous scores;
- intermediate levels;
- `partial` states;
- probabilistic mastery estimates;
- confidence scores.

The objective is to keep pedagogical decisions simple, auditable, and explainable.

---

## 11. Evidence Records

Every evaluated skill should create an independent evidence record.

A minimum record may contain:

```text
node_id
skill
result
timestamp
exercise_id
```

Example:

```text
node_id: service_level
skill: apply
result: demonstrated
timestamp: 2026-08-25T14:30
exercise_id: service_level_004
```

New evidence must be appended to the history.

It must not overwrite previous evidence.

---

## 12. Compound Exercises

When a single exercise evaluates multiple skills, each skill must still be recorded separately.

Example:

On day 15:

```text
Explain → demonstrated
```

On day 16:

```text
Relate → demonstrated
```

On day 17, an integrative exercise evaluates:

```text
Explain → demonstrated
Relate → demonstrated
Apply → demonstrated
Justify → demonstrated
```

The history should preserve:

```text
EXPLAIN
15/08 → demonstrated
17/08 → demonstrated

RELATE
16/08 → demonstrated
17/08 → demonstrated

APPLY
17/08 → demonstrated

JUSTIFY
17/08 → demonstrated
```

The `exercise_id` allows multiple evidence records to be linked to the same assessment without merging the skills into a single result.

---

## 13. Evidence History

The system should preserve a minimum history for all four dimensions:

```text
Explain
Relate
Apply
Justify
```

This allows the system to distinguish between:

**current state**

and

**the evidence trajectory that produced the current state**

Example:

```text
APPLY

25/08 → demonstrated
03/09 → not_demonstrated
10/09 → demonstrated
```

Evidence should not be overwritten.

If evidence volume later becomes operationally relevant, a compaction policy may be evaluated.

Evidence compaction is outside the MVP.

---

## 14. Learner State

Learner-specific state must remain separate from the Learning Graph.

The Learning Graph describes:

> what knowledge exists and how it is related.

The Learner State describes:

> what a specific learner has demonstrated about that knowledge.

Each concept should have:

```text
status
needs_reinforcement
```

Allowed states are:

```text
learning
sufficient
mastered
```

The independent reinforcement flag is:

```text
needs_reinforcement: true | false
```

`needs_reinforcement` is not itself a mastery state.

Example:

```text
node_id: service_level

status: sufficient
needs_reinforcement: true
```

This means:

> the learner has demonstrated enough understanding to progress, but the concept should still be reinforced.

---

## 15. Initial Concept Classification Rules

Classification follows the evidence matrix.

### 15.1 Learning

When the learner demonstrates:

```text
Explain ✓
```

the state is:

```text
status = learning
needs_reinforcement = true
```

### 15.2 Sufficient

When the learner demonstrates:

```text
Explain ✓
Relate ✓
```

the state is:

```text
status = sufficient
needs_reinforcement = true
```

### 15.3 Mastered

When the learner demonstrates:

```text
Explain ✓
Relate ✓
Apply ✓
Justify ✓
```

the state is:

```text
status = mastered
needs_reinforcement = false
```

For the MVP, `sufficient` is the minimum state required for a concept to satisfy progression readiness.

---

## 16. Progression Within a Domain

Every concept contained in the current domain must reach at least:

```text
status >= sufficient
```

Reaching `mastered` is not mandatory.

Example:

```text
AHT            sufficient
ASA            mastered
Service Level  sufficient
Hold           sufficient
ACW            sufficient
Abandonment    mastered
```

This satisfies the concept-level condition for progression.

However, it does not by itself unlock the next major domain.

---

## 17. Integrative Domain Assessment

The domain itself also has a Learner State.

Its `learning_objective` evaluates whether the learner can integrate the concepts contained in the domain.

Example:

```text
DOMAIN:
Contact Center Metrics
```

An integrative activity may present:

```text
Volume          stable
ASA             increasing
Service Level   decreasing
Abandonment     increasing
AHT             stable
Hold            stable
```

The objective is not to request isolated definitions.

The learner should be able to:

```text
observe
↓
relate multiple metrics
↓
construct an interpretation
↓
formulate a hypothesis
↓
apply domain knowledge
↓
justify the conclusion
```

The domain also uses the shared matrix:

```text
Explain
Relate
Apply
Justify
```

At domain level, these dimensions evaluate the integration of multiple concepts.

---

## 18. Progression Between Major Domains

The next major domain can be unlocked only when two conditions are satisfied.

### Condition 1 — Individual concepts

Every concept in the current domain must be at least:

```text
sufficient
```

### Condition 2 — Integrative domain understanding

The `Domain Node` itself must reach at least:

```text
sufficient
```

through an integrative activity.

Therefore:

```text
all concepts >= sufficient
              +
domain >= sufficient
              ↓
NEXT DOMAIN UNLOCKED
```

`mastered` is not required for progression.

---

## 19. Adaptive Reinforcement

Concepts that progress as `sufficient` may continue to be developed later.

When a difficulty appears in a future domain, the tutor should determine whether it is related to a previous prerequisite.

The process is:

```text
current topic
      ↓
difficulty
      ↓
query prerequisite_for
      ↓
inspect Learner State
      ↓
previous gap identified
      ↓
targeted reinforcement
      ↓
new evidence
      ↓
return to original topic
```

The tutor should avoid sending the learner back through an entire domain when the difficulty is related to a specific concept.

---

## 20. Treatment of `mastered`

The `mastered` state must not be interpreted as permanently acquired knowledge.

A single later difficulty must not cause an automatic downgrade.

Initial state:

```text
status = mastered
needs_reinforcement = false
```

Later evidence:

```text
Apply → not_demonstrated
```

Initial response:

```text
status = mastered
needs_reinforcement = true
```

The tutor should provide reinforcement and gather new evidence before changing the primary mastery state.

---

## 21. Delayed Retention Reassessment

A first demonstration of:

```text
Explain ✓
Relate ✓
Apply ✓
Justify ✓
```

allows the system to classify the knowledge as:

```text
mastered
```

However, this first demonstration is not treated as definitive evidence of durable retention.

The system should record:

```text
mastered_at
```

and seek another retrieval opportunity after an interval.

For the MVP, the initial delayed retrieval window is approximately:

```text
7–10 days
```

This interval is a **project heuristic** informed by retrieval practice, distributed practice, and successive relearning principles.

It must not be presented as a universally optimal learning interval.

The interval may be reconsidered later based on evidence collected during system use.

---

## 22. Natural Reassessment

A formal assessment is not required if the concept naturally reappears in a suitable later context.

Example:

```text
mastered concept
        ↓
several days later
        ↓
new problem requires the concept
        ↓
learner retrieves and applies it correctly
        ↓
new retention evidence
```

This interaction may serve as a delayed retrieval check.

When appropriate, the system should prefer evidence obtained in new contexts rather than simply repeating the original assessment question.

---

## 23. Contradictory Evidence

Evidence history should allow the system to observe changes over time.

Example:

```text
25/08 Apply → demonstrated
03/09 Apply → not_demonstrated
```

The first later failure should initially result in:

```text
mastered
↓
needs_reinforcement = true
```

rather than an automatic downgrade.

The process should be:

```text
difficulty identified
↓
needs_reinforcement = true
↓
targeted reinforcement
↓
new interval
↓
new assessment
```

If the difficulty persists across later evidence, the state should be recalculated using the same pedagogical matrix.

Example:

```text
Explain ✓
Relate ✓
Apply ✗
Justify ✗
```

The concept may return to:

```text
status = sufficient
needs_reinforcement = true
```

The objective is to avoid two extremes:

- preserving a `mastered` state that is no longer supported by evidence;
- downgrading previously demonstrated knowledge because of a single isolated error.

---

## 24. LLM Responsibilities

Within the MVP, the LLM may:

- explain knowledge;
- generate exercises;
- generate realistic scenarios;
- ask Socratic questions;
- evaluate responses against the relevant `learning_objective`;
- classify each evaluated skill as `demonstrated` or `not_demonstrated`;
- identify possible knowledge gaps;
- propose hypotheses about missing relationships;
- provide pedagogical feedback;
- suggest targeted reinforcement;
- use evidence history to contextualize future assessments.

The LLM must not have unrestricted authority over progression.

---

## 25. Deterministic Rule Responsibilities

Explicit system rules should determine:

```text
evidence
    ↓
Learner State

Learner State
    ↓
progression

identified gap
    ↓
reinforcement requirement

all concepts >= sufficient
+
domain >= sufficient
    ↓
next domain
```

The LLM may interpret learner responses, but it must not arbitrarily decide:

> "I think the learner is ready to progress."

Progression must remain verifiable through explicit rules.

---

## 26. Separation of Responsibilities

The pedagogical architecture preserves four distinct components.

### 26.1 Learning Graph

Represents:

```text
what must be learned
+
how knowledge elements are related
```

### 26.2 Evidence History

Represents:

```text
what the learner demonstrated
+
when it was demonstrated
```

### 26.3 Learner State

Represents:

```text
the learner's current pedagogical state
```

### 26.4 Tutor Policy

Represents:

```text
how the tutor should behave
```

Pedagogical decisions result from the interaction of these layers:

```text
Learning Graph
      +
Evidence History
      +
Learner State
      +
Tutor Policy
      ↓
Pedagogical Decision
```

---

## 27. Pedagogical Decision Flow

A simplified example is:

```text
learner begins a concept
        ↓
Learning Graph provides the learning_objective
        ↓
Tutor teaches the required knowledge
        ↓
Explain activity
        ↓
evidence recorded
        ↓
Relate activity
        ↓
evidence recorded
        ↓
concept = sufficient
        ↓
remaining domain concepts continue
        ↓
all concepts >= sufficient
        ↓
integrative Domain activity
        ↓
Domain = sufficient
        ↓
next domain unlocked
        ↓
previous concept appears later
        ↓
new evidence collected
        ↓
reinforcement or consolidation
```

---

## 28. MVP Boundaries

The MVP should not initially include:

- different weights for concepts or edges;
- mastery percentages;
- continuous scores;
- intermediate states such as `partial`;
- probabilistic knowledge inference;
- automatic graph modification by the LLM;
- complex recommendation algorithms;
- a complete enterprise Knowledge Graph;
- GraphRAG;
- a mandatory graph database;
- mandatory Neo4j;
- mandatory LangGraph;
- autonomous agents modifying the Learning Map;
- automatic optimization of repetition intervals;
- advanced models of human memory;
- complex pedagogical scoring mechanisms.

These possibilities may be evaluated later only when a concrete need justifies their inclusion.

---

## 29. Technology Neutrality

This specification defines **required behavior**, not the technology that must implement it.

The first implementation may use simple structures such as:

```text
Python
JSON
YAML
SQLite
```

before graph-specific technologies are considered.

Tools such as:

```text
NetworkX
Neo4j
LangGraph
GraphRAG
```

should be adopted only if they demonstrably solve a problem that simpler implementations cannot address adequately.

Technology selection should follow the architecture and system needs, not define them prematurely.

---

## 30. First Implementation Success Criteria

The first Learning Graph implementation is considered functional when it can demonstrate, using a small set of domains and concepts, the ability to:

1. represent `Domain Nodes`;

2. represent `Concept Nodes`;

3. represent `contains` relationships;

4. represent `prerequisite_for` relationships;

5. store `learning_objectives`;

6. record evidence for `Explain`, `Relate`, `Apply`, and `Justify`;

7. preserve the temporal history of evidence;

8. calculate `learning`, `sufficient`, and `mastered`;

9. record `needs_reinforcement`;

10. verify whether every concept in a domain has reached at least `sufficient`;

11. evaluate the domain through an integrative activity;

12. unlock or block progression to the next major domain;

13. identify a previous gap related to the current topic;

14. trigger targeted reinforcement;

15. return to the original topic after reinforcement;

16. record and use delayed reassessment evidence;

17. keep Learning Graph, Learner State, Evidence History, and Tutor Policy responsibilities separated.

The goal of the first implementation is not to build the complete platform.

The goal is to demonstrate that the central pedagogical logic can be represented and executed in an explicit, verifiable, and understandable way.

---

## 31. Document Status

**Document:** `LEARNING_GRAPH_SPEC.md`
**Version:** v0.1
**Language:** English
**Use:** Public project documentation
**Status:** Approved

This document defines the first specification of the Learning Graph and pedagogical state model for the Adaptive AI Onboarding Tutor.

It should serve as a basis for:

- the initial technical architecture;
- executable representation of the Learning Map;
- Learner State structure;
- Evidence History structure;
- assessment logic;
- progression logic;
- reinforcement rules;
- delayed retention reassessment;
- the first executable prototype.

Library, database, and framework choices should follow this specification while preserving technology neutrality and protection against overbuilding.

---

## Public Project Boundary

This specification describes an independent educational and portfolio project.

Genesys Cloud is referenced as a public technology ecosystem and as the initial case-study context.

The public implementation and documentation must not contain confidential employer or client information, credentials, production data, non-public procedures, proprietary architectures, or other restricted material.
