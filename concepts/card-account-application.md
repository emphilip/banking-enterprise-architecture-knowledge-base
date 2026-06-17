---
id: card-account-application
title: Card Account Application
type: artifact
domain: Cards
aliases: ["Card Product Application", "Card Onboarding Application"]
status: draft
sources: ["https://dashdevs.com/blog/card-issuing/", "https://www.korahq.com/blog/build-a-card-issuing-program"]
---

# Card Account Application

**Definition.** Card Account Application is the application document capturing applicant, product and credit-limit selection for a payment card. Card Account Application is the input artifact that initiates the card-issuance flow.

**Also known as:** Card Product Application, Card Onboarding Application.

## Relationships
- Card Account Application is related to the Cards domain.
- Card Account Application mentions Card Issuance.
- Card Account Application mentions Capture Card Application.

## Details
Card Account Application carries the applicant's identity and contact details, the selected card product and pricing, requested credit limit, declared income and obligations, and consent to identity and credit checks. It is captured at the start of the card-issuance flow, where KYC and credit/eligibility decisioning are applied and the credit limit assigned before production. For credit cards the application supports Reg Z disclosures and ability-to-pay assessment. Card Account Application is enriched into the approved card account record from which the Card Credential is later generated.

## References
- https://dashdevs.com/blog/card-issuing/
- https://www.korahq.com/blog/build-a-card-issuing-program
