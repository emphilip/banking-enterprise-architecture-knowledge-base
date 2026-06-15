---
id: investigate-break
title: Investigate Break
type: process-step
process: Reconciliation & Settlement
order: 5
aliases: ["Break Investigation", "Exception Handling"]
status: draft
sources: ["https://smart.stream/resources/smart-reconciliations-bank-to-bank-payments-exception-management/"]
---

# Investigate Break

**Definition.** Investigate Break investigates each break, raises investigation messages/recalls, and routes to owners for resolution.
**Also known as:** Break Investigation, Exception Handling.

## Relationships
- Investigate Break is defined in the Reconciliation & Settlement process.
- Investigate Break causes Post Adjustment.
- Investigate Break depends on the Workflow Orchestration capability.
- Investigate Break mentions Reconciliation Analyst.

## Details
The Reconciliation Analyst investigates each break. Inputs are reconciliation breaks; outputs are resolved breaks. Controls include segregation of duties and an escalation workflow, branching across resolve versus escalate.

## References
- [SmartStream exception management](https://smart.stream/resources/smart-reconciliations-bank-to-bank-payments-exception-management/)
