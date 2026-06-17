---
id: journal-validation-and-control
title: Journal Validation & Control
type: business-capability
domain: Finance & Treasury
level: L4
aliases: ["Journal Approval Control", "Posting Validation", "Journal SoD Control"]
status: draft
sources: ["https://www.apqc.org/resource-library/resource-listing/90-manage-financial-resources-definitions-and-key-measures-pcf", "https://bian.org/servicelandscape/"]
---

# Journal Validation & Control

**Definition.** Journal Validation & Control applies balancing, authorisation and segregation-of-duties controls to journal entries before they post, supporting the BIAN Financial Control service domain.
**Also known as:** Journal Approval Control, Posting Validation, Journal SoD Control.

## Relationships
- Journal Validation & Control is defined in the Finance & Treasury domain.
- Journal Validation & Control is derived from Journal Management.
- Journal Validation & Control depends on the General Ledger Engine capability.

## Details
Journal Validation & Control enforces that each entry balances, references a valid open period and active account combination, and has cleared a preparer/approver workflow before posting. These are key SOX/ICFR controls: a poster cannot approve their own journal (segregation of duties), high-value or manual top-side entries require additional sign-off, and every posted journal carries an immutable audit trail. The capability also runs automated edit checks and duplicate detection to block erroneous postings at source.

## References
- [APQC PCF 9.0 Manage Financial Resources](https://www.apqc.org/resource-library/resource-listing/90-manage-financial-resources-definitions-and-key-measures-pcf)
- [BIAN Service Landscape](https://bian.org/servicelandscape/)
