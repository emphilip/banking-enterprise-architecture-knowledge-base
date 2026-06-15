---
id: identify-breaks
title: Identify Breaks
type: process-step
process: Reconciliation & Settlement
order: 4
aliases: ["Break Detection", "Exception Identification"]
status: draft
sources: ["https://smart.stream/resources/smart-reconciliations-bank-to-bank-payments-exception-management/", "https://www.skydo.com/blog/nostro-reconciliation"]
---

# Identify Breaks

**Definition.** Identify Breaks surfaces unmatched items and discrepancies as reconciliation breaks and classifies them by type.
**Also known as:** Break Detection, Exception Identification.

## Relationships
- Identify Breaks is defined in the Reconciliation & Settlement process.
- Identify Breaks causes Investigate Break.
- Identify Breaks depends on the Workflow Orchestration capability.
- Identify Breaks mentions Reconciliation Analyst.
- Identify Breaks mentions Reconciliation Break Event.

## Details
The Reconciliation Analyst classifies unmatched items. Inputs are the reconciliation result; outputs are reconciliation breaks. The Reconciliation Break Event is raised on detection. Controls include break classification and ageing thresholds, branching across matched versus break.

## References
- [SmartStream exception management](https://smart.stream/resources/smart-reconciliations-bank-to-bank-payments-exception-management/)
- [Nostro reconciliation](https://www.skydo.com/blog/nostro-reconciliation)
