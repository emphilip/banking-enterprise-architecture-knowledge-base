---
id: interest-accrual-management
title: Interest Accrual Management
type: business-capability
domain: Lending & Credit
level: L4
aliases: ["Loan Interest Accrual", "Accrual Posting"]
status: draft
sources: ["https://bian.org/servicelandscape/", "https://www.apqc.org/process-frameworks"]
---

# Interest Accrual Management

**Definition.** Interest Accrual Management is the capability that calculates and posts daily interest accruals and rate resets on active loans, mapping to the BIAN Consumer Loan and Credit Facility service domains.
**Also known as:** Loan Interest Accrual, Accrual Posting.

## Relationships
- Interest Accrual Management is defined in the Lending & Credit domain.
- Interest Accrual Management is derived from Loan Account Maintenance.
- Interest Accrual Management depends on the Core Banking Processing capability.

## Details
The BIAN Consumer Loan and Credit Facility service domains depend on accurate accrued interest, which Interest Accrual Management computes and posts. A concrete banking specific: interest is accrued on a day-count basis (e.g. actual/365 or 30/360) and a loan that becomes non-accrual once classified as impaired stops recognising interest income, a treatment driven by IFRS 9 / ASC 326 (CECL) staging.

## References
- [BIAN Service Landscape](https://bian.org/servicelandscape/)
- [APQC Process Classification Framework](https://www.apqc.org/process-frameworks)
