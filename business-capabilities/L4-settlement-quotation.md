---
id: settlement-quotation
title: Settlement Quotation
type: business-capability
domain: Lending & Credit
level: L4
aliases: ["Payoff Quote", "Redemption Statement"]
status: draft
sources: ["https://bian.org/servicelandscape/", "https://www.apqc.org/process-frameworks"]
---

# Settlement Quotation

**Definition.** Settlement Quotation is the capability that calculates payoff and early-settlement figures including break costs for a loan, mapping to the BIAN Consumer Loan service domain.
**Also known as:** Payoff Quote, Redemption Statement.

## Relationships
- Settlement Quotation is defined in the Lending & Credit domain.
- Settlement Quotation is derived from Payoff & Closure.
- Settlement Quotation depends on the Core Banking Processing capability.

## Details
The BIAN Consumer Loan service domain provides the balance data from which Settlement Quotation derives a binding payoff figure. A concrete banking specific: a payoff/redemption statement quotes principal plus accrued interest to a good-through date with a per-diem amount, and UK regulated lenders must issue an early settlement figure assuming up to 28 days' notice under the Consumer Credit (Early Settlement) Regulations.

## References
- [BIAN Service Landscape](https://bian.org/servicelandscape/)
- [APQC Process Classification Framework](https://www.apqc.org/process-frameworks)
