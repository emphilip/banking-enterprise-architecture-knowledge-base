---
id: report-sanctions-block
title: Report Sanctions Block
type: process-step
process: Sanctions Screening Operations
order: 6
aliases: ["File Sanctions Report", "Block Reporting Step"]
status: draft
sources: ["https://www.lenzo.ai/blog/sanctions-screening-false-positives-resolution-criteria/", "https://salv.com/blog/sanctions-screening-guide/"]
---

# Report Sanctions Block

**Definition.** Report Sanctions Block reports the confirmed block to OFAC within the deadline and retains the record, and emits the Sanctions Alert Event.
**Also known as:** File Sanctions Report, Block Reporting Step.

## Relationships
- Report Sanctions Block is defined in the Sanctions Screening Operations process.
- Report Sanctions Block depends on the Regulatory Reporting Engine capability.
- Report Sanctions Block mentions Compliance Screening Officer.
- Report Sanctions Block mentions Sanctions Alert Event.

## Details
The Compliance Screening Officer reports the block decision to OFAC and retains the record. Controls include block and report within 10 business days, retention and acknowledgement, with completion signalled by the Sanctions Alert Event. This is the final step of Sanctions Screening Operations.

## References
- [Lenzo — False-positive resolution criteria](https://www.lenzo.ai/blog/sanctions-screening-false-positives-resolution-criteria/)
- [Salv — Sanctions screening guide](https://salv.com/blog/sanctions-screening-guide/)
