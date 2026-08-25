# Changelog

All notable changes to this project will be documented in this file.

The project is currently in early development. Entries are organized chronologically to document the evolution of product, learning architecture, and technical implementation.

## 2026-08-25

### Added

- Defined the initial Learning Graph specification.
- Introduced Domain Nodes and Concept Nodes for hierarchical learning representation.
- Defined `contains` and `prerequisite_for` as the initial graph relationships.
- Established concept-level and domain-level learning objectives.
- Formalized the Explain, Relate, Apply, and Justify pedagogical evidence matrix.
- Defined binary `demonstrated` and `not_demonstrated` evidence for the MVP.
- Introduced temporal Evidence History for learner assessment.
- Defined `learning`, `sufficient`, and `mastered` learner states.
- Added an independent `needs_reinforcement` mechanism.
- Defined concept-level and integrative domain progression requirements.
- Added targeted prerequisite reinforcement and return-to-context behavior.
- Introduced delayed retention reassessment using an initial 7–10 day project heuristic.
- Separated Learning Graph, Evidence History, Learner State, Tutor Policy, and deterministic progression responsibilities.
- Established technology neutrality for the first graph implementation.
- Explicitly deferred Neo4j, LangGraph, GraphRAG, graph databases, and advanced recommendation logic until justified by implementation needs.

## 2026-08-21

### Added

- Defined the initial product problem, target user, scope, and success criteria.
- Defined the competency profile for the initial Junior Data Analyst use case.
- Designed the macro learning progression for a 6–8 week onboarding period.
- Separated initial onboarding, autonomy development, and advanced role evolution.
- Introduced prerequisite-aware learning progression.
- Defined the Learner Reasoning Ownership Principle to preserve active problem-solving during tutoring.
- Established Contact Center Fundamentals, Contact Center Metrics, Genesys Cloud, and Genesys Data Access as core onboarding domains.
- Added basic Programming, Statistics, and Data Visualization as parallel onboarding competencies.
- Positioned Machine Learning and Artificial Intelligence as later stages of professional development.
- Established the distinction between pedagogical progression and future RAG-based knowledge retrieval.
- Defined the initial tutor behavior policy.
- Formalized direct-answer rules and the Learner Reasoning Ownership Principle.
- Defined a progressive assistance ladder for guided problem solving.
- Added explicit error-correction and learning-progression criteria.
- Defined prerequisite recovery and return-to-context behavior.
- Established a source hierarchy for Genesys Cloud and external technologies.
- Added software-version-aware official documentation rules.
- Defined uncertainty and non-fabrication requirements.
- Defined how real professional problems and urgent situations should be handled pedagogically.
- Established operational and confidentiality boundaries for the tutor.
