---
id: credit-limit-assignment
title: Credit Limit Assignment
type: business-capability
domain: Cards
level: L3
aliases: ["Credit Line Setting", "Limit Assignment"]
status: draft
sources: ["https://bian.org/servicelandscape/", "https://www.ecfr.gov/current/title-12/chapter-X/part-1026"]
---

# Credit Limit Assignment

**Definition.** Credit Limit Assignment sets and adjusts the cardholder credit line and exposure parameters, aligned to the BIAN Card Terms service domain and issuer credit policy.
**Also known as:** Credit Line Setting, Limit Assignment.

## Relationships
- Credit Limit Assignment is defined in the Cards domain.
- Credit Limit Assignment is derived from Card Issuing.
- Credit Limit Assignment depends on the Credit Decisioning Engine capability.

## Details
The BIAN Card Terms service domain holds the assigned limit, which is bounded by the issuer's ability-to-repay assessment required under Reg Z (12 CFR 1026.51) and the CARD Act's restrictions on raising limits or APR without consideration of income. Subsequent credit-line increases or decreases are driven by behavioural scoring and reflected back into the open-to-buy used by the authorization host on each ISO 8583 authorization request.

## References
- [BIAN Service Landscape](https://bian.org/servicelandscape/)
- [eCFR Regulation Z 1026.51 (ability to pay)](https://www.ecfr.gov/current/title-12/part-1026/section-1026.51)
