---
id: repayment-processing
title: Repayment Processing
type: business-capability
domain: Lending & Credit
level: L3
aliases: ["Loan Repayment Handling", "Installment Processing"]
status: draft
sources: ["https://bian.org/servicelandscape/", "https://www.apqc.org/process-frameworks"]
---

# Repayment Processing

**Definition.** Repayment Processing is the capability that schedules, collects and allocates principal and interest repayments across the loan lifecycle, mapping to the BIAN Repayment service domain.
**Also known as:** Loan Repayment Handling, Installment Processing.

## Relationships
- Repayment Processing is defined in the Lending & Credit domain.
- Repayment Processing is derived from Loan Servicing.
- Repayment Processing depends on the Core Banking Processing capability.
- Repayment Processing depends on the Analytics Platform capability.

## Details
The BIAN Repayment service domain administers the schedule and receipt of loan repayments; Repayment Processing drives its Update and Execute operations on each due date. A concrete banking specific: an instalment payment is posted to the core ledger and split per the payment-allocation waterfall (fees, then accrued interest, then principal), and a missed instalment that ages past due flags the account for delinquency treatment.

## References
- [BIAN Service Landscape](https://bian.org/servicelandscape/)
- [APQC Process Classification Framework](https://www.apqc.org/process-frameworks)
