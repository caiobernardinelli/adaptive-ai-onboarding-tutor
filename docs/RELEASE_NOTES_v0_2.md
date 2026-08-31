# Public Documentation Milestone — v0.2

**Date:** 2026-08-31

## Summary

This milestone updates the public portfolio documentation to the approved Learning Graph v0.2 baseline before final YAML implementation.

## Added

- Seven-Domain reference Learning Graph with 94 Concepts.
- Formal Concept prerequisites inside Domains.
- Runtime-derived Concept-layer model.
- Expanded operational Contact Center metrics.
- Agent / ACD Skills.
- Flow Disconnect volume and percentage.
- Customer Effort Score.
- Genesys Cloud Divisions as an organization/access-control Concept.
- Webhooks and Notifications terminology.
- Speech and Text Analytics, Virtual Agent, Containment, and Analytics Workspace / Performance Dashboards concepts.
- Python list, dictionary, set, and NumPy-array reading concepts.
- Introductory p-value.
- Public architecture documentation for Loader, Validator, Progression Engine, LLM boundary, DAL, and SQLite.
- Explicit public/private confidentiality boundary.

## Changed

- ACD moved from Contact Center Metrics to Contact Center Fundamentals.
- The Data Access model no longer duplicates Divisions as a formal Concept.
- `Conversation Participant Attributes Search` replaces the earlier public wording `Conversations Attributes Search`.
- The Learning Graph schema removes `domain_id` from Concept Nodes; membership is expressed exclusively through `contains`.
- Operational Workforce Management moved to post-onboarding.
- Machine Learning and advanced Artificial Intelligence remain post-onboarding.
- Public documentation now distinguishes Product/MVP version, YAML schema version, Learning Graph version, and documentation milestone version.

## Reference Graph Counts

```text
7 Domains
94 Concepts
94 contains
4 Domain prerequisite_for
106 Concept prerequisite_for
204 relationships total
```

## Version Domains

```text
Product / MVP design: v0.1
YAML schema:          0.1
Learning Graph:       0.2
Public docs milestone: v0.2
```

## Confidentiality

No employer-internal documentation, client information, client-specific configuration, credentials, private endpoints, or confidential operating rules are part of this public milestone.

Derived flow metrics are represented conceptually without publishing an employer-specific formula.

## Next Engineering Milestone

```text
final YAML v0.2
→ Loader
→ Loader tests
→ Graph Validator
→ Validator tests
```
