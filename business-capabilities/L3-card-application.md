---
id: card-application
title: Card Application
type: business-capability
domain: Cards
level: L3
aliases: ["Card Onboarding", "New Card Application"]
status: draft
sources: ["https://bian.org/servicelandscape/", "https://www.apqc.org/process-frameworks"]
---

# Card Application

**Definition.** Card Application captures and adjudicates requests for a new card product, mapping to the BIAN Card Capture and Card Terms service domains to establish eligibility and account terms.
**Also known as:** Card Onboarding, New Card Application.

## Relationships
- Card Application is defined in the Cards domain.
- Card Application is derived from Card Issuing.
- Card Application depends on the Workflow Orchestration capability.

## Details
The BIAN Card Capture service domain records the cardholder request and product selection, while Card Terms fixes the contractual basis (APR, fees, cardholder agreement) before issuance. For credit cards in the US, the application must surface Truth in Lending (Reg Z, 12 CFR 1026) Schumer-box disclosures and obtain the applicant's consent to terms; the capability also routes the application through credit-decisioning and KYC checks before an account number and BIN range are assigned.

## References
- [BIAN Service Landscape](https://bian.org/servicelandscape/)
- [eCFR Regulation Z, 12 CFR Part 1026](https://www.ecfr.gov/current/title-12/chapter-X/part-1026)
