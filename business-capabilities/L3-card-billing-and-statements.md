---
id: card-billing-and-statements
title: Card Billing & Statements
type: business-capability
domain: Cards
level: L3
aliases: ["Card Billing", "Statement Cycle Processing"]
status: draft
sources: ["https://bian.org/servicelandscape/", "https://www.ecfr.gov/current/title-12/chapter-X/part-1026"]
---

# Card Billing & Statements

**Definition.** Card Billing & Statements computes cardholder balances, fees, interest and produces periodic statements, realising the BIAN Card Billing and Payments service domain.
**Also known as:** Card Billing, Statement Cycle Processing.

## Relationships
- Card Billing & Statements is defined in the Cards domain.
- Card Billing & Statements is derived from Card Authorization.
- Card Billing & Statements depends on the Core Banking Processing capability.

## Details
The BIAN Card Billing and Payments service domain runs the billing cycle: it sums posted transactions, computes finance charges using the average-daily-balance method and the account APR, applies fees, and derives the minimum payment and payment due date. Statements must comply with Reg Z (12 CFR 1026.7) periodic-statement content rules and the CARD Act 21-day payment-window requirement, and surface the minimum-payment warning disclosure.

## References
- [BIAN Service Landscape](https://bian.org/servicelandscape/)
- [eCFR Regulation Z, 12 CFR Part 1026](https://www.ecfr.gov/current/title-12/chapter-X/part-1026)
