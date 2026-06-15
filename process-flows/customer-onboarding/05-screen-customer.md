---
id: screen-customer
title: Screen Customer
type: process-step
process: Customer Onboarding
order: 5
aliases: ["Screen Applicant", "Watchlist Check Step"]
status: draft
sources: ["https://www.sanctionscanner.com/blog/customer-onboarding-in-aml-and-kyc-1246", "https://seon.io/resources/kyc-onboarding/"]
---

# Screen Customer

**Definition.** Screen Customer screens the applicant against sanctions, PEP and adverse-media lists and holds and escalates any hits.
**Also known as:** Screen Applicant, Watchlist Check Step.

## Relationships
- Screen Customer is defined in the Customer Onboarding process.
- Screen Customer causes Assess Customer Risk.
- Screen Customer depends on the Transaction Monitoring Platform capability.
- Screen Customer mentions KYC Analyst.
- Screen Customer mentions KYC Profile.

## Details
The KYC Analyst screens the applicant. Inputs are the verified identity; outputs are a screened applicant recorded in the KYC Profile. The sanctions/PEP/adverse-media screening control branches on a hit (hold/escalate) versus clear.

## References
- [Sanction Scanner onboarding](https://www.sanctionscanner.com/blog/customer-onboarding-in-aml-and-kyc-1246)
- [SEON KYC onboarding](https://seon.io/resources/kyc-onboarding/)
