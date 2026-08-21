# Learning Map — Adaptive AI Onboarding Tutor

## 1. Purpose

The Learning Map defines the macro-level learning progression required for the learner to move from initial onboarding toward progressively effective performance as a Data Analyst in a Genesys Cloud environment.

This document is not yet a detailed lesson plan.

Its purpose is to define:

- which domains belong to the initial onboarding period;
- which knowledge areas should be developed further afterward;
- which domains depend on others;
- which competencies may develop in parallel;
- which competencies belong to medium- and long-term professional development;
- which pedagogical principles should guide the tutor's progression decisions.

The learning journey should not be interpreted as a completely linear sequence.

Some domains may develop in parallel once the minimum knowledge required for understanding them has been established.

---

## 2. Learning Progression Principle

The tutor must use **demonstrated understanding**, rather than content exposure alone, as the basis for progression.

A domain or topic must not be considered completed simply because its content has been presented to the learner.

The learner should demonstrate a minimum ability to:

- recognize the main concepts;
- explain them in simple terms using their own words;
- connect them with previously learned concepts;
- apply the knowledge to exercises or new situations;
- formulate plausible reasoning about problems related to the domain.

Prerequisites are not mandatory entry requirements.

If a knowledge gap prevents adequate understanding of a topic, the tutor should provide supporting content before or during the learning progression.

The objective is not to require the learner to arrive already prepared for every domain. The objective is to prevent new knowledge from being built on gaps that significantly compromise understanding.

---

## 2.1 Learner Reasoning Ownership Principle

The Adaptive AI Onboarding Tutor must preserve the learner's intellectual ownership of the learning process.

When a question, exercise, case study, or problem is intended to develop or evaluate a learner competency, the tutor must not immediately provide the final answer or complete solution, even if the learner explicitly requests it.

In these situations, the tutor should prioritize:

- guiding questions;
- decomposition of the problem into smaller parts;
- identification of relevant concepts;
- progressive hints;
- analogous examples that do not directly solve the current exercise;
- requests for hypotheses and justification from the learner;
- feedback on the learner's attempts.

The objective is for the learner to construct the reasoning required to reach the solution rather than simply receive a ready-made answer.

The level of assistance should increase progressively:

**Problem**  
→ learner attempt  
→ guiding question  
→ new attempt  
→ conceptual hint  
→ new attempt  
→ problem decomposition, when necessary  
→ feedback  
→ solution refinement

The tutor may explain concepts, definitions, tools, and knowledge required to solve a problem.

However, it must distinguish between:

**teaching the knowledge required to solve the problem**

and

**performing the core reasoning on behalf of the learner.**

After the learner has produced a sufficiently developed attempt, the tutor may:

- review the response;
- identify errors;
- explain why a particular reasoning path is problematic;
- discuss alternatives;
- explain trade-offs;
- suggest tests;
- demonstrate a better solution when doing so contributes to learning consolidation.

Refusing to provide a ready-made solution must not create a pedagogical dead end.

If the learner remains unable to progress, the tutor should gradually increase the level of support until learning can continue.

The general principle is:

> Provide the minimum amount of assistance required for the learner to continue constructing their own reasoning.

---

## 3. Learning Horizons

The learning journey is initially divided into three horizons:

1. Initial Onboarding — 6 to 8 weeks;
2. Next Phase — Increased Autonomy;
3. Role Evolution — Advanced Competencies.

A domain does not need to be fully completed to belong to the onboarding period.

Some domains should begin during the first weeks and continue to develop afterward.

---

## 4. Initial Onboarding — 6 to 8 Weeks

The objective of this phase is to enable the analyst to:

- understand the main concepts used by the team;
- follow discussions related to Genesys Cloud and Contact Center operations;
- recognize problems and decisions related to client scenarios;
- understand where the data used by the team comes from;
- perform basic data manipulation;
- interpret operational metrics and descriptive statistics;
- formulate plausible hypotheses and investigation paths;
- produce or interpret simple data visualizations;
- perform support tasks under supervision.

The main domains in this phase are:

1. Contact Center Fundamentals;
2. Contact Center Metrics;
3. Genesys Cloud;
4. Genesys / Data Access;
5. Basic Applied Programming;
6. Basic Descriptive Statistics;
7. Basic Data Visualization.

---

## 5. Onboarding Macro Structure

### 5.1 Contact Center Fundamentals

**Roadmap position:** beginning of onboarding.

**Prerequisites:** no previous Contact Center knowledge required.

**Learning purpose:** establish the basic mental model of the business domain before progressing into metrics, platform concepts, and data.

The learner should develop a minimum understanding of:

- what a Contact Center is;
- customer interactions;
- agents;
- queues;
- flows;
- operational objectives;
- the basic customer interaction journey.

This domain provides the main foundation for:

- Contact Center Metrics;
- Genesys Cloud.

---

### 5.2 Contact Center Metrics

**Main prerequisite:** Contact Center Fundamentals.

**Roadmap position:** beginning of onboarding.

The objective is to enable the learner to understand how Contact Center performance can be observed and measured.

Relevant concepts include:

- ACD;
- ASA;
- Service Level;
- AHT;
- ACW;
- NPS;
- Talk;
- Hold;
- Callback;
- Abandonment;
- Overflow.

The learning process should consider two main contexts:

- operational monitoring / Control Desk;
- deeper analytical investigation / Analytics.

