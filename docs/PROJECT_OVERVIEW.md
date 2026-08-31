# Public Project Overview

## Purpose

Adaptive AI Onboarding Tutor is a learning-system engineering project designed to support role-specific professional onboarding through explicit knowledge structure, learner evidence, deterministic progression, and LLM-assisted teaching.

The public reference case uses a Junior Data Analyst working with Contact Center analytics and Genesys Cloud.

## Product Hypothesis

A useful onboarding tutor should combine:

```text
explicit knowledge structure
+
learner-specific evidence
+
deterministic progression rules
+
LLM-based teaching and interpretation
```

rather than delegating the complete learning policy to an LLM.

## Why the Problem Is Interesting

The learner may need to understand business concepts, operational metrics, a SaaS platform, APIs, Python, SQL, statistics, and visualization at the same time.

The software therefore needs to distinguish:

```text
what exists in the curriculum
what the learner has demonstrated
what is currently allowed
what the tutor should do next
```

Those responsibilities are represented by different system components.

## MVP Learning Outcomes

The initial path is designed so the learner can progressively:

1. recognize role-relevant terminology;
2. explain concepts using their own words;
3. relate concepts to previously learned knowledge;
4. apply knowledge in unfamiliar situations;
5. justify an interpretation or proposed approach;
6. revisit weak knowledge without restarting an entire Domain.

## Explicit Non-Goals

The first MVP does not require:

- probabilistic mastery scoring;
- hidden confidence percentages;
- autonomous graph mutation by an LLM;
- GraphRAG;
- a graph database;
- multi-agent orchestration;
- enterprise cloud infrastructure;
- unrestricted tool-using agents.

These can be reconsidered only when the simpler design demonstrates a concrete limitation.

## Current Baseline

The approved reference graph v0.2 contains:

```text
7 Domains
94 Concepts
204 relationships
```

The technical YAML schema remains version `0.1`.

Operational WFM, applicable labor-regulation knowledge, Machine Learning, and advanced Artificial Intelligence are intentionally post-onboarding.

## Current Engineering Milestone

```text
YAML → Loader → Validator → Tests
```

Persistence and LLM orchestration follow only after the Learning Graph contract is stable.

## Confidentiality Boundary

The repository is a public portfolio adaptation. It excludes internal employer documents, client data, client-specific formulas, credentials, private endpoints, proprietary procedures, and non-public configurations.

Genesys Cloud terminology is used only as public technical context.
