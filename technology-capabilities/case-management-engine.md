---
id: case-management-engine
title: Case Management Engine
type: technology-capability
domain: Integration & APIs
level: L2
aliases: ["CMMN Engine", "Adaptive Case Management", "Dynamic Case Engine"]
status: draft
sources: ["https://camunda.com/platform/", "https://en.wikipedia.org/wiki/Decision_Model_and_Notation"]
---

# Case Management Engine

**Definition.** Case Management Engine supports adaptive, knowledge-worker-driven case handling (CMMN) where the path is determined at runtime rather than by a predefined process flow.
**Also known as:** CMMN Engine, Adaptive Case Management, Dynamic Case Engine.

## Relationships
- Case Management Engine is defined in the Integration & APIs domain.
- Case Management Engine is derived from Workflow Orchestration.
- Case Management Engine is related to Human Task Manager.

## Details
Case Management Engine executes OMG CMMN case models built from a case plan of stages, human tasks, milestones, and sentries (entry/exit criteria) that activate work dynamically based on data and events. Unlike rigid BPMN flows, a case worker can enable discretionary tasks at their judgement, so the engine fits investigation and dispute work where the sequence cannot be fully predetermined. In banking it backs AML case investigation, complaints, and dispute handling, tracking case data, evidence, and decisions to a defined milestone of resolution.

## References
- [Camunda platform](https://camunda.com/platform/)
- [Decision Model and Notation (Wikipedia)](https://en.wikipedia.org/wiki/Decision_Model_and_Notation)
