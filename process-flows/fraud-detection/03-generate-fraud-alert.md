---
id: generate-fraud-alert
title: Generate Fraud Alert
type: process-step
process: Fraud Detection
order: 3
aliases: ["Raise Fraud Alert", "Alert Generation Step"]
status: draft
sources: ["https://www.unit21.ai/blog/ach-fraud-investigation-from-first-alert-to-sar-filing"]
---

# Generate Fraud Alert

**Definition.** Generate Fraud Alert raises a Fraud Alert when the risk score breaches thresholds and deduplicates duplicate alerts.
**Also known as:** Raise Fraud Alert, Alert Generation Step.

## Relationships
- Generate Fraud Alert is defined in the Fraud Detection process.
- Generate Fraud Alert causes Apply Detection Block.
- Generate Fraud Alert depends on the Fraud Analytics capability.
- Generate Fraud Alert mentions Fraud Alert.

## Details
The Fraud Alert is raised when the risk score breaches calibrated thresholds. Controls include threshold governance, false-positive control and alert deduplication so investigators are not flooded with duplicates.

## References
- [Unit21 — ACH Fraud Investigation](https://www.unit21.ai/blog/ach-fraud-investigation-from-first-alert-to-sar-filing)
