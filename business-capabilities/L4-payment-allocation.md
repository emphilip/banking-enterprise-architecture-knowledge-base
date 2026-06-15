---
id: payment-allocation
title: Payment Allocation
type: business-capability
domain: Lending & Credit
level: L4
aliases: ["Repayment Allocation", "Waterfall Allocation"]
status: draft
sources: ["https://bian.org/servicelandscape/", "https://www.consumerfinance.gov/rules-policy/regulations/1026/53/"]
---

# Payment Allocation

**Definition.** Payment Allocation is the capability that applies received funds to principal, interest, fees and arrears according to allocation rules, mapping to the BIAN Repayment service domain.
**Also known as:** Repayment Allocation, Waterfall Allocation.

## Relationships
- Payment Allocation is defined in the Lending & Credit domain.
- Payment Allocation is derived from Repayment Processing.
- Payment Allocation depends on the Core Banking Processing capability.

## Details
The BIAN Repayment service domain posts received funds, which Payment Allocation distributes across components. A concrete banking specific: US credit-card payments above the minimum due must, under the CARD Act and Regulation Z, be applied first to the balance with the highest APR, constraining the allocation waterfall the bank may use.

## References
- [BIAN Service Landscape](https://bian.org/servicelandscape/)
- [Regulation Z payment allocation (CARD Act)](https://www.consumerfinance.gov/rules-policy/regulations/1026/53/)
