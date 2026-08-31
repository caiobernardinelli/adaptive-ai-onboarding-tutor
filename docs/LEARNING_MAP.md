# Learning Map — Adaptive AI Onboarding Tutor

## 1. Purpose

The Learning Map defines the formal learning structure for the public reference onboarding path.

The reference learner is a Junior Data Analyst in a Contact Center / Genesys Cloud analytics context.

The map defines:

- formal onboarding Domains;
- formal Concepts;
- approved prerequisite relationships;
- parallel Root Domains;
- post-onboarding boundaries.

It is not a rigid lesson sequence. Runtime progression is derived from graph prerequisites, learner evidence, and deterministic progression rules.

## 2. Learning Principle

Progression is based on **demonstrated understanding**, not content exposure.

The common pedagogical dimensions are:

```text
Explain
Relate
Apply
Justify
```

`Explain + Relate` is the minimum threshold for `sufficient`.

`Apply + Justify` are additionally required for `mastered`.

## 3. Onboarding Domains

The Learning Graph v0.2 contains seven formal Domains:

1. Contact Center Fundamentals;
2. Contact Center Metrics;
3. Genesys Cloud;
4. Genesys / Data Access;
5. Programming;
6. Statistics;
7. Data Visualization.

Operational WFM, labor-regulation topics, Machine Learning, and advanced AI are post-onboarding.

## 4. Domain Inventory

### 4.1 Contact Center Fundamentals — 9 Concepts

- Definition of a Contact Center;
- Customer Interaction / Service;
- Agents;
- Queues;
- Flows;
- Operational Objectives;
- Basic Interaction Journey;
- ACD — Automatic Call Distribution;
- Agent / ACD Skills.

### 4.2 Contact Center Metrics — 23 Concepts

- Offered;
- Answer / Answered;
- Abandonment;
- Flow-out;
- Flow Rate;
- Flow Disconnect — Volume;
- Flow Disconnect — Percentage;
- Flow Retention;
- Overflow;
- Answer %;
- Abandon %;
- ASA — Average Speed of Answer;
- Average Wait;
- Service Level;
- Talk Time;
- Hold Time;
- ACW — After Call Work;
- AHT — Average Handle Time;
- Repeat Contact;
- FCR — First Contact Resolution;
- CSAT — Customer Satisfaction;
- Customer Effort Score;
- NPS — Net Promoter Score.

`Flow Rate` and `Flow Retention` are project-defined derived operational concepts. Their formulas are not assumed to be universal and are not hard-coded in the graph.

### 4.3 Genesys Cloud — 23 Concepts

- General Platform Operation;
- Basic Genesys Interface;
- Queue / Flow Interaction;
- How an Interaction Works in Genesys;
- Main Genesys Products;
- Platform Capabilities;
- Divisions — Organization and Access Control;
- Integration Mechanisms;
- Genesys Cloud REST APIs;
- Data Actions;
- Triggers;
- Webhooks and Notifications;
- Campaigns;
- WEM — Workforce Engagement Management;
- Evaluations;
- WFM — Product Overview;
- Virtual Agent Fundamentals;
- Speech and Text Analytics;
- Sentiment;
- Topics / Topic Spotting;
- AI Scoring;
- Containment;
- Analytics Workspace and Performance Dashboards.

### 4.4 Genesys / Data Access — 11 Concepts

- Conversations Details Query;
- Conversation Participant Attributes Search;
- Routing Skills;
- Queues;
- Flows;
- Users;
- Wrap-ups;
- Outcomes;
- Data Tables;
- Transcript Search;
- Users Details Query.

Division data can be used through Data Access activities without creating a second `Divisions` Node.

### 4.5 Programming — 12 Concepts

- Basic Python Structures;
- Reading Simple Code;
- Reading Python Lists;
- Reading Python Dictionaries;
- Reading Python Sets;
- Reading NumPy Arrays;
- Data Structures for Analysis;
- Basic Data Manipulation;
- Basic Pandas;
- Basic SQL;
- Reading Team Scripts;
- Small Supervised Data Manipulations.

### 4.6 Statistics — 7 Concepts

- Mean;
- Median;
- Percentiles;
- Variance;
- Correlation;
- Basic Distribution Interpretation;
- p-value.

### 4.7 Data Visualization — 9 Concepts

- Chart Interpretation;
- Bar Charts;
- Column Charts;
- Time Series;
- Scatter Plots;
- Basic Visualization Selection;
- Introductory Gestalt Principles;
- Visual Communication;
- Simple Analytical Narrative.

Total:

```text
7 Domains
94 Concepts
```

## 5. Approved Domain Relationships

```text
Contact Center Fundamentals
    prerequisite_for
Contact Center Metrics

Contact Center Fundamentals
    prerequisite_for
Genesys Cloud

Contact Center Metrics
    prerequisite_for
Genesys / Data Access

Genesys Cloud
    prerequisite_for
Genesys / Data Access
```

Independent Root Domains:

```text
Programming
Statistics
Data Visualization
```

Preferred entry point:

```text
Contact Center Fundamentals
```

## 6. Approved Concept Prerequisite Structure

Every line below represents exactly one `CONCEPT → prerequisite_for → CONCEPT` relationship in the YAML. The public documentation lists each edge explicitly to avoid ambiguity between a dependency fan-out and a sequential chain.

### 6.1 Contact Center Fundamentals — 12 edges

