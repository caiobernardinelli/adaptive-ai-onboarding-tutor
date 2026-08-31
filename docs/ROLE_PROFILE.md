# Role Profile — Junior Data Analyst

## 1. Purpose

This document defines the progressive competency profile used by the public reference case of the Adaptive AI Onboarding Tutor.

The reference learner is a **Junior Data Analyst working in a Contact Center and Genesys Cloud environment**.

The Role Profile is intentionally broader than a single Learning Graph version. Not every competency described here must become a Node in the initial onboarding YAML.

## 2. Formal Onboarding Scope

The `junior_data_analyst_onboarding` reference graph v0.2 contains seven formal Domains:

1. Contact Center Fundamentals;
2. Contact Center Metrics;
3. Genesys Cloud;
4. Genesys / Data Access;
5. Programming;
6. Statistics;
7. Data Visualization.

Operational Workforce Management, labor-regulation content, Machine Learning, and advanced Artificial Intelligence belong to later professional-development paths.

## 3. Prerequisite Rule

Pedagogically useful prerequisites described in this Role Profile do **not** automatically create `prerequisite_for` relationships in the Learning Graph.

Only relationships explicitly approved in the versioned graph are structural prerequisites.

When a learner needs background knowledge that is not represented as a formal prerequisite, the tutor may provide supporting content without silently modifying the graph.

---

# Horizon A — Initial Onboarding

## 4. Contact Center Fundamentals

The learner should understand:

- what a Contact Center is;
- customer interactions;
- agents;
- queues;
- flows;
- operational objectives;
- the basic interaction journey;
- ACD — Automatic Call Distribution;
- agent / ACD skills.

The goal is to create a usable mental model of how an interaction is organized and routed before deeper metric and platform analysis.

## 5. Contact Center Metrics

The learner should understand and relate operational volumes, outcomes, times, rates, and customer-experience indicators.

The reference graph includes:

- Offered;
- Answer / Answered;
- Abandonment;
- Flow-out;
- Flow Rate;
- Flow Disconnect — Volume;
- Flow Disconnect — Percentage;
- Flow Retention;
- Overflow / transfer-to-another-destination behavior;
- Answer %;
- Abandon %;
- ASA — Average Speed of Answer;
- Average Wait;
- Service Level;
- Talk Time;
- Hold Time;
- ACW — After Call Work;
- AHT — Average Handle Time;
- repeat contact;
- FCR — First Contact Resolution;
- CSAT — Customer Satisfaction;
- Customer Effort Score;
- NPS — Net Promoter Score.

`Flow Rate` and `Flow Retention` are represented as **derived operational concepts** in the reference case. The public project does not publish or assume a universal employer-specific formula for them.

The learning context should support both operational monitoring and deeper analytics.

## 6. Genesys Cloud

The learner should develop an introductory but connected understanding of:

- general platform operation;
- basic interface navigation;
- queues and flows inside the platform;
- how an interaction is handled;
- major product families and capabilities;
- Divisions and their role in organization/access control;
- integration mechanisms;
- REST APIs;
- Data Actions;
- Triggers;
- Webhooks and Notifications;
- Campaigns;
- WEM — Workforce Engagement Management;
- Evaluations;
- WFM as a product-level overview;
- Virtual Agent fundamentals;
- Speech and Text Analytics;
- Sentiment;
- Topics / Topic Spotting;
- AI Scoring;
- Containment;
- Analytics Workspace and Performance Dashboards.

The initial graph includes only a **product-level WFM overview**. Operational WFM is post-onboarding.

## 7. Genesys / Data Access

The learner should understand how platform data can be located and used for analysis.

The formal reference Concepts include:

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

Access to Division data through APIs remains a relevant application topic, while the formal `Divisions` Concept belongs to the Genesys Cloud Domain to avoid duplicate Nodes.

Supporting knowledge such as HTTP, REST, JSON, request/response behavior, and authentication may be taught when needed without automatically becoming graph Nodes.

## 8. Programming

The onboarding objective is applied technical literacy rather than full software-engineering autonomy.

Formal Concepts include:

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

The learner should be able to explain the flow of small code fragments, understand common data structures, and perform small data-processing tasks under review.

## 9. Statistics

The onboarding scope includes:

- mean;
- median;
- percentiles;
- variance;
- correlation;
- basic distribution interpretation;
- introductory p-value interpretation.

Population vs. sample, the null hypothesis, and test-of-hypothesis fundamentals may be introduced as supporting content when required to prevent the p-value from becoming a memorized number without interpretation.

## 10. Data Visualization

The onboarding scope includes:

- chart interpretation;
- bar charts;
- column charts;
- time series;
- scatter plots;
- basic visualization selection;
- introductory Gestalt principles;
- visual communication;
- a simple analytical narrative.

The objective is to connect a question, the data, a suitable visual representation, and an evidence-based conclusion.

---

# Horizon B — Post-Onboarding Development

## 11. Workforce Management and Operational Journey

Reserved for a later learning path.

Topics include:

- WFM fundamentals;
- forecasting;
- staffing / capacity planning;
- scheduling;
- adherence;
- occupancy;
- working-time concepts;
- breaks;
- applicable labor-regulation concepts;
- workload and operational-capacity interpretation;
- the relationship among capacity, compliance, and operational planning.

This is intentionally separated from the initial Learning Graph even though a WFM product overview appears inside Genesys Cloud.

## 12. Machine Learning

Later development may include:

- classification;
- regression;
- clustering;
- Precision and Recall;
- KNN;
- linear and logistic regression;
- decision trees;
- Random Forest;
- XGBoost;
- SVM;
- cross-validation;
- K-Fold;
- K-Means.

## 13. Artificial Intelligence

Later development may include:

- RAG;
- embeddings;
- Prompt Engineering;
- AI agents;
- AI-assisted automation;
- AI-enabled pipelines.

AI should not be treated as the default solution when a simpler analytical or deterministic approach is sufficient.

---

# 14. Combined Professional Outcome

The competency profile aims to connect:

```text
business context
→ platform
→ data
→ analysis
→ communication
→ decision support
```

The expected direction is a data professional who can understand an operational problem, identify relevant platform concepts and data, perform supervised analysis, communicate findings, and progressively propose more advanced solutions when justified.

## Document State

- Public document version: `v0.2`
- Product / MVP design: `v0.1`
- Reference Learning Graph: `0.2`
- Status: approved public portfolio adaptation for YAML implementation
