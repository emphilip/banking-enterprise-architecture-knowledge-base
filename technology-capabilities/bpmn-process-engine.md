---
id: bpmn-process-engine
title: BPMN Process Engine
type: technology-capability
domain: Integration & APIs
level: L2
aliases: ["Process Engine", "BPMN Workflow Engine", "Process Execution Engine"]
status: draft
sources: ["https://docs.camunda.io/docs/components/concepts/concepts-overview/", "https://camunda.com/process-orchestration/"]
---

# BPMN Process Engine

**Definition.** BPMN Process Engine executes BPMN 2.0 process models on a stateful, event-driven runtime that triggers service calls, routes work, handles timeouts, and manages long-running process state.
**Also known as:** Process Engine, BPMN Workflow Engine, Process Execution Engine.

## Relationships
- BPMN Process Engine is defined in the Integration & APIs domain.
- BPMN Process Engine is derived from Workflow Orchestration.
- BPMN Process Engine is related to Workflow Decision Engine.

## Details
BPMN Process Engine interprets OMG BPMN 2.0 models: it advances tokens through tasks, gateways (exclusive, parallel, event-based), timer and message events, and sub-processes while persisting process instance state so workflows survive restarts and run for days or months. Camunda's engine executes service tasks via workers/connectors, raises incidents on failure for retry, and exposes APIs to start and signal instances. In banking it orchestrates loan origination and onboarding journeys, calling decision and human-task components at the right BPMN steps.

## References
- [Camunda concepts overview](https://docs.camunda.io/docs/components/concepts/concepts-overview/)
- [Camunda process orchestration](https://camunda.com/process-orchestration/)
