---
id: capture-clearing-response
title: Capture Clearing Response
type: process-step
process: Payment Processing
order: 8
aliases: ["Process Clearing Status", "Return Handling"]
status: draft
sources: ["https://www.cpg.de/en/glossary/pain-002-iso-20022-message/", "https://achdevguide.nacha.org/how-ach-works"]
---

# Capture Clearing Response

**Definition.** Capture Clearing Response ingests acknowledgements, status (pacs.002 / pain.002) and returns, updating payment status and triggering repair on returns.
**Also known as:** Process Clearing Status, Return Handling.

## Relationships
- Capture Clearing Response is defined in the Payment Processing process.
- Capture Clearing Response causes Confirm Settlement.
- Capture Clearing Response depends on the Payment Orchestration capability.
- Capture Clearing Response mentions Payment Operations Analyst.

## Details
The Payment Operations Analyst ingests status and returns for the submitted clearing batch. Inputs are the submitted clearing batch; outputs are a cleared payment. As the final Payment Processing step, it hands off to Confirm Settlement in the Reconciliation & Settlement flow. Controls include status reconciliation and return handling, branching across accepted versus returned.

## References
- [pain.002 ISO 20022 message](https://www.cpg.de/en/glossary/pain-002-iso-20022-message/)
- [Nacha ACH Dev Guide](https://achdevguide.nacha.org/how-ach-works)
