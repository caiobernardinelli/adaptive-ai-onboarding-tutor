# Adaptive AI Onboarding Tutor

> An auditable AI onboarding tutor for Contact Center, Genesys Cloud, Data Analytics, and Customer Experience roles, built around explicit learning graphs, prerequisite-aware progression, structured evidence, guided reasoning, and source-grounded knowledge retrieval.

## Overview

The **Adaptive AI Onboarding Tutor** is an AI and Data Engineering project exploring how a digital tutor can support professional onboarding in a complex technical and business environment.

The public reference case focuses on a **Junior Data Analyst working with Contact Center analytics and Genesys Cloud**.

The project is intentionally more than a document question-answering chatbot. It combines:

- role competency modeling;
- a versioned Learning Graph;
- prerequisite-aware progression;
- learner-specific Evidence History;
- deterministic Learner State calculation;
- guided reasoning and progressive assistance;
- application-based learning activities;
- source-grounded knowledge retrieval;
- explicit separation between LLM interpretation and application decisions.

The initial onboarding target is a **6–8 week learning journey**.

---

## Problem

Technical onboarding often requires learning several layers at the same time:

```text
business domain
→ platform
→ terminology
→ operational metrics
→ data access
→ programming
→ analysis
→ communication
→ decision support
```

A new analyst may already know Python, SQL, or visualization tools and still struggle to understand how those tools connect to a real operational environment.

A conventional RAG assistant can retrieve documentation, but retrieval alone does not answer:

- What should this learner study next?
- Which prerequisite is missing?
- Has the learner actually demonstrated understanding?
- Which topics are eligible now?
- Should a previously learned topic be reinforced?
- Can the system explain why progression was allowed or blocked?

This project treats those questions as **learning-system and software-architecture problems**.

---

## Why Not Just a RAG Chatbot?

RAG can answer:

> What does this concept mean?

The learning system must also answer:

> What is this learner ready to learn next, and what evidence supports that decision?

The architecture therefore separates the **knowledge layer** from the **pedagogical decision layer**.

RAG, embeddings, semantic retrieval, and source attribution may support the tutor, but **RAG is not the progression architecture itself**.

---

## Core Architecture

```text
Learning Graph YAML
        ↓
Learning Graph Loader
        ↓
Graph Validator
        ↓
 Progression Engine
   ├── State Calculation
   └── Progression Decision
        ↕
 Tutor Orchestrator
    ↙          ↘
  LLM      Data Access Layer
                  ↓
                SQLite
```

The central boundary is:

```text
LLM interprets
      ↓
application validates
      ↓
deterministic rules decide
      ↓
Data Access Layer persists
```

The LLM may generate teaching content, interpret natural-language responses, and return structured evidence. It does **not** directly decide persisted learner state, prerequisite satisfaction, active learning nodes, or path completion.

---

## Learning Model

Every Concept and Domain can be evaluated through four pedagogical dimensions:

```text
Explain
Relate
Apply
Justify
```

The MVP uses binary evidence:

```text
demonstrated
not_demonstrated
```

Minimum progression threshold:

```text
Explain ✓
Relate  ✓
→ sufficient
```

Deeper consolidation:

```text
Explain ✓
Relate  ✓
Apply   ✓
Justify ✓
→ mastered
```

`mastered` is not required for formal progression.

A Domain is complete only when:

```text
all Concepts >= sufficient
+
Domain integrative evidence >= sufficient
```

---

## Learner Reasoning Ownership

The tutor should not replace the learner's reasoning when reasoning is itself the learning objective.

Preferred assistance ladder:

```text
learner attempt
→ guiding question
→ conceptual hint
→ decomposition
→ analogous example
→ more explicit help when necessary
```

The rule is not “never give an answer.” The rule is:

> provide the minimum assistance required for the learner to continue constructing the reasoning.

---

## Reference Learning Graph v0.2

The approved public reference structure contains **7 Domains and 94 Concepts**:

| Domain | Concepts |
| --- | ---: |
| Contact Center Fundamentals | 9 |
| Contact Center Metrics | 23 |
| Genesys Cloud | 23 |
| Genesys / Data Access | 11 |
| Programming | 12 |
| Statistics | 7 |
| Data Visualization | 9 |
| **Total** | **94** |

Macro dependencies:

