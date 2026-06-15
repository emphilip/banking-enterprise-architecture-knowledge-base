---
id: decision-card-application
title: Decision Card Application
type: process-step
process: Card Issuance
order: 2
status: draft
sources: ["https://www.korahq.com/blog/build-a-card-issuing-program"]
---

# Decision Card Application

**Definition.** Decision Card Application runs KYC and credit/eligibility decisioning and assigns the credit limit.

## Relationships
- Decision Card Application is defined in the Card Issuance process.
- Decision Card Application causes Generate Card Credential.
- Decision Card Application depends on the Credit Decisioning Engine capability.
- Decision Card Application mentions Card Account Application.
- Decision Card Application mentions Card Issuance Officer.

## Details
Decision Card Application applies KYC, credit and eligibility policy to the application record and assigns the credit limit on approval, creating the approved card account.

## References
- [Build a card issuing program](https://www.korahq.com/blog/build-a-card-issuing-program)
