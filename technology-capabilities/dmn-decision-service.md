---
id: dmn-decision-service
title: DMN Decision Service
type: technology-capability
domain: Integration & APIs
level: L3
aliases: ["DMN Decision Table Service", "FEEL Decision Service", "Decision Modelling Service"]
status: draft
sources: ["https://www.omg.org/dmn/", "https://camunda.com/platform/decision-engine/"]
---

# DMN Decision Service

**Definition.** DMN Decision Service authors, versions, and executes standardized DMN decision tables and FEEL expressions that serve as both human-readable documentation and executable decision logic.
**Also known as:** DMN Decision Table Service, FEEL Decision Service, Decision Modelling Service.

## Relationships
- DMN Decision Service is defined in the Integration & APIs domain.
- DMN Decision Service is derived from Workflow Decision Engine.
- DMN Decision Service is related to BPMN Process Engine.

## Details
DMN Decision Service implements the OMG Decision Model and Notation standard: a Decision Requirements Diagram links decisions to input data and business knowledge models, decision tables encode rules with hit policies, and FEEL (Friendly Enough Expression Language) evaluates literal expressions and table cells. Camunda's decision engine runs DMN as a deployable, versioned decision service callable from BPMN or directly via API. Because the same DMN artefact is both readable by analysts and executable, decisions stay synchronized between documentation and runtime, supporting audit and regulatory explainability.

## References
- [OMG Decision Model and Notation](https://www.omg.org/dmn/)
- [Camunda decision engine](https://camunda.com/platform/decision-engine/)