```text
Contact Center Fundamentals
        ├──► Contact Center Metrics
        └──► Genesys Cloud

Contact Center Metrics ───► Genesys / Data Access
Genesys Cloud ─────────────► Genesys / Data Access

Programming        = independent Root Domain
Statistics         = independent Root Domain
Data Visualization = independent Root Domain
```

The preferred entry point is `Contact Center Fundamentals`.

The current schema supports only:

```text
contains
prerequisite_for
```

Concept-to-Concept prerequisites are allowed only inside the same Domain.

---

## What Changed in v0.2

The reference Learning Graph was expanded and reviewed before YAML implementation.

Notable changes include:

- ACD modeled as a Contact Center fundamental rather than as a metric;
- agent / ACD skills added to the fundamentals layer;
- expanded Contact Center volume, wait, handling, resolution, satisfaction, effort, and flow-performance metrics;
- Flow Disconnect volume and percentage included;
- derived flow metrics represented without hard-coded employer-specific formulas;
- Genesys Cloud `Divisions` modeled as an organization/access-control concept;
- terminology aligned around Webhooks and Notifications, Speech and Text Analytics, Virtual Agent, and Analytics Workspace / Performance Dashboards;
- Platform Data Access updated around conversation, participant-attribute, user, queue, flow, transcript, outcome, and related structures;
- Programming expanded with lists, dictionaries, sets, NumPy arrays, Pandas, SQL, and script reading;
- introductory `p-value` added to Statistics;
- operational Workforce Management, labor-regulation topics, Machine Learning, and advanced AI kept **outside the initial onboarding graph**.

A product-level WFM overview remains in the Genesys Cloud Domain so the learner can recognize where the product fits in the platform.

---

## Version Domains

The project intentionally separates version identifiers:

```text
Product / MVP design: v0.1
YAML schema:          0.1
Learning Graph:       0.2
Public docs milestone: v0.2
```

A Learning Graph content change does not automatically require a schema change.

Once a graph version is used by a learner enrollment, that graph version should be treated as immutable.

---

## Current Engineering Milestone

The current implementation milestone is deliberately constrained to:

```text
YAML
→ Loader
→ Validator
→ Tests
```

The intended implementation order is:

```text
YAML schema
→ Graph Loader
→ Graph Validator
→ SQLite schema
→ Data Access Layer
→ State Calculation
→ Progression Decision
→ Tutor Orchestrator
→ LLM Integration
```

The repository should not claim persistence, progression, orchestration, RAG, or agent capabilities as implemented until the corresponding code and tests exist.

---

## Repository Structure

```text
adaptive-ai-onboarding-tutor/
├── README.md
├── CHANGELOG.md
├── docs/
│   ├── PRODUCT.md
│   ├── ROLE_PROFILE.md
│   ├── LEARNING_MAP.md
│   ├── TUTOR_POLICY.md
│   ├── LEARNING_GRAPH_SPEC.md
│   ├── PROJECT_OVERVIEW.md
│   ├── ARCHITECTURE.md
│   └── RELEASE_NOTES_v0_2.md
├── learning_graphs/
├── src/
│   └── learning_graph/
│       ├── loader.py
│       └── validator.py
└── tests/
    ├── test_loader.py
    └── test_validator.py
```

Some implementation directories will appear only when the corresponding milestone is committed.

---

## Public / Private Boundary

This repository is a public portfolio adaptation of a real professional onboarding problem.

It intentionally excludes:

- employer-internal documents;
- customer or client data;
- client-specific configurations;
- credentials, private endpoints, and infrastructure secrets;
- proprietary operational procedures;
- confidential formulas or business rules.

Public vendor concepts such as Genesys Cloud products, APIs, and documented platform terminology are used only as publicly documented technical context.

---

## What This Project Demonstrates

Engineering:

- Python application design;
- YAML modeling and validation;
- DAG and dependency reasoning;
- deterministic rule engines;
- evidence and state modeling;
- persistence boundaries;
- structured LLM outputs;
- automated testing;
- versioned technical documentation.

AI-product design:

- adaptive tutoring with explicit constraints;
- explainable progression;
- evidence-based learning decisions;
- separation of deterministic and probabilistic responsibilities;
- responsible use of LLMs in a professional learning workflow.

---

## Status

**Learning Graph v0.2 design baseline approved.**

Current work:

```text
final YAML v0.2
→ Loader contract
→ Loader tests
→ Graph Validator
→ Validator tests
```

The project is under active development. Documentation may describe target behavior, but implemented behavior is claimed only after code and tests exist.
