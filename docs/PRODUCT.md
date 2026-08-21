# Product Definition — Adaptive AI Onboarding Tutor

## 1. Problem

The initial user observed difficulty in recognizing new terminology, understanding new ways of performing tasks, and understanding exactly how the new role creates value for the company.

At the same time, companies may not always have enough availability to provide continuous one-to-one onboarding support for a new employee.

This product proposes an AI-powered digital onboarding tutor designed to support the initial learning and development of a new employee.

## 2. Initial User — v0.1

The first user and tester of the system will be its creator.

The initial role is:

**Junior Data Analyst**

The role responsibilities and expected competencies were initially defined by the user's manager.

## 3. Expected Outcome

The goal of the first experiment is that, after approximately 6–8 weeks of use in a Customer Experience and Contact Center environment, the analyst should be able to:

- recognize most of the terminology used by the team;
- when encountering an unfamiliar term, relate it to previously learned concepts;
- understand decisions discussed in team meetings and explain, in simple terms, why those decisions were made;
- connect learned concepts to formulate possible solution paths for a given problem;
- propose technically plausible approaches, even when those approaches are not yet optimal;
- perform basic support tasks for colleagues under supervision.

The objective is not full professional autonomy after 6–8 weeks.

The objective is to build the mental model required to understand the environment and begin contributing meaningfully under supervision.

## 4. Essential Functions — v0.1

### 4.1 Learning Progression

The learning process must follow a logical sequence based on the knowledge required to achieve the expected outcome.

The tutor should begin with foundational concepts and progressively introduce more advanced topics.

A learner should only progress when they demonstrate sufficient understanding of the current topic and can explain the main concepts in their own words.

### 4.2 Explanations and Examples

Explanations should be simple and accessible while maintaining the technical rigor required by each topic.

The primary objective is comprehension.

The tutor should use clear and general examples to reduce unnecessary cognitive load when introducing new concepts.

Deep personalization based on the learner's previous professional background is not required in v0.1.

### 4.3 Exercises and Learning Follow-up

Small exercises should be used throughout the learning process.

At the end of a broader topic or learning unit, the learner should complete integrative exercises that require connecting multiple concepts.

These activities are not intended to operate as traditional exams.

Their purpose is to provide evidence that the learner can:

- connect concepts;
- reason about them;
- apply them to new situations;
- progress toward the professional outcomes defined for the onboarding process.

## 5. Out of Scope — v0.1

The following capabilities are intentionally excluded from the initial version:

- deep adaptive personalization based on the learner's previous knowledge and professional background;
- long-term career development after the initial onboarding objective has been achieved;
- advanced Machine Learning training;
- advanced Artificial Intelligence training;
- autonomous execution of real client operations;
- direct modification of production systems;
- use of confidential client or company information without explicit authorization.

These capabilities may be considered in later versions.

## 6. Success Criteria

Success will be evaluated across three dimensions.

### 6.1 Learning

The learner should be able to complete integrative exercises by:

- combining concepts learned during the topic;
- explaining the reasoning used;
- making connections between concepts;
- applying the knowledge to situations that are not simple repetitions of previous examples.

The goal is to measure understanding rather than memorization.

### 6.2 Knowledge Transfer

The learner should be able to analyze a realistic work-related problem and formulate at least one technically plausible solution path based on the knowledge acquired.

The proposed solution does not need to be optimal.

However, it should demonstrate coherent reasoning and should not depend on a fundamental misunderstanding of the concepts involved.

### 6.3 Professional Application

In real team discussions or supervised activities, the learner should progressively be able to:

- understand decisions being discussed;
- explain why a given decision may have been taken;
- understand the expected outcome of that decision;
- formulate relevant questions;
- contribute basic hypotheses or possible solution paths;
- perform support activities with supervision.

## 7. Initial Product Hypothesis

The initial product hypothesis is:

> If a new employee receives progressive, role-oriented learning with prerequisite-aware progression, guided reasoning, frequent application exercises, and reliable access to domain knowledge, the employee may build the mental model required to understand the role and contribute under supervision faster than through unstructured self-learning alone.

This hypothesis must be treated as something to validate, not as an already proven outcome.

## 8. Product Boundary

The Adaptive AI Onboarding Tutor is not intended to be only a document-question answering system.

Document retrieval may support the learning experience, but the product must also represent and manage:

- role competencies;
- learning progression;
- prerequisite relationships;
- learner progress;
- evidence of understanding;
- guided reasoning;
- progression decisions.

The objective is not simply to answer:

> "What is the correct information?"

The system should also reason about:

> "What should this learner understand next, and what is the minimum support required for them to reach that understanding?"