Contact Center Metrics and Genesys Cloud may partially develop in parallel once the initial fundamentals have been understood.

---

### 5.3 Genesys Cloud

**Main prerequisites:**

- Contact Center Fundamentals;
- basic Cloud and SaaS concepts.

**Roadmap position:** beginning and middle of onboarding.

The objective is to connect Contact Center concepts to the way they are implemented within Genesys Cloud.

The learner should progressively understand:

- the general operation of the platform;
- interaction between queues and flows;
- how an interaction is handled;
- basic familiarity with the interface;
- major product capabilities;
- different capabilities available within the platform;
- mechanisms used by Genesys Cloud to communicate and integrate with other systems.

Concepts related to the following mechanisms should also be introduced:

- REST APIs;
- Data Actions;
- Triggers;
- Hooks.

Intermediate or advanced Genesys Cloud capabilities may also be introduced when appropriate, including:

- Campaigns;
- WEM;
- Evaluations;
- WFM;
- journey-related capabilities;
- AI Scoring;
- Speech & Analytics.

Contact Center Metrics do not need to be completely mastered before Genesys Cloud learning begins.

The two domains may partially develop in parallel.

---

### 5.4 Genesys / Data Access

**Main prerequisites:**

- Contact Center Fundamentals;
- Genesys Cloud;
- understanding of the main Contact Center metrics;
- basic concepts of system integration and API consumption.

**Roadmap position:** middle of onboarding.

The objective is to connect platform operation with the data used by the team.

The learner should begin to understand how information available in Genesys Cloud can be retrieved and used for analysis.

Relevant APIs and structures include:

- Conversations Details Query;
- Conversations Attributes Search;
- Routing Skills;
- Queues;
- Flows;
- Users;
- Wrap-ups;
- Divisions;
- Outcomes;
- Data Tables;
- Transcript Search;
- Users Details Query.

Supporting concepts such as REST, JSON, request/response structures, and other integration fundamentals may be taught by the tutor whenever knowledge gaps are identified.

---

## 6. Parallel Technical Competencies During Onboarding

Programming, Statistics, and Data Visualization should not necessarily begin only after the learner completes the Contact Center and Genesys domains.

These competencies should progressively develop in parallel with business, platform, and data knowledge.

Whenever appropriate, their learning should be connected to problems that resemble the professional context.

---

### 6.1 Basic Applied Programming

**Phase:** begins during onboarding and continues into the next phase.

The initial objective is not to develop an autonomous Python software developer.

During onboarding, the learner should develop sufficient ability to:

- understand simple code;
- use basic Python structures;
- perform basic data manipulation;
- use Pandas for simple operations;
- understand common data structures used in analysis;
- understand and execute basic SQL applied to data;
- follow scripts used by the team;
- perform small data-processing tasks under supervision.

Foundational concepts such as programming logic, variables, loops, data structures, or SQL fundamentals should be provided as supporting content when knowledge gaps are identified.

---

### 6.2 Basic Descriptive Statistics

**Phase:** onboarding.

The objective is to enable appropriate interpretation of information produced by metrics and analyses.

Concepts developed during this phase should include:

- mean;
- median;
- percentiles;
- variance;
- correlation;
- basic interpretation of distributions.

The learner should begin to understand that a single measure does not necessarily provide an adequate description of the behavior of a dataset.

Statistics should be developed as a tool for reasoning about data rather than merely as a collection of formulas.

---

### 6.3 Basic Data Visualization

**Phase:** begins during onboarding and continues afterward.

The initial objective is to enable the learner to transform data and metrics into understandable visual representations.

Fundamentals introduced during onboarding should include:

- chart interpretation;
- basic visualization selection;
- bar charts;
- column charts;
- time series;
- scatter plots;
- introductory Gestalt principles;
- visual communication;
- basic narrative construction for an analysis.

Tools such as Matplotlib and Streamlit may be introduced progressively according to the needs of the learning activities.

---

## 7. Relationships Between Onboarding Domains

The initial macro-level dependency structure is:

**Contact Center Fundamentals**  
→ Contact Center Metrics

**Contact Center Fundamentals**  
→ Genesys Cloud

**Genesys Cloud**  
→ Genesys / Data Access

**Contact Center Metrics**  
→ Genesys / Data Access

**Basic Programming**  
→ manipulation of data retrieved from Genesys Cloud

**Basic Statistics**  
→ interpretation of metrics and data

**Genesys / Data Access + Programming + Statistics**  
→ Data Analysis

**Data Analysis + Data Visualization**  
→ Ad-hoc Analysis

**Ad-hoc Analysis + Business Knowledge**  
→ Decision Support

This structure does not represent a rigid sequence.

After the initial fundamentals are established, several learning paths may progress in parallel.

---

## 8. Conceptual Representation of the Onboarding Path

```text
                CONTACT CENTER FUNDAMENTALS
                           |
                +----------+----------+
                |                     |
                v                     v
        CONTACT CENTER          GENESYS CLOUD
            METRICS                  |
                |                     |
                +----------+----------+
                           |
                           v
                GENESYS / DATA ACCESS
                           |
                +----------+----------+
                |                     |
                v                     v
          PROGRAMMING            STATISTICS
                |                     |
                +----------+----------+
                           |
                           v
                    DATA ANALYSIS
                           |
                           v
                 DATA VISUALIZATION
                           |
                           v
                    AD-HOC ANALYSIS
                           |
                           v
                    DECISION SUPPORT