```text
Definition of a Contact Center → Customer Interaction / Service
Definition of a Contact Center → Agents
Definition of a Contact Center → Queues
Definition of a Contact Center → Flows
Definition of a Contact Center → Operational Objectives

Customer Interaction / Service → Basic Interaction Journey
Queues → Basic Interaction Journey
Flows → Basic Interaction Journey

Agents → ACD
Queues → ACD

Agents → Agent / ACD Skills
ACD → Agent / ACD Skills
```

### 6.2 Contact Center Metrics — 30 edges

```text
Offered → Answered
Offered → Abandonment
Offered → Flow-out
Offered → Overflow

Offered → Flow Rate
Flow-out → Flow Rate

Flow Disconnect Volume → Flow Disconnect Percentage

Flow Disconnect Volume → Flow Retention
Flow Disconnect Percentage → Flow Retention

Offered → Answer %
Answered → Answer %

Offered → Abandon %
Abandonment → Abandon %

Answered → ASA

Answered → Average Wait
Abandonment → Average Wait
Flow-out → Average Wait

Answered → Service Level
Offered → Service Level

Answered → Talk Time
Answered → Hold Time
Answered → ACW

Talk Time → AHT
Hold Time → AHT
ACW → AHT

Answered → Repeat Contact

Answered → FCR
Repeat Contact → FCR

Answered → CSAT
Answered → NPS
```

Customer Effort Score remains a Root Concept inside the Metrics Domain because this graph does not require another metric to be `sufficient` before CES can be understood.

### 6.3 Genesys Cloud — 24 edges

```text
General Platform Operation → Basic Interface
General Platform Operation → Queue / Flow Interaction
General Platform Operation → Main Products
General Platform Operation → Platform Capabilities
General Platform Operation → Divisions
General Platform Operation → Integration Mechanisms

Queue / Flow Interaction → How an Interaction Works in Genesys

Integration Mechanisms → REST APIs
Integration Mechanisms → Triggers
Integration Mechanisms → Webhooks and Notifications

REST APIs → Data Actions

Main Products → Campaigns
Main Products → WEM
Main Products → Virtual Agent Fundamentals

WEM → Evaluations
WEM → WFM Product Overview

Platform Capabilities → Speech and Text Analytics

Speech and Text Analytics → Sentiment
Speech and Text Analytics → Topics
Speech and Text Analytics → AI Scoring

Evaluations → AI Scoring

Virtual Agent Fundamentals → Containment

Basic Interface → Analytics Workspace and Performance Dashboards
Platform Capabilities → Analytics Workspace and Performance Dashboards
```

### 6.4 Genesys / Data Access — 8 edges

```text
Queues → Conversations Details Query
Users → Conversations Details Query
Flows → Conversations Details Query
Wrap-ups → Conversations Details Query

Conversations Details Query → Conversation Participant Attributes Search
Conversations Details Query → Transcript Search

Flows → Outcomes
Users → Users Details Query
```

Routing Skills and Data Tables remain Root Concepts inside this Domain.

### 6.5 Programming — 14 edges

```text
Basic Python Structures → Reading Simple Code
Basic Python Structures → Reading Lists
Basic Python Structures → Reading Dictionaries
Basic Python Structures → Reading Sets

Reading Lists → Reading NumPy Arrays

Reading Lists → Data Structures for Analysis
Reading Dictionaries → Data Structures for Analysis
Reading Sets → Data Structures for Analysis
Reading NumPy Arrays → Data Structures for Analysis

Data Structures for Analysis → Basic Data Manipulation
Basic Data Manipulation → Basic Pandas

Reading Simple Code → Reading Team Scripts

Basic Pandas → Small Supervised Data Manipulations
Reading Team Scripts → Small Supervised Data Manipulations
```

Basic SQL remains a Root Concept in this Domain.

### 6.6 Statistics — 7 edges

```text
Mean → Variance
Variance → Correlation

Mean → Basic Distribution Interpretation
Median → Basic Distribution Interpretation
Percentiles → Basic Distribution Interpretation
Variance → Basic Distribution Interpretation

Basic Distribution Interpretation → p-value
```

### 6.7 Data Visualization — 11 edges

```text
Chart Interpretation → Bar Charts
Chart Interpretation → Column Charts
Chart Interpretation → Time Series
Chart Interpretation → Scatter Plots

Bar Charts → Basic Visualization Selection
Column Charts → Basic Visualization Selection
Time Series → Basic Visualization Selection
Scatter Plots → Basic Visualization Selection

Basic Visualization Selection → Visual Communication
Introductory Gestalt Principles → Visual Communication

Visual Communication → Simple Analytical Narrative
```

Total formal Concept prerequisites:

```text
12 + 30 + 24 + 8 + 14 + 7 + 11 = 106
```

## 7. Runtime Layers

`layer` is derived from incoming prerequisites and is **not** stored in the YAML.

```text
no incoming Concept prerequisite
→ layer 0

otherwise
→ 1 + max(layer of direct prerequisites)
```

The Progression Engine works on the lowest incomplete layer inside the active Domain.

## 8. Post-Onboarding

The following areas remain outside Learning Graph v0.2:

- operational Workforce Management;
- forecasting;
- staffing;
- scheduling;
- adherence;
- occupancy;
- labor-regulation topics;
- Machine Learning;
- advanced Artificial Intelligence.

The public design may later model those areas in separate, versioned learning paths.

## 9. Document State

- Public document version: `v0.2`
- Reference graph version: `0.2`
- YAML schema version: `0.1`
- Status: approved for YAML materialization
