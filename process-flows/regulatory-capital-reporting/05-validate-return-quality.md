---
id: validate-return-quality
title: Validate Return Quality
type: process-step
process: Regulatory Capital Reporting
order: 5
aliases: ["Validate COREP", "Run Taxonomy Checks"]
status: draft
sources: ["https://www.sas.com/en_us/software/regulatory-content-eba-taxonomies.html", "https://www.eba.europa.eu/publications-and-media/press-releases/eba-publishes-updated-dpm-and-xbrl-taxonomy-remittance"]
---

# Validate Return Quality

**Definition.** Validate Return Quality validates the return against the regulator DPM/XBRL taxonomy and validation rules, resolving errors.
**Also known as:** Validate COREP, Run Taxonomy Checks.

## Relationships
- Validate Return Quality is defined in the Regulatory Capital Reporting process.
- Validate Return Quality causes Attest Capital Return.
- Validate Return Quality causes Assemble Capital Return.
- Validate Return Quality depends on the Regulatory Capital Management capability.
- Validate Return Quality mentions Regulatory Reporting Specialist.
- Validate Return Quality mentions Capital Adequacy Return.

## Details
The Regulatory Reporting Specialist validates the Capital Adequacy Return against the regulator DPM/XBRL taxonomy and validation rules. Inputs are the Capital Adequacy Return and taxonomy rules; outputs are the validated return and a validation report. Controls include COREP/FINREP taxonomy validation and validation-error clearance. A validation error causes a return to Assemble Capital Return for correction.

## References
- [EBA taxonomies](https://www.sas.com/en_us/software/regulatory-content-eba-taxonomies.html)
- [EBA DPM and XBRL taxonomy](https://www.eba.europa.eu/publications-and-media/press-releases/eba-publishes-updated-dpm-and-xbrl-taxonomy-remittance)
