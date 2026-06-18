---
id: process-monitoring-and-analytics
title: Process Monitoring & Analytics
type: technology-capability
domain: Integration & APIs
level: L2
aliases: ["Process Intelligence", "Workflow Analytics", "Process Optimization"]
status: draft
sources: ["https://camunda.com/process-orchestration/", "https://arxiv.org/pdf/1610.05788"]
---

# Process Monitoring & Analytics

**Definition.** Process Monitoring & Analytics provides real-time visibility, KPIs, bottleneck detection, and historical reporting over running and completed processes to optimize workflow performance.
**Also known as:** Process Intelligence, Workflow Analytics, Process Optimization.

## Relationships
- Process Monitoring & Analytics is defined in the Integration & APIs domain.
- Process Monitoring & Analytics is derived from Workflow Orchestration.
- Process Monitoring & Analytics depends on BPMN Process Engine.

## Details
Process Monitoring & Analytics consumes the event stream and history a process engine emits per instance and step to compute cycle time, throughput, SLA breaches, and stage-level bottlenecks, and to display heatmaps over the BPMN diagram. Camunda Optimize builds dashboards, alerts, and process improvement reports from this data, while mining techniques reconstruct as-is flows from logs. In banking it surfaces where onboarding or dispute cases stall, supports capacity planning, and provides audit evidence of how long regulated steps took.

## References
- [Camunda process orchestration](https://camunda.com/process-orchestration/)
- [Process analytics research](https://arxiv.org/pdf/1610.05788)
