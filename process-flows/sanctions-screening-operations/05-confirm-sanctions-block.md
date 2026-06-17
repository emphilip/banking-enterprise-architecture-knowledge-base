---
id: confirm-sanctions-block
title: Confirm Sanctions Block
type: process-step
process: Sanctions Screening Operations
order: 5
aliases: ["Approve Sanctions Block", "Block Confirmation Step"]
status: draft
sources: ["https://www.descartes.com/resources/knowledge-center/best-practices-and-tools-reducing-false-positives-ofac-sanctions", "https://docs.oracle.com/en/industries/financial-services/ofs-analytical-applications/customer-screening/8.1.2.10.0/csoug/alert-decision.html"]
---

# Confirm Sanctions Block

**Definition.** Confirm Sanctions Block performs L2 four-eyes review of true matches and blocks or rejects the transaction or relationship on confirmation.
**Also known as:** Approve Sanctions Block, Block Confirmation Step.

## Relationships
- Confirm Sanctions Block is defined in the Sanctions Screening Operations process.
- Confirm Sanctions Block causes Report Sanctions Block.
- Confirm Sanctions Block depends on the Payment Sanctions Filter capability.
- Confirm Sanctions Block mentions Compliance Screening Officer.
- Confirm Sanctions Block mentions Sanctions Alert Event.

## Details
The Compliance Screening Officer reviews the hit disposition under four-eyes to produce a block decision. Controls include four-eyes approval, supervisor sign-off, blocking action and audit trail, raising the Sanctions Alert Event on confirmation.

## References
- [Descartes — Reducing false positives in OFAC sanctions](https://www.descartes.com/resources/knowledge-center/best-practices-and-tools-reducing-false-positives-ofac-sanctions)
- [Oracle — Customer screening alert decision](https://docs.oracle.com/en/industries/financial-services/ofs-analytical-applications/customer-screening/8.1.2.10.0/csoug/alert-decision.html)
