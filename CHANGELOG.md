# Changelog

All notable changes to this project will be documented in this file.

The project is currently in early development. Entries are organized chronologically to document the evolution of product, learning architecture, and technical implementation.


### 3. CHANGELOG

```markdown
## 2026-09-03

### Added

- Added the executable public Learning Graph v0.2.
- Added the Learning Graph Loader and deterministic Graph Validator.
- Added 38 automated tests covering Loader behavior, Validator rules, and full public Learning Graph integration.
- Added the initial SQLite persistence foundation using Python's standard `sqlite3` module.
- Added `learners`, `enrollments`, and `learner_progress` tables.
- Added foreign-key integrity for learner/enrollment relationships.
- Added a partial unique index enforcing at most one active enrollment per learner, graph, and graph version.
- Added a public database bootstrap script using `adaptive_onboarding_tutor.db`.
- Added Git rules excluding runtime SQLite database files.

### Changed

- Converted public Validator messages, comments, fixtures, and tests to English while preserving the approved validation rules and error codes.
- Adapted the reference Learning Graph to a public English portfolio version without employer-internal content.
- Updated the implementation milestone from Learning Graph validation to the SQLite persistence foundation.

### Verification

- `38 passed` for the Learning Graph, Loader, Validator, and integration test suite.
- SQLite bootstrap manually verified with foreign keys enabled.
- Verified creation of `learners`, `enrollments`, and `learner_progress`.
- Verified `ux_enrollments_one_active_per_graph_version`.
- Confirmed runtime `.db` files are excluded from version control.

### Next engineering milestone

- Automated persistence tests.
- `learner_state`.
- Data Access Layer.

## 2026-08-31

### Added

- Consolidated the public Learning Graph v0.2 baseline with 7 Domains and 94 Concepts.
- Added formal Concept prerequisite relationships and runtime-derived Concept-layer behavior.
- Added agent / ACD skills and expanded Contact Center metric coverage.
- Added Flow Disconnect volume and percentage, Customer Effort Score, and project-defined derived flow-performance concepts.
- Added Genesys Cloud Divisions, Webhooks and Notifications, Virtual Agent, Speech and Text Analytics, Sentiment, Topics, Containment, and Analytics Workspace / Performance Dashboards.
- Expanded Programming with Python lists, dictionaries, sets, NumPy arrays, Pandas, SQL, and script-reading concepts.
- Added introductory p-value to the onboarding Statistics Domain.
- Added public architecture and project-overview documentation.
- Added a public/private confidentiality boundary for the portfolio repository.

### Changed

- Moved ACD from Contact Center Metrics to Contact Center Fundamentals.
- Updated the Data Access model to avoid duplicating Divisions as a formal Concept.
- Updated `Conversations Attributes Search` to `Conversation Participant Attributes Search`.
- Removed `domain_id` from the Learning Graph Concept schema; Concept membership is represented only through `contains`.
- Moved operational Workforce Management to post-onboarding while keeping a product-level WFM overview inside Genesys Cloud.
- Kept Machine Learning and advanced Artificial Intelligence outside the initial onboarding graph.
- Clarified version separation among Product/MVP v0.1, YAML schema 0.1, Learning Graph 0.2, and public documentation milestone v0.2.

### Current engineering milestone

- `YAML → Loader → Validator → Tests`.

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
