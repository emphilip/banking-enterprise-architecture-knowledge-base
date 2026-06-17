---
id: route-fraud-alert
title: Route Fraud Alert
type: process-step
process: Fraud Detection
order: 5
aliases: ["Dispatch Alert", "Alert Routing Step"]
status: draft
sources: ["https://www.unit21.ai/blog/ach-fraud-investigation-from-first-alert-to-sar-filing"]
---

# Route Fraud Alert

**Definition.** Route Fraud Alert prioritizes and routes the Fraud Alert to the appropriate investigation queue and emits the Fraud Alert Raised Event.
**Also known as:** Dispatch Alert, Alert Routing Step.

## Relationships
- Route Fraud Alert is defined in the Fraud Detection process.
- Route Fraud Alert depends on the Workflow Orchestration capability.
- Route Fraud Alert mentions Fraud Alert.
- Route Fraud Alert mentions Fraud Alert Raised Event.

## Details
Route Fraud Alert hands the routed Fraud Alert off to investigation and emits the Fraud Alert Raised Event. Controls include routing rules, severity prioritization and clean hand-off to the Fraud Investigation process. This is the final step of Fraud Detection.

## References
- [Unit21 — ACH Fraud Investigation](https://www.unit21.ai/blog/ach-fraud-investigation-from-first-alert-to-sar-filing)
