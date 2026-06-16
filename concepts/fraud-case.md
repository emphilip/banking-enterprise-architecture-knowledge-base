---
id: fraud-case
title: Fraud Case
type: artifact
domain: Risk Management
aliases: ["Fraud Investigation Case", "Fraud Case File"]
status: draft
sources: ["https://www.unit21.ai/blog/ach-fraud-investigation-from-first-alert-to-sar-filing", "https://www.fincen.gov/resources/filing-information"]
---

# Fraud Case

**Definition.** Fraud Case is the case record that tracks a fraud investigation from alert through evidence gathering, disposition, recovery and any Suspicious Activity Report filing.

**Also known as:** Fraud Investigation Case, Fraud Case File.

## Relationships
- Fraud Case is related to the Risk Management domain.
- Fraud Case mentions Open Fraud Case.
- Fraud Case mentions Fraud Investigation.

## Details
Fraud Case is created in the case-management system when a routed Fraud Alert is adjudicated as having enough signal to investigate. It assembles the originating alert, the customer and account context (often several months of transaction history), the evidence gathered, customer-contact records, the investigator's findings, and the final disposition (confirmed fraud, dismissed or referred). Where fraud is confirmed, the Fraud Case records funds blocked or reversed, recovery actions and outcomes, any SAR filed and its reference and deadline, and the loss booked. Fraud Case is the system of record for fraud operations: it supports audit, regulatory recordkeeping, loss accounting and performance metrics, and supplies confirmed-outcome labels that feed back to detection models.

## References
- https://www.unit21.ai/blog/ach-fraud-investigation-from-first-alert-to-sar-filing
- https://www.fincen.gov/resources/filing-information
