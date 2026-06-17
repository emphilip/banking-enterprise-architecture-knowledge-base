---
id: source-regulatory-data
title: Source Regulatory Data
type: process-step
process: Regulatory Capital Reporting
order: 1
aliases: ["Gather Capital Data", "Ingest Reg Data"]
status: draft
sources: ["https://www.regnology.net/en/resources/regulatory-topics/common-reporting-corep/", "https://www.hcltech.com/knowledge-library/what-are-eba-regulatory-reporting-requirements"]
---

# Source Regulatory Data

**Definition.** Source Regulatory Data sources and reconciles finance (GL) and risk (exposure) data feeds for the reporting reference date.

## Relationships
- Source Regulatory Data is defined in the Regulatory Capital Reporting process.
- Source Regulatory Data causes Calculate RWA.
- Source Regulatory Data depends on the Regulatory Capital Management capability.
- Source Regulatory Data mentions Regulatory Reporting Specialist.

## Details
The Regulatory Reporting Specialist sources and reconciles GL and risk data once the Reporting Deadline Reached Event approaches. Inputs are GL data, risk exposures and reference data; outputs are a reconciled regulatory dataset. Controls include data-quality reconciliation and GL-to-risk tie-out.

## References
- [Common Reporting (COREP)](https://www.regnology.net/en/resources/regulatory-topics/common-reporting-corep/)
- [EBA regulatory reporting requirements](https://www.hcltech.com/knowledge-library/what-are-eba-regulatory-reporting-requirements)
