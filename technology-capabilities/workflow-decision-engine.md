---
id: workflow-decision-engine
title: Workflow Decision Engine
type: technology-capability
domain: Integration & APIs
level: L2
aliases: ["Business Rules Engine", "Decision Automation Engine", "Workflow Rules Engine"]
status: draft
sources: ["https://camunda.com/blog/2024/01/decision-engines-what-they-are-what-they-do/", "https://www.omg.org/dmn/"]
---

# Workflow Decision Engine

**Definition.** Workflow Decision Engine evaluates business rules and decision tables (DMN) invoked from processes to produce consistent, auditable automated decisions within orchestrated workflows.
**Also known as:** Business Rules Engine, Decision Automation Engine, Workflow Rules Engine.

## Relationships
- Workflow Decision Engine is defined in the Integration & APIs domain.
- Workflow Decision Engine is derived from Workflow Orchestration.
- Workflow Decision Engine is related to BPMN Process Engine.

## Details
Workflow Decision Engine externalizes business logic from process code so analysts can author and change rules independently. It evaluates DMN decision tables with configurable hit policies (unique, first, collect) and FEEL expressions, returning typed outputs such as eligibility, risk band, or pricing tier. Camunda's decision engine runs DMN as a callable service from BPMN business-rule tasks and versions each decision for audit. Banks use it for credit policy, fee waivers, and routing rules where decisions must be transparent, repeatable, and regulator-explainable.

## References
- [Decision engines: what they are and do](https://camunda.com/blog/2024/01/decision-engines-what-they-are-what-they-do/)
- [OMG Decision Model and Notation](https://www.omg.org/dmn/)
