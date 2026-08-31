# Learning Graph Specification — Adaptive AI Onboarding Tutor

## 1. Purpose

The Learning Graph represents:

```text
what knowledge exists
+
how knowledge elements depend on one another
```

Learner-specific progress is deliberately stored outside the graph.

The conceptual architecture is:

```text
Learning Graph
+
Learner State
+
Evidence History
+
Tutor Policy
→ Pedagogical Decision
```

## 2. Graph Principles

1. Learning is not modeled as a rigid sequence of lessons.
2. Domains represent broad competency areas.
3. Concepts represent specific units of knowledge.
4. Explicit prerequisites control structural eligibility.
5. The learner does not need to reach `mastered` before progressing.
6. Every Concept in the active Domain must reach at least `sufficient`.
7. The Domain itself must also reach at least `sufficient` through integrative evidence.
8. Later weakness can trigger targeted reinforcement without erasing historical evidence.
9. Learner State remains separate from graph structure.
10. The LLM may interpret evidence but cannot silently modify the approved graph.

## 3. YAML Root Contract

The schema permits exactly these root fields:

```text
schema_version
graph_id
graph_version
primary_entry_domain
domains
concepts
relationships
```

Example identity:

```yaml
schema_version: "0.1"
graph_id: junior_data_analyst_onboarding
graph_version: "0.2"
primary_entry_domain: contact_center_fundamentals
```

`schema_version` and `graph_version` are different version domains.

## 4. Node Contract

The MVP contains two node types.

### 4.1 Domain

Every Domain has exactly:

```text
id
name
description
learning_objective
```

A Domain learning objective should be integrative.

### 4.2 Concept

Every Concept also has exactly:

```text
id
name
description
learning_objective
```

**There is no `domain_id` field in the v0.1 schema.**

Concept membership exists only through:

```text
DOMAIN ── contains ──► CONCEPT
```

Every Concept must receive exactly one incoming `contains`.

Every Domain must contain at least two Concepts.

## 5. ID Rules

Node IDs are stable identities.

They must:

- use lowercase `snake_case`;
- contain no spaces;
- contain no accents;
- be globally unique across Domain and Concept Nodes.

`name` is presentation text and may change independently when a wording improvement does not change node identity.

## 6. Relationship Contract

The MVP uses only:

```text
contains
prerequisite_for
```

Every relationship has exactly:

```text
from
to
type
```

### 6.1 `contains`

Allowed direction:

```text
DOMAIN → CONCEPT
```

Every Concept must receive exactly one.

### 6.2 `prerequisite_for`

Direction:

```text
PREREQUISITE → DEPENDENT
```

Allowed:

```text
DOMAIN → DOMAIN
CONCEPT → CONCEPT
```

Rejected:

```text
DOMAIN → CONCEPT
CONCEPT → DOMAIN
```

In the MVP, Concept prerequisites are allowed only when both Concepts belong to the **same Domain**.

No self-reference is allowed.

The prerequisite graph must be acyclic.

## 7. Root Nodes

A Root Domain has no incoming Domain-level `prerequisite_for`.

Multiple Root Domains are allowed.

The graph has exactly one `primary_entry_domain`, and it must reference a valid Root Domain.

A Root Concept is a Concept with no incoming Concept-level prerequisite inside its Domain.

A Root Concept is not an orphan as long as it has its required `contains` relationship.

## 8. Concept Layers

Layers are derived at runtime.

```text
if no incoming prerequisite:
    layer = 0
else:
    layer = 1 + max(layer of direct prerequisites)
```

`layer` and `order` are **not** stored in the YAML.

Within an active Domain, formal Concept selection must prioritize the lowest incomplete layer.

## 9. Evidence Model

The pedagogical dimensions are:

```text
explain
relate
apply
justify
```

Evidence is binary:

```text
demonstrated
not_demonstrated
```

Evidence History is append-only.

A conceptual evidence record includes:

```text
evidence_id
activity_id
node_id
skill
result
timestamp
```

The latest evidence does not delete historical evidence.

## 10. Learner State

Persisted states:

```text
learning
sufficient
mastered
```

`not_started` is inferred when no Learner State exists for a graph Node in an enrollment.

Independent flag:

```text
needs_reinforcement: true | false
```

Thresholds:

```text
Explain ✓ + Relate ✓
→ sufficient

Explain ✓ + Relate ✓ + Apply ✓ + Justify ✓
→ mastered
```

## 11. Domain Completion

A Domain is formally complete only when:

```text
every Concept >= sufficient
+
Domain >= sufficient through integrative evidence
```

`mastered` is not required for progression.

## 12. Graph Relationship Policy

The approved graph is the structural source of truth.

The LLM may identify a possible missing dependency, but that is only a pedagogical hypothesis.

```text
observed difficulty
→ possible dependency
→ hypothesis
→ verification
→ evidence
→ later review
→ possible future graph version
```

The LLM does not edit the graph at runtime.

## 13. Validator Contract

The Graph Validator must check, at minimum:

1. `schema_version` exists and has the correct type;
2. `graph_id` exists and is valid;
3. `graph_version` exists and is valid;
4. `primary_entry_domain` exists;
5. `domains` is a list;
6. `concepts` is a list;
7. `relationships` is a list;
8. there are no unknown root fields;
9. at least one Domain exists;
10. all IDs are valid;
11. all IDs are globally unique;
12. every Node has `name`;
13. every Node has `description`;
14. every Node has `learning_objective`;
15. required text fields are non-empty;
16. every Domain contains at least two Concepts;
17. every Concept receives exactly one `contains`;
18. `contains` always follows `DOMAIN → CONCEPT`;
19. relationship IDs reference existing Nodes;
20. relationship type is allowed;
21. every `(from, to, type)` tuple is unique;
22. prerequisite self-reference is rejected;
23. `DOMAIN → CONCEPT` prerequisites are rejected;
24. `CONCEPT → DOMAIN` prerequisites are rejected;
25. Concept prerequisites stay inside one Domain;
26. prerequisites contain no cycles;
27. `primary_entry_domain` exists;
28. `primary_entry_domain` is a Domain;
29. `primary_entry_domain` is a Root Domain.

The Validator should collect all detectable semantic validation errors in one run.

Minimum error structure:

```text
code
path
message
```

YAML syntax errors are Loader/parser failures and occur before graph validation.

## 14. Reference Graph v0.2

The public reference graph contains:

```text
7 Domains
94 Concepts
94 contains relationships
4 Domain prerequisite_for relationships
106 Concept prerequisite_for relationships
204 total relationships
```

Root Domains:

```text
contact_center_fundamentals
programming
statistics
data_visualization
```

Preferred entry:

```text
contact_center_fundamentals
```

## 15. Versioning

Once a Learning Graph version is used by an enrollment, it should be treated as immutable.

Material changes to:

- Domains;
- Concepts;
- relationships;
- learning objectives;

require a new `graph_version`.

A schema change is required only when the technical YAML contract itself changes.

## 16. Public Adaptation Boundary

The public project preserves architecture, learning methodology, graph design, and public technology concepts.

It does not publish employer-specific documents, client information, private infrastructure, or confidential operational rules.
