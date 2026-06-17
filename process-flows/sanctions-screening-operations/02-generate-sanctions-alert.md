---
id: generate-sanctions-alert
title: Generate Sanctions Alert
type: process-step
process: Sanctions Screening Operations
order: 2
aliases: ["Raise Sanctions Alert", "Alert Generation Step (Sanctions)"]
status: draft
sources: ["https://salv.com/blog/sanctions-screening-guide/", "https://www.descartes.com/resources/knowledge-center/best-practices-and-tools-reducing-false-positives-ofac-sanctions"]
---

# Generate Sanctions Alert

**Definition.** Generate Sanctions Alert raises a Sanctions Hit alert for each candidate match above threshold and queues it for triage.
**Also known as:** Raise Sanctions Alert, Alert Generation Step (Sanctions).

## Relationships
- Generate Sanctions Alert is defined in the Sanctions Screening Operations process.
- Generate Sanctions Alert causes Triage Potential Match.
- Generate Sanctions Alert depends on the Payment Sanctions Filter capability.
- Generate Sanctions Alert mentions Compliance Screening Officer.
- Generate Sanctions Alert mentions Sanctions Hit.

## Details
The Compliance Screening Officer turns candidate matches into a Sanctions Hit and an alert queue. Controls include threshold governance, alert dedup and prioritisation.

## References
- [Salv — Sanctions screening guide](https://salv.com/blog/sanctions-screening-guide/)
- [Descartes — Reducing false positives in OFAC sanctions](https://www.descartes.com/resources/knowledge-center/best-practices-and-tools-reducing-false-positives-ofac-sanctions)
