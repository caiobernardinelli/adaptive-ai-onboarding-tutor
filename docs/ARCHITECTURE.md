# Technical Architecture

## Objective

The system separates concerns that are often collapsed into one LLM prompt:

```text
knowledge structure
learner state
evidence history
progression rules
natural-language tutoring
```

The design goal is **auditability**.

The system should be able to explain why a learning node is:

- eligible;
- blocked;
- sufficient;
- mastered;
- in need of reinforcement.

## Main Components

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

## Learning Graph

Stores stable, versioned learning structure:

- Domains;
- Concepts;
- `contains`;
- `prerequisite_for`;
- descriptions;
- learning objectives.

It does not store learner-specific progress.

## Loader

Responsible only for:

- opening the file;
- reading UTF-8 text;
- YAML parsing;
- returning the parsed Python structure.

A missing file is a loading failure.

Malformed YAML is a parsing failure.

Syntactically valid but structurally invalid content belongs to the Validator.

## Graph Validator

Applies project-specific structural and semantic rules after parsing.

Validation errors must support at least:

```text
code
path
message
```

The Validator should collect all detectable semantic errors in one execution.

## Evidence History

Evidence is append-only and records what the learner demonstrated over time.

The LLM may generate a structured evidence candidate, but the application validates the candidate before persistence.

## State Calculation

Deterministically calculates learner state from validated evidence.

The LLM does not directly set:

```text
learning
sufficient
mastered
needs_reinforcement
```

## Progression Decision

Determines what is structurally eligible based on:

- Domain prerequisites;
- Concept prerequisites;
- learner state;
- lowest incomplete Concept layer;
- Domain completion;
- reinforcement and retention rules.

## Tutor Orchestrator

Coordinates:

- the active learning context;
- eligible nodes;
- learning activities;
- LLM calls;
- structured evidence;
- feedback.

The Orchestrator may choose among structurally eligible options, but it may not bypass the Progression Engine.

## LLM Boundary

The LLM may:

- explain;
- ask questions;
- create examples and learning activities;
- interpret natural-language answers;
- produce structured evidence candidates;
- give feedback.

The LLM may not directly decide persisted learner state, active path nodes, prerequisite satisfaction, or enrollment completion.

## Data Access Layer

Owns reads and writes to persistence.

There is no direct LLM-to-database write path.

## Initial Technology Choices

```text
Python
YAML
SQLite
LLM API
```

Not required for the first MVP:

```text
Neo4j
NetworkX
LangGraph
GraphRAG
SQLAlchemy
vector database
multi-agent architecture
```

## Implementation Order

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

## Current Milestone

```text
YAML → Loader → Validator → Tests
```

The project deliberately avoids advancing to persistence or advanced AI orchestration before this contract is tested.

## Versioning Rule

Once a graph version is used by an enrollment, material graph changes require a new `graph_version`.

This preserves the interpretability of historical learner evidence and state.
