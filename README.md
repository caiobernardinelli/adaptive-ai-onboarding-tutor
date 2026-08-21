# Adaptive AI Onboarding Tutor

> An adaptive AI onboarding tutor for Genesys Cloud, Data Analytics, and Customer Experience roles, designed around role-based learning paths, prerequisite-aware progression, guided reasoning, and source-grounded knowledge retrieval.

## Overview

The **Adaptive AI Onboarding Tutor** is an early-stage AI and Data Engineering project exploring how a digital tutor can support the onboarding of professionals working with complex technical and business domains.

The initial case study focuses on a **Junior Data Analyst operating in a Contact Center and Genesys Cloud environment**.

Instead of functioning only as a document question-answering chatbot, the project aims to combine:

- role competency modeling;
- prerequisite-aware learning progression;
- learner progress tracking;
- guided reasoning;
- application-based exercises;
- source-grounded knowledge retrieval;
- progressive development toward professional autonomy.

The initial onboarding target is a **6–8 week learning journey** designed to help the learner understand the business context, follow technical discussions, interpret Contact Center metrics, understand Genesys Cloud data structures, and begin contributing to supervised analytical tasks.

---

## Problem

Technical onboarding often requires learning several layers at the same time:

**business domain → platform → terminology → data → analysis → decision-making**

A new analyst may already know individual tools such as Python, SQL, or Data Visualization while still struggling to understand how those tools connect to the company's real workflows and client problems.

At the same time, experienced team members may have limited availability for continuous one-to-one onboarding.

This project investigates whether an AI tutor can provide a structured learning layer between documentation, technical training, and real professional practice.

---

## Why Not Just a RAG Chatbot?

Retrieval-Augmented Generation can help answer questions from documentation.

However, answering:

> "What does this concept mean?"

is different from deciding:

> "What should this learner understand next?"

The project therefore separates two responsibilities.

### Knowledge Layer

Responsible for retrieving reliable information from authorized sources.

Future capabilities may include:

- Retrieval-Augmented Generation (RAG);
- embeddings;
- semantic retrieval;
- source attribution.

### Pedagogical Layer

Responsible for managing the learning process.

It should eventually consider:

- role competencies;
- prerequisite relationships;
- learner progress;
- demonstrated understanding;
- previous difficulties;
- exercises completed;
- when to explain;
- when to ask a question;
- when to provide a hint;
- when to review;
- when the learner is ready to progress.

RAG may become part of the system, but **RAG is not the learning architecture itself**.

---

## Learner Reasoning Ownership

A core design principle of the project is that the AI tutor should not replace the learner's reasoning.

When an exercise or problem is intended to develop a competency, the tutor should avoid immediately providing the final solution, even when explicitly requested.

The preferred interaction is:

```text
Problem
  ↓
Learner attempt
  ↓
Guiding question
  ↓
New attempt
  ↓
Progressive hint
  ↓
Feedback
  ↓
Solution refinement