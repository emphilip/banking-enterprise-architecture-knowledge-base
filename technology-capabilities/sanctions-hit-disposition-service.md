---
id: sanctions-hit-disposition-service
title: Sanctions Hit Disposition Service
type: technology-capability
domain: Core Processing
level: L3
aliases: ["Hit Disposition Workbench", "Sanctions Alert Disposition", "Screening Hit Workflow"]
status: draft
sources: ["https://www.acamstoday.org/ai-transforming-model-validation-in-sanctions-screening/", "https://www.linkedin.com/pulse/payments-ecosystem-topic-banks-payment-engine-sreenivasula-jambapuram-fvtrc"]
---

# Sanctions Hit Disposition Service

**Definition.** Sanctions Hit Disposition Service manages the workflow for triaging, investigating and clearing or escalating sanctions screening hits raised during in-flight payment screening.
**Also known as:** Hit Disposition Workbench, Sanctions Alert Disposition, Screening Hit Workflow.

## Relationships
- Sanctions Hit Disposition Service is defined in the Core Processing domain.
- Sanctions Hit Disposition Service is derived from Payment Sanctions Filter.

## Details
Sanctions Hit Disposition Service handles every potential match the inline filter raises against a payment held in flight. It presents the matched payment field and list entry side by side, captures the analyst's decision to release a false positive or escalate a true match, records the rationale and reviewer for audit, and supports four-eyes approval and Level 2 escalation. The service tracks whitelisting of confirmed false positives to suppress repeat hits and measures disposition turnaround, since held payments accrue settlement and customer-experience cost. AI-assisted triage is increasingly used to pre-score and rank hits for analyst review.

## References
- [AI in sanctions screening model validation (ACAMS Today)](https://www.acamstoday.org/ai-transforming-model-validation-in-sanctions-screening/)
- [Bank payment engine in the payments ecosystem (LinkedIn)](https://www.linkedin.com/pulse/payments-ecosystem-topic-banks-payment-engine-sreenivasula-jambapuram-fvtrc)
